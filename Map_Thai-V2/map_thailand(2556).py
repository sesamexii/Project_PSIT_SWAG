"""Map Thailand 2556"""
import requests,folium
import xlrd
def map_thailand():
    """Show map thailand and show the suicide rate in each province, separate male and female in the year 2556."""
    file_2556 = "C:/Users/admin.admin-PC/Desktop/Project_PSIT_SWAG/Data/2556.xls"
    workbook = xlrd.open_workbook(file_2556)
    sheet = workbook.sheet_by_index(0)
    list_rate = []
    list_suicide = []
    list_male = []
    list_female = []
    for i in range(4, 81):
        list_rate.append(str(sheet.cell_value(i, 11)))
        list_suicide.append(str(sheet.cell_value(i, 8)))
        list_male.append(str(sheet.cell_value(i, 6)))
        list_female.append(str(sheet.cell_value(i, 7)))
        if str(sheet.cell_value(i, 8)) == "นราธิวาส":
            break
    imap = folium.Map(location=[15.0000, 100.0000], zoom_start=7)
    list_one = [[18.586653, 99.023295], [19.896964, 99.851953], [18.791226, 99.009497], [12.710346, 101.130559], [12.610811, 102.088633], [19.214983, 100.144908], \
                [13.349855, 100.956761], [12.247227, 102.506697], [10.488862, 99.152830], [13.814812, 100.065513], [19.304669, 97.943770], [18.148071, 100.118720], \
                [15.702056, 100.012178], [13.521992, 99.791195], [18.293230, 99.414827], [17.009515, 99.870529], [16.303553, 101.153740], [14.891717, 100.393207], \
                [18.762005, 100.764256], [13.701824, 101.037841], [15.185280, 100.114941], [14.523917, 100.907547], [13.835648, 102.035261], [13.550055, 100.280514], \
                [14.459145, 100.084440], [14.010358, 99.457337], [14.802343, 100.641320], [12.963273, 99.641118], [17.621119, 100.110168], [7.553986, 99.601640], \
                [11.826060, 99.666830], [16.492846, 99.482608], [15.010249, 102.140600], [14.022129, 100.516166], [13.407223, 99.991299], [9.120066, 99.362991], \
                [14.200423, 101.190850], [8.421077, 99.877407], [14.034428, 101.631379], [16.884690, 99.096371], [15.397711, 100.002302], [13.592122, 100.599132], \
                [16.276729, 100.329681], [8.450931, 98.553625], [9.952928, 98.630417], [14.360477, 100.587340], [17.480160, 101.685196], [14.587764, 100.449866], \
                [7.949531, 98.333150], [14.985765, 103.060718], [15.810896, 102.015316], [13.757283, 100.544534], [14.023461, 100.502433], [7.608630, 100.071784], \
                [15.131690, 104.279828], [17.030188, 100.511542], [14.875375, 103.493077], [17.879109, 102.767585], [8.088373, 98.943127], [16.433487, 102.773562], \
                [15.874417, 104.616645], [16.009949, 103.084914], [15.791488, 104.150822], [17.223231, 102.322932], [16.549679, 104.470711], [16.051280, 103.636957], \
                [17.153904, 104.150815], [7.183917, 100.619733], [15.278368, 104.786886], [16.438208, 103.522093], [17.413266, 102.817054], [17.404481, 104.722714], \
                [18.360717, 103.634091], [6.621198, 100.056437], [6.534190, 101.263307], [6.761324, 101.340628],[6.431660, 101.788539]]
    list_two = ['ลำพูน', 'เชียงราย', 'เชียงใหม่', 'ระยอง', 'จันทบุรี', 'พะเยา', 'ชลบุรี', 'ตราด', 'ชุมพร', 'นครปฐม', 'แม่ฮ่องสอน', 'แพร่', 'นครสวรรค์', 'ราชบุรี', 'ลำปาง', 'สุโขทัย', 'เพชรบูรณ์', 'สิงห์บุรี', 'น่าน', 'ฉะเชิงเทรา', 'ชัยนาท',  'สระบุรี', 'สระแก้ว', 'สมุทรสาคร', 'สุพรรณบุรี', 'กาญจนบุรี', 'ลพบุรี', 'เพชรบุรี', 'อุตรดิตถ์', 'ตรัง', 'ประจวบคีรีขันธ์', 'กำแพงเพชร', 'นครราชสีมา', 'ปทุมธานี', 'สมุทรสงคราม', 'สุราษฎร์ธานี', 'นครนายก', 'นครศรีธรรมราช', 'ปราจีนบุรี', 'ตาก', 'อุทัยธานี', 'สมุทรปราการ', 'พิจิตร', 'พังงา', 'ระนอง', 'พระนครศรีอยุธยา', 'เลย', 'อ่างทอง', 'ภูเก็ต', 'บุรีรัมย์', 'ชัยภูมิ', 'กรุงเทพมหานคร', 'นนทบุรี', 'พัทลุง', 'ศรีสะเกษ', 'พิษณุโลก', 'สุรินทร์', 'หนองคาย', 'กระบี่', 'ขอนแก่น', 'อำนาจเจริญ', 'มหาสารคาม', 'ยโสธร', 'หนองบัวลำภู', 'มุกดาหาร', 'ร้อยเอ็ด', 'สกลนคร', 'สงขลา', 'อุบลราชธานี', 'กาฬสินธุ์', 'อุดรธานี', 'นครพนม', 'บึงกาฬ', 'สตูล', 'ยะลา', 'ปัตตานี', 'นราธิวาส']
    for i in range(77):
         popup1="""
               จังหวัด : %s <br>
               ปี พ.ศ. 2556 <br>
               จำนวนคนฆ่าตัวตาย(คน) : %s  <br>
               ผู้ชาย(คน) : %s  <br>
               ผู้หญิง(คน) : %s <br>
               อัตราการฆ่าตัวตายต่อประชากรหนึ่งแสนคน : %s <br>
               """ % (list_two[i],list_suicide[i],list_male[i],list_female[i],list_rate[i])
         imap.simple_marker(location=[list_one[i][0], list_one[i][1]], popup=(popup1))
    imap.create_map(path='map_thailand(2556).html')
map_thailand()

