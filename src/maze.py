from components import Door, Key, Player, Road, Wall
from coordinate import Coordinate


class Maze:
    MIN_PLAYER_LABEL = 1
    MAX_PLAYER_LABEL = 9

    def __init__(self, maze_content: list[str]) -> None:
        self._maze_content = self._remove_empty_lines(maze_content)
        self.width = len(maze_content[0])
        self.height = len(maze_content)
        self.visited = self._create_visit_grid()
        self.player_locations = []
        self.maze_components = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]
        self._process_maze()

    def _process_maze(self) -> None:
        for row in range(0, self.height):
            row_length = len(self._maze_content[row])
            if row_length != self.width:
                raise ValueError(
                    f"line {row + 1} wrong length (was {row_length} but should be {self.width})"
                )
            for col in range(0, self.width):
                char = self._maze_content[row][col]
                if char == "#":
                    self.maze_components[row][col] = Wall()
                elif char.isalpha():
                    if char.islower():
                        self.maze_components[row][col] = Key(char)
                    else:
                        self.maze_components[row][col] = Door(char)
                elif (
                    char.isdigit()
                    and self.MIN_PLAYER_LABEL <= int(char) <= self.MAX_PLAYER_LABEL
                ):
                    self.maze_components[row][col] = Player(char)
                    self.player_locations.append(Coordinate(row, col))
                else:
                    self.maze_components[row][col] = Road()

    def is_wall(self, row: int, col: int) -> bool:
        return self._is_valid_component(row, col, Wall)

    def is_key(self, row: int, col: int) -> bool:
        return self._is_valid_component(row, col, Key)

    def is_door(self, row: int, col: int) -> bool:
        return self._is_valid_component(row, col, Door)

    def is_explored(self, row: int, col: int) -> bool:
        return self.visited[row][col]

    def set_visited(self, row: int, col: int) -> None:
        self.visited[row][col] = True

    def get_player(self, row: int, col: int) -> Player:
        player = self.maze_components[row][col]
        if isinstance(player, Player):
            return player
        raise ValueError(f"It's not a player {player}")

    def reset_visited_points(self) -> None:
        self.visited = self._create_visit_grid()

    @staticmethod
    def _remove_empty_lines(maze_content: list[str]) -> list[str]:
        return list(filter(None, maze_content))

    def _create_visit_grid(self) -> list[bool]:
        return [[False for _ in range(self.width)] for _ in range(self.height)]

    def is_valid_location(self, row: int, col: int) -> bool:
        return (
            False
            if row < 0 or row >= self.height or col < 0 or col >= self.width
            else True
        )

    def _is_valid_component(self, row: int, col: int, component: object) -> bool:
        return isinstance(self.maze_components[row][col], component)
