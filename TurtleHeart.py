import turtle
import math
import pygame
import sys
import random
import time
from threading import Thread
import subprocess

# Global message for the Pygame display (Change with your desired message)
message = "Sample Text"

# Paths to the audio and image files (change with your desired song and image)
mp3_file = r"Die With A Smile - Bruno Mars, Lady Gaga.mp3"
image_path = r"duckface.jpg"

# Starting timestamp for the audio file (change according to your song)
start_time = 116.2

# Suppress all unhandled exceptions globally
sys.excepthook = lambda *args: None

# Global flag to track if the image viewer is open
image_open = False

# Function to calculate heart coordinates using parametric equations
def heart(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

# Function to play music starting from a specific time
def play_music(start_time):
    try:
        pygame.mixer.init()  # Initialize the mixer
        pygame.mixer.music.load(mp3_file)  # Load the MP3 file
        pygame.mixer.music.play(start=start_time)  # Play from the given start time
        while pygame.mixer.music.get_busy():  # Keep the thread alive while music is playing
            time.sleep(1)
    except Exception:
        pass  # Suppress errors to ensure smooth program execution

# Function to draw hearts using Turtle Graphics
def turtle_heart():
    try:
        t = turtle.Turtle()
        t.speed(0)  # Set the fastest drawing speed
        t.color("red")  # Set the turtle color to red
        turtle.bgcolor("black")  # Set the background color to black
        t.penup()

        for i in range(15):  # Draw 15 progressively larger hearts
            t.goto(0, 0)  # Start from the center
            t.pendown()
            for n in range(0, 100, 2):  # Parametric loop for heart shape
                x, y = heart(n / 10)
                t.goto(x * i, y * i)  # Scale and plot the heart coordinates
            t.penup()
        t.hideturtle()  # Hide the turtle after drawing
        turtle.done()  # Keep the Turtle Graphics window open
    except Exception:
        pass  # Suppress errors

# Function to display colorful text in a Pygame window
def pygame_display():
    try:
        pygame.init()  # Initialize Pygame

        # Font and spacing settings
        font = pygame.font.Font(None, 100)  # Default font with size 100
        letter_spacing = 8  # Spacing between letters

        # Calculate total width of the message with spacing
        total_width = sum(
            font.size(letter)[0] + letter_spacing for letter in message
        ) - letter_spacing  # Remove the extra spacing at the end

        # Set window dimensions dynamically based on message length
        window_width = max(total_width + 400, 400)  # Add padding, with a minimum width of 400
        window_height = window_width / 2  # Set height proportional to the width
        screen = pygame.display.set_mode((int(window_width), int(window_height)))
        pygame.display.set_caption("Happy Birthday!")

        # Function to generate random colors
        def random_color():
            return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Function to render the colorful message centered in the window
        def draw_colorful_message(surface, message, font, center_x, center_y):
            x = center_x - total_width // 2  # Start rendering from the horizontal center
            for letter in message:
                color = random_color()  # Generate a random color for each letter
                text_surface = font.render(letter, True, color)
                surface.blit(text_surface, (x, center_y - font.get_height() // 2))  # Center vertically
                x += text_surface.get_width() + letter_spacing  # Adjust position for the next letter

        while True:
            for event in pygame.event.get():  # Event handling
                if event.type == pygame.QUIT:  # Close the window
                    pygame.quit()
                    return

            screen.fill((0, 0, 0))  # Clear the screen with black
            draw_colorful_message(screen, message, font, window_width // 2, window_height // 2)
            pygame.display.flip()  # Update the display
    except Exception:
        pass  # Suppress errors

# Function to display the image using the default system viewer
def show_image():
    global image_open
    try:
        image_open = True
        subprocess.Popen(["start", image_path], shell=True)  # Open the image with the default viewer
        while image_open:  # Keep the thread alive while the image viewer is open
            time.sleep(1)
    except Exception:
        pass  # Suppress errors

# Main program flow
def main():
    global image_open
    try:
        # Start the music playback thread
        music_thread = Thread(target=play_music, args=(start_time,), daemon=True)
        music_thread.start()

        # Start the Turtle Graphics thread
        turtle_thread = Thread(target=turtle_heart, daemon=True)
        turtle_thread.start()

        # Wait for the Turtle Graphics to complete
        time.sleep(15)

        # Start the Pygame display thread
        pygame_thread = Thread(target=pygame_display, daemon=True)
        pygame_thread.start()

        # Wait for a few seconds before showing the image
        time.sleep(3)

        # Start the image viewer thread
        image_thread = Thread(target=show_image, daemon=True)
        image_thread.start()

        # Monitor the music thread and keep the program alive until all windows are closed
        while music_thread.is_alive():
            time.sleep(1)
    except Exception:
        pass  # Suppress errors
    print("All windows closed. Program exiting.")

# Entry point of the program
if __name__ == "__main__":
    try:
        main()  # Run the main program
    except KeyboardInterrupt:  # Handle Ctrl+C gracefully
        pygame.quit()
        image_open = False
        sys.exit(0)
