import tkinter as tk

# define fonts and colours
background = "#004E98"
foreground = "#517664"
correct_place_colour = "#89ce94"
incorrect_place_colour = "#F1D302"
incorrect_colour = "#c1292e"


def validate(*args):
    """Validate the entry box to see if it is longer than 1 character, or not an alpha character;
    if it is either, reset the entry to contain 1 character (or no character if invalid)."""
    if len(let_var.get()) > 1:
        let_var.set(let_var.get()[:1])
    if not let_var.get().isalpha():
        let_var.set("")

    if len(let_var_1.get()) > 1:
        let_var_1.set(let_var_1.get()[:1])
    if not let_var_1.get().isalpha():
        let_var_1.set("")

    if len(let_var_2.get()) > 1:
        let_var_2.set(let_var_2.get()[:1])
    if not let_var_2.get().isalpha():
        let_var_2.set("")

    if len(let_var_3.get()) > 1:
        let_var_3.set(let_var_3.get()[:1])
    if not let_var_3.get().isalpha():
        let_var_3.set("")

    if len(let_var_4.get()) > 1:
        let_var_4.set(let_var_4.get()[:1])
    if not let_var_4.get().isalpha():
        let_var_4.set("")

    if len(let_var_5.get()) > 1:
        let_var_5.set(let_var_5.get()[:1])
    if not let_var.get().isalpha():
        let_var_5.set("")

    if len(let_var_6.get()) > 1:
        let_var_6.set(let_var_6.get()[:1])
    if not let_var_1.get().isalpha():
        let_var_6.set("")

    if len(let_var_7.get()) > 1:
        let_var_7.set(let_var_7.get()[:1])
    if not let_var_2.get().isalpha():
        let_var_7.set("")

    if len(let_var_8.get()) > 1:
        let_var_8.set(let_var_8.get()[:1])
    if not let_var_8.get().isalpha():
        let_var_8.set("")

    if len(let_var_9.get()) > 1:
        let_var_9.set(let_var_9.get()[:1])
    if not let_var_9.get().isalpha():
        let_var_9.set("")

    if len(let_var_10.get()) > 1:
        let_var_10.set(let_var_10.get()[:1])
    if not let_var_10.get().isalpha():
        let_var_10.set("")

    if len(let_var_11.get()) > 1:
        let_var_11.set(let_var_11.get()[:1])
    if not let_var_11.get().isalpha():
        let_var_11.set("")

    if len(let_var_12.get()) > 1:
        let_var_12.set(let_var_12.get()[:1])
    if not let_var.get().isalpha():
        let_var_12.set("")

    if len(let_var_13.get()) > 1:
        let_var_13.set(let_var_13.get()[:1])
    if not let_var_13.get().isalpha():
        let_var_13.set("")

    if len(let_var_14.get()) > 1:
        let_var_14.set(let_var_14.get()[:1])
    if not let_var_14.get().isalpha():
        let_var_14.set("")

    if len(let_var_15.get()) > 1:
        let_var_15.set(let_var_15.get()[:1])
    if not let_var_15.get().isalpha():
        let_var_15.set("")

    if len(let_var_16.get()) > 1:
        let_var_16.set(let_var_16.get()[:1])
    if not let_var_16.get().isalpha():
        let_var_16.set("")

    if len(let_var_17.get()) > 1:
        let_var_17.set(let_var_17.get()[:1])
    if not let_var_17.get().isalpha():
        let_var_17.set("")

    if len(let_var_18.get()) > 1:
        let_var_18.set(let_var_18.get()[:1])
    if not let_var_18.get().isalpha():
        let_var_18.set("")

    if len(let_var_19.get()) > 1:
        let_var_19.set(let_var_19.get()[:1])
    if not let_var_19.get().isalpha():
        let_var_19.set("")

    if len(let_var_20.get()) > 1:
        let_var_20.set(let_var_20.get()[:1])
    if not let_var_20.get().isalpha():
        let_var_20.set("")

    if len(let_var_21.get()) > 1:
        let_var_21.set(let_var_21.get()[:1])
    if not let_var_21.get().isalpha():
        let_var_21.set("")


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

