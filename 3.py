import pygal
line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2540, 2558))
line_chart.add('Male', [10.66, 12.62, 13.32, 13.36, 11.9, 11.97, 10.98, 10.52, 9.87, 9.24, 9.48, 9.32, 9.36, 9.29, 9.45, 9.66, 9.7, 10])
line_chart.add('Female', [3.2, 3.65, 3.91, 3.7, 3.64, 3.77, 3.34, 3.3, 2.88, 2.38, 2.55, 2.72, 2.68, 2.62, 2.72, 2.85, 2.58, 2.64])
line_chart.render_to_file('thailand2014.svg')

