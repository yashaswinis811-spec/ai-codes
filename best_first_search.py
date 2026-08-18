#include <iostream>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

// Best-First Search function
void bestFirstSearch(int start, int goal,
                     const vector<vector<pair<int, int>>>& graph,
                     const vector<int>& heuristic) {

    // Min-priority queue:
    // {heuristic value, node}
    priority_queue<
        pair<int, int>,
        vector<pair<int, int>>,
        greater<pair<int, int>>
    > pq;

    vector<bool> visited(graph.size(), false);

    pq.push({heuristic[start], start});

    cout << "\nBest-First Search Traversal: ";

    while (!pq.empty()) {

        int current = pq.top().second;
        pq.pop();

        // Skip if already visited
        if (visited[current]) {
            continue;
        }

        visited[current] = true;

        cout << current << " ";

        // Goal reached
        if (current == goal) {
            cout << "\nGoal node " << goal << " reached!" << endl;
            return;
        }

        // Add unvisited neighbors to priority queue
        for (auto neighbor : graph[current]) {
            int nextNode = neighbor.first;

            if (!visited[nextNode]) {
                pq.push({heuristic[nextNode], nextNode});
            }
        }
    }

    cout << "\nGoal node " << goal << " could not be reached." << endl;
}

int main() {

    int vertices, edges;

    cout << "Enter number of vertices: ";
    cin >> vertices;

    cout << "Enter number of edges: ";
    cin >> edges;

    // Graph represented using adjacency list
    // pair = {neighbor, edge cost}
    vector<vector<pair<int, int>>> graph(vertices);

    cout << "\nEnter edges (u v cost):" << endl;

    for (int i = 0; i < edges; i++) {
        int u, v, cost;

        cin >> u >> v >> cost;

        // Undirected graph
        graph[u].push_back({v, cost});
        graph[v].push_back({u, cost});
    }

    // Heuristic values
    vector<int> heuristic(vertices);

    cout << "\nEnter heuristic value for each vertex:" << endl;

    for (int i = 0; i < vertices; i++) {
        cout << "Heuristic[" << i << "]: ";
        cin >> heuristic[i];
    }

    int start, goal;

    cout << "\nEnter starting vertex: ";
    cin >> start;

    cout << "Enter goal vertex: ";
    cin >> goal;

    // Perform Best-First Search
    bestFirstSearch(start, goal, graph, heuristic);

    return 0;
}
