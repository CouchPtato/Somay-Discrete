def complete_graph(graph, num_vertices):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i!=j and graph[i][j] != 1:
                return False
    return True

def main():
    graph = []
    num_vertices = int(input("Enter the number of vertices : "))
    print("Enter the adjacency matrix of the graph")
    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            cell = int(input(f"Enter the value of {i,j} :"))
            row.append(cell)
        graph.append(row)

    print('\nAdjacency matrix representation: ')
    print(f'{graph}\n')

    if(complete_graph(graph, num_vertices)):
        print('It is complete graph')
    else:
        print('It is not a complete graph')

if __name__ == "__main__":
    main()