import os
import xlrd
from xlutils.copy import copy

#目的：参数化，pytest list
#自定义异常
class SheetTypeError:
    pass
#1、验证文件是否存在，存在读取，不存在报错
class ExcelReader:
    def __init__(self,excel_file,sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileExistsError("文件不存在")
#2、读取sheet方式，名称，索引
    def data(self):
        #存在data值不读取，不存在data值读取
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [str,int]:
                raise SheetTypeError("请输入Int or Str")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)
    #3、读取sheet内容
            #返回list，元素：字典
            # 格式[{"a":"a1","b":"b1"},{"a":"a2","b":"b2"}]
            # 1.获取首行的信息
            title = sheet.row_values(0)
            #print(title)
            # 2.遍历测试行，与行首组成dict，放在list
                #1 循环，过滤首行，从1开始
            for col in range(1,sheet.nrows):
                col_value = sheet.row_values(col)
                a = dict(zip(title, col_value))
                a["sheet_name"] = self.sheet_by
                print(a)
                # 2 与首组成字典，放list
                # self._data.append(dict(zip(title, col_value)))
                self._data.append(a)
#4、结果返回
        return self._data

# 写入数据
    def write_value(self,excel_file,sheet_by,row, col, value):
            '''
            写入到excel数据
            row,col,value
            '''
            read_data = xlrd.open_workbook(excel_file,formatting_info = True)
            write_data = copy(read_data)
            sheet_data = write_data.get_sheet(sheet_by)
            sheet_data.write(row, col, value)
            # write_data.save(self.excel_file)
            write_data.save('../data/testdata_res.xls')

    def copy_excel(self):
            '''
            写入到excel数据
            row,col,value
            '''
            read_data = xlrd.open_workbook(self.excel_file,formatting_info = True)
            write_data = copy(read_data)
            # write_data.save('../data/testdata_res.xls')
            write_data.save(r'C:\Users\wangchao\Desktop\InterAutoTest\data\testdata_res.xls')

head = ["a","b"]
value1 = ["a1","b1"]
value2 =  ["a2","b2"]
data_list= list()
# #zip
# print(list(zip(head,value1)))
# print(dict(zip(head,value1)))
# print(dict(zip(head,value2)))
# data_list.append(dict(zip(head,value1)))
# data_list.append(dict(zip(head,value2)))
# print(data_list)

if __name__ == "__main__":
    reader = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
    print(reader.data())