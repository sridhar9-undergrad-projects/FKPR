import math
import  Constants
import cv2
import numpy as np
def findMatchingScore(test_img_ips, train_img_ips):
    has=np.zeros(len(train_img_ips))
    score=0
    #for i in range(len(train_img_ips)):
    #    has.append(0)
    for i in range(len(test_img_ips)):
        best=float(-1.0)
        matched_point=-1
        secondbest=float(-1.0)
        test_ip=test_img_ips[i]
        for j in range(len(train_img_ips)):
            if(has[j]==1):
                continue
            train_ip=train_img_ips[j]
            euclidean_dist = getEuclideanDist(test_ip,train_ip)
            if(best>euclidean_dist or best==-1.0):
                if(best!=-1.0 and (secondbest>best or secondbest==-1.0) ):
                    secondbest=best
                best=euclidean_dist
                matched_point=j
            else:
                if(secondbest>euclidean_dist or secondbest==-1.0):
                    secondbest=euclidean_dist
        ratio=float(0.0)
        ##if(best==-1.0):
        #    continue;
        ratio=best/secondbest
        #print(str(secondbest)+" "+str(best)+" "+str(ratio)+" "+str(matched_point))
        if(best<Constants.MATCHING_THRESHOLD*secondbest and matched_point!=-1):
            has[matched_point]=1
            score+=1
    return score
def matchingScore(test_img_ips,train_img_ips):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(train_img_ips, test_img_ips, k=2)
    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < Constants.MATCHING_THRESHOLD * n.distance:
            good.append([m])
    return len(good)
def getEuclideanDist(test_ip,train_ip):
    dist=float(0.0)
    for i in range(len(test_ip)):
        diff=float(test_ip[i])-float(train_ip[i])
        dist=dist+diff*diff
    dist=math.sqrt(dist)
    return  dist