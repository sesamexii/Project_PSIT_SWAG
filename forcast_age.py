"""Graph """
import xlrd
def forcast_age():
    """Write forcast_age graph in SVG file"""
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
    print(list_age_0_9)
    print(list_age_10_19)
    print(list_age_20_29)
    print(list_age_30_39)
    print(list_age_40_49)
    print(list_age_50_59)
    print(list_age_60_69)
    print(list_age_70_79)
    print(list_age_80_up)
forcast_age()
