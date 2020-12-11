import cv2
import Constants
import numpy as np
import  math
from PIL import Image
def preprocessing(img):
    interpolated_image=img.copy()
    #interpolated_image=cv2.normalize(img,interpolated_image,0,255,cv2.NORM_MINMAX)
    interpolated_image=interpolation(img.copy())
    #interpolated_image=filtering(img)
   # interpolated_image=cv2.blur(img,(5,5));
   # blur = cv2.GaussianBlur(img, (5, 5), 0)
    #mean_filter(img,cv2.blur(img,(3,3)))
#    cv2.imshow("INTERPOLATION", interpolated_image)#cv2.subtract(img,interpolated_image))
    #sub=cv2.subtract(img,interpolated_image);
    #cv2.imshow("AFTER SUB",interpolated_image-img)#cv2.subtract(img,interpolated_image))
    #hist_eq=cv2.equalizeHist(sub)
    #cv2.imshow("HISTOGRAM",hist_eq);
 #   hist_eq=applyHistEq(sub_image)
    #sub_image=cv2.subtract(img,interpolated_image);
    sub_image=sub(img,interpolated_image)
    hist_eq=applyHistEq(sub_image)
    cv2.imshow("HISTO",sub_image)
    #cv2.imshow("SHOW",hist_eq)
    return hist_eq
    #sub(img,sub_image)
def applyHistEq(sub_image):
    r,c=sub_image.shape
    new_img=sub_image.copy();
    for i in range(0,r,Constants.BLOCK_SIZE):
        for j in range(0,c,Constants.BLOCK_SIZE):
            temp=np.zeros((Constants.BLOCK_SIZE,Constants.BLOCK_SIZE),np.uint8)
            for ii in range(0,Constants.BLOCK_SIZE):
                for jj in range(0,Constants.BLOCK_SIZE):
                    xx=i+ii
                    yy=j+jj
                    if(xx<r and yy<c):
                        temp[ii][jj]=sub_image[xx][yy]
            temp=cv2.equalizeHist(temp)
            #clahe = cv2.createCLAHE()
            #temp = clahe.apply(temp)
            for ii in range(0,Constants.BLOCK_SIZE):
                for jj in range(0,Constants.BLOCK_SIZE):
                    xx=i+ii
                    yy=j+jj;
                    if(xx<r and yy<c):
                        new_img[xx][yy]=temp[ii][jj];
    return  new_img
def filtering(img):
    r,c=img.shape
    new_img=img;#cv2.blur(img,(10,10))
    for i in range(0,r):
        for j in range(0,c):
            sum=0;
            for ii in range(-5,6):
                for jj in range(-5,6):
                    xx=i+ii
                    yy=j+jj
                    if(xx<r and yy<c and xx>=0 and yy>=0):
                        sum+=img[xx][yy]
            new_img[i][j]=sum/121;
    return  new_img
def mean_filter(img,final):
    r,c=img.shape
    new_img=np.zeros(img.shape,np.uint8);
    for i in range(0,r):
        for j in range(0,c):
            sum=0
            numb=0;
            for k in range(-5,6,1):
                for l in range(-5,6,1):
                    xx=i+k;
                    yy=j+l;
                    if(xx>=0 and xx<r and yy>=0 and yy<c):
                        sum=sum+img[xx][yy]
                        numb+=1;
                      #  print (str(i)+" "+str(j)+" "+str(img[xx][yy])+" "+str(xx)+" "+str(yy))
            #if(sum!=0):
            new_img[i][j]=sum/numb;
            print(str(i)+" "+str(j)+" "+str(img[i][j])+" "+str(new_img[i][j]) + " "+str(final[i][j]))
    cv2.imshow("MEAN",new_img);
    return ;
def interpolation(img):
    r,c =img.shape
    #print("shape of image "+str(r)+" "+str(c))
    rows=-1;
    cols=0
    new_img=np.zeros((r/Constants.BLOCK_SIZE,c/Constants.BLOCK_SIZE),np.uint8)
    '''for i in range(0,r/11+1):
        for j in range(0,c/11+1):
            new_img[i][j]=img[i][j];'''
    for i in range(0,r,Constants.BLOCK_SIZE):
        col=0;
        rows+=1
      #  new_img.append([])
        for j in range(0,c,Constants.BLOCK_SIZE):
            mean=np.uint32(0);
            totalCells=0;
            for k  in range(0,Constants.BLOCK_SIZE):
                for l in range(0,Constants.BLOCK_SIZE):
                    xx=i+k;
                    yy=j+l;
                    if(xx<r and yy <c):
                        totalCells+=1
                        mean+=img[xx][yy]
            mean= mean/(totalCells);
            #print(str(rows)+" "+str(col)+" "+str(mean)+" "+str(i)+" "+str(j)+" "+str(totalCells))
            #if(i+5<r and j+5<c):
            new_img[rows][col]=mean;
         #   new_img[rows].append(mean)
            #new_img[rows].append(mean)
            col+=1
  #  print(new_img)
  #  new_img=np.array(new_img);
#    cv2.imshow("NEWIMAGE",new_img)#[r/11+1:c/11+1]);
    interpolated_image = cv2.resize(new_img,(c,r),interpolation=cv2.INTER_CUBIC);
    #print(str(img.shape)+" "+str(interpolated_image.shape))
    return interpolated_image
def sub(image1,image2):
    final_image=image1.copy()
    r,c=image1.shape
    for i in range(0,r):
        for j in range(0,c):
            #else:
            final_image[i][j]=image1[i][j]-image2[i][j]
    #final_image = cv2.normalize(final_image,final_image,0,255,cv2.NORM_MINMAX)
    return final_image