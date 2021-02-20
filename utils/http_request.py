import requests


class HttpRequest:
    # def http_request(self,url,data,http_method,headers,cookies):
    #     if http_method.lower()=='get':
    #         try:
    #             res = requests.get(url,data,headers,cookies)
    #         except Exception as e:
    #             print("get请求报错了：{0}".format(e))
    #             raise e
    #     elif http_method.lower()=='post':
    #         try:
    #             res = requests.post(url,data,headers,cookies)
    #         except Exception as e:
    #             print("post请求报错了：{0}".format(e))
    #             raise e
    #     else:
    #         print("输入的请求方法不对")
    #     return res

    def http_request(self,url,data = None,http_method="get",json=None,headers=None,cookies=None):
        if http_method.lower()=='get':
            try:
                res = requests.get(url,data = data, json=json, headers=headers,cookies=cookies)
            except Exception as e:
                print("get请求报错了：{0}".format(e))
                raise e
        elif http_method.lower()=='post':
            try:
                res = requests.post(url,data = data, json=json, headers=headers,cookies=cookies)
            except Exception as e:
                print("post请求报错了：{0}".format(e))
                raise e
        else:
            print("输入的请求方法不对")
        return res