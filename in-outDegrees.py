def compute_degrees(graph, num_vertices) :
    in_degrees = [0] * num_vertices
    out_degrees = [0] * num_vertices

    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                out_degrees[i] += 1
                in_degrees[j] += 1

    return in_degrees, out_degrees

def main():
    graph = []
    num_vertices = int(input("Enter the no. of vertices present in graph: "))
    
    print()

    for i in range(num_vertices):
        rows = []
        for j in range(num_vertices):
            cell = int (input(f"Enter the value of {i, j}: "))
            rows.append (cell)
        graph.append (rows)

    in_degrees, out_degrees = compute_degrees(graph, num_vertices)
    print()
    print("Vertex\tIn-Degree\tout-Degree")
    for i in range(len (graph) ):
        print (f" {i}\t{in_degrees [i]} \t\t{out_degrees [i] } ")

if __name__ == "__main__":
    main()