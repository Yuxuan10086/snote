<template>
	<div id="basic-layout">
		<a-layout>
			<a-layout-sider class="sider" :width="256">
				<Sider />
			</a-layout-sider>
			<a-layout>
				<a-layout-header class="header">Header</a-layout-header>
				<a-layout-content class="content">
					<router-view />
				</a-layout-content>
			</a-layout>
		</a-layout>
	</div>
</template>

<script setup lang="ts">
import Sider from "@/components/GlobalSider.vue";
</script>

<style scoped>
	#basic-layout .header{
		text-align: center;
		color: #fff;
		height: 64px;
		padding-inline: 50px;
		line-height: 64px;
		background-color: #7dbcea;
	}
	#basic-layout .content{
		color: #000;
		text-align: center;
  		background-color: '#108ee9';
		height: 500px;
	}
	#basic-layout .sider{
		background-color: transparent;
	}
</style>
