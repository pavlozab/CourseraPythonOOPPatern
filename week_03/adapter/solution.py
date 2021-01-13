class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        lights, obstacles = [], []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    lights.append((j, i))
                if grid[i][j] == -1:
                    obstacles.append((j, i))

        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)

        return self.adaptee.generate_lights()