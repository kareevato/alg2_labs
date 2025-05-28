from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as f:
        start = tuple(map(int, f.readline().strip().split(','))) 
        end = tuple(map(int, f.readline().strip().split(',')))    
        rows, cols = map(int, f.readline().strip().split(','))   
        matrix = [list(map(int, f.readline().strip().split())) for _ in range(rows)]  

    print(f"Start position: {start}")
    print(f"End position: {end}")
    print(f"Value at End position: {matrix[end[0]][end[1]]}")

    print("Matrix:")
    for row in matrix:
        print(row)

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        raise ValueError("Start position is out of bounds")

    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        raise ValueError("End position is out of bounds")

    if matrix[start[0]][start[1]] != 1:
        raise ValueError("Start position is not walkable (not 1)")
    if matrix[end[0]][end[1]] != 1:
        raise ValueError("End position is not walkable (not 1)")

    return start, end, rows, cols, matrix

def bfs(matrix, start, end, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])

    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist  

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1  

def main():
    try:
        start, end, rows, cols, matrix = read_input('input.txt')  
        distance = bfs(matrix, start, end, rows, cols)

        with open('output.txt', 'w') as f:
            f.write(str(distance))  
    except Exception as e:
        with open('output.txt', 'w') as f:
            f.write(f"Error: {e}")
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
