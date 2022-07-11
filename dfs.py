from components import Door
from maze import Maze
from coordinate import Coordinate


class DFS:
    DIRECTIONS = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]

    def __init__(self, maze: Maze) -> None:
        self.maze = maze
        self.current_player = None
        self.inventory = []
        self.path = []

    def _reset_inventory(self) -> None:
        self.inventory = []
        self.path = []

    def _open_door(self, door: Door) -> bool:
        return any(key.label.upper() == door.label for key in self.inventory)

    def solve(self) -> None:
        for player_location in self.maze.player_locations:
            x = player_location.x
            y = player_location.y
            self.current_player = self.maze.get_player(x, y)

            self._reset_inventory()
            self.maze.reset_visited_points()
            print(f"=> ({x}, {y}) Current player: {self.current_player.label}\n")

            self._explore(x, y)
            print(f"\n[x] Path traveled: {len(self.path)}")
            print("--------------------------------\n")

    def _explore(self, row: int, col: int) -> bool:
        if (
            not self.maze.is_valid_location(row, col)
            or self.maze.is_wall(row, col)
            or self.maze.is_explored(row, col)
        ):
            return False

        coordinate = Coordinate(row, col)
        self.path.append(coordinate)
        self.maze.set_visited(row, col)

        if self.maze.is_key(row, col):
            key = self.maze.maze_components[row][col]
            self.inventory.append(key)
            print(f"({row}, {col}) [*] Key [{key.label}] found!")

        if self.maze.is_door(row, col):
            door = self.maze.maze_components[row][col]
            if not self._open_door(door):
                return False
            print(f"({row}, {col}) [-] Opening door: {door.label}")

        for direction in self.DIRECTIONS:
            next_coordinate = Coordinate(row + direction[0], col + direction[1])
            if self._explore(next_coordinate.x, next_coordinate.y):
                return True
        return False
