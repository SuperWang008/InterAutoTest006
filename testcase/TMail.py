import json
from common.Base import init_db
from utils.RequestsUtil import requests_get
from utils.RequestsUtil import requests_post
from utils.RequestsUtil import CRequest
from config.Conf import ConfigYaml
import pytest
from utils.AssertUtil import AssertUtil

"""
登录	登录成功	http://meiduo.boxuegu.cn/authorizations/
	POST	json	{"username":"python","password":"12345678"}
"""
#登录
#1、导入包
import requests
#2、定义登录方法
def test_login():
#3、定义测试数据
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path+"/authorizations/"
    #url="http://211.103.136.242:8064/authorizations/"
    data={"username":"python","password":"12345678"}
#4、发送POST请求
    #r=requests.post(url,json=data)
    #r=requests_post(url,json=data)
    req = CRequest()
    r = req.post(url,json=data)
#5、输出结果
    #print(r.json())
    print(r)
    #验证
    #返回状态码
    code = r["code"]
    #assert code == 200
    AssertUtil().assert_code(code,200)
#返回结果内容
    #body = json.dumps(r["body"])
    body = r["body"]
    #assert '"user_id": 1, "username": "python"' in body
    AssertUtil().assert_in_body(body,'"username": "python", "user_id": 1')

    #1、初始化数据库对象
    conn = init_db("db_1")
    #2、查询结果
    res_db = conn.fetchone("select id,username from tb_users where username='python'")
    print("数据库查询结果",res_db)
    #3、验证
    user_id = body["user_id"]
    assert user_id == res_db["id"]
    #2、查询数据信息
    #3、验证


"""
个人信息	获取个人信息正确	http://211.103.136.242:8064/user/	登录	get	
 headers: {
           'Authorization': 'JWT ' + this.token
 }
"""
def testinfo():
    #1、参数
    url="http://211.103.136.242:8064/user/"
    token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTM3MDIyMTAsInVzZXJuYW1lIjoicHl0aG9uIiwiZW1haWwiOiI5NTI2NzM2MzhAcXEuY29tIiwidXNlcl9pZCI6MX0.ru_DABMxzjywE_HynLA6a9XGLcQQy6KNyIP-5xQ-S_g'}"
    headers = {
           'Authorization': 'JWT ' + token
    }
    #2、get请求
    #r=requests.get(url,headers=headers)
    #r=requests_get(url,headers=headers)
    #from utils.RequestsUtil import CRequest
    req = CRequest()
    r = req.get(url,headers=headers)
    #输出
    #print(r.json())
    print(r)

"""
商品列表数据	商品列表数据正确	
http://211.103.136.242:8064/categories/115/skus/
get    json	" {
 ""page"":""1"",
 ""page_size"": ""10"",
 ""ordering"": ""create_time""
 }"
 """
def goods_list():
    #1、参数
    url = "http://211.103.136.242:8064/categories/115/skus/"
    data  = {
             "page":"1",
             "page_size": "10",
             "ordering": "create_time"
             }
    #2、请求
    r = requests.get(url,json=data)
    #3、结果
    print(r.json())
"""
购物车	添加购物车成功	http://211.103.136.242:8064/cart/	
登录	post	json	
{"sku_id": "3","count": "1", "selected": "true"}"""

def cart():
    url = "http://211.103.136.242:8064/cart/"
    data = {"sku_id": "3","count": "1", "selected": "true"}
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTM3MDIyMTAsInVzZXJuYW1lIjoicHl0aG9uIiwiZW1haWwiOiI5NTI2NzM2MzhAcXEuY29tIiwidXNlcl9pZCI6MX0.ru_DABMxzjywE_HynLA6a9XGLcQQy6KNyIP-5xQ-S_g'}"
    headers = {
        'Authorization': 'JWT ' + token
    }
    r = requests.post(url,json=data,headers=headers)
    #r = requests_post(url,json=data,headers=headers)
    print(r.json())
    #print(r)

"""
订单	保存订单	http://211.103.136.242:8064/orders/	
登录	post	json	{ "address":"1","pay_method":"1" }
"""
def order():
    url = "http://211.103.136.242:8064/orders/"
    data = { "address":"1","pay_method":"1" }
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTM3MDIyMTAsInVzZXJuYW1lIjoicHl0aG9uIiwiZW1haWwiOiI5NTI2NzM2MzhAcXEuY29tIiwidXNlcl9pZCI6MX0.ru_DABMxzjywE_HynLA6a9XGLcQQy6KNyIP-5xQ-S_g'}"
    headers = {
        'Authorization': 'JWT ' + token
    }
    r= requests.post(url,json=data,headers=headers)
    print(r.json())


if __name__ == '__main__':
    # login()
    # info()
    # goods_list()
    # cart()
    # order()

    #1、根据默认运行规则，调整py文件命名，函数名
    #2、pytest.main()运行，或者命令行直接pytest运行
    if __name__ == '__main__':
        pytest.main(["-s","TMail.py"])
