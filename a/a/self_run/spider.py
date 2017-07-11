'''
Created on 10 Jul 2017

@author: it
'''
import urllib.request    
import socket    
import re    
import sys    
import os 

class Spider(object):
    '''
    classdocs
    '''
    def reverse(self,li):
        for i in range(0, len(li)/2):
            temp = li[i]
            li[i] = li[-i-1]
            li[-i-1] = temp
            
    
    def destFile(self,path):  
        print ("entering")
        targetDir = 'd:\\tmp\\Pppp'  #文件保存路径  
        
        if not os.path.isdir(targetDir):     #文件夹不存在则创建新的
            os.mkdir(targetDir)    
        pos = path.rindex('/')  
        t = os.path.join(targetDir, path[pos+1:])    
        print("path=",t)  
        return t


    def __init__(self, params):
        print(params)
        #if __name__ == "__main__":  #程序运行入口  
        weburl = "http://test.88lifa.com:8080/index.shtml"
        print(weburl)
        webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}   
        req = urllib.request.Request(url=weburl, headers=webheaders)  #构造请求报头  
        webpage = urllib.request.urlopen(req)  #发送请求报头  
        contentBytes = webpage.read() 
        print(str(contentBytes))
        
        ctr=0
        for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(contentBytes))):  #正则表达式查找所有的图片  
            print("link=",link) 
            ctr+=1 
            try:   
                urllib.request.urlretrieve(link, self.destFile(link)) #下载图片  
            except:  
                print (Exception)
                print('失败') #异常抛出
            if(ctr>=3):
                break
        
        
        
#python3.4 爬虫教程  
#爬取网站上的图片  
#林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)  


o = Spider("passed params")
   
    



