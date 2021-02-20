import requests
import xlrd
from xlutils.copy import copy
from config.Conf import ConfigYaml
from config import Conf
import os
from common.ExcelDatat import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import CRequest
import json
import pytest
from common import Base
from utils.AssertUtil import AssertUtil
from common.Base import init_db
import allure
from utils.ExcelUtil import ExcelReader
from utils.operation_token import OperationHeader
from utils.operation_json import OperationJson
from utils.operation_excel import OperationExcel
from jsonpath_rw import jsonpath, parse
from utils.regxUtil import DoRegx
from common.get_data import Getdata



# # #读取excel用例
# excelDir = r'C:\Users\Administrator\PycharmProjects\InterAutoTest\data\testdata.xls'
# #1-1：打开excel--formatting_info=True
# workbook = xlrd.open_workbook(excelDir,formatting_info = True)
# workbookNew = copy(workbook)
# workSheetNew = workbookNew.get_sheet(0)
# # workSheet = workbook.sheet_by_name('美多商城接口测试')

#1、初始化信息
#1）.初始化测试用例文件
case_file = os.path.join(Conf.get_data_path(),ConfigYaml().get_excel_file())
result_file = os.path.join(Conf.get_data_path(),ConfigYaml().get_result_file())
#2）.初始化测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
ExcelReader(case_file, sheet_name).copy_excel()
#3）.获取运行测试用例列表
data_init = Data(case_file,sheet_name)
run_list = data_init.get_run_data()
#4）.日志
log = my_log()
#初始化dataconfig
data_key = ExcelConfig.DataConfig
#2、测试用例方法，参数化运行
#一个用例的执行
class TestExcel:
    #1、增加Pytest
    #2、修改方法参数
    #3、重构函数内容
    #4、pytest.main
    # def run_api(self,url,method,params=None,header=None,cookie=None):
    def run_api(self, url, method, params=None, header=None, cookie=str(getattr(Getdata,'cookies'))):
        """
        发送请求api
        :return:
        """
        # 2）.接口请求
        request = CRequest()
        header = Base.json_parse(header)
        cookie = Base.json_parse(cookie)
        # params 转义json
        # 验证params有没有内容
        if len(str(params).strip()) != 0:
            params = json.loads(params)
        # method post/get
        if str(method).lower() == "get":
            # 2.增加Headers
            res = request.get(url, json=params, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            res = request.post(url, json=params, headers=header, cookies=cookie)
        else:
            log.error("错误请求method: %s" % method)
        return res

    def run_pre(self,pre_case):
        case_id = pre_case[data_key.case_id]
        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]
        # header = Base.json_parse(headers)
        # cookie = Base.json_parse(cookies)
        res = self.run_api(url, method, params, headers, cookies)
        print("前置用例执行：%s"%res)
        return res

