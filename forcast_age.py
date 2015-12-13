"""Graph """
import xlrd
import pygal
def forecast_age():
    """Write forecast_age graph in SVG file"""
    file_age = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/work.xls"
    workbook = xlrd.open_workbook(file_age)
    sheet = workbook.sheet_by_index(0)
    list_age_0_9 = []
    list_age_10_19 = []
    list_age_20_29 = []
    list_age_30_39 = []
    list_age_40_49 = []
    list_age_50_59 = []
    list_age_60_69 = []
    list_age_70_79 = []
    list_age_80_up = []
    for i in range(2, 19):
        list_age_0_9.append(int(sheet.cell_value(i, 2)))
        list_age_10_19.append(int(sheet.cell_value(i, 3)))
        list_age_20_29.append(int(sheet.cell_value(i, 4)))
        list_age_30_39.append(int(sheet.cell_value(i, 5)))
        list_age_40_49.append(int(sheet.cell_value(i, 6)))
        list_age_50_59.append(int(sheet.cell_value(i, 7)))
        list_age_60_69.append(int(sheet.cell_value(i, 8)))
        list_age_70_79.append(int(sheet.cell_value(i, 9)))
        list_age_80_up.append(int(sheet.cell_value(i, 10)))
    list_age_0_9.append(sum(list_age_0_9[6:])/11)
    list_age_10_19.append(sum(list_age_10_19[6:])/11)
    list_age_20_29.append(sum(list_age_20_29[6:])/11)
    list_age_30_39.append(sum(list_age_30_39[6:])/11)
    list_age_40_49.append(sum(list_age_40_49[6:])/11)
    list_age_50_59.append(sum(list_age_50_59[6:])/11)
    list_age_60_69.append(sum(list_age_60_69[6:])/11)
    list_age_70_79.append(sum(list_age_70_79[6:])/11)
    list_age_80_up.append(sum(list_age_80_up[6:])/11)
    line_chart = pygal.Line()
    line_chart.title = 'Forecast suicide direction'
    line_chart.x_labels = ('2540', '2541', '2542', '2543', '2544', '2545', '2546', '2547',\
                              '2548', '2549', '2550', '2551', '2552', '2553', '2554', '2555',\
                              '2556', 'predict')
    line_chart.add('age 0-9', list_age_0_9)
    line_chart.add('age 10-19', list_age_10_19)
    line_chart.add('age 20-29', list_age_20_29)
    line_chart.add('age 30-39', list_age_30_39)
    line_chart.add('age 40-49', list_age_40_49)
    line_chart.add('age 50-59', list_age_50_59)
    line_chart.add('age 60-69', list_age_60_69)
    line_chart.add('age 70-79', list_age_70_79)
    line_chart.add('age 80 up', list_age_80_up)
    line_chart.render_to_file('forecast_age.svg')
forecast_age()
