import  Constants
import  matplotlib.pyplot as plt
def findEER(totalclasses,classes_in_system):
    test_matching_scores=[]
    for i  in range(0,totalclasses):
        test_matching_scores.append([])
    with open(Constants.SAVE_FILE_PATH,'r') as matching_scores:
        for line in matching_scores:
            line_values=line.split()
            classified_class=int(line_values[0])
            original_class = int(line_values[1])
            matching_score = float(line_values[2])
            #print(str(classified_class)+" "+str(original_class)+" "+str(matching_score))
            test_matching_scores[original_class].append((classified_class,original_class,matching_score))
            #test_matching_scores[original_class].append(matching_score,classified_class,original_class)
    print "inside findEER\n"
    max_matching_score=float(0.0)
    min_matching_score=float(10000.2)
    in_system=float(0.0)
    out_system=float(0.0)
    for i in range(0, totalclasses):
        l = len(test_matching_scores[i])
        for j in range(0, l):
            classified_class = test_matching_scores[i][j][0]
            original_class = test_matching_scores[i][j][1]
            matching_score = test_matching_scores[i][j][2]
            if(max_matching_score < matching_score):
                max_matching_score = matching_score
            if(min_matching_score > matching_score):
                min_matching_score = matching_score
            if(original_class<classes_in_system):
                in_system+=1
            else:
                out_system+=1
            #print("matching score "+str(matching_score)+" max matching score " + str(max_matching_score) + " Min matching score " + str(min_matching_score))
    print("max matching score "+ str(max_matching_score)+" Min matching score "+str(min_matching_score)+" in_system "+str(in_system)+" out_system "+str(out_system))
    final_frr=0.0
    final_far=0.0
    final_threshold=0.0
    final_gar=0.0
    min_diff=Constants.EPSILON
    FAR=[]
    THRESH=[]
    for  thresholds in range(8000,10000):
        far =float(0.0)
        gar=float(0.0)
        frr=float(0.0)
        threshold=float(thresholds)/float(10000.0)
        for i in range(0,totalclasses):
            l = len(test_matching_scores[i])
            for j in range(0,l):
                classified_class=test_matching_scores[i][j][0]
                original_class = test_matching_scores[i][j][1]
                matching_score=test_matching_scores[i][j][2]
                normalized_score = float(matching_score-min_matching_score)/float(max_matching_score-min_matching_score)
                normalized_score = 1-normalized_score
                if(normalized_score < threshold):
                    if(classified_class == original_class):
                        gar+=1
                    else:
                        if(original_class>=classes_in_system):
                            far+=1
                else:
                    if(original_class<classes_in_system):
                        frr+=1

        #print(str(test_matching_scores[i][0])+" "+str(test_matching_scores[i][1])+" "+str(test_matching_scores[i][2]))
        far=far*100.0/float(out_system)
        frr=frr*100.0/float(in_system)
        gar=gar*100.0/float(in_system)
        FAR.append(far)
        THRESH.append(threshold)
        if ( abs(far-frr)<min_diff):
            final_far=far
            final_frr =frr
            final_gar=gar
            min_diff=abs(far-frr)
            final_threshold=threshold
        print("threshold "+str(threshold)+" GAR "+str(gar)+" FRR "+str(frr)+" FAR "+str(far))
    print ("EER ")
    print("threshold " + str(final_threshold) + " GAR " + str(final_gar) + " FRR " + str(final_frr) + " FAR " + str(final_far))
    plt.plot(FAR,THRESH,'ro')
    plt.show()
findEER(591,500)