#1）.初始化信息，url，data
    # 1、增加Pytest
    @pytest.mark.parametrize("case",run_list)
    # 2、修改方法参数
    def test_run(self,case):
        # data_key = ExcelConfig.DataConfig
        case_no = int(case[data_key.case_no])
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_model]
        is_run = case[data_key.is_run]
        method = case[data_key.method]
        url = ConfigYaml().get_conf_url() + case[data_key.url]
        is_wtoken = case[data_key.is_wtoken]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        pre_exec = case[data_key.pre_exec]
        res_data = case[data_key.res_data]
        depend_field = case[data_key.depend_field]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        print('------params的类型：%s'%type(params))
        expect_result = case[data_key.expect_result]
        actual_result = case[data_key.actual_result]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]
        test_result = case[data_key.test_result]
        # 1、验证前置条件
        if pre_exec:
            pass
        # 2、找到执行用例
            # 前置测试用例
            # 判断pre_exec是依赖单个还是多个用例
            if pre_exec.find(',') != -1:
                pre_exec_list = pre_exec.split(",")
                # 对多个依赖用例进行循环请求并保存返回值
                for pre_exec in pre_exec_list:
                    pre_case = data_init.get_case_pre(pre_exec)
                    # 判断请求参数或者请求头是否有变量需要替换
                    if pre_case[data_key.headers].find('${')!=-1:
                        op_json = OperationJson("../data/token.json")
                        tokenvalue = op_json.get_data('data')['token']
                        setattr(Getdata, 'token', tokenvalue)
                        pre_case[data_key.headers] = DoRegx().do_regx(pre_case[data_key.headers])
                    if pre_case[data_key.params].find('${')!=-1:
                        DoRegx().get_parmvalue(pre_case[data_key.case_no])
                        pre_case[data_key.params] = DoRegx().do_regx(pre_case[data_key.params])
                    pre_res = self.run_pre(pre_case)
                    print('pre_res:%s' % pre_res)
                    print('pre_case[data_key.case_no]:%s' % pre_case[data_key.case_no])
                    # if pre_res["cookies"]:
                    #     pre_case[data_key.cookies] = pre_res["cookies"]
                    #     setattr(Getdata, 'cookies', pre_case[data_key.cookies])
                    # 如果header字段值为write则将该接口的返回的token写入到token.json文件
                    if pre_case[data_key.is_wtoken] == "write":
                        op_header = OperationHeader(pre_res)
                        op_header.write_token()
                    ExcelReader(result_file, sheet_name).write_value(pre_case[data_key.case_no], 16, str(pre_res))
            else:
                pre_case = data_init.get_case_pre(pre_exec)
                pre_res = self.run_pre(pre_case)
                if pre_case[data_key.is_wtoken] == "write":
                    op_header = OperationHeader(pre_res)
                    op_header.write_token()
                # if pre_res["cookies"]:
                #     pre_case[data_key.cookies] = pre_res["cookies"]
                #     setattr(Getdata, 'cookies', pre_case[data_key.cookies])
                ExcelReader(result_file,sheet_name).write_value(pre_case[data_key.case_no], 16, str(pre_res))
        if headers.find('${') != -1:
            op_json = OperationJson("../data/token.json")
            tokenvalue = op_json.get_data('data')['token']
            setattr(Getdata, 'token', tokenvalue)
            headers = DoRegx().do_regx(headers)
            # header = Base.json_parse(header)
            print("-----------header:%s"%headers)
        if params.find('${') != -1:
            DoRegx().get_parmvalue(case_no)
            params =DoRegx().do_regx(params)
            print("-----------params:%s" % params)
            print(type(params))
        res = self.run_api(url,method,params,headers,cookies)
        print("测试用例执行：%s" % res.text)

        # allure
        # sheet名称  feature 一级标签
        allure.dynamic.feature(sheet_name)
        # 模块   story 二级标签
        allure.dynamic.story(case_model)
        # 用例ID+接口名称  title
        allure.dynamic.title(case_id + case_name)
        # 请求URL  请求类型 期望结果 实际结果描述
        desc = "<font color='red'>请求URL-111: </font>{}<Br/>" \
               "<font color='red'>请求类型: </font>{}<Br/>" \
               "<font color='red'>期望结果: </font>{}<Br/>" \
               "<font color='red'>实际结果: </font>{}".format(url, method, expect_result, res)
        allure.dynamic.description(desc)

        # 断言验证
        # 状态码，返回结果内容，数据库相关的结果的验证
        # 状态码
        assert_util = AssertUtil()
        res_code = assert_util.assert_code(int(res["code"]), int(code))
        if res_code:
            # 返回结果内容
            is_body = assert_util.assert_in_body(str(res["body"]), str(expect_result))
            # 数据库结果断言
            # if len(db_verify):
            #     is_db = Base.assert_db("db_1", res["body"], db_verify)
            #     if is_db:
            #         workSheetNew.write(1,9,str(res))
            #         workSheetNew.write(1,16,'pass')
            #     else:
            #         workSheetNew.write(1,9,str(res))
            #         workSheetNew.write(1,16,'fail')
            if is_body:
                ExcelReader(result_file, sheet_name).write_value(case_no, 16, str(res))
                ExcelReader(result_file, sheet_name).write_value(case_no, 19, 'pass')
            else:
                ExcelReader(result_file, sheet_name).write_value(case_no, 16, str(res))
                ExcelReader(result_file, sheet_name).write_value(case_no, 19, 'fail')
        else:
            ExcelReader(result_file, sheet_name).write_value(case_no, 16, str(res))
            ExcelReader(result_file, sheet_name).write_value(case_no, 19, 'fail')


    def get_correlation(self,headers,cookies,pre_res,pattern_data):
        """
        关联
        :param headers:
        :param cookies:
        :param pre_res:
        :return:
        """
        #验证是否有关联
        headers_para,cookies_para = Base.params_find(headers,cookies,pattern_data)
        #有关联，执行前置用例，获取带有关联信息的结果
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
            # 结果替换
            headers = Base.res_sub(headers, headers_data,pattern_data)
        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
            # 结果替换
            cookies = Base.res_sub(headers, cookies_data,pattern_data)
        return headers, cookies



if __name__ == '__main__':
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep + "html"
    pytest.main(["-s", "return_excel_result.py", "--alluredir", report_path])
    # params='{ "address":"1","pay_method":"1","token":"${token}","mobile":"${mobile}"}'
    # DoRegx().get_parmvalue(9)
    # params = DoRegx().do_regx(params)
    # print("params:%s" % params)
    # workbook = xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\InterAutoTest\data\testdata_res.xls')
    # worksheet = workbook.sheet_by_name('美多商城接口测试')
    # lng = worksheet.cell(10,11).value
    # print('第3行值', lng)
