import cv2
import  Constants
import DetectIP
import  os
import CalcMatchingScore
img = cv2.imread(r'C:\Users\saksham\Desktop\Final Project\FINAL\test100\001_left index\09ROI.png',0)
#img = cv2.imread(r'C:\Users\saksham\Desktop\Final Project\FKP ROI\FKP ROI\ROI Images\001_left index\01ROI.jpg',0)
r,c=img.shape
interpolated_image = cv2.resize(img, (int(0.8*c), int(0.8*r)), interpolation=cv2.INTER_LINEAR)
#img1=cv2.imread(r'C:\Users\saksham\Desktop\Final Project\FKP3.png',0)
img1=cv2.imread(r'C:\Users\saksham\Desktop\Final Project\FKP ROI\FKP ROI\ROI Images\001_left index\09ROI.jpg',0)
#img1=cv2.imread(r'C:\Users\saksham\Desktop\Final Project\FINAL\test100\001_left index\09ROI.png',0)
#img1=img
print(img1.shape)
print (img.shape)
r,c=img1.shape
for i in range(0,r):
    for j in range(0,c):
        #img1[i][j]=img[i][j]
        if(img1[i][j]!=img[i][j]):
            print("FUCK " + str(i)+" "+str(j)+" "+str(img[i][j])+" "+str(img1[i][j]))
#cv2.imwrite(r'C:\Users\saksham\Desktop\Final Project\FKP3.png',img)
'''saveFile = open(Constants.SAVE_FILE_PATH,'w+')
x=2
y=2
z=14.2
saveFile.write(str(x)+' '+str(y)+' '+str(z)+'\n')
saveFile.write(str(y))
saveFile.write(str(z))
saveFile.write('\n')
saveFile.close()
with open(Constants.SAVE_FILE_PATH,'r') as saveFile:
    for line in saveFile:
        data = line.split()
        print str(int(data[0]))+" "+str(int(data[1]))+" "+str(float(data[2]))'''
