import os.path
import os
rootdir = '.'                                   # 指明被遍历的文件夹

for parent,dirnames,filenames in os.walk(rootdir): 
    for file in filenames:  # 输出文件信息
        if os.path.splitext(file)[-1] == ".rst":
                f=open(os.path.join(parent, file),'w+')
                for line in f:
                        line.replace(os.path.splitext(file)[0]+os.path.splitext(file)[0]+os.path.splitext(file)[0],'\n')
 
                f.close()  