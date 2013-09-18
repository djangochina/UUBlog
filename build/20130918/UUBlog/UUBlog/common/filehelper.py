#-*- coding:utf-8 -*-

import time
import os.path 
import shutil 

def CopyFiles(sourceDir,  targetDir): 
    if sourceDir.find(".svn") > 0: 
        return 
    for filePath in os.listdir(sourceDir): 
        sourceFile = os.path.join(sourceDir,  filePath) 
        targetFile = os.path.join(targetDir,  filePath) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                    open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
        if os.path.isdir(sourceFile): 
            
            CopyFiles(sourceFile, targetFile)

#删除文件
def DeleteFile(*filePaths):
    for filePath in filePaths:
        if os.path.isfile(filePath): 
            os.remove(filePath)


#删除一级目录下的所有文件：
def DeleteFileInDir(targetDir): 
    for filePath in os.listdir(targetDir): 
        targetFile = os.path.join(targetDir,  filePath) 
        if os.path.isfile(targetFile): 
            os.remove(targetFile)
#复制一级目录下的所有文件到指定目录：
def coverFiles(sourceDir,  targetDir): 
    for filePath in os.listdir(sourceDir): 
        sourceFile = os.path.join(sourceDir,  filePath) 
        targetFile = os.path.join(targetDir,  filePath) 
        #cover the files 
        if os.path.isfile(sourceFile): 
            open(targetFile, "wb").write(open(sourceFile, "rb").read())
#复制指定文件到目录：
def moveFileto(sourceDir,  targetDir): 
    shutil.copy(sourceDir,  targetDir)

#往指定目录写文本文件：
def writeVersionInfo(targetDir):    
    open(targetDir, "wb").write("Revison:")

#返回当前的日期，以便在创建指定目录的时候用：
def getCurTime(): 
    nowTime = time.localtime() 
    year = str(nowTime.tm_year) 
    month = str(nowTime.tm_mon) 
    if len(month) < 2: 
        month = '0' + month 
    day =  str(nowTime.tm_yday) 
    if len(day) < 2: 
        day = '0' + day 
    return (year + '-' + month + '-' + day)










