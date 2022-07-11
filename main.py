import os
import sys

from dfs import DFS
from maze import Maze

sys.setrecursionlimit(10000)

MAP = "map7.txt"


def main() -> None:
    with open(f"./maps/{MAP}") as file:
        maze = Maze(file.read().splitlines())

        print(
            f"===  Traveling through {os.path.basename(file.name)} ({maze.width}x{maze.height}) ==="
        )
        print("-----------------------------------------------\n")
        dfs = DFS(maze)
        dfs.solve()


if __name__ == "__main__":
    main()
