# mazeDFS

This dead-end maze version was developed thorugh a college project and it's only objective is to tell the maximum path a player can take, taking into account the keys and doors he can find on the way.

Players don't move diagonally, but can walk around the map finding different things:

``#``   -> It's a rock where one cannot pass;

``.``   -> Represents the free space to walk;

``a-z`` -> Are keys that can be collected by the player and don't block the way;

``A-Z`` -> Are closed doors and can only be opened if the player has the proper key;

``1-9`` -> Are starting points for players.