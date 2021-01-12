import glob 

def file_path_save(): 
    filenames = [] 
    files = sorted(glob.glob("D:/darknet-master/build/darknet/x64/data/data/images/*.jpg")) 
    for i in range(len(files)):
        f = open("D:/darknet-master/build/darknet/x64/data/data/train.txt", 'a')
        f.write(files[i] + "\n") 

if __name__ == '__main__': 
    file_path_save()


import glob 

def file_path_save(): 
    filenames = [] 
    files = sorted(glob.glob("D:/darknet-master/build/darknet/x64/data/mydata/images/*.jpg")) 
    for i in range(len(files)):
        f = open("D:/darknet-master/build/darknet/x64/data/mydata/train.txt", 'a')
        f.write(files[i] + "\n") 

if __name__ == '__main__': 
    file_path_save()

