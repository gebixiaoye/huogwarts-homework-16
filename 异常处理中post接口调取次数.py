#! /usr/bin/python
#coding=utf-8
# #链接orcle数据库
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

parser = reqparse.RequestParser()
parser.add_argument('post',type = int )

class PostList(Resource):
    def get(self):      #用字典装载查询数据
        posts=[]
        oracle_cursor.execute('select * from sheet1 t  ')
        columns = [column[0] for column in oracle_cursor.description]       #获取字段名
        for row in oracle_cursor.fetchall():        #将每条数据装载成字典
            posts.append(dict(zip(columns, row)))
        return posts

    def post(self):         #查询接口调用次数
        json_data = request.get_json(force=True)
        CXZD = 'icr_num' #查询字段
        CXB= 'sheet1'    #查询表
        oracle_cursor.execute('select t.{} from {} t  where rownum = 1'.format(CXZD,CXB))
        countNum = int(oracle_cursor.fetchall()[0][0])  #查询初始值
        updateSQL='update {} set {}={}+1'
        oracle_cursor.execute(updateSQL.format(CXB,CXZD,countNum))#执行语句
        oracle_conn.commit()  # 提交事务
        oracle_cursor.execute('select t.{} from {} t  where rownum = 1'.format(CXZD,CXB))
        result='此接口调用了{}次'.format(oracle_cursor.fetchall()[0][0])
        return result,201



api.add_resource(PostList,'/posts')


if __name__ ==  '__main__':
    app.run(debug=True)
    oracle_cursor.close()  # 关闭连接