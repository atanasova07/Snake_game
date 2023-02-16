import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from choices import Choice
import tkinter as tk
import time

STARTING_POSITIONS1 = [(40, -10), (20, -10), (0, -10)]
STARTING_POSITIONS2 = [(-50, 40), (-70, 40), (-90, 40)]

choice = Choice()
timer = 0

obstacle_first = []
obstacle_second = []
obstacle_third = []


def one_obstacle(position_x, position_y):
    obs = turtle.Turtle()
    obs.shape("square")
    obs.color("#00BFFF")
    obs.penup()
    obs.goto(position_x, position_y)
    if len(obstacle_first) != 4:
        obstacle_first.append(obs)
    elif len(obstacle_second) != 3:
        obstacle_second.append(obs)
    else:
        obstacle_third.append(obs)


def obstacles(position_x, position_y, size):
    for _ in range(0, size):
        one_obstacle(position_x, position_y)
        position_y += 20


if choice.is_one_player or choice.is_two_players:
    one_pl = choice.is_one_player
    two_pl = choice.is_two_players

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    obstacles(50, -290, 4)
    obstacles(-200, 100, 3)
    obstacles(150, 180, 1)

    if two_pl:
        snake2 = Snake(STARTING_POSITIONS2)
        screen.listen()
        screen.onkey(snake2.w, "w")
        screen.onkey(snake2.s, "s")
        screen.onkey(snake2.a, "a")
        screen.onkey(snake2.d, "d")

        scoreboard2 = Scoreboard(-120, 265)
        scoreboard2.color(snake2.color_head)

        snake = Snake(STARTING_POSITIONS1)
        scoreboard = Scoreboard(100, 265)
        scoreboard.color(snake.color_head)

    elif one_pl:
        snake = Snake(STARTING_POSITIONS1)
        scoreboard = Scoreboard(0, 265)
        scoreboard.color(snake.color_head)

    food = Food()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        for el in obstacle_first:
            if two_pl:
                if snake.head.distance(el) < 15 or snake2.head.distance(el) < 15:
                    game_is_on = False
                    scoreboard.game_over()
                if food.distance(el) < 2:
                    food.refresh()
            else:
                if snake.head.distance(el) < 15:
                    game_is_on = False
                    scoreboard.game_over()
                if food.distance(el) < 2:
                    food.refresh()

        for el in obstacle_second:
            if two_pl:
                if snake.head.distance(el) < 15 or snake2.head.distance(el) < 15:
                    game_is_on = False
                    scoreboard.game_over()
                if food.distance(el) < 2:
                    food.refresh()
            else:
                if snake.head.distance(el) < 15:
                    game_is_on = False
                    scoreboard.game_over()
                if food.distance(el) < 2:
                    food.refresh()

        for el in obstacle_third:
            if two_pl:
                if snake.head.distance(el) < 15 or snake2.head.distance(el) < 15:
                    game_is_on = False
                    scoreboard.game_over()
                if food.distance(el) < 2:
                    food.refresh()
            else:
                if snake.head.distance(el) < 15:
                    game_is_on = False
                    scoreboard.game_over()
                if food.distance(el) < 2:
                    food.refresh()

        if food.shape() == "turtle":
            timer += 1
            if timer == 30:
                food.refresh()
                timer = 0

        if food.shape() == "triangle":
            timer += 1
            if timer == 70:
                food.refresh()
                timer = 0

        if food.shape() == "square":
            timer += 1
            if timer == 20:
                food.refresh()
                timer = 0

        if two_pl:
            snake2.move()

        if snake.head.distance(food) < 15:
            if food.shape() == "turtle":
                for _ in range(0, 3):
                    snake.extend()
                    scoreboard.increase_score()
            elif food.shape() == "circle":
                snake.extend()
                scoreboard.increase_score()
            elif food.shape() == "triangle":
                if len(snake.segments) >= 4:
                    snake.remove()
                    snake.remove()
                else:
                    game_is_on = False
                    scoreboard.game_over()
            else:
                snake.has_lives = True

            food.refresh()
            timer = 0

        if two_pl and snake2.head.distance(food) < 15:
            if food.shape() == "turtle":
                for _ in range(0, 3):
                    snake2.extend()
                    scoreboard2.increase_score()
            elif food.shape() == "circle":
                snake2.extend()
                scoreboard2.increase_score()
            elif food.shape() == "triangle":
                if len(snake2.segments) >= 3:
                    snake2.remove()
                    snake2.remove()
                else:
                    game_is_on = False
                    scoreboard2.game_over()
            else:
                snake2.has_lives = True

            food.refresh()
            timer = 0

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                if not snake.has_lives:
                    game_is_on = False
                    scoreboard.game_over()
                else:
                    snake.has_lives = False

        if two_pl:
            for segment in snake2.segments[1:]:
                if snake2.head.distance(segment) < 10:
                    if not snake2.has_lives:
                        game_is_on = False
                        scoreboard.game_over()
                    else:
                        snake2.has_lives = False

        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            if not snake.has_lives:
                game_is_on = False
                scoreboard.game_over()
            else:
                snake.has_lives = False

        if two_pl and (snake2.head.xcor() > 280 or snake2.head.xcor() < -290 or snake2.head.ycor() > 290
                       or snake2.head.ycor() < -290):
            if not snake2.has_lives:
                game_is_on = False
                scoreboard.game_over()
            else:
                snake2.has_lives = False

    screen.exitonclick()


if choice.is_scoreboard:
    win = tk.Tk()
    win.geometry("600x600")
    win.title("Scoreboard")

    all_scores = []
    file = open("scores.txt", 'r')
    count = 0
    for line in file:
        all_scores.append(line)
        count += 1
        if count == 10:
            break
    file.close()

    pos_x = 280
    pos_y = 70

    lab2 = tk.Label(win, text="The last 10 results:", font=15).place(x=pos_x - 60, y=10)

    count = 1
    for el in all_scores:
        lab = tk.Label(win, text=str(str(count) + ")  " + str(el)), font=8).place(x=pos_x, y=pos_y)
        pos_y = pos_y + 40
        count = count + 1

    win.mainloop()

    win.destroy()
