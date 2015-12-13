"""
This File is put the data from .xls file (MS Excel) to list by
create sub-list data that have index from province numberic code
and storage raw data by put it in form [[province_code, province_name,
male_population, female_population, total_population, suicided_male,
suicided_female, total_suicided, male_sphtpr, female_sphtpr,
total_sphtpr], [...]](sphtpr: suicide per hundred thousand population rate)
"""
import xlrd
#help you by sort data
def sortsheet(file_dir, prov_max=100):
    """return list of sub-list data by enter .xls file direrctory
       to use your must call function like getsheet(str(dir))[code][sub]
       prov_max is maximum of province code
       data summary has province key = 0
       use '/' not '\\' in dir path
    """
    workbook = xlrd.open_workbook(file_dir)
    sheet = workbook.sheet_by_index(0)
    ##the code above is open excel sheet(python begin at 0)
    ##sheet.cell_value(row, col) used to look at cell directly
    data_slot = []
    for i in range(prov_max): data_slot.append([i])
    list_pos = 0
    for row_num in range(6, sheet.nrows):
        temp = []
        for col_num in range(1, sheet.ncols):
            temp.append(sheet.cell_value(row_num, col_num))
        if type(temp[0]) == float or type(temp[0]) == int:
            list_pos = int(temp[0])
        else:
            list_pos = 0
        data_slot[list_pos] = temp
    return data_slot

###uncomment below to see output###
##  all data  ##
#print(sortsheet(str(input("Enter data directory: "))))
##  easy and only one province  ##
#all_data = sortsheet(str(input("Enter data directory: ")))
#bangkok = all_data[10]
#print(bangkok)
##  specific data(bangkok male population)  ##
#all_data = sortsheet(str(input("Enter data directory: ")))
#bkk_male_pop = all_data[10][3]
#print(bkk_male_pop)
