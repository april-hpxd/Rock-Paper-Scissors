import tkinter as tk
import random
import pygame

pygame.mixer.init()

def play_sound(file):
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    except Exception as e:
        print("Error playing sound:", e)


# --- Game setup ---
choices = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0
WIN_SCORE = 3

# --- Game logic ---
def play(player_choice):
    global player_score, computer_score

    if player_score >= WIN_SCORE or computer_score >= WIN_SCORE:
        return  # game already finished

    computer_choice = random.choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win this round!"
        player_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1

    result_label.config(text=f"Computer chose {computer_choice}\n{result}")
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}")

    check_winner()

def check_winner():
    global player_score, computer_score
    if player_score == WIN_SCORE:
        play_sound("win_sound.wav") 
        result_label.config(text=random.choice([
            "🏆 You’re unstoppable!",
            "🎉 You crushed the machine!",
            "🌟 Legendary victory, human!"
        ]))
        end_game()
    elif computer_score == WIN_SCORE:
        play_sound("lose_sound.wav") 
        result_label.config(text=random.choice([
            "💀 Computer reigns supreme 😈",
            "🤖 Bow down to your AI overlord!",
            "☠️ You fought bravely... but lost."
        ]))
        end_game()


def end_game():
    for widget in button_frame.winfo_children():
        widget.config(state="disabled")
    reset_btn.config(text="Play Again")

def reset_game():
    global player_score, computer_score
    player_score = computer_score = 0
    score_label.config(text="Player: 0 | Computer: 0")
    result_label.config(text="Make your move!")
    for widget in button_frame.winfo_children():
        widget.config(state="normal")
    reset_btn.config(text="Reset")

# --- UI setup ---
root = tk.Tk()
root.title("Rock Paper Scissors ✊📄✂️")
root.geometry("420x450")
root.config(bg="#1b1b2f")

# 🎨 You can change this to your favorite aesthetic font
base_font = ("Comic Sans MS", 13, "bold")  # try "Poppins", "Nunito", or "Verdana"

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Comic Sans MS", 22, "bold"), bg="#1b1b2f", fg="#e43f5a")
title_label.pack(pady=20)

result_label = tk.Label(root, text="Make your move!", font=(base_font[0], 14), bg="#1b1b2f", fg="#ffd369")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Player: 0 | Computer: 0", font=base_font, bg="#1b1b2f", fg="#00adb5")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#1b1b2f")
button_frame.pack(pady=20)

buttons = [
    ("Rock 🪨", "Rock"),
    ("Paper 📄", "Paper"),
    ("Scissors ✂️", "Scissors")
]

for text, choice in buttons:
    tk.Button(
        button_frame,
        text=text,
        width=12,
        height=2,
        bg="#393e46",
        fg="#eeeeee",
        font=base_font,
        command=lambda c=choice: play(c)
    ).pack(side=tk.LEFT, padx=10)

reset_btn = tk.Button(root, text="Reset", command=reset_game, bg="#00adb5", fg="#eeeeee", font=base_font)
reset_btn.pack(pady=25)

root.mainloop()
