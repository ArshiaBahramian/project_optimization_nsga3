import networkx as nx

def calculate_critical_path(activities, dependencies):
    G = nx.DiGraph()
    G.add_nodes_from(activities.keys())
    for activity, prereqs in dependencies.items():
        for prereq in prereqs:
            G.add_edge(prereq, activity, weight=-activities[activity])

    # اطمینان از وجود مسیر از Start به End
    if not nx.has_path(G, 'Start', 'End'):
        return [], 0

    # محاسبه طولانی‌ترین مسیر (مسیر بحرانی)
    length, path = nx.single_source_bellman_ford(G, 'Start', target='End', weight='weight')
    critical_path = path
    total_duration = -length

    return critical_path, total_duration

activities = {
    'Start': 0,
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 4,
    'E': 6,
    'F': 1,
    'End': 0
}

dependencies = {
    'Start': ['A', 'B'],
    'A': ['C'],
    'B': ['C'],
    'C': ['D', 'E'],
    'D': ['End'],
    'E': ['F'],
    'F': ['End']
}

critical_path, total_duration = calculate_critical_path(activities, dependencies)
if critical_path:
    print("Critical Path:", " -> ".join(critical_path))
    print("Total Duration:", total_duration)
else:
    print("No valid path from Start to End.")
