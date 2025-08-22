class State:
  def __init__(self, x, y, grid):
    self.x = x
    self.y = y
    self.grid = grid
    self.n = len(grid)
    self.goal = (self.n - 1, self.n - 1)

  def goalTest(self):
    return (self.x, self.y) == self.goal

  def moveGen(self):
    children = []
    directions = [(-1,0),(1,0),(0,-1),(0,1),
                  (-1,-1),(-1,1),(1,-1),(1,1)]
    for dx, dy in directions:
      nx = self.x + dx
      ny = self.y + dy
      if 0 <= nx < self.n and 0 <= ny < self.n and self.grid[nx][ny] == 0:
        children.append(State(nx, ny, self.grid))
    return children

  def h(self):
    gx, gy = self.goal
    return abs(self.x - gx) + abs(self.y - gy)

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash((self.x, self.y))

  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"


class AStarSearch:
  def removeSeen(self, children, open, closed):
    new_nodes = []
    open_nodes = [node for node, parent in open]
    closed_nodes = [node for node, parent in closed]
    for child in children:
      if child not in open_nodes and child not in closed_nodes:
        new_nodes.append(child)
    return new_nodes

  def reconstructPath(self, node_pair, closed):
    path = []
    node, parent = node_pair
    parent_map = {n: p for n, p in closed}
    path.insert(0, node)
    while parent is not None:
      path.insert(0, parent)
      parent = parent_map.get(parent)
    return path

  def search(self, start):
    open = [(start, None)]
    closed = []
    g_values = {start: 0}

    while open:
      open.sort(key=lambda pair: g_values[pair[0]] + pair[0].h())
      node, parent = open.pop(0)

      if node.goalTest():
        closed.append((node, parent))
        return self.reconstructPath((node, parent), closed)

      closed.append((node, parent))
      children = node.moveGen()
      new_children = self.removeSeen(children, open, closed)
      for child in new_children:
        g_values[child] = g_values[node] + 1
        open.append((child, node))
    return None


if __name__ == "__main__":
  grid = [[0, 1, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 0, 1, 0],
          [0, 0, 0, 0, 0]]

  start = State(0, 0, grid)
  astar = AStarSearch()
  path = astar.search(start)
  if path:
    print("Path found:")
    for node in path:
      print(node)
  else:
    print("No path found")
