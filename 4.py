import pygal
line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, ['age 0-9', 'age 10-19', 'age 20-29', 'age 30-39', 'age 40-49', 'age 50-59', 'age 60-69', 'age 70-79', 'age 80-89'])
line_chart.add('AGE', [2.41, 383.76, 1065.05, 1038.29, 761.29, 477.82, 311.17, 170.17, 52.76])
line_chart.render_to_file('age.svg')
