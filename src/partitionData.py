import  os,shutil
import  numpy as np
from PIL import  Image
import Constants
import  cv2
folder_path=r'C:\Users\saksham\Desktop\Final Project\testingdt'
train_path=r'C:\Users\saksham\Desktop\Final Project\testingdt\train'
test_path=r'C:\Users\saksham\Desktop\Final Project\testingdt\test'
totalclasses=0
if not os.path.exists(test_path):
    os.makedirs(test_path)
if not os.path.exists(train_path):
    os.makedirs(train_path)
for  dirs in os.listdir(test_path):
    shutil.rmtree(os.path.join(test_path,dirs))
    #for file in os.listdir(os.path.join(test_path,dirs)):
    #    file_path=os.path.join(file,os.path.join(test_path,dirs))
    #    os.remove(file_path)
    #os.rmdir(os.path(test_path,dirs))
for  dirs in os.listdir(train_path):
    shutil.rmtree(os.path.join(train_path,dirs))
    #for file in os.listdir(os.path.join(train_path,dirs)):
    #    file_path=os.path.join(file,os.path.join(train_path,dirs))
    #    os.remove(file_path)
    #os.rmdir(os.path(train_path,dirs))
for dirname in os.listdir(folder_path):
    if(os.path.isdir(os.path.join(folder_path,dirname)) and (not ('test' in dirname)) and (not 'train' in dirname) and dirname!='train'):
        if (not os.path.exists(os.path.join(train_path, dirname))) and totalclasses<500 :
            os.makedirs(os.path.join(train_path, dirname))
        if not os.path.exists(os.path.join(test_path, dirname)):
            os.makedirs(os.path.join(test_path, dirname))
        for file in os.listdir(os.path.join(folder_path,dirname)):
            name = os.path.basename(os.path.join(os.path.join(folder_path,dirname),file))
            new_train_path=os.path.join(train_path,dirname)
            new_test_path=os.path.join(test_path,dirname)
            for i in range(len(name)):
                if(name[i]=='R'):
                    ones=int(name[i-1])
                    tens=int(name[i-2])
                    img_index=tens*10+ones
                    l=len(name)
                    new_name=name[:-4]+str('.png')
                    if(img_index<=Constants.TRAIN_ISTO_TEST ):#and totalclasses<500):
                        img = cv2.imread(os.path.join(os.path.join(folder_path,dirname),file))
                        #img = Image.open(os.path.join(os.path.join(folder_path,dirname),file)).convert('L')
                        #im = np.array(img)
                        #fft_mag = np.abs(np.fft.fftshift(np.fft.fft2(im)))
                        #visual = np.log(fft_mag)
                        #visual = (visual - visual.min()) / (visual.max() - visual.min())
                        #result = Image.fromarray((visual * 255).astype(np.uint8))
                        cv2.imwrite(os.path.join(new_train_path,new_name),img)
                        #img.save(os.path.join(new_train_path,name))
                    else:
                        #print(totalclasses)
                        img = cv2.imread(os.path.join(os.path.join(folder_path, dirname), file),0)
                        #img = Image.open(os.path.join(os.path.join(folder_path,dirname),file)).convert('L')
                        #im = np.array(img)
                        #fft_mag = np.abs(np.fft.fftshift(np.fft.fft2(im)))
                        #visual = np.log(fft_mag)
                        #visual = (visual - visual.min()) / (visual.max() - visual.min())
                        #result = Image.fromarray((visual * 255).astype(np.uint8))
                        #img.save(os.path.join(new_test_path,name))
                        r,c = img.shape
                        interpolated_image = cv2.resize(img, (int(0.4 * c), int(0.4 * r)),
                                                        interpolation=cv2.INTER_CUBIC)
                        cv2.imwrite(os.path.join(new_test_path,new_name),img)
        totalclasses+=1


