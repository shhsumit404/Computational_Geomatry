import convex_hull

if __name__ == '__main__':
    # Driver Code
    points = [convex_hull.Point(0, 3), convex_hull.Point(2, 2), convex_hull.Point(1, 1), convex_hull.Point(2, 1),
              convex_hull.Point(3, 0), convex_hull.Point(0, 0), convex_hull.Point(3, 3)]

    convex_hull.convexHull(points, len(points))
