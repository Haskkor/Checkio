##A ring topology is a network configuration where the devices are connected to each other in a circular shape. Optical rings are widely used in mobile networks to transport the traffic from a base station to the backbone, through the mobile backhaul.
##
##Definition of a ring
##
##For the sake of simplicity, in this task, we define a ring as a connex graph which vertexes:
##
##- have a degree 2, which means they have 2 incident edges.
##- are connected to two distinct vertexes
##
##These two conditions ensure that there is a single link between each pair of adjacent nodes. Ring are represented as a string made of distinct characters, which position in the string reflects the position in the ring. For instance, the ring "AEFCBG" defines the following topology:
##ring definition
##
##Multiple traffic flows will be routed on the ring. 
##Each flow is routed on the shortest path from the ingress node (starting point of the traffic) to the egress node (exit point of the traffic).
##If there are two shortest paths, the path which order fits the ring definition is kept.
##Let's consider the following situation:
##paths along the ring
##
##The path from A to B (and from B to A) will be "A - G - B", because it uses only two links, while the path going the other way around ("A - E - F - C - B") uses five links.
##However, there are two paths of equal length to route a traffic from A to C: "A - E - F - C" and "A - G - B - C". The first one, "A - E - F - C", is kept: it is the same order as in the ring definition ("AEFCBG").
##The traffic from C to A will use the path "C - B - G - A": the routing is asymmetric in that case.
##Flow aggregation
##
##A traffic flow is represented as a couple (s, dr) where:
##
##- s is a string of length 2, containing the ingress node and the egress node.
##- dr is the data rate in Gbps (gigabit per second).
##
##The data rate of a traffic flow will be counted for all the links of the shortest path.
##A traffic flow ("AB", 5) means that 5 Gbps will be routed on the shortest path from A to B. 
##We count 5 Gbps on the link "AG" and 5 Gbps on the link "GB". For a traffic flow ("CA", 15), we count 15 Gbps on the links "CB", "BG", and "GA".
##In order to simplify the model, we consider that the traffic flows ingress -> egress and egress -> ingress are equivalent with regard to dimensioning.
##Two traffic flows ("AG", 3) and ("GA", 3) induce a 6-Gbps flow on the link AG, as would ("AG", 6) or ("GA", 6): links are not directional. Given a list of traffic flows, we consider the resulting bandwidth on each link to dimension the ring.
##Ethernet links dimensioning
##
##There are five main types of Ethernet links used in mobile networks:
##
##- Fast Ethernet (FE): 100 Mbps (or 0.1 Gbps)
##- Gigabit Ethernet (GE): 1 Gbps.
##- 10 Gigabit Ethernet (10GE): 10 Gbps
##- 40 Gigabit Ethernet (40GE): 40 Gbps.
##- 100 Gigabit Ethernet (100GE): 100 Gbps.
##
##In order to select a type of link, we look for the smallest bandwidth allowing to carry the whole traffic with a single link. Handling a 5-Gbps traffic would require 50 FE links, 5 GE links, or 1 10GE link. Therefore, a 10GE Ethernet link is used. For a 15-Gbps traffic, a 40GE Ethernet link is required. For a traffic higher than 100 Gbps, 100GE Ethenet links are used (2 100GE Ethernet links for a 101-Gbps flow).
##Given a ring and a list of traffic flows, you should return the number of Ethernet links of each type that are required to carry the resulting bandwidth:
##resulting dimensioning
##
##In this example, we have 10 Gbps from E to C, 5 Gbps from A to C and 60 Gbps from A to B.
##These traffic flows induce the following bandwidth: 15 Gbps from E to C, 5 Gbps from A to E and 60 Gbps from A to B.
##The link dimensioning results in 2 100GE, 2 40GE and 1 10GE Ethernet links.
##The result is given as a list containing the number of links for each category, from 100GE to FE. In our example, the result is [2, 2, 1, 0, 0]
##
##Input: A variable number of arguments. The first one is a ring, represented as a string where each character is a node. The remaining arguments are traffic flows, represented as couples (s, dr) where s is a 2-characters string (ingress node, egress node) and dr is a positive value (traffic in Gbps).
##
##Output: A list with 5 integers, one per type of link, in decreasing order of bandwidth capacity.
##
##Example:
##
##checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
##checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
##checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]
##
##How it is used: Links dimensioning is used for network planning and design. For real networks, various softwares are used to dimension the network based on the expected traffic load (for pre-sales engineers, when the network does not yet exist), or traffic measurements (for post-sales engineers to compute how much traffic the network can handle, and plan the network evolution). 
##However, real-life network dimensioning is much more complex than what is described in this task, as it deals with traffic differentiation and protection against equipment failure.
##
##Preconditions:
##The ring is a valid ring (connex, 2-degree nodes).
##The traffic is a positive value (integer or float).

ETHERNET = (100, 40, 10, 1, 0.1) # Ethernet bandwidth capacity in Gbps

def find_sp(ring,flow):
    path_flow = ""
    modified_ring = ring[ring.index(flow[0]):]+ring[:ring.index(flow[0])]
    for letter in modified_ring:
        if letter == flow[1]:
            path_flow += letter
            break
        else:path_flow += letter
    return path_flow

def checkio(ring, *flows):
    dict_segments = dict()
    for flow in flows:
        if len(find_sp(ring,flow[0])) > len(find_sp(ring,flow[0][1]+flow[0][0])):
            shortest_path = find_sp(ring,flow[0][1]+flow[0][0])
        else:shortest_path = find_sp(ring,flow[0])
        for i in range(len(shortest_path) - 1):
            if (shortest_path[i]+shortest_path[i+1]) in dict_segments:
                dict_segments[(shortest_path[i]+shortest_path[i+1])] += flow[1]
            else:
                dict_segments[(shortest_path[i]+shortest_path[i+1])] = flow[1]
    result = []
    for i in range(len(ETHERNET)-1):
        sum = 0
        for val in dict_segments.values():
            if val <= ETHERNET[i] and val > ETHERNET[i+1]:
                sum += 1
        result.append(sum)
    sum = 0
    for val in dict_segments.values():
        if val < 0.1:
            sum += 1
    result.append(sum)
    for val in dict_segments.values():
        if val > 100:
            result[0] += val//100
            if val % 100 != 0:
                result[0] += 1
    return result
        
if __name__ == '__main__':
    # These "asserts" are used only for self-checking and not necessary for auto-testing
    assert checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]
