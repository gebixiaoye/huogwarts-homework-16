

# import httplib2
#
#
# http_client = None
#
# http_client = httplib2.HTTPConnection('localhost','8080',timeout=30)
# http_client.request('GET','/jenkins/api/json?pretty=true')
#
# response = http_client.getresponse()
#
# print( response.status)
# print(response.read())


# import unittest
# def div(a,b):
#     return a / b
#
# class MyfirstTestCass(unittest.TestCase):
#     def setUp(self):
#         print("run before every test")
#
#     def tearDown(self):
#         print("run after every test")
#
#     def test_1_div_1(self):
#
#         self.assertEqual(div(1,1),1/1)
#         print("1_div_1")
#
#     def test_3_div_4(self):
#         self.assertEqual(div(3,4),3/4)
#         print("3_div_4")
#
#     def test_3_div_0(self):
#         print("3_div_0")
#         self.assertRaises(ZeroDivisionError,div,3,0)
#
# if __name__ == '__main__':
#     unittest.main()



# 测试get请求的返回报文
# import unittest
# import json
# import requests
# from requests.auth import HTTPBasicAuth
#
#
# class JenkinsGetTestCase(unittest.TestCase):
#
#     def setUp(self):
#         #访问待需要登录用户名和密码的接口 要使用auth
#         self.r = requests.get('http://localhost:8080/jenkins/api/json?pretty=true',auth=('admin','123456'))
#
#     def test_get_all_job_names(self):
#         result = self.r.text
#         json_result = json.loads(result)
#         print(json_result)
#         self.assertEqual(json_result['assignedLabels'][0]['name'],'master')
#
#     def test_get_all_job_names_simple_way(self):
#         json_result1 =self.r.json()
#         self.assertEqual(json_result1['views'][0]['name'],'all')
#
#
# if __name__ == '__main__':
#     unittest.main()


#
#
# import unittest
# import json
# import requests
# from requests.auth import HTTPBasicAuth
#
#
# class JenkinsGetTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.bulid_job_url= 'http://localhost:8080/jenkins/job/chechk_python_version/build'
#         self.disable_job_url='http://localhost:8080/jenkins/job/chechk_python_version/disable'
#         self.job_url = 'http://localhost:8080/jenkins/job/chechk_python_version/api/json'
#
#     def test_build_job(self):
#         r = requests.post(self.bulid_job_url,body={},auth=('admin','123456'))
#         print(r.status_code)
#         self.assertEqual(r.status_code,201)
#
#
#     def test_disable_job(self):
#         job_info = requests.get(self.job_url,auth=('admin','123456')).json()
#         self.assertEqual(job_info['buildable'])
#
#         r = requests.post(self.disable_job_url,body={},auth=('admin','123456'))
#         print(r.status_code)
#         self.assertEqual(r.status_code,200)
#
#         job_info = requests.get(self.job_url,auth=('admin','123456')).json()
#         self.assertFalse(job_info['buildable'])
#
#
# if __name__ == '__main__':
#     unittest.main()



#链接orcle数据库
import cx_Oracle
oracle_conn=cx_Oracle.connect('credit/credit@10.1.28.61:1521/BBWXV')
oracle_cursor=oracle_conn.cursor()
BAH=  '8a818ea16efdfd7f016efdfd7fff0000'
versionCode ='V2.4'
SQL="select * from gs_syptcgslist where req_id='{}' "
print(SQL.format(BAH))
sql = oracle_cursor.execute(SQL.format(BAH))#执行语句
result = oracle_cursor.fetchall()   #获取查询结果
print(result)
if len(result)==0:
    print("未查询到结果")
else:
    print("查询结果有{}条".format(len(result)))

# oracle_conn.commit()    #提交事务
# oracle_cursor.close()   #关闭连接






# 接口实现功能
# from flask import Flask,request
# from flask_restful import reqparse,abort,Api,Resource
#
# app = Flask(__name__)
# api = Api(app)
#
# POSTS = [
#     {},
#     {'title':'first post','content':'first post'},
#     {'title':'last post','content':'last post'},
#     {'title':'how to learn interface test','content':'how to learn interface test'}
# ]
#
# def abort_if_post_dosnt_exist(post_id):
#     try:
#         POSTS[post_id]
#     except IndexError:
#         abort(404,message = "POSTS doesn't exist")
#
# parser = reqparse.RequestParser()
# parser.add_argument('post',type = int )
#
# class Post(Resource):
#     def get(self,post_id):
#         post_id = int(post_id)
#         abort_if_post_dosnt_exist(post_id)
#         return POSTS[post_id]
#
#     def delete(self,post_id):
#         post_id = int(post_id)
#         abort_if_post_dosnt_exist(post_id)
#         del POSTS[post_id]
#         return '',204
#
#     def put(self,post_id):
#         json_data = request.get_json(force=True)
#         post_id = int(post_id)
#         post = {'title':json_data['title'],'content':json_data['content']}
#         POSTS[post_id] = post
#         return post,201
#
# class PostList(Resource):
#     def get(self):
#         posts = []
#         for post in POSTS:
#             if post:
#                 new_post = {}
#                 new_post['url'] = '/posts/' + str(POSTS.index(post))
#                 new_post['title'] = post['title']
#                 posts.append(new_post)
#         return posts
#
#     def post(self):
#         json_data = request.get_json(force=True)
#         post_id = len(POSTS)
#         POSTS.append({'title':json_data['title'],'content':json_data['content']})
#         return POSTS[post_id],201
#
# api.add_resource(PostList,'/posts')
# api.add_resource(Post,'/posts/<post_id>')
#
# if __name__ ==  '__main__':
#     app.run(debug=True)
