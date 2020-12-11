import cv2
import  Constants
import DetectIP
import  os
import CalcMatchingScore
classes=0
trainfeatures=[]
for dirs in os.listdir(Constants.TRAIN_DATA_PATH):
    path=os.path.join(Constants.TRAIN_DATA_PATH,dirs)
    trainfeatures.append([]);
    for file in os.listdir(path):
        image =  cv2.imread(os.path.join(path,file),0);
        _,surfdes=DetectIP.findDescriptors(image);
        trainfeatures[classes].append(surfdes)
    classes+=1
totalclasses=classes
print(str(totalclasses)+"-TotalClasses ");
classes=0
correct_matches=0
total_system_images=0
total_non_system=0
test_matching_scores=[]
max_matching_score=-1
min_matching_score=-1
for dirs in os.listdir(Constants.TEST_DATA_PATH):
    path=os.path.join(Constants.TEST_DATA_PATH,dirs)
    class_matching=0;
    class_images=0;
    test_matching_scores.append([])
    for file in os.listdir(path):
        image =  cv2.imread(os.path.join(path,file),0);
        _,test_img_ip=DetectIP.findDescriptors(image);
        if(classes>=totalclasses):
            total_non_system+=1
        else:
            total_system_images+=1
        matching_score=0
        classified_class=-1
        class_images+=1
        for train_class in range(totalclasses):
            totalImages=len(trainfeatures[train_class])
            for img in range(totalImages):
                train_img_ip=trainfeatures[train_class][img]
                temp_matching_score=CalcMatchingScore.matchingScore(test_img_ip,train_img_ip)
                if(matching_score<temp_matching_score):
                    matching_score=temp_matching_score
                    classified_class=train_class
                    #print(str(train_class)+" ")
        test_matching_scores[classes].append((matching_score,classified_class,classes))
        if(max_matching_score < matching_score or max_matching_score == -1):
            max_matching_score = matching_score
        if(min_matching_score > matching_score or  min_matching_score == -1):
            min_matching_score = matching_score
        '''normalized_score=float(matching_score-mini)
        normalized_score=normalized_score/(maxi-mini)
        #normalized_score=1-normalized_score
        if(classified_class!=-1 and classes >=totalclasses and normalized_score>Constants.THRESHOLD):
            far+=1
        if(classes<totalclasses and normalized_score<Constants.THRESHOLD):#classified_class==-1 and classes<totalclasses ):
            frr+=1
        if(classes<totalclasses and normalized_score>Constants.THRESHOLD):'''
        if(classified_class == classes):
            correct_matches+=1
            class_matching+=1
        print("Classiefied in "+str(classified_class)+" OriginalClass "+str(classes)+"Matching score "+str(matching_score))
    print("Class "+str(classes)+" CorrectMatchings "+str(class_matching)+" TotalImages "+str(class_images))
    classes+=1
far=0
gar=0
frr=0
#max_matching_score=302
for testclasses in range(classes):
    files =  len(test_matching_scores[testclasses])
    for file in range(files):
        normalized_score=float(0)
        score=test_matching_scores[testclasses][file][0]
        class_classified = test_matching_scores[testclasses][file][1]
        actual_class = test_matching_scores[testclasses][file][2]
        normalized_score = float(score-min_matching_score)/float(max_matching_score-min_matching_score)
        normalized_score=float(1)-normalized_score
        if(normalized_score < Constants.THRESHOLD):
            if(actual_class >= totalclasses):
                far+=1
            else:
                if(actual_class == class_classified):
                    gar+=1
        else:
            if(actual_class < totalclasses):
                frr+=1
print("GAR "+ "Correct Matches "+str(gar)+" totalImages "+str(total_system_images))
print("FRR "+str(frr)+" totalImages "+str(total_system_images))
print("FAR "+str(far)+"images "+str(total_non_system))