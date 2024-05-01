def is_complete_graph(graph, num_vertices):
    for i in range(num_vertices):
        for j in range (num_vertices) :
            if i != j and j not in graph[i]:
                return False
    return True

def main():
    graph = {}
    num_vertices = int (input("Enter the number of vertices in the graph: "))
    
    print('\nNote: Here whole numbers are used to represent vertices\n')
    print("Enter the graph in adjacency list")
    for i in range(num_vertices):
        vertex = input(f"Enter the vertices connected to vertex {i}, separated by commas: ")
        vertices = [int(v) for v in vertex.split(", ")]
        graph[i] = vertices 

    print("\nAdjacency list representation: ")
    for vertex, neighbors in graph.items():
        print(f" {vertex}: {neighbors}")
    
    if is_complete_graph(graph, num_vertices):
        print("The graph is a complete graph.")
    else:
        print("The graph is NOT a complete graph.")

if __name__ == "__main__":
    main()