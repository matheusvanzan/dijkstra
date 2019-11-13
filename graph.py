import networkx as nx

			
G = nx.DiGraph()

inf = float('inf')
G.add_node('A', visited = False, weight = inf, path = [])
G.add_node('B', visited = False, weight = inf, path = [])
G.add_node('C', visited = False, weight = inf, path = [])
G.add_node('D', visited = False, weight = inf, path = [])
G.add_node('E', visited = False, weight = inf, path = [])
G.add_node('F', visited = False, weight = inf, path = [])

G.add_edge('A', 'B', distance = 3)
G.add_edge('B', 'A', distance = 3)
G.add_edge('A', 'D', distance = 4)
G.add_edge('D', 'A', distance = 4)
G.add_edge('A', 'C', distance = 2)
G.add_edge('C', 'A', distance = 2)
G.add_edge('B', 'D', distance = 2)
G.add_edge('D', 'B', distance = 2)
G.add_edge('B', 'F', distance = 5)
G.add_edge('F', 'B', distance = 5)
G.add_edge('C', 'E', distance = 1)
G.add_edge('E', 'C', distance = 1)
G.add_edge('D', 'E', distance = 1)
G.add_edge('E', 'D', distance = 1)
G.add_edge('D', 'F', distance = 3)
G.add_edge('F', 'D', distance = 3)
G.add_edge('E', 'F', distance = 2)
G.add_edge('F', 'E', distance = 2)


def not_visited(g):
	return [k for k, v in g.nodes.items() if not v['visited']]

def min_weight_not_visited(g):
	min_key = ''
	min_value = float('inf')

	for k, v in g.nodes.items():
		if v['weight'] < min_value and not v['visited']:
			min_key = k
			min_value = v['weight']

	return min_key


current = 'A'
G.nodes[current]['weight'] = 0
G.nodes[current]['path'] = [current]

while len(not_visited(G)) > 0:

	for k in G.adj[current]:
		node = G.nodes[current]
		other = G.nodes[k]
		edge = G.edges[current, k]

		if node['weight'] + edge['distance'] < other['weight']:
			other['weight'] = node['weight'] + edge['distance']
			other['path'] = node['path'] + [k]

	node['visited'] = True
	current = min_weight_not_visited(G)

for k, v in G.nodes.items():
	print(k, v)