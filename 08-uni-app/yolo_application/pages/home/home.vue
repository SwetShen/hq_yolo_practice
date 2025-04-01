<template>
	<view class="home-page">
		<view class='adv'>
			<swiper class="adv-swiper" circular indicator-dots="true" autoplay="autoplay">
				<swiper-item class="swiper-item">
					<image mode="aspectFill" src="/static/adv/bg.jpg"></image>
				</swiper-item>
				<swiper-item class="swiper-item">
					<image mode="aspectFill" src="/static/adv/bg2.jpg"></image>
				</swiper-item>
				<swiper-item class="swiper-item">
					<image mode="aspectFill" src="/static/adv/bg3.jpg"></image>
				</swiper-item>
			</swiper>
		</view>
		<view class="news">
			<view class="home-header">
				<view class="home-title">新闻热点</view>
				<view class="home-more">查看更多>></view>
			</view>
			<ul>
				<li>🔈区经济负责人陈云海同志访问公司</li>
				<li>🎉公司AI产业转型取得重大成果</li>
				<li>👍同事王星在全国高校比赛中作为评委</li>
				<li>👊跟进时事，抓住机遇，认真对待</li>
			</ul>
		</view>
		<view class='nav'>
			<view class="home-header">
				<view class="home-title">监测功能</view>
				<view class="home-more">查看更多>></view>
			</view>
			<ul class="nav-list">
				<li @click="openCamera">
					<view>拍摄检测</view>
					<image src="/static/tools/cap.png"></image>
				</li>
				<li>
					<view>实时检测</view>
					<image src="/static/tools/face-detection.png"></image>
				</li>
				<li>
					<view>串流设备</view>
					<image src="/static/tools/live.png"></image>
				</li>
				<li>
					<view>其他功能</view>
					<image src="/static/tools/gallery.png"></image>
				</li>
			</ul>
		</view>
		<view class='info'>
			<view class="home-header">
				<view class="home-title">公司产品</view>
				<view class="home-more">查看更多>></view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data(){
			return {
				
			}
		},
		methods:{
			openCamera(){
				uni.navigateTo({
					url:'/pages/camera/camera'
				})
			}
		}
	}
</script>

<style lang="less">
.home-page{
	.adv{
		.adv-swiper{
			width: 100%;
			height: 400rpx;
			.swiper-item{
				image{
					width: 100%;
				}
			}
		}
	}
	.news{
		margin: 10rpx 0;
	}
	.nav{
		margin: 10rpx 0;
		.nav-list{
			display: flex;
			flex-wrap: wrap;
			padding: 0;
			justify-content: space-between;
			li{
				border: 2rpx solid #666666;
				list-style: none;
				width: 30%;
				padding: 20rpx 0;
				margin: 10rpx;
				text-align: center;
				image{
					width: 80rpx;
					height: 80rpx;
				}
			}
		}
	}
	.home-header{
		display: flex;
		justify-content: space-between;
		margin: 30rpx 20rpx;
		background-color: #8a8a8a;
		.home-title{
			background-color: #d81e06;
			padding: 5rpx 10rpx;
			color: white;
		}
		.home-more{
			float: right;
			color: white;
			font-size: 20rpx;
		}
	}
}
</style>