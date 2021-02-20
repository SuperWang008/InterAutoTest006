#定义类
class DataConfig:
#定义列属性
    #用例ID	模块	接口名称	请求URL	前置条件	请求类型	请求参数类型
    #请求参数  预期结果  实际结果  备注	是否运行	headers	cookies	status_code	数据库验证
    #用例ID
    case_no = "编号"
    case_id = "用例ID"
    case_model = "模块"
    case_name = "接口名称"
    is_run = "是否运行"
    method = "请求类型"
    url = "请求URL"
    is_wtoken = "是否写入token"
    headers = "headers"
    cookies = "cookies"
    pre_exec = "前置条件"
    res_data = "依赖的返回数据"
    depend_field = "依赖的字段"
    params_type = "请求参数类型"
    params = "请求参数"
    expect_result = "预期结果"
    actual_result = "实际结果"
    code = "status_code"
    db_verify = "数据库验证"
    test_result = "测试结果"