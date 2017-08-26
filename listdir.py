import os
path="/home/hadoop/"
def listDir(path):
    l=os.listdir(path)
    for i in l:
        fp = os.path.join(path,i)
        if(os.path.isdir(fp)):
            listDir(fp);
        else:
            print fp

listDir(path)
