import json
from picking_tasks import PickingTask, PickingOrder

def decodePickingDataJSON(json_file):
	fileh = open(json_file)
	
	data = json.load(fileh)

	tasks = data['tasks']
	print(tasks[0]['orders'][1])
	
	for i in range(len(tasks)):
		json_task_i = tasks[i]
		json_orders = json_task_i['orders']

		task_i_id = json_task_i['taskId']
		isTraining = json_task_i['isTrainingTask']
		task_i = PickingTask(task_i_id, isTraining)

		for j in range(len(json_orders)):
			json_order_j = json_orders[j]
			order_id = json_order_j['orderId']

			pickingOrder = PickingOrder(order_id)

	fileh.close()

if __name__ == "__main__":
	import sys
	decodePickingDataJSON(sys.argv[1])