# created by 김대엽 2020253113
#imports
import numpy as np
import random
import sys
import time
data = []
result1 = []
result2 = []
result3 = []
result4 = []
result5 = []
result6 = []
result7 = []
result8 = []
result9 = []
result10 = []

'''
def main(args):
    with open(args, 'r') as file:
        for line in file:
            data.append(line.strip().split('\t'))
            
if __name__ == '__main__':
    main(sys.argv[1])
'''
start = time.time()
with open("assignment2_input.txt", "r") as file :
    for line in file :
        data.append(line.strip().split('\t'))

data = np.asarray(data, dtype=float)

def euclidist(x, y) :
    result = np.round(np.sqrt(np.sum((x - y)**2, axis=0)), 3)
    return result

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def find_nearest(array, value):
    idx = array - value
    return idx

def kmedoids(datas) :
    dists = []
    distsum = []
    medoids = []
    fresult1 = []
    fresult2 = []
    fresult3 = []
    fresult4 = []
    fresult5 = []
    fresult6 = []
    fresult7 = []
    fresult8 = []
    fresult9 = []
    fresult10 = []

    for i in range(499) :
        distresults = euclidist(datas[i], datas[i + 1])
        dists.append(distresults)
    dists = np.asarray(list_chunk(dists, 1))

    for j in range(498) :
        distsumresults = dists[j] + dists[j + 1]
        distsum.append(distsumresults)
    distsum = np.concatenate(distsum)
    distsum = np.array(distsum)

    medoid = np.partition(distsum, 10) #argpartition
    for k in range(10) :
        medoids.append(medoid[k])

    for l in range(498) :
        near = find_nearest(distsum[l], medoids[0])
        fresult1.append(near)
    fresult1 = np.array(fresult1, dtype=float)
    fresult2 = np.argpartition(fresult1, 50)
    for p in range(50) :
        fresult3.append(fresult2[p])

    for q in range(498) :
        near = find_nearest(distsum[q], medoids[6])
        fresult4.append(near)
    fresult4 = np.array(fresult4, dtype=float)
    fresult5 = np.partition(fresult4, 50)
    for t in range(50):
        fresult6.append(fresult5[t])
    print(fresult3)
    print(fresult4)


kmedoids(data)

print("process time : ", round((time.time() - start), 4))