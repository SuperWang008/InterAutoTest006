import configparser
from config.Conf import *

class Readconfig:
    def read_config(self,file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf.get(section,option)

if __name__=='__main__':
    res = eval(Readconfig().read_config(test_config_file, 'MODE', 'mode'))
    for key in res:
        print(key)
