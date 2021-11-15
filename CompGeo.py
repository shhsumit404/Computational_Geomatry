import csv
import math
import sys

def write_result(arr):
    with open('return_file.csv', mode='w') as return_file:
        file_writer = csv.writer(return_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        for each in range(len(arr)):
            print(each)
            if str(arr[each][0]) == 'l':
                x = 1
                while x <= len(arr[each])-4:
                    file_writer.writerow([arr[each][x], arr[each][x+1], arr[each][x+2], arr[each][x+3]])
                    x = x+4
            elif str(arr[each][0])=='c':
                print(arr[each])
                file_writer.writerow([arr[each][1], arr[each][2], arr[each][3], arr[each][4], arr[each][5], arr[each][6]])
            elif str(arr[each][0]) == 'h':
                x = 1
                print(arr[each])
                while x <= len(arr[each])-2:
                    file_writer.writerow([arr[each][x], arr[each][x+1]])
                    x = x+2
                pass

    return
def Left_index(points):
    minn = 0
    for i in range(1,len(points)):
        if float(points[i]["x"]) < float(points[minn]["x"]):
            minn = i
        elif float(points[i]["x"]) == float(points[minn]["x"]):
            if float(points[i]["y"]) > float(points[minn]["y"]):
                minn = i
    
    return minn

def orientation(p, q, r):
    val = (float(q["y"]) - float(p["y"])) * (float(r["x"]) - float(q["x"])) - (float(q["x"]) - float(p["x"])) * (float(r["y"]) - float(q["y"]))

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2
def lineSegment(arr):
    
    if((len(arr)-1) % 4 !=0): #check to make sure number of pointer variables in arr are multiples of 4
        print("Array used for line segement intersection does not have the correct number of variables")
        return
    lines=[] #list of line dicts
    i = 1 #iterator for arr
    x = 0 #iterator for lines
    ret_arr=[]
    ret_arr.append("l")

    while i <= (len(arr)-4):
        line = {}#dict contain x1, y1, x2 and y2 for all line segments
        #set the x and y for the line segments contained in the line dict and append to list Lines
        line["x1"] = arr[i]
        i+=1
        line["y1"] = arr[i]
        i+=1
        line["x2"] = arr[i]
        i+=1
        line["y2"] = arr[i]
        lines.append(line)
        i+=1

    #compute the slope for all line segments in lines
    for z in range(len(lines)):
        lines[z]["slope"] = (float(lines[z].get('y2')) - float(lines[z].get('y1'))) / (float(lines[z].get('x2')) - float(lines[z].get('x1'))) 

    for outer in range(len(lines)-1):
        A1 = float(lines[outer]["y2"])-float(lines[outer]["y1"])
        B1 = float(lines[outer]["x1"])-float(lines[outer]["x2"])
        C1 = (A1 * float(lines[outer]["x1"])) +(B1 * float(lines[outer]["y1"]))

        for inner in range((outer+1), len(lines)):
            A2 = float(lines[inner]["y2"])-float(lines[inner]["y1"])
            B2 = float(lines[inner]["x1"])-float(lines[inner]["x2"])
            C2 = (A2 * float(lines[inner]["x1"])) + (B2 * float(lines[inner]["y1"]))
            
            det = (A1 * B2) - (A2 * B1)
            if det == 0:
                print("Line Segment ",outer," is parallel to Line Segment",inner)
            else:
                x = (B2 * C1 - B1 * C2)/det
                y = (A1 * C2 - A2 * C1)/det
                minX1 = min(float(lines[outer]["x1"]), float(lines[outer]["x2"]))
                maxX1 = max(float(lines[outer]["x1"]), float(lines[outer]["x2"]))
                minX2 = min(float(lines[inner]["x1"]), float(lines[inner]["x2"]))
                maxX2 = max(float(lines[inner]["x1"]), float(lines[inner]["x2"]))


                if minX1 <= x <= maxX1 and minX2 <= x <= maxX2:
                    ret_arr.append(outer)
                    ret_arr.append(inner)
                    ret_arr.append(x)
                    ret_arr.append(y)
                    print("Line Segment ",outer," intersects with line segment ",inner," at x:",x,"and y:",y)

        
    return ret_arr

def closestPair(arr):
    if((len(arr)-1) % 2 !=0): #check to make sure number of pointer variables in arr are multiples of 2
        print("Array used for Closest Pair Of Pointes does not have the correct number of variables")
        return

    points = []
    i = 1
    while i <= (len(arr)-2):
        point = {}#dict contains x and y for all points
        #set the x and y for each point in points
        point["x"] = arr[i]
        i+=1
        point["y"] = arr[i]
        i+=1
        points.append(point)
        
    minPairs = {}
    minPairs["distance"] = sys.maxsize
    for outer in range(len(points)-1):
        for inner in range((outer + 1), len(points)):
            if points[outer]["x"] == points[inner]["x"] and points[outer]["y"] == points[inner]["y"]:
                print("File for Closest Pairs contains duplicate points point:", outer," and point:", inner,"this distance will not be calculated")
            else:
                dist = math.sqrt((float(points[outer]["x"]) - float(points[inner]["x"]))**2 + (float(points[outer]["y"]) - float(points[inner]["y"]))**2)
                if dist < float(minPairs["distance"]):
                    minPairs["distance"] = dist
                    minPairs["point1"] = points[outer]
                    minPairs["point2"] = points[inner]


    print("the closest pair of points is point ", outer, minPairs["point1"]," and point ", inner, minPairs["point2"]," whith a distance of ", minPairs["distance"])
    ret_arr = []
    ret_arr.append("c")
    ret_arr.append(outer)
    ret_arr.append(minPairs["point1"]["x"])
    ret_arr.append(minPairs["point1"]["y"])
    ret_arr.append(inner)
    ret_arr.append(minPairs["point2"]["x"])
    ret_arr.append(minPairs["point2"]["y"])


    
    return ret_arr

# copied from https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/ 
# https://www.programcreek.com/python/example/91991/scipy.spatial.ConvexHull 
# https://scipy-cookbook.readthedocs.io/items/Finding_Convex_Hull.html 
# http://chris35wills.github.io/convex_hull/ 
# https://www.geeksforgeeks.org/quickhull-algorithm-convex-hull/
# https://algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Jarvis-s-March/ 

def convexHull(arr):
    
    if((len(arr)-1) % 2 !=0): #check to make sure number of pointer variables in arr are multiples of 2
        print("Array used for Closest Pair Of Pointes does not have the correct number of variables")
        return
    points = []
    i = 1
    while i <= (len(arr)-2):
        point = {}#dict contains x and y for all points
        #set the x and y for each point in points
        point["x"] = arr[i]
        i+=1
        point["y"] = arr[i]
        i+=1
        points.append(point)
    
    n = len(points)
    if n < 3:
        return
 
    # Find the leftmost point
    l = Left_index(points)
 
    hull = []
    
     
    '''
    Start from leftmost point, keep moving counterclockwise
    until reach the start point again. This loop runs O(h)
    times where h is number of points in result or output.
    '''
    p = l
    q = 0
    while(True):
         
        # Add current point to result
        hull.append(p)
 
        '''
        Search for a point 'q' such that orientation(p, q,
        x) is counterclockwise for all points 'x'. The idea
        is to keep track of last visited most counterclock-
        wise point in q. If any point 'i' is more counterclock-
        wise than q, then update q.
        '''
        q = (p + 1) % n
 
        for i in range(n):
             
            # If i is more counterclockwise
            # than current q, then update q
            if(orientation(points[p], points[i], points[q]) == 2):
                q = i
 
        '''
        Now q is the most counterclockwise with respect to p
        Set p as q for next iteration, so that q is added to
        result 'hull'
        '''
        p = q
 
        # While we don't come to first point
        if(p == l):
            break
 
    # Print Result
    ret_val = []
    for each in hull:
        print(points[each]["x"], points[each]["y"])
        ret_val.append(points[each]["x"])
        ret_val.append(points[each]["y"])
    ret_val.insert(0, "h")
    return ret_val

#https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
def largestEmptyCircle(arr):
    
    # https://gist.github.com/w8r/85d5c38a0d574d2555e94821032ed232 
#     function getLargestEmptyCircle(nodes, triangles, n = 1, minRadius = 0) {
#   //var triangles = new Delaunay(nodes).triangulate();
#   var convexhull = convexHull(nodes);
#   var candidates = [], radii = {}, t, c;
#   for (var i = 0, len = triangles.length; i < len; i += 3) {
#     c = getCircumcenter(triangles[i], triangles[i + 1], triangles[i + 2]);
#     if (inside(convexhull, c)) {
#       candidates.push(i);
#       radii[i] = circumcircleRadiusSquared(triangles[i], triangles[i + 1], triangles[i + 2]);
#     }
#   }
#   candidates.sort((a, b) => radii[a] - radii[b]);

#   var max = candidates[0], r;
#   var maxR = circumcircleRadiusSquared(triangles[max], triangles[max + 1], triangles[max + 2]);
#   var circles = [];
#   var minRadiusSquared = minRadius * minRadius;

#   for (var i = 0, len = candidates.length; i < len; i++) {
#     t = candidates[i];
#     r = circumcircleRadiusSquared(triangles[t], triangles[t + 1], triangles[t + 2]);
#     if (r > maxR && r > minRadiusSquared) {
#       max = t;
#       maxR = r;
#       circles.push(max);
#       if (circles.length > n) circles.shift();
#     }
#   }
#   return circles.map((c) => makeCircle(triangles[c], triangles[c + 1], triangles[c + 2]));
# }
    return 

def main():
    print("For CSV files input into this program this first entry in each row should be the letter corresponding with the function you want preformed on the entries of that row.")
    print("L for line segment intersection")
    print("C for closest pair of points")
    print("H for convex hull")
    print("E for largest empty circle")
    print("After the fuction designator point values should be entered with the x value first followed by the y value with commas seperating everything.")
    csv_file_name = input("Enter file path of the CSV file you wish to use :")
    print(csv_file_name)
    #stuff to handle
    #csv file read
    with open(csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)
        rows = []
        retValues = []
        i = 0
        for row in csv_reader:
            rows.append(row)
            if rows[i][0].lower() == 'l':
               lsOut =  lineSegment(rows[i])
               retValues.append(lsOut)
            elif rows[i][0].lower() == 'c':
                CpOut = closestPair(rows[i])
                retValues.append(CpOut)
            elif rows[i][0].lower() == 'h':
                ChOut = convexHull(rows[i])
                retValues.append(ChOut)
            elif rows[i][0].lower() == 'e':
                largestEmptyCircle(rows[i])
            else:
                print("Function designator for row ", i ,"not found, must be L, C, H or E.")

         
            i = i + 1
        write_result(retValues)

      
    #Line segment intersection: find the intersections between given line segments
    #closet pair of points: find the two with the smallest distance from eachother
    #convex hull: given a set of points, find the smallest convex polyhedron/polygon containing all the points, represented as the set of points on the polygon edge. 
    #largest empty circle: given a set of points, find the largest circle with its center inside of their convex hull and enclosing none of them. 

if __name__ == '__main__':
    main()
