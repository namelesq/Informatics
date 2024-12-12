import math
def EuclideanDistance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
file = open('demo_2025_27_А.txt')
file.readline()
points = [list(map(float,s.replace(',','.').split()))for s in file]
finalCentroids=[]
minSumDistance = 10**10
for i in range(len(points)):
    for j in range(i+1,len(points)):
        sum_dist = 0
        for point in points:
            dist1 = EuclideanDistance(point,points[i])
            dist2 = EuclideanDistance(point,points[j])
            sum_dist += min(dist1,dist2)
            if sum_dist<minSumDistance:
                minSumDistance = sum_dist
                finalCentroids = [points[i],points[j]]
X = int(sum([x for x,y in finalCentroids])/2*10000)
Y = int(sum([y for x,y in finalCentroids])/2*10000)
print(X,Y)
