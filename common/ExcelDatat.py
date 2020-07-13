from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig
from config.Conf import ConfigYaml

class Data:
    def __init__(self,testcase_file,sheet_name):
    #1、使用excel工具类，获取结果list
       #self.reader = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
       self.reader = ExcelReader(testcase_file,sheet_name)
       #print(reader.data())
    #2、列是否运行内容，y代表运行
    def get_run_data(self):
        """
        根据是否运行列==y，获取执行测试用例
        :return:
        """
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                #print(line)
        #3、保存要执行结果，放到新的列表。
                run_list.append(line)
        print(run_list)
        return run_list

    def get_case_list(self):
        """
        获取全部测试用例
        :return:
        """
        # run_list=list()
        # for line in self.reader.data():
        #         run_list.append(line)
        # return run_list
        # 列表推导方法
        run_list = [line for line in self.reader.data()]
        return run_list

    def get_case_pre(self,pre):
        """
        根据前置条件：从全部测试用例取到测试用例
        :param pre:
        :return:
        """
        # 获取全部测试用例
        run_list = self.get_case_list()
        # list判断，执行，获取
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None

