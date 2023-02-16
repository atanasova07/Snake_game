from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.all_scores = []
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.write_in_file()
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FONT)

    def write_in_file(self):
        with open('scores.txt', 'r+') as file:
            data = file.read()
            file.seek(0, 0)
            file.write(str(self.score) + '\n' + data)
        file.close()

    def read_from_file(self):
        file = open("scores.txt", 'r')
        count = 0
        for line in file:
            self.all_scores.append(line)
            count += 1
            if count == 10:
                break
        file.close()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def decrease_score(self):
        self.score -= 1
        self.clear()
        self.update_scoreboard()
