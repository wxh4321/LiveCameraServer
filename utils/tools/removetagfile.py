#coding:utf-8
import os,sys,platform
class RemoveTagFile(object):
    path=None
    def removeFile(self,path,remove_list,retain_list): #path后面要跟/
        self.path=path
        system_test=platform.system()
        if(system_test=='Windows'):
            path_last=self.path[-1]
            if(path_last!='\\' ):
                self.path=self.path+'\\'
        elif(system_test=='Linux'):
            path_last = self.path[-1]
            if (path_last != '/'):
                self.path = self.path + '/'
        if(len(remove_list)==0 and len(retain_list)==0):  #如果remove_list,retain_list都是空则删除path目录下所有文件及文件夹
            self.remove_file(self.eachFile(self.path))
        elif(len(remove_list)>0 and len(retain_list)==0):
            self.remove_file(remove_list)
        elif(len(remove_list)==0 and len(retain_list)>0):
            list=self.eachFile(self.path)
            for f in retain_list:
                if(f in list):
                    list.remove(f)
                else:
                    print('There is no file in the directory!')
            self.remove_file(list)
        elif (len(remove_list) > 0 and len(retain_list) > 0):
            for f in retain_list:
                if(f in remove_list):
                    remove_list.remove(f)
            self.remove_file(remove_list)

    def remove_file(self,file_list):
        for filename in file_list:
            if(os.path.exists(self.path+filename)):   #判断文件是否存在
                if(os.path.isdir(self.path+filename)):
                    self.del_file(self.path+filename)
                else:
                    if(os.path.exists(self.path+filename)):
                        os.remove(self.path+filename)
            else:
                print(self.path+filename+' is not exist!')
        for filename in file_list:
            if(os.path.exists(self.path+filename)):
                self.del_dir(self.path+filename)
    def del_file(self,path):     #递归删除目录及其子目录下的文件
        for i in os.listdir(path):
            path_file = os.path.join(path, i) #取文件绝对路径
            if os.path.isfile(path_file):     #判断是否是文件
                os.remove(path_file)
            else:
                self.del_file(path_file)
    def del_dir(self,path):  #删除文件夹
        for j in os.listdir(path):
            path_file = os.path.join(path, j)  # 取文件绝对路径
            if not os.listdir(path_file):    #判断文件如果为空
                os.removedirs(path_file)   #则删除该空文件夹，如果不为空删除会报异常
            else:
                self.del_dir(path_file)
    def eachFile(self,filepath):   #获取目录下所有文件的名称
        pathDir = os.listdir(filepath)
        list=[]
        for allDir in pathDir:
            child = os.path.join('%s%s' % (filepath, allDir))
            fileName=child.replace(filepath,'')
            list.append(fileName)
            return list
if __name__ == '__main__':
    rtf=RemoveTagFile()
    #以下表示只删除D:\Test\目录下的a文件夹、a.txt文件、b.txt文件
    """
    规则：
    1、如果remove_list、retain_list都为空则删除path目录下所有文件及文件夹
    2、如果remove_list为空、retain_list不为空，则删除不在retain_list中的所有文件及文件夹
    3、如果remove_list不为空、retain_list为空，则删除在remove_list中的所有文件及文件夹
    4、如果remove_list、retain_list都不为空，则删除不在retain_list中且在remove_list中的所有文件及文件夹
    """
    path = 'D:\Test'
    remove_list = ['a', 'a.txt', 'b.txt']  # 要删除的文件名称
    retain_list = ['c.txt']  # 要保留的文件名称
    rtf.removeFile(path,remove_list,retain_list)
