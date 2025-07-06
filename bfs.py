#implementation of bfs algorithm using python 

MAX_VERTICES = 100

# Node class
class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None #pointer points to the next node in linked list
#Graph class
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_lists = [None] * num_vertices  #each element is initially none
        self.visited = [False] * num_vertices #no nodes are visited first


    def add_edge(self, src, dest):
        # Add edge from source to destination
        new_node = Node(dest)
        new_node.next = self.adj_lists[src]
        self.adj_lists[src] = new_node

        # Add edge from destination to source
        new_node = Node(src)
        new_node.next = self.adj_lists[dest]
        self.adj_lists[dest] = new_node

# Queue class
class Queue:
    def __init__(self):
        self.items = [0] * MAX_VERTICES
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.rear == -1

    def enqueue(self, value):
        if self.rear == MAX_VERTICES - 1:
            print("Queue overflow")
            return
        if self.is_empty():
            self.front = 0
        self.rear += 1
        self.items[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return None
        item = self.items[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        return item

# BFS function
def bfs(graph, start_vertex):
    q = Queue()
    graph.visited[start_vertex] = True
    q.enqueue(start_vertex)

    while not q. is_empty():
        current_vertex = q.dequeue()
        print(current_vertex, end=" ")

        temp = graph.adj_lists[current_vertex]
        while temp:
            adj_vertex = temp.vertex
            if not graph.visited[adj_vertex]:
                graph.visited[adj_vertex] = True
                q.enqueue(adj_vertex)
            temp = temp.next

# Main execution
if __name__ == "__main__":
    g = Graph(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)

    print("BFS :")
    
    bfs(g, 0)
