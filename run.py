import os
import pytest
from config import Conf

if __name__ == '__main__':
    # report_path = Conf.get_report_path() + os.sep + "result"
    # report_html_path = Conf.get_report_path() + os.sep + "html"
    # pytest.main(["-s","--alluredir", report_path])
 report_path = Conf.get_report_path() + os.sep + "result"
 report_html_path = Conf.get_report_path() + os.sep + "html"
 # pytest.main(["-s","--alluredir", report_path])
 os.system('pytest --alluredir C:/Users/wangchao/Desktop/InterAutoTest/report/result --clean-alluredir')
 # os.system('allure serve ./report/result')
 # allure serve allure 报告目录 -o 生成html文件目录  --clean
 os.system('allure generate %s -o %s --clean'%(report_path,report_html_path))
 # os.system('allure serve ./report/result')
 # os.system('allure generate %s -o %s --clean' % ('C:/Users/wangchao/Desktop/InterAutoTest/report/result', 'C:/Users/wangchao/Desktop/InterAutoTest/report/html'))
 # os.system('allure generate C:/Users/wangchao/Desktop/InterAutoTest/report/result -o C:/Users/wangchao/Desktop/InterAutoTest/report/html  --clean')
 # os.system('--alluredir=C:/Users/wangchao/Desktop/InterAutoTest/report/result --clean-alluredir')
 # os.system("allure generate <allure测试结果目录> -o <存放报告的目录> --clean")
 # os.system("allure generate result -o html --clean")