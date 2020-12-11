import cv2
import Constants
import Image_Enhancement
import  Image_Enhancement_prev
def findDescriptors(img):
    #img = cv2.imread(r'C:\Users\saksham\Desktop\Final Project\FKP ROI\FKP ROI\ROI Images\035_left index\03ROI.jpg',0);
    #img = cv2.imread(r'F:\Memories\Sakshi Weeding\DCIM\Camera\IMG_20160901_125636738.jpg',0)
    #cv2.imshow("GRay",cv2.blur(img,(11,11)));
    #cv2.waitKey();
    img=Image_Enhancement.preprocessing(img.copy())
    sift=cv2.SIFT(180);
    surf=cv2.SURF(Constants.HESSIAN_THRESHOLD,Constants.NUMBER_OF_OCTAVES,Constants.NUMBER_OF_OCTAVE_LAYERS,Constants.SURF_EXTENDED,Constants.SURF_UPRIGHT);
    kp,surfDes=surf.detectAndCompute(img,None);
    kp2,siftDes=sift.detectAndCompute(img,None)
    return  kp2[0:200],surfDes[0:200]
def find_SURF_Descriptors(img2):
    img=img2.copy()
    img = Image_Enhancement.preprocessing(img)
    surf = cv2.SURF(Constants.HESSIAN_THRESHOLD, Constants.NUMBER_OF_OCTAVES, Constants.NUMBER_OF_OCTAVE_LAYERS,
                    Constants.SURF_EXTENDED, Constants.SURF_UPRIGHT)
    kp,surfDes = surf.detectAndCompute(img, None)
    return kp,surfDes[0:250]
def find_SIFT_Descriptors(img2):
    img=img2.copy()
    img = Image_Enhancement.preprocessing(img)
    sift=cv2.SIFT(200)
    kp,siftDes=sift.detectAndCompute(img,None)
    return kp,siftDes
#img2=cv2.drawKeypoints(img,kp,None,(255,0,0),4);
#cv2.imshow("KEYP",img2);
#cv2.imshow("SIFT",cv2.drawKeypoints(img,kp2,None,(255,0,0),4));
#cv2.waitKey();