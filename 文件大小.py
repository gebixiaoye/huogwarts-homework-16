import os
#获取当前路径下所有文件
sywj = os.listdir(os.curdir)

dirc = dict()

#循环单个文件
for flie_each in sywj:
    
    #判断单个文件的类型
    if os.path.isfile(flie_each):
     #存储每一种类型的大小\
        dirc.setdefault(flie_each,os.path.getsize(flie_each))
        print("文件名：%s，大小为：%s"%(flie_each,dirc[flie_each]))
