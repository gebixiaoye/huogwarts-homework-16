#链接orcle数据库
import cx_Oracle
from flask import Flask,request
from flask_restful import reqparse,abort,Api,Resource


oracle_conn=cx_Oracle.connect('credit/credit@10.1.28.61:1521/BBWXV')
oracle_cursor=oracle_conn.cursor()
# BAH=  'U'
# versionCode ='V2.4'
# SQL="update ide_engine_version t set t.version_state= '{}' where t.version_code='{}' "
# oracle_cursor.execute(SQL.format(BAH,versionCode))#执行语句
# oracle_conn.commit()    #提交事务




app = Flask(__name__)
api = Api(app)

POSTS = [{}]
oracle_cursor.execute('select * from tb_applicantinformation t  ')
columns = [column[0] for column in oracle_cursor.description]  # 获取字段名
for row in oracle_cursor.fetchall():  # 将每条数据装载成字典
    POSTS.append(dict(zip(columns, row)))

def abort_if_post_dosnt_exist(indname):
    try:
        POSTS[indname]
    except IndexError:
        abort(404,message = "POSTS doesn't exist")

parser = reqparse.RequestParser()
parser.add_argument('post',type = int )

class Post(Resource):
    def get(self,post_id):
        post_id = int(post_id)
        abort_if_post_dosnt_exist(post_id)
        return POSTS[post_id]

    def delete(self,post_id):
        post_id = int(post_id)
        abort_if_post_dosnt_exist(post_id)
        del POSTS[post_id]
        return '',204

    def put(self,post_id):
        json_data = request.get_json(force=True)
        post_id = int(post_id)
        post = {'title':json_data['title'],'content':json_data['content']}
        POSTS[post_id] = post
        return post,201

class PostList(Resource):
    def get(self):
        posts = []
        for post in POSTS:
            if post:
                new_post = {}
                new_post['url'] = '/posts/' + str(POSTS.index(post))
                new_post['title'] = post['title']
                posts.append(new_post)
        return posts

    def post(self):
        json_data = request.get_json(force=True)
        post_id = len(POSTS)
        POSTS.append({'title':json_data['title'],'content':json_data['content']})
        return POSTS[post_id],201

api.add_resource(PostList,'/posts')
api.add_resource(Post,'/posts/<post_id>')

if __name__ ==  '__main__':
    app.run(debug=True)
    oracle_cursor.close()  # 关闭连接