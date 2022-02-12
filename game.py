import tkinter as tk
import random
import threading
import time

# define fonts and colours
background = "#004E98"
foreground = "#517664"
correct_place_colour = "#89ce94"
incorrect_place_colour = "#F1D302"
incorrect_colour = "#c1292e"

# word list (to guess)
word_list = ["alert", "allow", "arena", "array", "audio", "baker", "brown", "cable", "chest", "chief",
             "grand", "hotel", "house", "joint", "human", "local", "loose", "lunch", "robin", "sleep", "smart"]


# choose a word from the list
chosen_word = random.choice(word_list)

# set up an int that will keep track of the amount of guesses a player has made
num_guesses = 0


def validate(*args):
    """Validate the entry box to see if it is longer than 1 character, or not an alpha character;
    if it is either, reset the entry to contain 1 character (or no character if invalid)."""
    if len(let_var.get()) > 1:
        let_var.set(let_var.get()[:1])
    if not let_var.get().isalpha() or let_var.get().isupper():
        let_var.set("")

    if len(let_var_1.get()) > 1:
        let_var_1.set(let_var_1.get()[:1])
    if not let_var_1.get().isalpha() or let_var_1.get().isupper():
        let_var_1.set("")

    if len(let_var_2.get()) > 1:
        let_var_2.set(let_var_2.get()[:1])
    if not let_var_2.get().isalpha() or let_var_2.get().isupper():
        let_var_2.set("")

    if len(let_var_3.get()) > 1:
        let_var_3.set(let_var_3.get()[:1])
    if not let_var_3.get().isalpha() or let_var_3.get().isupper():
        let_var_3.set("")

    if len(let_var_4.get()) > 1:
        let_var_4.set(let_var_4.get()[:1])
    if not let_var_4.get().isalpha() or let_var_4.get().isupper():
        let_var_4.set("")


def check_guess():
    """Check to see if the letters written in the entries match the selected word, changing the entry colours
    accordingly."""

    global num_guesses

    # increment num_guesses each time a guess is made
    num_guesses += 1
    num_guesses_label.config(text="Number of guesses: " + str(num_guesses))

    user_word = entry_1.get() + entry_2.get() + entry_3.get() + entry_4.get() + entry_5.get()

    if user_word == chosen_word:
        entry_1.config(bg=correct_place_colour)
        entry_2.config(bg=correct_place_colour)
        entry_3.config(bg=correct_place_colour)
        entry_4.config(bg=correct_place_colour)
        entry_5.config(bg=correct_place_colour)

        confirm_button.config(text="You won!", state=tk.DISABLED)
        reset_game_thread()

    else:
        if entry_1.get() == chosen_word[0]:
            entry_1.config(bg=correct_place_colour)
        else:
            if entry_1.get() in chosen_word and entry_1.get() != "":
                entry_1.config(bg=incorrect_place_colour)
            else:
                entry_1.config(bg=incorrect_colour)

        if entry_2.get() == chosen_word[1]:
            entry_2.config(bg=correct_place_colour)
        else:
            if entry_2.get() in chosen_word and entry_2.get() != "":
                entry_2.config(bg=incorrect_place_colour)
            else:
                entry_2.config(bg=incorrect_colour)

        if entry_3.get() == chosen_word[2]:
            entry_3.config(bg=correct_place_colour)
        else:
            if entry_3.get() in chosen_word and entry_3.get() != "":
                entry_3.config(bg=incorrect_place_colour)
            else:
                entry_3.config(bg=incorrect_colour)

        if entry_4.get() == chosen_word[3]:
            entry_4.config(bg=correct_place_colour)
        else:
            if entry_4.get() in chosen_word and entry_4.get() != "":
                entry_4.config(bg=incorrect_place_colour)
            else:
                entry_4.config(bg=incorrect_colour)

        if entry_5.get() == chosen_word[4]:
            entry_5.config(bg=correct_place_colour)
        else:
            if entry_5.get() in chosen_word and entry_5.get() != "":
                entry_5.config(bg=incorrect_place_colour)
            else:
                entry_5.config(bg=incorrect_colour)


def reset_game_thread():
    """Thread the reset_game function to allow for a delay between resets."""
    thread = threading.Thread(target=reset_game)
    thread.start()


def reset_game():
    """Reset all entries and variables and choose a new word to be guessed."""
    global num_guesses
    global chosen_word

    time.sleep(3)

    let_var.set("")
    let_var_1.set("")
    let_var_2.set("")
    let_var_3.set("")
    let_var_4.set("")

    entry_1.config(bg="white")
    entry_2.config(bg="white")
    entry_3.config(bg="white")
    entry_4.config(bg="white")
    entry_5.config(bg="white")


    num_guesses = 0
    num_guesses_label.config(text="Number of guesses: ")

    chosen_word = random.choice(word_list)

    confirm_button.config(text="Confirm Guess", state=tk.NORMAL)



# define main window
root = tk.Tk()
root.title("Wordle")
root.geometry("600x600")
root.resizable(0, 0)
root.config(bg=background)

# create title
tk.Label(root, text="WORDLE", font=("Century", 50), bg=background, fg=correct_place_colour).pack(pady=20)

# create game frame
game_frame = tk.Frame(root, bg=foreground)
game_frame.pack(pady=20)

# create confirm button
confirm_button = tk.Button(root, text="Confirm Guess", font=("Century", 25), bg=foreground, fg=correct_place_colour, command=check_guess)
confirm_button.pack(side=tk.BOTTOM, pady=5)

num_guesses_label = tk.Label(root, text="Number of guesses: ", font=("Century", 25), bg=foreground, fg=correct_place_colour)
num_guesses_label.pack(side=tk.BOTTOM)

# create a StringVar for each entry to be validated
let_var = tk.StringVar()
let_var.trace('w', validate)
let_var_1 = tk.StringVar()
let_var_1.trace('w', validate)
let_var_2 = tk.StringVar()
let_var_2.trace('w', validate)
let_var_3 = tk.StringVar()
let_var_3.trace('w', validate)
let_var_4 = tk.StringVar()
let_var_4.trace('w', validate)

# create 5 entries
entry_1 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var, justify=tk.CENTER)
entry_1.grid(row=0, column=0, padx=8, pady=5)
entry_2 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_1, justify=tk.CENTER)
entry_2.grid(row=0, column=1, padx=8, pady=5)
entry_3 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_2, justify=tk.CENTER)
entry_3.grid(row=0, column=2, padx=8, pady=5)
entry_4 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_3, justify=tk.CENTER)
entry_4.grid(row=0, column=3, padx=8, pady=5)
entry_5 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_4, justify=tk.CENTER)
entry_5.grid(row=0, column=4, padx=8, pady=5)


root.mainloop()