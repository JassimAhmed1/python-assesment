import os
import random
import time

# Game settings
ROAD_WIDTH = 3
ROAD_HEIGHT = 12
PLAYER_ICON = "🏎️"
OBSTACLE_ICON = "💥"
EMPTY_ICON = "  "

def clear_screen():
    # Clears the terminal screen for smooth rendering
    os.system("cls" if os.name == "nt" else "clear")

def print_road(player_pos, obstacles, score, speed):
    clear_screen()
    print("=" * 16)
    print(f" SPEED: {speed} KM/H | SCORE: {score}")
    print("=" * 16)
    
    # Draw the road from top to bottom
    for r in range(ROAD_HEIGHT):
        row_str = "|"
        for c in range(ROAD_WIDTH):
            if [r, c] in obstacles:
                row_str += OBSTACLE_ICON
            elif r == ROAD_HEIGHT - 1 and c == player_pos:
                row_str += PLAYER_ICON
            else:
                row_str += EMPTY_ICON
            row_str += "|"
        print(row_str)
    print("=" * 16)
    print("Controls: [A] Left  [D] Right  [W] Straight -> Press Enter")

def main():
    player_pos = 1  # Start in the middle lane (0=Left, 1=Middle, 2=Right)
    obstacles = []  # List holding coordinates [row, col] of obstacles
    score = 0
    speed = 100
    spawn_timer = 0

    while True:
        print_road(player_pos, obstacles, score, speed)
        
        # Player Input
        move = input("Your move: ").lower().strip()
        if move == "a" and player_pos > 0:
            player_pos -= 1
        elif move == "d" and player_pos < ROAD_WIDTH - 1:
            player_pos += 1
        
        # Move obstacles down by one step
        for obs in obstacles:
            obs[0] += 1
            
        # Filter out obstacles that left the screen and increase score
        old_count = len(obstacles)
        obstacles = [obs for obs in obstacles if obs[0] < ROAD_HEIGHT]
        score += (old_count - len(obstacles)) * 10
        
        # Check if a crash occurred (obstacle is in player's grid position)
        if any(obs[0] == ROAD_HEIGHT - 1 and obs[1] == player_pos for obs in obstacles):
            print_road(player_pos, obstacles, score, speed)
            print("\n💥 CRASH! Game Over! 💥")
            print(f"Final Score: {score}")
            break
            
        # Spawn new obstacles dynamically
        spawn_timer += 1
        if spawn_timer % 2 == 0:  # Spawn every 2 turns
            spawn_lane = random.randint(0, ROAD_WIDTH - 1)
            obstacles.append([0, spawn_lane])
            
        # Scale speed slightly as score increases
        speed = 100 + (score // 20) * 10

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame exited. Thanks for playing!")
