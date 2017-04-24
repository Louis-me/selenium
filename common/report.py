import xlsxwriter
class OperateReport:
    def __init__(self, wd):
        self.wd = wd
    def init(self, worksheet, data={}):
         # 设置列行的宽高
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")

        worksheet.merge_range('A1:D1', '测试报告总概况', define_format_H1)
        worksheet.merge_range('A2:D2', '测试概括', define_format_H2)
        _write_center(worksheet, "A3", '项目名称', self.wd)
        _write_center(worksheet, "A4", '用例总数', self.wd)
        _write_center(worksheet, "A5", '测试日期', self.wd)
        _write_center(worksheet, "B3", data['title'], self.wd)
        _write_center(worksheet, "B4", data['sum'], self.wd)
        _write_center(worksheet, "B5", data['test_date'], self.wd)
        _write_center(worksheet, "C3", "通过总数", self.wd)
        _write_center(worksheet, "C4", "失败总数", self.wd)
        _write_center(worksheet, "C5", "测试耗时", self.wd)
        _write_center(worksheet, "D3", data['pass'], self.wd)
        _write_center(worksheet, "D4", data['fail'], self.wd)
        _write_center(worksheet, "D5", data['sum_time'], self.wd)
        self.pie(self.wd, worksheet)

    def pie(self, workbook, worksheet):
     chart1 = workbook.add_chart({'type': 'pie'})
     chart1.add_series({
         'name': '自动化测试统计',
         'categories': '=测试总况!$C$3:$C$4',
         'values': '=测试总况!$D$3:$D$4',
     })
     chart1.set_title({'name': '自动化测试统计'})
     chart1.set_style(10)
     worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})
        # pie(self.wd, worksheet)
    def test_detail(self, worksheet, data=[{}]):
        # 设置列行的宽高
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)

        worksheet.merge_range('A1:H1', '测试详情', get_format(self.wd, {'bold': True, 'font_size': 18, 'align': 'center',
                                                                     'valign': 'vcenter', 'bg_color': 'blue',
                                                                     'font_color': '#ffffff'}))
        _write_center(worksheet, "A2", '用例ID', self.wd)
        _write_center(worksheet, "B2", '模块', self.wd)
        _write_center(worksheet, "C2", '用例介绍', self.wd)
        _write_center(worksheet, "D2", '用例名称', self.wd)
        _write_center(worksheet, "E2", '测试结果', self.wd)
        _write_center(worksheet, "F2", '失败原因', self.wd)
        _write_center(worksheet, "G2", '截图', self.wd)

        temp = 3
        for item in data:
            for k in item:
                _write_center(worksheet, "A" + str(temp), item["id"], self.wd)
                _write_center(worksheet, "B" + str(temp), item["moudle"], self.wd)
                _write_center(worksheet, "C" + str(temp), item["intr"], self.wd)
                _write_center(worksheet, "D" + str(temp), item["casename"], self.wd)
                _write_center(worksheet, "E" + str(temp), item["result"], self.wd)
                _write_center(worksheet, "F" + str(temp), item.get("reason", ""), self.wd)
                # _write_center(worksheet, "G" + str(temp), item["img"], self.wd)
                if item.get("img", "") == "":
                    _write_center(worksheet, "G" + str(temp), "", self.wd)
                else:
                    worksheet.set_row(temp-1, 100)
                    worksheet.insert_image('G' + str(temp), item["img"], {'x_scale': 0.2, 'y_scale':0.2})
                temp = temp + 1

                break
    def close(self):
        self.wd.close()
def get_format(wd, option={}):
    return wd.add_format(option)

def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center','valign': 'vcenter','border':num})
def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)

def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))
def set_row(worksheet, num, height):
    worksheet.set_row(num, height)


if __name__ == '__main__':
    info =[{'id': 'test001', 'img': 'D:\\app\\selenium\\log\\20170424172414\\登录功能CheckPoint_2_NG.png', 'result': '失败', 'moudle': '登录', 'casename': 'testLogin', 'intr': '登录功能', 'reason': '无法找到检查点'}, {'id': 'test002', 'img': 'D:\\app\\selenium\\log\\20170424172414\\设置CheckPoint_3_NG.png', 'result': '失败', 'moudle': '登录', 'casename': 'testSetting', 'intr': '设置', 'reason': '无法找到检查点'}]
    data = {'test_date': '2017-04-24 17:24:49', 'fail': 2, 'pass': 0, 'title': '项目名称', 'sum': 2, 'sum_time': '39秒'}

    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    re = OperateReport(wd=workbook)
    re.init(worksheet, data=data)
    re.test_detail(worksheet2, data=info)
    re.close()
    #



