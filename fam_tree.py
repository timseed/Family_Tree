import networkx as nx
import matplotlib.pyplot as plt
import random
G = nx.Graph()
#G = nx.path_graph(8)


pop=20
kid_cnt=9
generation_cnt=6
DIVORCE_RATE=10

for i in range(pop):
    G.add_node(i)

married=random.sample(range(pop),pop)
for i in range(0,pop,2):
    print(str.format('Married {} to {}',married[i],married[i+1]))
print('-------------------')


def expand(G,level,pop_array,kid_cnt):
    new_born=[]
    #We need to randomize the un-married population
    #Else brother marries sister etc
    #pop_array=random.sample(set(pop_array),len(pop_array))
    random.shuffle(pop_array)
    for i in range(0,len(pop_array),2):
        try:
            #print(str.format('Married {} to {}',married[i],married[i+1]))
            G.add_edge(married[i],married[i+1],{'rel': 'Married'})
            p=len(G.nodes())
            #print(str.format('Current pop is {}',p))
            for kids in range(random.randint(0,kid_cnt)):
                G.add_node((p+kids))
                new_born.append((p+kids))
                #G.add_node("%i",int(p+kids))
                G.add_edge(married[i],(p+kids),{'rel':'Parent of'})
                G.add_edge(married[i+1],(p+kids),{'rel':'Parent of'})
                #print(str.format('Parent {} -> Child {}',married[i],(p+kids)))
                #print(str.format('Parent {} -> Child {}',married[i+1],(p+kids)))
                #print("Processing kid %d"%kids)
        except IndexError:
            pass
    #
    #Divorce time !!!
    #From the pop_array (these people have just had kids)
    #We need to pick 3% - and then place them in the new_born array
    #So they can be married again and have kids again
    df=open("divorce_list.txt","a")
    num_of_divorce = int(len(pop_array)*DIVORCE_RATE/100)
    for divorce_id in range(num_of_divorce):

        divorce_person_idx=random.randint(0,len(pop_array)-1)
        div_id = pop_array[divorce_person_idx]
        new_born.append(div_id)
        df.write(str.format('Divorced {}\n',div_id))

    df.close()

    return new_born

for generation in range(generation_cnt):
    married=expand(G,generation,married,kid_cnt)
    p=len(G.nodes())
    print(str.format('Gen {} Current pop is {}',generation,p))


with open('edges.csv','w') as of:
    for e in G.edges(data=True):
        of.write(str.format('{},{},{}\n',e[0],e[1],e[2]['rel']))
    of.close()
print("edges.csv is done")

plt.title("draw_networkx")
#nx.draw_networkx(G)
#plt.show()