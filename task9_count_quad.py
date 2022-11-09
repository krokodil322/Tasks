

def processing_input_data() -> None:
	quarter_points = {
				  		"Первая четверть": 0, 
				  		"Вторая четверть": 0,
				  		"Третья четверть": 0,
				  		"Четвертая четверть": 0
				 	 }
	amount_of_ponts = int(input())
	points, input_point = [{'x': 0, 'y': 0} for quan in range(0, amount_of_ponts)], []
	count = 0
	while count != amount_of_ponts:
		input_point = input().split()
		points[count]['x'] = int(input_point[0])
		points[count]['y'] = int(input_point[1])
		count += 1
	quarter_points = analysis_points(points, quarter_points)
	for key, value in quarter_points.items():
		print(f"{key}: {value}")
	
	return None


def analysis_points(points: list, quarter_points: dict) -> dict:
	count = 0
	while count != len(points):
		if points[count]['x'] > 0 and points[count]['y'] > 0:
			quarter_points["Первая четверть"] += 1
		elif points[count]['x'] < 0 and points[count]['y'] > 0:
			quarter_points["Вторая четверть"] += 1
		elif points[count]['x'] < 0 and points[count]['y'] < 0:
			quarter_points["Третья четверть"] += 1
		elif points[count]['x'] > 0 and points[count]['y'] < 0:
			quarter_points["Четвертая четверть"] += 1
		count += 1

	return quarter_points


processing_input_data()