"""Top 5 Province"""
import xlrd
import math
import pygal
def top_province():
    """Print Top 5 Province that have most suicide"""
    file_2540 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2540.xls"
    file_2541 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2541.xls"
    file_2542 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2542.xls"
    file_2543 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2543.xls"
    file_2544 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2544.xls"
    file_2545 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2545.xls"
    file_2546 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2546.xls"
    file_2547 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2547.xls"
    file_2548 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2548.xls"
    file_2549 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2549.xls"
    file_2550 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2550.xls"
    file_2551 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2551.xls"
    file_2552 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2552.xls"
    file_2553 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2553.xls"
    file_2554 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2554.xls"
    file_2555 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2555.xls"
    file_2556 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2556.xls"
    list_excel = [file_2540, file_2541, file_2542, file_2543, file_2544, file_2545, file_2546,\
                  file_2547, file_2548, file_2549, file_2550, file_2551, file_2552, file_2553,\
                  file_2554, file_2555, file_2556]
    dict_city = {}
    for data in list_excel[:14:]:
        workbook = xlrd.open_workbook(data)
        sheet = workbook.sheet_by_index(0)
        for i in range(6, 82):
            dict_city.setdefault(str(sheet.cell_value(i, 2)), 0)
            suicide_num = str(0)
            for num in str(sheet.cell_value(i, 8)):
                if num != '.':
                    suicide_num = suicide_num + num
                else:
                    break
            dict_city[str(sheet.cell_value(i, 2))] += int(suicide_num)
    for data in list_excel[15::]:
        workbook = xlrd.open_workbook(data)
        sheet = workbook.sheet_by_index(0)
        for i in range(4, 81):
            dict_city.setdefault(str(sheet.cell_value(i, 3)), 0)
            suicide_num = str(0)
            for num in str(sheet.cell_value(i, 9)):
                if num != '.':
                    suicide_num = suicide_num + num
                else:
                    break
            dict_city[str(sheet.cell_value(i, 3))] += int(suicide_num)
    workbook = xlrd.open_workbook(file_2554)
    sheet = workbook.sheet_by_index(0)
    for i in range(3, 80):
        dict_city.setdefault(str(sheet.cell_value(i, 3)), 0)
        suicide_num = str(0)
        for num in str(sheet.cell_value(i, 9)):
            if num != '.':
                suicide_num = suicide_num + num
            else:
                break
        dict_city[str(sheet.cell_value(i, 3))] += int(suicide_num)
    #หาค่าเฉลี่ย
    for i in dict_city:
        if i == 'บึงกาฬ':
            dict_city[i] = dict_city[i]//3
        else:
            dict_city[i] = dict_city[i]//16
    list_most = list(sorted(dict_city.values(), reverse=True))
    for k, v in dict_city.items():
        if v == list_most[0] or v == list_most[1] or v == list_most[2]\
           or v == list_most[3] or v == list_most[4]:
            print(k, ':', v )
    line_chart = pygal.Bar()
    line_chart.title = 'Top five province'
    line_chart.add('เชียงใหม่', [320])
    line_chart.add('กรุงเทพมหานคร', [216])
    line_chart.add('นครราชสีมา', [197])
    line_chart.add('เชียงราย', [190])
    line_chart.add('ชลบุรี', [127])
    line_chart.render_to_file('top_province.svg')
top_province()
