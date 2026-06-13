"""
Create an anagram game!
"""
import random
import tkinter as tk

# TODO Use this dictionary of anagrams to create an anagrams GUI word game.
#  Look at 'anagrams_game_example.png' in this folder for an example.
word_anagrams = {
    "action": ["cation"],
    "agree": ["eager"],
    "calm": ["clam"],
    "charming": ["marching"],
    "clean": ["lance"],
    "cool": ["loco"],
    "creative": ["reactive"],
    "delight": ["lighted"],
    "earnest": ["eastern", "nearest"],
    "easy": ["ayes", "yeas"],
    "free": ["reef"],
    "great": ["grate"],
    "green": ["genre"],
    "grin": ["ring"],
    "hearty": ["earthy"],
    "idea": ["aide"],
    "ideal": ["ailed"],
    "keen": ["knee"],
    "lively": ["evilly", "vilely"],
    "lovely": ["volley"],
    "merit": ["miter", "remit", "timer"],
    "open": ["nope", "peon", "pone"],
    "prepared": ["dapperer"],
    "quiet": ["quite"],
    "refined": ["definer"],
    "restored": ["resorted", "rostered"],
    "reward": ["drawer", "redraw", "warder", "warred"],
    "rewarding": ["redrawing", "wardering"],
    "right": ["girth"],
    "secure": ["rescue"],
    "simple": ["impels"],
    "smile": ["limes", "miles", "slime"],
    "super": ["puers", "purse"],
    "tops": ["opts", "post", "pots", "spot", "stop"],
    "unreal": ["neural"],
    "wonderful": ["underflow"],
    "zeal": ["laze"]}

def new_word():
    global current_word

    current_word = random.choice(list(word_anagrams.keys()))

    # Use one of the anagrams as the scrambled word
    scrambled = random.choice(word_anagrams[current_word])

    word_label.config(text=scrambled)
    guess_entry.delete(0, tk.END)
    result_label.config(text="")


def check_guess():
    print("shrek")
    guess = guess_entry.get().lower().strip()

    if guess == current_word:
        result_label.config(text="u actually got something right", fg="green")
    else:
        result_label.config(text=f"incorrect, u stupid monkey, the answer was '{current_word}'",fg="red")



root = tk.Tk()
root.title("anagrams")
root.geometry("350x350")

title_label = tk.Label(root, text="anagrams", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 14))
guess_entry.pack(pady=5)

check_button = tk.Button(root, text="check guess", command=check_guess)
check_button.pack(pady=5)

next_button = tk.Button(root, text="new word", command=new_word)
next_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

new_word()

root.mainloop()
