import os 
dicr = dict()
for  one in os.listdir(os.curdir):#显示当前的文件夹
#循环提取所有文件内容，
        if os.path.isdir(one):	#判断是否文件夹
                dicr.setdefault('文件夹',0)
                dicr['文件夹']+=1
        else :	#判断是什么文件类型
                kzm = os.path.splitext(one)[1]
                dicr.setdefault(kzm,0)
                dicr[kzm]+=1
for i in dicr.keys():
        print("该文件夹下共有类型为%s的文件%d个"%(i,dicr[i]))
