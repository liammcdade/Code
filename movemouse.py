import pyautogui
import time
import random
import math

# Move the mouse in random directions every 10 seconds
def move_mouse_random():
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Define the maximum distance for each movement
    max_distance = min(screen_width, screen_height) // 2

    while True:
        # Move the mouse to a random position
        pyautogui.moveTo(random.randint(0, screen_width), random.randint(0, screen_height), duration=1)

        # Move the mouse in a random direction
        angle = random.uniform(0, 2 * 3.14159)  # Generate a random angle
        distance = random.randint(10, max_distance)  # Generate a random distance

        # Calculate the new position based on the angle and distance
        new_x = pyautogui.position().x + int(distance * round(math.cos(angle)))
        new_y = pyautogui.position().y + int(distance * round(math.sin(angle)))

        # Move the mouse to the new position
        pyautogui.moveTo(new_x, new_y, duration=1)

        # Pause for 10 seconds before the next movement
        time.sleep(10)

if __name__ == "__main__":
    # Give some time to switch to the target window
    time.sleep(5)

    # Move the mouse in random directions every 10 seconds in an infinite loop
    move_mouse_random()

