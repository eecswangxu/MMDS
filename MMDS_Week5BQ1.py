import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def points_distance(a, b):
    return math.sqrt(math.pow((a.x - b.x), 2) + math.pow((a.y - b.y), 2))


def compute_centroid(cluster):
    sum_x = 0.0
    sum_y = 0.0
    for point in cluster.points:
        sum_x += point.x
        sum_y += point.y
    n = len(cluster.points)
    return Point(sum_x / n, sum_y / n)


def print_point(point):
    print "(%0.1f,%0.1f)" % (point.x, point.y)


class Cluster(object):
    def __init__(self, centroid, points):
        self.centroid = centroid
        self.points = points


def print_cluster(cluster):
    print "------------------ Cluster ------------------"
    print "Centroid:"
    print_point(cluster.centroid)
    print "Points:"
    for point in cluster.points:
        print_point(point)

def print_clusters(clusters):
    for cluster in clusters:
        print_cluster(cluster)

points = [Point(28,145), Point(65,140), Point(50,130), Point(25,125), Point(55,118),
          Point(38,115), Point(44,105), Point(29,97), Point(50,90), Point(63,88),
          Point(43,83), Point(35,63), Point(55, 63), Point(50, 60), Point(42,57),
          Point(23,40), Point(64,37), Point(50,30), Point(33,22), Point(55,20)]

centroids = [Point(25,125), Point(44, 105), Point(29,97), Point(35,63), Point(55,63),
             Point(42,57), Point(23, 40), Point(64,37), Point(33,22), Point(55,20)]

clusters = []
for centroid in centroids:
    clusters.append(Cluster(centroid, []))

#print_clusters(clusters)
#print

# Assign points to clusters initially
for point in points:
    #print_point(point)
    min_dist = None
    its_cluster = clusters[0]
    for cluster in clusters:
        dist = points_distance(point, cluster.centroid)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            its_cluster = cluster

    #print "its_cluster is now:"
    #print_cluster(its_cluster)
    #print

    #print "Assigning the point to"
    #print_point(its_cluster.centroid)

    its_cluster.points.append(point)
    #print "its_cluster is now:"
    #print_cluster(its_cluster)
    #print

print "Initial clusters:\n"
print_clusters(clusters)

# Recompute the centroids of each of the clusters
for cluster in clusters:
    cluster.centroid = compute_centroid(cluster)

print "After recomputing the centroids of clusters:\n"
print_clusters(clusters)


# Assign points to clusters again
for cluster in clusters:
    for point in cluster.points:
        min_dist = points_distance(point, cluster.centroid)
        for another_cluster in [c for c in clusters if c.centroid != cluster.centroid]:
            dist = points_distance(point, another_cluster.centroid)
            if dist < min_dist:
                min_dist = dist
                print "Changing cluster for "
                print_point(point)

#print "After reassigning points to clusters again:\n"
#print_clusters(clusters)