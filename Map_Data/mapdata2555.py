"""Map list data"""
import xlrd
def map_data(list_rate, list_suicide, list_male, list_female):
    """
       Print 4 list of data in 2555 thare are
       1.  list_rate
           In this list are data of suicide rate each province.
       2.  list_suicide
           In this list are data of amount of people that suicided
       3.  list_male
           In this list are data of male Thai that suicided
       4.  list_female
           In this list are data of female Thai that suicided
    """
    file_2555 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2555.xls"
    workbook = xlrd.open_workbook(file_2555)
    sheet = workbook.sheet_by_index(0)
    for i in range(6, 82):
        list_rate.append(str(sheet.cell_value(i, 11)))
        list_suicide.append(str(sheet.cell_value(i, 8)))
        list_male.append(str(sheet.cell_value(i, 6)))
        list_female.append(str(sheet.cell_value(i, 7)))
    print(list_rate)
    print(list_suicide)
    print(list_male)
    print(list_female)
map_data([], [], [], [])
