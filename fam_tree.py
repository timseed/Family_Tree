import networkx as nx
import matplotlib.pyplot as plt
import random
G = nx.Graph()
#G = nx.path_graph(8)


pop=40
kid_cnt=3
for i in range(pop):
    G.add_node(i)

married=random.sample(range(pop),pop)
for i in range(0,pop,2):
    print(str.format('Married {} to {}',married[i],married[i+1]))
print('-------------------')
for i in range(0,pop,2):
    print(str.format('Married {} to {}',married[i],married[i+1]))
    G.add_edge(married[i],married[i+1])
    p=len(G.nodes())
    print(str.format('Current pop is {}',p))
    for kids in range(kid_cnt):
        G.add_node((p+kids))
        #G.add_node("%i",int(p+kids))
        G.add_edge(married[i],(p+kids))
        G.add_edge(married[i+1],(p+kids))
        print(str.format('Parent {} -> Child {}',married[i],(p+kids)))
        print(str.format('Parent {} -> Child {}',married[i+1],(p+kids)))
        print("Processing kid %d"%kids)

plt.title("draw_networkx")
nx.draw_networkx(G)
plt.show()