let_var_5 = tk.StringVar()
let_var_5.trace('w', validate)
let_var_6 = tk.StringVar()
let_var_6.trace('w', validate)
let_var_7 = tk.StringVar()
let_var_7.trace('w', validate)
let_var_8 = tk.StringVar()
let_var_8.trace('w', validate)
let_var_9 = tk.StringVar()
let_var_9.trace('w', validate)

let_var_10 = tk.StringVar()
let_var_10.trace('w', validate)
let_var_11 = tk.StringVar()
let_var_11.trace('w', validate)
let_var_12 = tk.StringVar()
let_var_12.trace('w', validate)
let_var_13 = tk.StringVar()
let_var_13.trace('w', validate)
let_var_14 = tk.StringVar()
let_var_14.trace('w', validate)

let_var_15 = tk.StringVar()
let_var_15.trace('w', validate)
let_var_16 = tk.StringVar()
let_var_16.trace('w', validate)
let_var_17 = tk.StringVar()
let_var_17.trace('w', validate)
let_var_18 = tk.StringVar()
let_var_18.trace('w', validate)
let_var_19 = tk.StringVar()
let_var_19.trace('w', validate)

let_var_20 = tk.StringVar()
let_var_20.trace('w', validate)
let_var_21 = tk.StringVar()
let_var_21.trace('w', validate)
let_var_22 = tk.StringVar()
let_var_22.trace('w', validate)
let_var_23 = tk.StringVar()
let_var_23.trace('w', validate)
let_var_24 = tk.StringVar()
let_var_24.trace('w', validate)

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

# create next row
entry_1 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_5, justify=tk.CENTER)
entry_1.grid(row=1, column=0, padx=8, pady=5)
entry_2 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_6, justify=tk.CENTER)
entry_2.grid(row=1, column=1, padx=8, pady=5)
entry_3 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_7, justify=tk.CENTER)
entry_3.grid(row=1, column=2, padx=8, pady=5)
entry_4 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_8, justify=tk.CENTER)
entry_4.grid(row=1, column=3, padx=8, pady=5)
entry_5 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_9, justify=tk.CENTER)
entry_5.grid(row=1, column=4, padx=8, pady=5)

# create next row
entry_1 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_10, justify=tk.CENTER)
entry_1.grid(row=2, column=0, padx=8, pady=5)
entry_2 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_11, justify=tk.CENTER)
entry_2.grid(row=2, column=1, padx=8, pady=5)
entry_3 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_12, justify=tk.CENTER)
entry_3.grid(row=2, column=2, padx=8, pady=5)
entry_4 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_13, justify=tk.CENTER)
entry_4.grid(row=2, column=3, padx=8, pady=5)
entry_5 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_14, justify=tk.CENTER)
entry_5.grid(row=2, column=4, padx=8, pady=5)

# create next row
entry_1 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_15, justify=tk.CENTER)
entry_1.grid(row=3, column=0, padx=8, pady=5)
entry_2 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_16, justify=tk.CENTER)
entry_2.grid(row=3, column=1, padx=8, pady=5)
entry_3 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_17, justify=tk.CENTER)
entry_3.grid(row=3, column=2, padx=8, pady=5)
entry_4 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_18, justify=tk.CENTER)
entry_4.grid(row=3, column=3, padx=8, pady=5)
entry_5 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_19, justify=tk.CENTER)
entry_5.grid(row=3, column=4, padx=8, pady=5)

# create next row
entry_1 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_20, justify=tk.CENTER)
entry_1.grid(row=4, column=0, padx=8, pady=5)
entry_2 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_21, justify=tk.CENTER)
entry_2.grid(row=4, column=1, padx=8, pady=5)
entry_3 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_22, justify=tk.CENTER)
entry_3.grid(row=4, column=2, padx=8, pady=5)
entry_4 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_23, justify=tk.CENTER)
entry_4.grid(row=4, column=3, padx=8, pady=5)
entry_5 = tk.Entry(game_frame, font=("Century", 40), width=2, textvariable=let_var_24, justify=tk.CENTER)
entry_5.grid(row=4, column=4, padx=8, pady=5)










root.mainloop()