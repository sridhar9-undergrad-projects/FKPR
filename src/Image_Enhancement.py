import cv2
import Constants
import numpy as np
import  math
def preprocessing(img):
    #img=img2.copy()
    interpolated_image=np.zeros(img.shape,np.uint8)
    interpolated_image=cv2.normalize(img,interpolated_image,0,255,cv2.NORM_MINMAX)
    #r,c=img.shape
    #img3 = cv2.resize(img,(Constants.IMAGE_ROWS,Constants.IMAGE_COLS))
    #interpolated_image=estimate_reflection(img3,r,c)
    #cv2.imshow("ESTIMATE REf",interpolated_image)
    #cv2.waitKey()
    #interpolated_image=cv2.blur(cv2.bitwise_not(interpolated_image),(3,3))
    #interpolated_image=interpolation(interpolated_image)
   # interpolated_image=cv2.blur(img,(5,5));
   # blur = cv2.GaussianBlur(img, (5, 5), 0)
    #mean_filter(img,cv2.blur(img,(3,3)))
#    cv2.imshow("INTERPOLATION", interpolated_image)#cv2.subtract(img,interpolated_image))
    #sub_image2=cv2.absdiff(img,interpolated_image)
    #sub_image=img
    #print(img.shape)
    '''for i in range(0,r):
        for j in range(0,c):
            if(interpolated_image[i][j] >img[i][j] and interpolated_image[i][j]-img[i][j]>=100):
                sub_image[i][j]=interpolated_image[i][j]-img[i][j]
            else:
                sub_image[i][j]=img[i][j]'''
    #cv2.imshow("AFTER SUB",interpolated_image)#cv2.subtract(img,interpolated_image))
    #hist_eq=cv2.equalizeHist(sub)
    #cv2.imshow("HISTOGRAM",hist_eq);
 #   hist_eq=applyHistEq(sub_image)
    #sub_image=cv2.absdiff(img,interpolated_image)
    #for i in range(0,r):
    #    for j in range(0,c):
    #        sub_image[i][j]=img[i][j]
            #if(interpolated_image[i][j] >= 220):
    #        sub_image[i][j]=interpolated_image[i][j]-img[i][j]
    #print ("IMAGE "+str(img[i][j])+" "+str(interpolated_image[i][j]))
    #sub_image=cv2.GaussianBlur(sub_image,(3,3),0)
    #hist_eq=applyHistEq(sub_image2)
    #hist_eq=cv2.equalizeHist(hist_eq)
#    cv2.imshow("HISTO",sub_image)
    smooth=cv2.GaussianBlur(interpolated_image,(3,3),0)
    #smooth=cv2.blur(hist_eq,(3,3))
    clahe = cv2.createCLAHE()
    smooth = clahe.apply(smooth)
    #smooth=cv2.dilate(smooth,(11,11))
   # smooth=cv2.equalizeHist(smooth)
    #smooth=cv2.blur(hist_eq,(3,3))
    #smooth=cv2.bilateralFilter(hist_eq, 25, 75, 75)
    return smooth# cv2.equalizeHist(img)
def applyHistEq(sub_image):
    r,c=sub_image.shape
    new_img=sub_image.copy()
    for i in range(0,r,Constants.BLOCK_SIZE):
        for j in range(0,c,Constants.BLOCK_SIZE):
            temp=np.zeros((Constants.BLOCK_SIZE,Constants.BLOCK_SIZE),np.uint8)
            for ii in range(0,Constants.BLOCK_SIZE):
                for jj in range(0,Constants.BLOCK_SIZE):
                    xx=i+ii
                    yy=j+jj
                    if(xx<r and yy<c):
                        temp[ii][jj]=sub_image[xx][yy]
            #temp = cv2.GaussianBlur(temp, (5, 5), 0)
            temp=cv2.equalizeHist(temp)
            #temp=cv2.blur(temp,(3,3),0)
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
    return
def estimate_reflection(img,original_r,original_c):
    r,c=img.shape
    new_img=np.zeros((Constants.BLOCK_SIZE+1,Constants.BLOCK_SIZE+1),np.uint8)
    rows=-1
    for i in range(0,r,Constants.BLOCK_SIZE):
        rows+=1
        col=-1
        for j in range(0,c,Constants.BLOCK_SIZE):
            col+=1
            sum=0
            for ii in range(0,Constants.BLOCK_SIZE):
                for jj in range(0,Constants.BLOCK_SIZE):
                    sum = sum + img[i+ii][j+jj]

            mean= sum/(Constants.BLOCK_SIZE * Constants.BLOCK_SIZE)
            #print(str(i)+" "+str(j)+" "+str(mean))
            new_img[rows][col]=mean
            #print("ROWS " + str(rows) + " " + str(col) + " " + str(r) + " " +str(c)+" "+str(i)+" "+str(j))
            #new_img[i%Constants.BLOCK_SIZE][j%Constants.BLOCK_SIZE]=mean
    return  cv2.resize(new_img,(original_c,original_r),interpolation=cv2.INTER_CUBIC)
def interpolation(img):
    r,c =img.shape
   # print("shape of image "+str(r)+" "+str(c))
    rows=-1;
    cols=0
    new_img=np.zeros((r/Constants.BLOCK_SIZE,c/Constants.BLOCK_SIZE),np.uint8)
    #interpolated_image=img.copy()#np.zeros(img.shape,np.uint8)
    '''for i in range(0,r/11+1):
        for j in range(0,c/11+1):
            new_img[i][j]=img[i][j];'''
    for i in range(0,r,Constants.BLOCK_SIZE):
        col=0;
        rows+=1
      #  new_img.append([])
        for j in range(0,c,Constants.BLOCK_SIZE):
            mean=0;
            totalCells=0;
            for k  in range(0,Constants.BLOCK_SIZE):
                for l in range(0,Constants.BLOCK_SIZE):
                    xx=i+k;
                    yy=j+l;
                    if(xx<r and yy <c):
                        totalCells+=1
                        mean+=img[xx][yy]
            mean= mean/(totalCells);
          #  print(str(rows)+" "+str(col)+" "+str(mean)+" "+str(i)+" "+str(j)+" "+str(totalCells))
            #if(i+5<r and j+5<c):
            #temp_img=cv2.resize(mean,(Constants.BLOCK_SIZE,Constants.BLOCK_SIZE),interpolation=cv2.INTER_CUBIC)
            if( rows<r/Constants.BLOCK_SIZE and col<c/Constants.BLOCK_SIZE):
                new_img[rows][col]=mean
            #tempr,tempc=temp_img.shape
            #for ii in range(0,tempr):
                #for jj in range(0,tempc):
                    #interpolated_image[i+ii][j+jj]=temp_img[ii][jj]
         #   new_img[rows].append(mean)
            #new_img[rows].append(mean)
            col+=1
  #  print(new_img)
  #  new_img=np.array(new_img);
#    cv2.imshow("NEWIMAGE",new_img)#[r/11+1:c/11+1]);
    interpolated_image = cv2.resize(new_img,(c,r),interpolation=cv2.INTER_LINEAR);
    #print(str(img.shape)+" "+str(interpolated_image.shape))
    return interpolated_image

