#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Breadth First Search (BFS)
void BFS(int start, const vector<vector<int>>& graph) {
    int n = graph.size();
    vector<bool> visited(n, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    cout << "BFS Traversal: ";

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        cout << current << " ";

        for (int neighbor : graph[current]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }

    cout << endl;
}

// Depth First Search (DFS)
void DFS(int current, const vector<vector<int>>& graph,
         vector<bool>& visited) {

    visited[current] = true;
    cout << current << " ";

    for (int neighbor : graph[current]) {
        if (!visited[neighbor]) {
            DFS(neighbor, graph, visited);
        }
    }
}

int main() {
    int vertices, edges;

    cout << "Enter number of vertices: ";
    cin >> vertices;

    cout << "Enter number of edges: ";
    cin >> edges;

    // Adjacency list
    vector<vector<int>> graph(vertices);

    cout << "Enter edges (u v):" << endl;

    for (int i = 0; i < edges; i++) {
        int u, v;
        cin >> u >> v;

        // Undirected graph
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int start;
    cout << "Enter starting vertex: ";
    cin >> start;

    // BFS
    BFS(start, graph);

    // DFS
    vector<bool> visited(vertices, false);

    cout << "DFS Traversal: ";
    DFS(start, graph, visited);
    cout << endl;

    return 0;
}
