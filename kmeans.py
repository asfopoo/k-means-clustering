import math

# set all necessary variables
points = []
num_centroids = 4
centroids = []
clusters = [[], [], [], []]
cluster_zero_size = len(clusters[0])
cluster_one_size = len(clusters[1])
cluster_two_size = len(clusters[2])
cluster_three_size = len(clusters[3])
total_iterations = 0
keep_going = True

# open kmeans.txt
with open('/Users/edwardnardo/desktop/kmeans.txt', 'r') as reader:
    # set max iterations to the first line of the text file
    max_iterations = reader.readline()
    # set num points to the next line of the text file
    num_points = reader.readline()
    # set num clusters to the next line of the text file
    num_clusters = reader.readline()
    # read in the next 4 lines and append them to a list
    for i in range(num_centroids):
        centroid = reader.readline()
        # clean up the elements as we append them
        centroids.append(centroid.strip().split(","))
    for line in reader:
        # read in the rest of the file line by line and append each line to the points list
        points.append(line.strip().split(","))
    # convert centroids from nested list to one list
    centroids = sum(centroids, [])

    # loop while we haven't converged or haven't reached max iterations
while keep_going and total_iterations < int(max_iterations):
    # Compute the distance between the current point and each of the k centroids
    for index, point in enumerate(points):
        distances = []
        for cent in centroids:
            # skip calculating our centroid
            if index == int(cent):
                continue
            # d = sqrt((x2 - x1)^2 + (y2 -y1)^2)
            d = math.sqrt(math.pow(float(point[0]) - float(points[int(cent)][0]), 2) +
                          math.pow(float(point[1]) - float(points[int(cent)][1]), 2))
            # append each distance from THIS one point to each centroid to a list of distances
            distances.append(d)
        # append the point to its respective cluster by grabbing the index of the smallest distance
        # skipping the centroids
        if str(index) not in centroids:
            clusters[distances.index(min(distances))].append(point)

    # Compute the mean of all x and y values
    mean_x = 0
    mean_y = 0
    for i in range(len(clusters)):
        for x, y in clusters[i]:
            # push all x and y values respectively
            mean_x += int(x)
            mean_y += int(y)
        # divide each by total number of values to find mean
        mean_x = mean_x / len(clusters[i])
        mean_y = mean_y / len(clusters[i])
        # Update the cluster’s centroid with the results from mean calculations
        points[int(centroids[i])] = (mean_x, mean_y)

    # check if any points changed clusters
    if cluster_zero_size != len(clusters[0]) or cluster_one_size != len(clusters[1]) or cluster_two_size != len(
            clusters[2]) or cluster_three_size != len(clusters[3]):
        # since one or more clusters changed, increment the total iterations
        total_iterations += 1
        # Store/update the current size of each cluster in a list
        cluster_zero_size = len(clusters[0])
        cluster_one_size = len(clusters[1])
        cluster_two_size = len(clusters[2])
        cluster_three_size = len(clusters[3])
        # clear contents of each cluster if not last iteration
        clusters = [[], [], [], []]
    # no clusters changed so we are finished
    else:
        keep_going = False

# print results
print("iterations to achieve stability: " + str(total_iterations))
for i in range(len(centroids)):
    print("Centroid " + str(i) + ": " + str(points[int(centroids[i])]))
    print("Number of Points in cluster " + str(i) + ": " + str(len(clusters[i])))
    print("Cluster " + str(i) + ": " + str(clusters[i]))
