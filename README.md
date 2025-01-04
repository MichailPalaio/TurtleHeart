# 🎉 TurtleHeart Program: An Interactive Multimedia Celebration! 🎨🎶

## Description

**TurtleHeart** is a dynamic multimedia Python application that combines animation, music, colorful text, and imagery to create a memorable celebratory experience.

- **Turtle Graphics**: Watch animated hearts gracefully drawn on the screen.
- **Colorful Text**: A vibrant message displayed in a dynamically sized window.
- **Image Display**: A surprise image opens in the system's default viewer.
- **Background Music**: Plays your selected song from a specified timestamp.

---

## Features

- 🖌 **Dynamic Turtle Graphics**: Draws animated hearts on a black background using Turtle Graphics.
- 🌈 **Colorful Text Display**: Shows a colorful, animated message in a window dynamically sized based on the message length.
- 🖼 **Image Viewer**: Displays a custom image using the system's default image viewer.
- 🎵 **Custom Background Music**: Plays a user-specified MP3 file starting from a given timestamp.

---

## Requirements

To run this program, you need Python installed along with the following libraries:

1. **Python 3.10 or later**
    ```bash
    sudo apt install python3
    ```
    
2. **Required Libraries**:
    - `turtle` (built-in)
    - `pygame`


3. Ensure the `mp3` and `image` files you wish to use are accessible and correctly referenced in the script.

---

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/MichailPalaio/TurtleHeart
cd TurtleHeart
```

### Step 2: Install Dependencies

Install the required Python libraries:
```bash
sudo apt install python3-pygame
```
 If `turtle` is not buit-in python, install it with:
```bash
sudo apt-get update
sudo apt-get install python3-tk
```
    
## Costumize
1. **Audio File**: Place your MP3 file in the project directory or in your desired path. Update the `mp3_file variable` in the script with its path:
```python
mp3_file = r"path/to/your/music.mp3"
```
2. **Image File**: Place your image (JPG/PNG) in the project directory or in your desired path. Update the `image_path` variable in the script:
```python
image_path = r"path/to/your/image.jpg"
```
3. **Message**: Customize the message you want to appear on screen by updating the `message` variable:
```python
message = "Sample Text"
```

---

## Running the program
Go to the same directory as the program and run it from your terminal:

```bash
python3 TurtleHeart.py
```

---
## How It Works

1. **Music Playback**: Your chosen song starts playing in the background from the specified timestamp.
2. **Turtle Graphics**: A window opens to dynamically draw animated hearts.
3. **Colorful Text**: A dynamically sized Pygame window displays your colorful message.
4. **Image Viewer**: Your custom image opens in the system’s default viewer.
5. **Independent Execution**: Each feature operates independently. The program terminates only when all windows are closed.

---
## Troubleshooting
### Common Issues and Fixes
* **Audio Playback Issues**: Ensure `pygame` is installed correctly and the MP3 file exists at the specified path.
* **Turtle Graphics Window Doesn't Appear**: Ensure the Turtle Graphics module is properly installed.
* **Pygame Window Issues**: Ensure `pygame` is installed and your system supports graphical rendering.
* **Image Viewer Issues**: Ensure the image file exists and your system’s default viewer can open the format.

### Debugging Tips
* Check the paths to your audio and image files.
* Ensure your Python version is 3.10 or later:
```bash
python3 --version
```
* Use `pip freeze` to verify that pygame is installed:

```bash
pip freeze | grep pygame
```
If you haven't installed `pip`, do so with:
   
```bash
sudo apt install python3-pip
```
* Use this command to verify that `turtle` is installed:
```bash
python3 -c "import turtle; turtle.Screen(); print('Turtle module works!')"
```

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you wish.

---

## Author
Developed with ❤️ by Michail Palaiologos.