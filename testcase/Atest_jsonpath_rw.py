from jsonpath_rw import jsonpath, parse
import requests

data = {
    "error_code": 0,
    "stu_info": [
        {
            "id": 309,
            "name": "小红",
            "sex": "男",
            "age": 28,
            "addr": "河南省济源市北海大道32号",
            "grade": "天蝎座",
            "phone": "18512572946",
            "gold": 100
        },
        {
            "id": 310,
            "name": "小白",
            "sex": "男",
            "age": 28,
            "addr": "河南省济源市北海大道32号",
            "grade": "天蝎座",
            "phone": "18516572946",
            "gold": 100
        }
    ]
}

json_expr = parse('stu_info[1].name')
male = json_expr.find(data)
m = [math.value for math in male][0]
print(type(m))
print(m)

data1 = {"status":0,"msg":"","data":{"id":13693747}}
json_expr = parse('data[id]')
male = json_expr.find(data1)
n = [math.value for math in male][0]
print(n)


