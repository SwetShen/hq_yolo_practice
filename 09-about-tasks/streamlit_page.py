import streamlit as st
import cv2
import os
import time
from datetime import datetime
from ultralytics import YOLO
from PIL import Image

# 初始化配置
st.set_page_config(layout="wide")
model = YOLO("../save/yolov5su.pt")  # 提前加载模型
OUTPUT_DIR = "detection_history"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 会话状态初始化
if "current_mode" not in st.session_state:
    st.session_state.current_mode = "图片检测"
if "detection_history" not in st.session_state:
    st.session_state.detection_history = []

# 侧边栏设计
with st.sidebar.expander("⚙️ 控制面板", expanded=True):
    selected_mode = st.radio(
        "操作模式",
        ["图片检测", "实时检测", "检测记录"],
        index=0
    )

    st.divider()
    conf_threshold = st.slider("置信度阈值", 0.0, 1.0, 0.4)
    st.caption("历史记录存储路径：`./detection_history`")

# 主界面布局
main_col = st.columns([0.7, 0.3])  # 7:3分栏

# 图片检测模式
if selected_mode == "图片检测":
    with main_col[0]:
        uploaded_file = st.file_uploader(
            "上传图片/视频",
            type=["jpg", "png", "jpeg", "mp4"],
            accept_multiple_files=False
        )

        if uploaded_file:
            file_type = "video" if uploaded_file.type.startswith("video") else "image"
            st.session_state.current_mode = file_type

            # 执行检测
            with st.spinner("检测中..."):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                save_path = os.path.join(OUTPUT_DIR, f"{timestamp}.{uploaded_file.name.split('.')[-1]}")

                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                if file_type == "image":
                    img = Image.open(uploaded_file)
                    results = model.predict(img, conf=conf_threshold)
                    plotted_img = results[0].plot()[:, :, ::-1]  # RGB转BGR
                    main_col[0].image(plotted_img, use_column_width=True)
                else:
                    temp_video = os.path.join(OUTPUT_DIR, "temp.mp4")
                    with open(temp_video, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    cap = cv2.VideoCapture(temp_video)
                    frame_placeholder = st.empty()

                    while cap.isOpened():
                        ret, frame = cap.read()
                        if not ret:
                            break

                        results = model.predict(frame, conf=conf_threshold)
                        plotted_frame = results[0].plot()
                        frame_placeholder.image(plotted_frame, channels="BGR")

                    cap.release()

                # 保存记录
                st.session_state.detection_history.append({
                    "time": datetime.now(),
                    "file_path": save_path,
                    "file_type": file_type
                })

# 实时检测模式
elif selected_mode == "实时检测":
    with main_col[0]:
        cam_enabled = st.checkbox("启用摄像头")
        frame_placeholder = st.empty()
        stop_button = st.button("停止检测")

        if cam_enabled and not stop_button:
            cap = cv2.VideoCapture(0)

            while cam_enabled and not stop_button:
                ret, frame = cap.read()
                if not ret:
                    st.error("摄像头访问失败")
                    break

                results = model.predict(frame, conf=conf_threshold)
                plotted_frame = results[0].plot()
                frame_placeholder.image(plotted_frame, channels="BGR")

            cap.release()

# 检测记录模式
elif selected_mode == "检测记录":
    with main_col[0]:
        st.subheader("历史检测记录")
        cols = st.columns(3)

        for idx, record in enumerate(st.session_state.detection_history):
            with cols[idx % 3]:
                st.caption(record["time"].strftime("%Y-%m-%d %H:%M:%S"))

                if record["file_type"] == "image":
                    st.image(record["file_path"], use_column_width=True)
                else:
                    st.video(record["file_path"])

                st.download_button(
                    f"下载结果 {idx + 1}",
                    data=open(record["file_path"], "rb"),
                    file_name=os.path.basename(record["file_path"])
                )

# 右侧信息面板
with main_col[1]:
    st.subheader("实时统计")

    if selected_mode in ["图片检测", "实时检测"]:
        if hasattr(st.session_state, "last_results"):
            results = st.session_state.last_results
            class_counts = results[0].boxes.cls.unique().shape[0]
            st.metric("检测到类别数", class_counts)

            class_dist = results[0].boxes.cls.cpu().numpy()
            st.bar_chart(class_dist)
    else:
        st.write("选择检测模式后显示统计信息")

    st.divider()
    st.write("最近5次检测记录")
    for record in st.session_state.detection_history[-5:]:
        st.caption(f"{record['time'].strftime('%H:%M:%S')} - {record['file_type']}")

# 运行命令：streamlit run app.py