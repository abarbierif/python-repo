from point2d import *
import numpy as np

N = 10
points = [Point2D((np.random.randint(0,20),np.random.randint(0,20))) for _ in range(N)]

origin = Point2D((0,0))
points_sorted = sorted(points, key=lambda x:x.euclidean_distance(origin), reverse=False)

if __name__ == '__main__':

    for _ in points_sorted:
        print('point:',_,'euclidean distance:',_.euclidean_distance(origin))
