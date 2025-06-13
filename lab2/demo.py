import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# BFSS
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    if start == goal:
        return [start]
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            visited.add(node)
    return []

# DFS 
def dfs(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return []

def draw_graph(graph_data, path):
    G = nx.Graph()
    for node, neighbors in graph_data.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    edge_colors = ['red' if (u in path and v in path and abs(path.index(u) - path.index(v)) == 1) else 'gray' for u, v in G.edges()]
    node_colors = ['orange' if node in path else 'lightgray' for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color=node_colors, node_size=800, font_weight='bold')
    st.pyplot(plt.gcf())
    plt.clf()

st.set_page_config(page_title="BFS & DFS Visualization", layout="centered")
st.title("Mô phỏng thuật toán BFS và DFS")

graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'B'],
    'B': ['S', 'A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'G'],
    'G': ['D']
}

nodes = list(graph.keys())

start = st.selectbox("Chọn đỉnh bắt đầu", nodes, key="start")
goal = st.selectbox("Chọn đỉnh kết thúc", nodes, key="goal")
algo = st.radio("Chọn thuật toán", ["BFS", "DFS"])

if st.button("Tìm đường đi"):
    if algo == "BFS":
        path = bfs(graph, start, goal)
    else:
        path = dfs(graph, start, goal)

    if path:
        st.success(f"Đường đi từ {start} đến {goal} ({algo}): {' → '.join(path)}")
        draw_graph(graph, path)
    else:
        st.error("Không tìm được đường đi.")