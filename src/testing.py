import cv2
import DetectIP
import CalcMatchingScore
import Image_Enhancement
import Image_Enhancement_prev
import Constants
from matplotlib import pyplot as py
#img1_path=r'C:\Users\saksham\Desktop\Final Project\dataset\test\001_left index\11ROI.jpg'
#img1_path=r'C:\Users\saksham\Desktop\Final Project\dataset\train\007_left index\01ROI.jpg'
#img1_path=r'C:\Users\saksham\Desktop\Final Project\dataset\train\001_left index\05ROI.jpg'
#img1_path=r'C:\Users\saksham\Desktop\Final Project\FKP ROI\FKP ROI\ROI Images\004_right index\01ROI.jpg'
#img1_path=r'C:\Users\saksham\Desktop\Final Project\FKP ROI\FKP ROI\ROI Images\004_right index\01ROI.jpg'
img1_path=r'C:\Users\saksham\Desktop\Final Project\train\001_right index\03ROI.jpg'
#img1_path=r'C:\Users\saksham\Desktop\Final Project\train\002_left index\03ROI.jpg'
#img1_path=r'C:\Users\saksham\Desktop\Final Project\train\001_left middle\10ROI.jpg'
img2_path=r'C:\Users\saksham\Desktop\Final Project\dataset\test\001_left index\12ROI.jpg'
#img2_path=r'C:\Users\saksham\Desktop\tesst.jpg'
#img2_path=r'C:\Users\saksham\Desktop\Final Project\FKP ROI\FKP ROI\ROI Images\004_right index\09ROI.jpg'
#img2_path=r'C:\Users\saksham\Desktop\Final Project\FKP ROI\FKP ROI\ROI Images\004_right middle\02ROI.jpg'
#img2_path=r'C:\Users\saksham\Desktop\Final Project\dataset\test\007_left index\12ROI.jpg'
#img2_path=r'C:\Users\saksham\Desktop\Final Project\train\001_left index\03ROI.jpg'
#img2_path=r'C:\Users\saksham\Desktop\Final Project\test\001_left index\12ROI.jpg'
#img2_path=r'C:\Users\saksham\Desktop\Final Project\test\001_left middle\11ROI.jpg'
#img2_path=r'C:\Users\saksham\Desktop\Final Project\test2\002_left index\11ROI.jpg'
image1=cv2.imread(img1_path,0)
image2=cv2.imread(img2_path,0)
#cv2.imshow("Original",image1);
#cv2.imshow("ENHNCED",Image_Enhancement.preprocessing(image1));
kp1,train=DetectIP.findDescriptors(image1.copy());
cv2.imshow("train",cv2.drawKeypoints(Image_Enhancement.preprocessing(image1.copy()),kp1,None,(255,0,0),4))
kp2,test=DetectIP.findDescriptors(image2.copy());
print (len(train))
bf = cv2.BFMatcher()
matches = bf.knnMatch(train,test, k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < Constants.MATCHING_THRESHOLD*n.distance:
        good.append([m])
# cv2.drawMatchesKnn expects list of lists as matches.
print ("length of Good "+ str(len(good)))
cv2.imshow("test",cv2.drawKeypoints(Image_Enhancement.preprocessing(image2.copy()),kp2,None,(255,0,0),4));
cv2.imshow("train2",image1)
cv2.imshow("test2",image2)
cv2.imshow("etrain",Image_Enhancement.preprocessing(image1.copy()))
cv2.imshow("etest",Image_Enhancement.preprocessing(image2.copy()))
#print(str(CalcMatchingScore.findMatchingScore(test,train)) + " "+str(len(test))+" "+str(len(train)))
cv2.waitKey()