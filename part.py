"""Top part"""
import xlrd
import pygal
def top_part():
    """Arrange suicide of part by maximun to minimun"""
    central, west, east, north, south, north_e = 0, 0, 0, 0, 0, 0
    file_2540 = "D:/Excel_PSIT/2540.xls"
    file_2541 = "D:/Excel_PSIT/2541.xls"
    file_2542 = "D:/Excel_PSIT/2542.xls"
    file_2543 = "D:/Excel_PSIT/2543.xls"
    file_2544 = "D:/Excel_PSIT/2544.xls"
    file_2545 = "D:/Excel_PSIT/2545.xls"
    file_2546 = "D:/Excel_PSIT/2546.xls"
    file_2547 = "D:/Excel_PSIT/2547.xls"
    file_2548 = "D:/Excel_PSIT/2548.xls"
    file_2549 = "D:/Excel_PSIT/2549.xls"
    file_2550 = "D:/Excel_PSIT/2550.xls"
    file_2551 = "D:/Excel_PSIT/2551.xls"
    file_2552 = "D:/Excel_PSIT/2552.xls"
    file_2553 = "D:/Excel_PSIT/2553.xls"
    file_2554 = "D:/Excel_PSIT/2554.xls"
    file_2555 = "D:/Excel_PSIT/2555.xls"
    file_2556 = "D:/Excel_PSIT/2556.xls"
    list_excel = [file_2540, file_2541, file_2542, file_2543, file_2544, file_2545, file_2546,\
                  file_2547, file_2548, file_2549, file_2550, file_2551, file_2552, file_2553,\
                  file_2554, file_2555, file_2556]
    for data in list_excel:
        workbook = xlrd.open_workbook(data)
        sheet = workbook.sheet_by_index(0)
        if data in [file_2540, file_2541, file_2542, file_2543, file_2544, file_2545, file_2546,\
                  file_2547, file_2548, file_2549, file_2550, file_2551, file_2552, file_2553]:
            for i in range(6, 82):
                if 80 <= sheet.cell_value(i, 1) and sheet.cell_value(i, 1) <= 96:
                    south += sheet.cell_value(i, 8)
                elif 30 <= sheet.cell_value(i, 1) and sheet.cell_value(i, 1) <= 49:
                    north_e += sheet.cell_value(i, 8)
                elif 50 <= sheet.cell_value(i, 1) and sheet.cell_value(i, 1) <= 58:
                    north += sheet.cell_value(i, 8)
                elif sheet.cell_value(i, 1) in [63, 70, 71, 76, 77]:
                    west += sheet.cell_value(i, 8)
                elif sheet.cell_value(i, 1) in [20, 21, 22, 23, 24, 25, 27]:
                    east += sheet.cell_value(i, 8)
                else:
                    central += sheet.cell_value(i, 8)
        elif data == file_2554:
            for i in range(3, 80):
                if 80 <= sheet.cell_value(i, 2) and sheet.cell_value(i, 2) <= 96:
                    south += sheet.cell_value(i, 9)
                elif 30 <= sheet.cell_value(i, 2) and sheet.cell_value(i, 2) <= 49:
                    north_e += sheet.cell_value(i, 9)
                elif 50 <= sheet.cell_value(i, 2) and sheet.cell_value(i, 2) <= 58:
                    north += sheet.cell_value(i, 9)
                elif sheet.cell_value(i, 2) in [63, 70, 71, 76, 77]:
                    west += sheet.cell_value(i, 9)
                elif sheet.cell_value(i, 2) in [20, 21, 22, 23, 24, 25, 27]:
                    east += sheet.cell_value(i, 9)
                else:
                    central += sheet.cell_value(i, 9)
        elif data in [file_2555, file_2556]:
            for i in range(4, 81):
                if 80 <= sheet.cell_value(i, 2) and sheet.cell_value(i, 2) <= 96:
                    south += sheet.cell_value(i, 9)
                elif 30 <= sheet.cell_value(i, 2) and sheet.cell_value(i, 2) <= 49:
                    north_e += sheet.cell_value(i, 9)
                elif 50 <= sheet.cell_value(i, 2) and sheet.cell_value(i, 2) <= 58:
                    north += sheet.cell_value(i, 9)
                elif sheet.cell_value(i, 2) in [63, 70, 71, 76, 77]:
                    west += sheet.cell_value(i, 9)
                elif sheet.cell_value(i, 2) in [20, 21, 22, 23, 24, 25, 27]:
                    east += sheet.cell_value(i, 9)
                else:
                    central += sheet.cell_value(i, 9)
    top = []
    for i in [central, west, east, north, south, north_e]:
        top.append(i)
    top = sorted(top)
    coun = 1
    for i in top[::-1]:
        if i == central:
            print(str(coun)+" : Central " + str(int(i)))
        elif i == west:
            print(str(coun)+" : West " + str(int(i)))
        elif i == east:
            print(str(coun)+" : East " + str(int(i)))
        elif i == north:
            print(str(coun)+" : North " + str(int(i)))
        elif i == south:
            print(str(coun)+" : South " + str(int(i)))
        else:
            print(str(coun)+" : NorthEast " + str(int(i)))
        coun += 1
        line_chart = pygal.Bar()
        line_chart.title = 'Suicide region of Thailand'
        line_chart.add('Central', [20417/16])
        line_chart.add('NorthEast', [18083/16])
        line_chart.add('North', [15359/16])
        line_chart.add('South', [8047/16])
        line_chart.add('East', [6518/16])
        line_chart.add('West', [4125/16])
        line_chart.render_to_file('suicide_region.svg')
top_part()
