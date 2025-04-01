<template>
	<view class="camera-page">
		<view class="camera-show">
			<image mode="aspectFit" :src="image_url"></image>
		</view>
		<button class="take-photo" @click="takePhoto">选择照片</button>
		<button class="detect-photo" @click="detectPhoto">识别</button>
		<view class="detect-info">
			{{data}}
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				image_url: '/static/tools/gallery.png',
				data: ""
			}
		},
		methods: {
			takePhoto() {
				uni.chooseImage({
					success: (chooseImageRes) => {
						const tempFilePaths = chooseImageRes.tempFilePaths;
						this.image_url = tempFilePaths[0]
					}
				});
			},
			detectPhoto() {
				let that = this
				uni.uploadFile({
					url: 'http://192.168.12.8:9000/detect', //仅为示例，非真实的接口地址
					filePath: that.image_url,
					name: 'file',
					formData: {
						'user': 'test'
					},
					success: (uploadFileRes) => {
						let res = JSON.parse(uploadFileRes.data)
						console.log(res)
						that.image_url = 'http://192.168.12.8:9000' + res.result
						that.data = JSON.stringify(res.data)
					}
				});
			}
		}
	}
</script>

<style scoped lang="less">
	.camera-page {
		.camera-show {
			text-align: center;
		}
	}
</style>