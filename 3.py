from collections import deque

def findPath(maze):
    n = len(maze)
    q = deque([(0, 0, "")])
    visited = set()
    while q:
        x, y, path = q.popleft()
        if x == n - 1 and y == n - 1:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if x > 0 and maze[x - 1][y] == 1:
            q.append((x - 1, y, path + "U"))
        if x < n - 1 and maze[x + 1][y] == 1:
            q.append((x + 1, y, path + "D"))
        if y > 0 and maze[x][y - 1] == 1:
            q.append((x, y - 1, path + "L"))
        if y < n - 1 and maze[x][y + 1] == 1:
            q.append((x, y + 1, path + "R"))
    return -1

maze = [
  [1, 0, 0, 0],
  [1, 1, 0, 1],
  [0, 1, 0, 0],
  [1, 1, 1, 1],
]

path = findPath(maze)

print(path) # "RRDD"
