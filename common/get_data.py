import pandas as pd
import os


class Getdata:
      SMScode=None
      moblie=None
      pwd=88888888
      token=None
      username=None
      cookies=None
      id=None

      # 项目路径：
      base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
      # 测试用例路径
      case_path = os.path.join(base_path, 'data', 'testdata.xls')
      name = pd.read_excel(case_path,sheet_name='init').iloc[0, 1]


if __name__ == '__main__':
    print(Getdata.base_path)
    print(Getdata.case_path)
    print(Getdata.name)
