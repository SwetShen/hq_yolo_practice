<template>
	<view class="watch-page">
		<view class="container">
			<echartsUniappVue ref="echarts" :option="option1" canvasId="echarts"></echartsUniappVue>
		</view>
		<view class="predict">
			<echartsUniappVue ref="predict" :option="option2" canvasId="predict"></echartsUniappVue>
		</view>
	</view>

</template>

<script>
	import echartsUniappVue from '../../components/echarts-uniapp/echarts-uniapp.vue';

	export default {
		data() {
			return {
				option1: {},
				option2: {}
			}
		},
		components: {
			echartsUniappVue
		},
		onReady() {
			this.option1 = {
				title: {
					text: '监控内容统计',
					subtext: '2025年3月25日',
					left: 'center'
				},
				tooltip: {
					trigger: 'item'
				},
				legend: {
					orient: 'vertical',
					left: 'left'
				},
				series: [{
					name: 'Access From',
					type: 'pie',
					radius: '50%',
					data: [{
							value: 1048,
							name: 'Person'
						},
						{
							value: 735,
							name: 'Car'
						},
						{
							value: 580,
							name: 'Bus'
						},
						{
							value: 484,
							name: 'Dog'
						},
						{
							value: 300,
							name: 'Bicycle'
						}
					],
					emphasis: {
						itemStyle: {
							shadowBlur: 10,
							shadowOffsetX: 0,
							shadowColor: 'rgba(0, 0, 0, 0.5)'
						}
					}
				}]
			};

			this.option2 = {
				title: {
					text: ''
				},
				tooltip: {
					trigger: 'axis',
					axisPointer: {
						type: 'cross',
						label: {
							backgroundColor: '#6a7985'
						}
					}
				},
				legend: {
					data: ['真实人流量', '模型预测人流量']
				},
				toolbox: {
					feature: {
						saveAsImage: {}
					}
				},
				grid: {
					left: '3%',
					right: '4%',
					bottom: '3%',
					containLabel: true
				},
				xAxis: [{
					type: 'category',
					boundaryGap: false,
					data: ['6:00-8:00', '8:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00',
						'16:00-18:00'
					]
				}],
				yAxis: [{
					type: 'value'
				}],
				series: [{
						name: '真实人流量',
						type: 'line',
						stack: 'Total',
						areaStyle: {},
						emphasis: {
							focus: 'series'
						},
						data: [120, 132, 101, 134, 90, 230, 210]
					},
					{
						name: '模型预测人流量',
						type: 'line',
						stack: 'Total',
						areaStyle: {},
						emphasis: {
							focus: 'series'
						},
						data: [220, 182, 191, 234, 290, 330, 310]
					}
				]
			};

		}
	}
</script>
<style scoped>
	.container {
		height: 600rpx;
	}
	.predict{
		height: 400rpx;
	}
</style>