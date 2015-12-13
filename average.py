"""Suicide Average"""
import xlrd
def average():
    """Print suicide average in 2540-2556"""
    file_2540 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2540.xls"
    file_2541 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2541.xls"
    file_2542 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2542.xls"
    file_2543 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2543.xls"
    file_2544 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2544.xls"
    file_2545 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2545.xls"
    file_2546 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2546.xls"
    file_2547 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2547.xls"
    file_2548 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2548.xls"
    file_2549 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2549.xls"
    file_2550 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2550.xls"
    file_2551 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2551.xls"
    file_2552 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2552.xls"
    file_2553 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2553.xls"
    file_2554 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2554.xls"
    file_2555 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2555.xls"
    file_2556 = "C:/Users/Administrator/Documents/GitHub/Project_PSIT_SWAG/Data/2556.xls"
    list_suicide = []
    list_excel = [file_2540, file_2541, file_2542, file_2543, file_2544, file_2545, file_2546,\
                  file_2547, file_2548, file_2549, file_2550, file_2551, file_2552, file_2553,\
                  file_2554, file_2555, file_2556]
    for data in list_excel[:14:]:
        workbook = xlrd.open_workbook(data)
        sheet = workbook.sheet_by_index(0)
        list_suicide.append(int(sheet.cell_value(82, 8)))
    for data in list_excel[15::]:
        workbook = xlrd.open_workbook(data)
        sheet = workbook.sheet_by_index(0)
        list_suicide.append(int(sheet.cell_value(81, 9)))
    workbook = xlrd.open_workbook(file_2554)
    sheet = workbook.sheet_by_index(0)
    list_suicide.append(int(sheet.cell_value(80, 9)))
    sc_average = sum(list_suicide)/16
    print("suicide per year :", sc_average)
    print("suicide per month :", suicide_per_month(sc_average))
    print("suicide per day :", suicide_per_day(suicide_per_month(sc_average)))

def suicide_per_month(data):
    """Return suicide people per month"""
    sc_per_month = data / 12
    return sc_per_month

def suicide_per_day(data):
    """Return suicide people per day"""
    sc_per_day = data / 31
    return sc_per_day

average()
