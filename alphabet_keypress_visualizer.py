import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Message will play once the play button is initiated
def start_game():
    messagebox.showinfo("Start", "Starting the game...")

    # Activate key bindings only in game
    root.bind("<Key>", handle_key_press)

    # Hide main menu elements
    bg_label.place_forget()
    title_label.place_forget()
    bottom_text_label.place_forget()
    play_btn.place_forget()
    quit_btn.place_forget()

    # Show game screen
    game_frame.place(x=0, y=0, relwidth=1, relheight=1)


def quit_game():
    root.destroy()


# Handles key presses during the game
def handle_key_press(event):
    letter = event.char.lower()

    # Ignore non-letter keys
    if not letter.isalpha() or len(letter) != 1:
        return

    try:
        img_path = f"assets/letters/{letter}.png"
        img_raw = Image.open(img_path)
        img_raw = img_raw.resize((500, 500), Image.LANCZOS)
        img = ImageTk.PhotoImage(img_raw)

        # Remove previous image
        if hasattr(root, "image_label"):
            root.image_label.destroy()

        # Display new image inside game_frame
        root.image_label = tk.Label(game_frame, image=img, bg="white")
        root.image_label.image = img
        root.image_label.place(x=290, y=100)

    except Exception as e:
        print(f"No image found for key '{letter}':", e)


# Create the main window
root = tk.Tk()
root.title("Game Menu :3")
root.geometry("1080x720")
root.resizable(False, False)


# Main menu background image
bg_image = Image.open("assets/TheRock.png")
bg_image = bg_image.resize((1080, 720), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
root.bg_photo = bg_photo

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# Main menu title text
title_label = tk.Label(root, text="ARE WE COOKING", font=("Courier", 48, "bold"), fg="white")
title_label.place(relx=0.5, y=40, anchor="center")


# Bottom text
bottom_text_label = tk.Label(root, text="CAUSE THE ROCK IS COOKING", font=("Courier", 32, "bold"), fg="white")
bottom_text_label.place(relx=0.5, y=650, anchor="center")


# Play button image
play_img_raw = Image.open("assets/startButton.png")
play_img_raw = play_img_raw.resize((500, 50), Image.LANCZOS)
play_img = ImageTk.PhotoImage(play_img_raw)

# Quit button image
quit_img_raw = Image.open("assets/exit.png")
quit_img_raw = quit_img_raw.resize((500, 50), Image.LANCZOS)
quit_img = ImageTk.PhotoImage(quit_img_raw)


# Play button
play_btn = tk.Button(root, image=play_img, command=start_game, borderwidth=0, highlightthickness=0)
play_btn.place(x=290, y=200)

# Quit button
quit_btn = tk.Button(root, image=quit_img, command=quit_game, borderwidth=0, highlightthickness=0)
quit_btn.place(x=290, y=350)


#
# GAME SCREEN (Initially hidden)
#
game_frame = tk.Frame(root, width=1080, height=720)
game_frame.place_forget()


# Game background image
try:
    game_bg_image = Image.open("assets/finalProjectBackround1111.png")
    game_bg_image = game_bg_image.resize((1080, 720), Image.LANCZOS)
    game_bg_photo = ImageTk.PhotoImage(game_bg_image)
    root.game_bg_photo = game_bg_photo

    game_bg_label = tk.Label(game_frame, image=game_bg_photo)
    game_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

except Exception as e:
    print("Failed to load game background:", e)


# Run the window
root.mainloop()