import networkx as nx
import csv
import pandas as pd

fIn = open("stormofswords.csv", "r")
G = nx.Graph()
csvreader = csv.reader(fIn)

nodeset = set()
ln = 0
for row in csvreader:
    ln+=1
    if (ln == 1):
        continue
    for i in range(2):
        n = row[i]
        if (not n in nodeset):
            nodeset.add(n)
            G.add_node(n)
    G.add_edge(row[0], row[1], weight=int(row[2]))

# create & sort by greatest to least
deg = nx.degree_centrality(G)
eigen = nx.eigenvector_centrality(G)
close = nx.closeness_centrality(G)
between = nx.betweenness_centrality(G)

ldeg = list(dict(sorted(deg.items(), key=lambda item: item[1], reverse = True)))
leigen = list(dict(sorted(eigen.items(), key=lambda item: item[1], reverse = True)))
lclose = list(dict(sorted(close.items(), key=lambda item: item[1], reverse = True)))
lbetween = list(dict(sorted(between.items(), key=lambda item: item[1], reverse = True)))

column_names = ["degree", "eigenvector", "closeness", "betweeness"]
df = pd.DataFrame(columns = column_names)
for i in range(len(ldeg)):
    row = [ldeg[i] + "(" + str(deg[ldeg[i]]) + ")",
               leigen[i] + "(" + str(eigen[leigen[i]]) + ")",
               lclose[i] + "(" + str(close[lclose[i]]) + ")",
               lbetween[i] + "(" + str(between[lbetween[i]]) + ")"]
    df.loc[len(df)] = row

print(df)

#print(G.number_of_nodes())
#print(G.number_of_edges())