import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


class Choice:

    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry("400x400")
        self.win.title("Snake game")
        self.win.configure(bg="#FFE4C4")

        self.load_image()

        self.one_player_button = tk.Button(self.win, text="One player", font=('Arial', 18), command=self.one_player)
        self.one_player_button.place(x=125, y=120)
        self.is_one_player = False

        self.two_players_button = tk.Button(self.win, text="Two players", font=('Arial', 18), command=self.two_players)
        self.two_players_button.place(x=120, y=185)
        self.is_two_players = False

        self.scoreboard_button = tk.Button(self.win, text="Scoreboard", font=('Arial', 18), command=self.scoreboard_list)
        self.scoreboard_button.place(x=121, y=245)
        self.is_scoreboard = False

        self.win.mainloop()

    def one_player(self):
        self.is_one_player = True
        self.win.destroy()

    def two_players(self):
        self.is_two_players = True
        self.win.destroy()

    def scoreboard_list(self):
        self.is_scoreboard = True
        self.win.destroy()

    @staticmethod
    def load_image():
        image = Image.open("snake_image.jpg")
        resized_image = image.resize((400, 80), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(resized_image)
        label = tk.Label(image=im)
        label.image = im
        label.place(x=0, y=0)

