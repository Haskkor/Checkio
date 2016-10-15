import copy

def find_link(elem,segments,result,len_seg,results):
    if len(result) == len_seg:
        results.append(result)
        return
    for i in range(len(segments)):
        for perm in [segments[i],segments[i][2:]+segments[i][:2]]:
            if elem[2:] == perm[:2]:
                temp_result = copy.deepcopy(result) + [perm]
                find_link(perm,segments[:i]+segments[i+1:], \
                temp_result,len_seg,results)

def format_result(result):
    temp = [tuple(result[0][:2]),tuple(result[0][2:])]
    for i in range(1,len(result)):
        temp.append(tuple(result[i][2:]))
    return temp

def draw(segments):
    segments,results = [list(segment) for segment in segments],[]

    # Create a set of vertices and a dict with linked vertices
    vertices, graph = set(), dict()
    for a,b,c,d in segments:
        vertices = vertices.union({(a,b),(c,d)})
        if (a,b) in graph.keys():graph[(a,b)].add((c,d))
        else:graph[(a,b)] = {(c,d)}
        if (c,d) in graph.keys():graph[(c,d)].add((a,b))
        else:graph[(c,d)] = {(a,b)}
    # Create a list of vertices linked to an odd number of vertices
    odd_vertices = [vertice for vertice in vertices if len(graph[vertice]) % 2]
    # To use the Eulerian Cycle, the number of "odd vertices" must be
    # 0 or 2
    if len(odd_vertices) in (0,2):
        
        for i in range(len(segments)):
            for elem in [segments[i],segments[i][2:]+segments[i][:2]]:
                result = [elem]
                print(elem)
                find_link(elem,segments[:i]+segments[i+1:],result,len(segments),results)
        if results:return format_result(results[0])
        else:return results

    else:return []

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, in_data, is_possible=True):
        print(in_data)
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
    assert checker(draw,
                   {(8,4,8,6),(4,8,6,2),(6,8,8,6),(4,8,8,6),(2,6,4,2),(6,2,8,4),(6,8,6,2),
                   (2,6,6,2),(2,4,8,4),(6,8,8,4),(4,2,6,2),(4,2,8,6),(2,4,2,6),(4,2,6,8),
                   (4,2,4,8),(2,4,6,2),(2,4,4,8),(4,8,6,8),(6,2,8,6),(4,8,8,4),(2,6,8,6),
                   (2,6,6,8),(2,4,4,2),(4,2,8,4),(2,4,6,8),(2,6,4,8),(2,6,8,4),(2,4,8,6)}), "Example 4"
