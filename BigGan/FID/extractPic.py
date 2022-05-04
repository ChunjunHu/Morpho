import os, random, shutil
def moveFile(fileDir,tarDir):
        pathDir = os.listdir(fileDir)    #取图片的原始路径
        picknumber=2048              # 自定义选取图片数目
        sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片

        for name in sample:
            shutil.move(fileDir+name, tarDir+name)


fileDir = "./dataset/groundTruth/"
tarDir =  "./FID/realImage2048/"
moveFile(fileDir,tarDir)
