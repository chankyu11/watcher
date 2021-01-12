import random

txt = open('D:/darknet-master/build/darknet/x64/data/data/train.txt','r')
f = open('D:/darknet-master/build/darknet/x64/data/data/train_suffle.txt','w')

tmp = []

while True :
    line = txt.readline()
    if not line:
        break
        
    tmp.append(line)
    
random.shuffle(tmp)
        
for i in tmp :  
    f.write(i)

txt.close()
f.close()