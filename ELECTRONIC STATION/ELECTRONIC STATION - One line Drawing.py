##Our Robots have been spending some time researching the great artists from the Human civilization and would like to learn some of the fundamentals of art. For their first lesson, they need to learn to control their left hand-manipulators well enough to make smooth motions. For this exercise, they have decided to draw various figures on graph paper with an extra challenge rule -- don't lift your pen.
##
##A figure is represented as a set of segments in the rectangular coordinate system. Each segment is represented as a sequence of 4 numbers: (x1, y1, x2, y2), where x1, y1 are coordinates for the first end and x2, y2 -- for the second. Segments are undirected. All points in a figure are connected, so you can reach each point from any point.
##
##You should find a path in order to draw the figure. You can pass through each segment only once and are not allowed to lift the pen. The result must be represented as a sequence of points (tuples with coordinates) in the order of how the pen moves to create the drawing. The path may be started and ended at any point. If it's impossible to draw a figure then return an empty sequence. Let's look at some examples:
##
##Example 1: the figure is represented as {(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5)} and can be two path - ((7,2),(1,2),(1,5),(4,7),(7,5)) or ((7,5),(4,7),(1,5),(1,2),(7,2)).
##Example 2: the figure {(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2)} can not be drawn with the given rules, so the result is an empty list or tuple.
##Example 3: it's like fig.2 but with one more segment (1,5,7,5) and can be drawn several ways. One of them ((7,2),(1,2),(1,5),(4,7),(7,5),(7,2),(1,5),(7,5),(1,2)).
##
##Input: Figure segments as a set of tuples with 4 integers each.
##
##Output: The path as a list or tuple of tuples with 2 integers each.
##
##Example:
##
##draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5)}) == ((7,2),(1,2),(1,5),(4,7),(7,5))
##draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2)}) == []
##draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2),(1,5,7,5)}) == ((7,2),(1,2),(1,5),(4,7),(7,5),(7,2),(1,5),(7,5),(1,2))
##​
##How it is used: This mission illustrates the basics of computer generated vector graphics. The same principles may also be applied to AI pathfinding and topological work.
##
##Precondition:
##0 < len(segments) < 30
##all(all(0 < x < 100 for x in s) for s in segments)

def draw(segments):
    # Create a set of vertices and a dict with linked vertices
    vertices, graph, edges = set(), dict(), set()
    for a,b,c,d in segments:
        edges = edges.union({((a,b),(c,d))})
        vertices = vertices.union({(a,b),(c,d)})
        if (a,b) in graph.keys():graph[(a,b)].add((c,d))
        else:graph[(a,b)] = {(c,d)}
        if (c,d) in graph.keys():graph[(c,d)].add((a,b))
        else:graph[(c,d)] = {(a,b)}
    # Create a list of vertices linked to an odd number of vertices
    odd_vertices = [vertice for vertice in vertices if len(graph[vertice]) % 2]
    # Eulerian cycle test
    if len(odd_vertices) in (0,2):
        # Find Eulerian path
        result, temp_result, done = [],[],False
        current_vertice = odd_vertices[0] if odd_vertices \
                          else next(iter(vertices))
        while not done:
            edges_current = [edge for edge in edges \
                             if current_vertice in edge]
            connections_current = [vertice for edge in edges_current \
                                   for vertice in edge if \
                                   vertice != current_vertice]
            if connections_current :
                temp_result.append(current_vertice)
                current_vertice = connections_current[0]
                temp = [edge for edge in edges_current \
                        if current_vertice in edge]
                edges.remove(temp[0])
            else:
                result.append(current_vertice)
                if not temp_result:done = True
                else: current_vertice = temp_result.pop()
        return result
    else:return []
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                    (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
                   False), "Example 2"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
                    (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
