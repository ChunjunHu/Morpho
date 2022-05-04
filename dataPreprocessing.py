import os  
import shutil 
import cv2
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def is_valid(filePath):
    img_cv   = cv2.imread(filePath)#读取数据
    a = True
    try:
        img_cv.shape
    except:
        a = False
    return a 


def picConvertJPG(path, new_path):
    try:
        img = Image.open(path)
        rgb_im = img.convert('RGB')
        rgb_im.save(new_path)
        return True
    except:
        print("IOError: Can not read Image Path:", new_path)
        return False


def pilConvertJPG(path):
    for a, _, c in os.walk(path):
        print(_)
        for n in c:
            print(n)
            try:
                if '.jpg' in n or '.png' in n or '.jpeg' in n or '.JPEG' in n:
                    img = Image.open(os.path.join(a, n))
                    rgb_im = img.convert('RGB')
                    # error_img_path = os.path.join(a,n)
                    # os.remove(error_img_path)
                    n = ''.join(filter(lambda n: ord(n) < 256, n))
                    jpg_img_path = os.path.splitext(os.path.join(a, n).replace('\\', '/'))[0]
                    print(jpg_img_path)
                    jpg_img_path += '.jpg'
                    print(jpg_img_path)
                    # rgb_im.save(jpg_img_path)
                else:
                    print("error:", n)
            except:
                continue
 
path = "../sneaker_dataset/images/train"
new_path = "../sneaker_dataset/groundTruth"


# pilConvertJPG(path)

removeNum = 0
errorNum = 0
sneakerNameList = []
flag = -1
counter = 0

for root, dirs, files in os.walk(path):
    if dirs:
        sneakerNameList = dirs

    for i in range(len(files)):
        #print(files[i])
        if (files[i][-3:] == 'jpg') or (files[i][-3:] == 'png') or (files[i][-3:] == 'JPG') or (files[i][-4:] == 'jpeg') or (files[i][-4:] == 'JPEG'):
            file_path = root+'/'+files[i]
            if is_valid(file_path):
                # new_file_path = new_path+ '/'+ files[i]
                # shutil.copy(file_path,new_file_path)
                # rename_path = new_path + '/' + sneakerNameList[flag] + '_' + files[i]
                # os.rename(new_file_path, rename_path)
                newClass = sneakerNameList[flag].replace(" ", "_")
                new_file_path = new_path + '/' + newClass + '_' + files[i]
                # print(new_file_path)
                a = picConvertJPG(file_path, new_file_path)
                counter = counter + 1
                print(counter)
                if a == False:
                    errorNum = errorNum + 1

                # print(rename_path)
            else:
                os.remove(file_path)
                removeNum = removeNum + 1
                print("Remove pic Num:", removeNum)
    flag = flag + 1

print("Number of corrupted pictures:", removeNum) # 739
print("Number of pictures in unknown format:", errorNum) # 11

# useable pic #52747










