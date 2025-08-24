# Goal
# Represent the maze using a 2D list (# = Wall, ' ' = Path, P = Player, E = Exit)
# Move the player using W/A/S/D keys
# End the game when the player reaches the exit


print("🌀 Maze Escape Game (Move with WASD)")

# Maze map
maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "P", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", "E", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

# Player start position
player_x, player_y = 1, 1

def print_maze():
    for row in maze:
        print("".join(row))

while True:
    print_maze()
    move = input("Move (WASD): ").upper()

    dx, dy = 0, 0
    if move == "W": dx, dy = -1, 0
    elif move == "S": dx, dy = 1, 0
    elif move == "A": dx, dy = 0, -1
    elif move == "D": dx, dy = 0, 1
    else:
        print("⚠ Invalid input")
        continue

    nx, ny = player_x + dx, player_y + dy

    if maze[nx][ny] == "#":
        print("🚫 You hit a wall!")
        continue
    elif maze[nx][ny] == "E":
        print("🎉 You found the exit! Escape successful!")
        break

    # Update player position
    maze[player_x][player_y] = " "
    maze[nx][ny] = "P"
    player_x, player_y = nx, ny
