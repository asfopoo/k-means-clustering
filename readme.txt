1. Author: Edward Nardo, JHED ID: C2FFF9
2. Module Info: Module 4, k-means clustering, due: Sunday, February 28, 2021
3. Approach:

kmeans.py - I began by declaring all necessary variables on lines 4-13.  I then open the kmeans.txt file using the with
keyword which will automatically close the file for me when finished. I then read the first line only and set its value equal to
a variable called max_iterations.  I then read in the second line and set it equal to num_points, then the third line.
I then read in the next 4 lines which are each centroids, and append them to a list named centroids.  I then read in
the remaining lines of the text file and append them to another list called points, after cleaning up white space, and
unneeded characters.  On line 32, the list of centroids was a nested list so I flattened it to a single list.
On line 35 I then start my while loop, looping until convergence(noted by a boolean variable named keep_going) or until
we've reached our max iterations.  The next section from lines 37-51 is where I compute distance and add the point to
its respective cluster.  I begin by looping the list of points.  I used `for index, point in enumerate(points):` so
that I could access not only each point but also its index in the list of points.  Then for each point, I loop my list of
4 centroids and calculate distance using the formula d = sqrt((x2 - x1)^2 + (y2 -y1)^2).  I also skip the points that
represent centroids noted on lines 41-42.  This gives me 4 distances.  I add them to a list called distances.  Now, here's
where the magic happens!  Since lists guarantee the order of its elements, We map the 4 distances to the 4 centroids and
the 4 clusters.  So for example, in our list of distances, if element 1 is the smallest, that means it is closest to
element 1 of the centroids list. So we can then add it to element 1 of the clusters list.  So all three lists are nested
lists containing four lists each, which all correspond to each other.  Grabbing the smallest distance was done using the
built in function <list>.index(min(<list>)) shown on line 51.  So what I did there was grab the index of the smallest distance,
I then append the current point to the clusters list at that smallest distance index since the indexes map to each other.
The next section from lines 54-65 compute the mean of all the x and y values in each list and update the centroid
points with those means.  So on line 54 and 55 I set mean x and y to 0.  I then loop the four lists inside the list of
clusters using a nested for loop.  I add all of the x and y values together then divide by the length of the list.
I then update the centroids in the points list.  I use the index of the outer loop to get the value in the centroids list,
which is the index of the centroid in the points list (line 65). I then update that point with the new means.  I then check
if any of the sizes of the clusters have changed, If they did I reset their size, clear out the clusters list and loop
the while loop again.  If they did not, we assume we have reached convergence and set keep_going to false which will
terminate the while loop.  I then print all of the iterations, centroids, and clusters.

4. Known bugs:  When checking if any of the cluster lengths have changed, we assume, if they haven't that we have reached
convergence.  But there is the possibility that 2 points could have swapped clusters, meaning we haven't reached
convergence but our lengths did not change either.

Also My final numbers do not match what is in the assignment example.  I have troubleshooted everything and can't find out
why.  The root of the problem is that one or two stray points are getting added to the wrong cluster but I can't find out
why.  This is throwing the final calculations off by just a little bit.