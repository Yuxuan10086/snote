<template>
	<a-menu
		id="dddddd"
		v-model:openKeys="openKeys"
		v-model:selectedKeys="selectedKeys"
		style="width: 256px"
		mode="inline"
		:items="items"
		@click="handleClick"
	></a-menu>
</template>


<script lang="ts" setup>
import { reactive, ref, watch, VueElement, onMounted, h } from 'vue';
import { BarChartOutlined, CalendarOutlined, CheckSquareOutlined} from '@ant-design/icons-vue';
import type { MenuProps, ItemType } from 'ant-design-vue';
import axios from "axios";

const selectedKeys = ref<string[]>(['1']);
const openKeys = ref<string[]>(['sub1']);

function getItem(
	label: VueElement | string,
	key: string,
	icon?: any,
	children?: ItemType[],
	type?: 'group',): ItemType { 
		return { key, icon, children, label, type, } as ItemType;
}

const items: ItemType[] = reactive([]);

axios.get("http://127.0.0.1:8000/navigation?user_id=1")
    .then(response => {
        const data = response.data;
        const newItems: ItemType[] = [];
		let icon;
		let keyPrefix:string;

		icon = () => h(BarChartOutlined);
		keyPrefix = "gantt";
		const gantt_children: any = (data.navigation[0].children || []).map((child: any) =>
			getItem(child.name, `${keyPrefix}_child_${child.id}`)
		);
		newItems.push(getItem(data.navigation[0].name, `${keyPrefix}`, icon, gantt_children));

		newItems.push(getItem("待办", "todo", h(CheckSquareOutlined)));

		icon = () => h(CalendarOutlined);
		keyPrefix = "daily";
		const daily_children: any = (data.navigation[1].children || []).map((child: any) =>
			getItem(child.date, `${keyPrefix}_child_${child.id}`)
		);
		newItems.push(getItem(data.navigation[1].name, `${keyPrefix}`, icon, daily_children));
		
        items.splice(0, items.length, ...newItems);
    })
    .catch(error => {
        console.error("获取导航栏数据失败:", error);
    });

// const itemm: ItemType[] = reactive([
// 	getItem('Navigation One', 'sub1', () => h(MailOutlined), [
// 		getItem('Item 1', 'g1', null, [getItem('Option 1', '1'), getItem('Option 2', '2')], 'group'),
// 		getItem('Item 2', 'g2', null, [getItem('Option 3', '3'), getItem('Option 4', '4')], 'group'),
// 	]),

// 	getItem('Navigation Two', 'sub2', () => h(AppstoreOutlined), [
// 		getItem('Option 5', '5'),
// 		getItem('Option 6', '6'),
// 		getItem('Submenu', 'sub3', null, [getItem('Option 7', '7'), getItem('Option 8', '8')]),
// 	]),
// ]);
// items.splice(0, items.length, ...itemm);
// console.log(items);

const handleClick: MenuProps['onClick'] = e => {
	console.log('click', e);
};

watch(openKeys, val => {
	console.log('openKeys', val);
});

</script>
	
	