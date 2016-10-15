import networkx as nx
import matplotlib.pyplot as plt
import random
G = nx.Graph()
#G = nx.path_graph(8)


pop=30
kid_cnt=9
for i in range(pop):
    G.add_node(i)

married=random.sample(range(pop),pop)
for i in range(0,pop,2):
    print(str.format('Married {} to {}',married[i],married[i+1]))
print('-------------------')


def expand(G,pop_array,kid_cnt):
    new_born=[]
    for i in range(0,len(pop_array),2):
        try:
            #print(str.format('Married {} to {}',married[i],married[i+1]))
            G.add_edge(married[i],married[i+1])
            p=len(G.nodes())
            #print(str.format('Current pop is {}',p))
            for kids in range(random.randint(0,kid_cnt)):
                G.add_node((p+kids))
                new_born.append((p+kids))
                #G.add_node("%i",int(p+kids))
                G.add_edge(married[i],(p+kids))
                G.add_edge(married[i+1],(p+kids))
                #print(str.format('Parent {} -> Child {}',married[i],(p+kids)))
                #print(str.format('Parent {} -> Child {}',married[i+1],(p+kids)))
                #print("Processing kid %d"%kids)
        except IndexError:
            pass
    return new_born

for generation in range(6):
    married=expand(G,married,kid_cnt)
    p=len(G.nodes())
    print(str.format('Gen {} Current pop is {}',generation,p))


with open('edges.csv','w') as of:
    for e in G.edges():
        of.write(str.format('{},{}\n',e[0],e[1]))
    of.close()
print("edges.csv is done")

plt.title("draw_networkx")
#nx.draw_networkx(G)
#plt.show()