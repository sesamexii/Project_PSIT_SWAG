"""Map list data"""
import xlrd
def map_data(list_rate, list_suicide, list_male, list_female):
    """
       Print 4 list of data in 2554 thare are
       1.  list_rate
           In this list are data of suicide rate each province.
       2.  list_suicide
           In this list are data of amount of people that suicided
       3.  list_male
           In this list are data of male Thai that suicided
       4.  list_female
           In this list are data of female Thai that suicided
    """
    file_2554 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2554.xls"
    workbook = xlrd.open_workbook(file_2554)
    sheet = workbook.sheet_by_index(0)
    for i in range(3, 80):
        list_rate.append(str(sheet.cell_value(i, 12)))
        list_suicide.append(str(sheet.cell_value(i, 9)))
        list_male.append(str(sheet.cell_value(i, 7)))
        list_female.append(str(sheet.cell_value(i, 8)))
    print(list_rate)
    print(list_suicide)
    print(list_male)
    print(list_female)
map_data([], [], [], [])
