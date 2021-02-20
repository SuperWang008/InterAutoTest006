import json
from utils.operation_json import OperationJson
# from base.runmethod import RunMethod
class OperationHeader:

    def __init__(self, response):
        # self.response = json.loads(response)
        self.response = response


    # def get_response_token(self):
    #     '''
    #     获取登录返回的token
    #     '''
    #     token = {"data":{"token":self.response['body']['token']}}
    #     return token

    def get_response_token(self):
        '''
        获取登录返回的token
        '''
        token = {"data":self.response['data']}
        return token


    def write_token(self):
        op_json = OperationJson()
        op_json.write_data(self.get_response_token())


    # def get_token(self):
    #     '''
    #     获取登录返回的token
    #     '''
    #     token = {"data":{"token":self.response['token']}}
    #     return token

    def get_token(self):
        '''
        获取登录返回的token
        '''
        token = {"data":{"token":self.response['token']}}
        return token


    def writes_tokens(self):
        op_json = OperationJson()
        op_json.write_data(self.get_token())



if __name__ == '__main__':

    # url = "http://xxxxx"
    #
    # data = {
    #     "username": "1111",
    #     "password": "123456"
    # }
    # run_method=RunMethod()
    # # res = json.dumps(requests.post(url, data).json())
    # res=run_method.run_main('Post', url, data)
    res = {'body': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTUzNDYwMzEsIn', 'user_id': 1, 'username': 'python'}, 'code': 200}
    res1 = {"code":200,"data":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJVUk3nlKjmiLforqTor4EiLCJhdWQiOnsibG9naW5OYW1lIjoid3VoYW4iLCJhcHBJZCI6IjY2N2MyMmQxLTQ5NzgtNDY5ZC05MGU4LWMzZjY3ZDAwODk1ZiIsImlkIjoiNTA2OGRkODMtZWYxYi00NWQ0LTgzYTUtMTFlZDc5NTU3MzU1In0sImlzcyI6IlVSTSIsImV4cCI6MTYxMTY1OTM5NjczMSwiaWF0IjoxNjExNjU3NTk2NzMxLCJqdGkiOiIzZmU1NWRjNS01ZDM3LTQyZDEtODQzMC04MWJkZTY3MWIzN2EifQ.FC6ZGQ6NR3BjQJ9ZlXB8sOPjwGkhrjUBfNAvLQVreQ8"}
    # res = json.dumps(res)
    op = OperationHeader(res1)
    op.write_token()
