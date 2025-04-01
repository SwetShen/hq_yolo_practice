import cv2
import ffmpeg
import subprocess

# 指定 FFmpeg 的完整路径（根据你的安装路径修改）
ffmpeg_path = r'D:/ffmpeg-7.0.2-essentials_build/bin/ffmpeg.exe'

# 摄像头设备号（Windows 通常为0）
camera_index = 0

# RTMP服务器地址
rtmp_url = "rtmp://localhost/live/stream"

# 初始化摄像头
cap = cv2.VideoCapture(camera_index)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 使用ffmpeg-python构建FFmpeg推流管道，并指定ffmpeg路径
process = (
    ffmpeg
    .input('pipe:', format='rawvideo', pix_fmt='bgr24', s=f'{width}x{height}', r=fps)
    .output(rtmp_url,
            vcodec='libx264',
            pix_fmt='yuv420p',
            preset='ultrafast',
            f='flv')
    .overwrite_output()
    .run_async(pipe_stdin=True, cmd=ffmpeg_path)  # 关键：通过 cmd 参数指定 ffmpeg 路径
)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 将帧写入FFmpeg的输入管道
        process.stdin.write(frame.tobytes())

except Exception as e:
    print(f"Error: {e}")

finally:
    # 释放资源
    cap.release()
    process.stdin.close()
    process.wait()