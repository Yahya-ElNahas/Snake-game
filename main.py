from tkinter import *
from snake import *
from food import *

score = 0
canvas_squares = []

def drawLines():
    for i in range(0, int(Game_HEIGHT / TILE_SIZE)):
        canvas.create_line(0, i * TILE_SIZE, Game_WIDTH, i * TILE_SIZE, fill="#307030")
    for i in range(0, int(Game_WIDTH / TILE_SIZE)):
        canvas.create_line(i * TILE_SIZE, 0, i * TILE_SIZE, Game_HEIGHT, fill="#307030")

def updateGame(snake, food):
    for i in range(0, len(canvas_squares)):
        canvas.delete(canvas_squares[0])
        del canvas_squares[0]
    c1 = canvas.create_oval(food.x * TILE_SIZE + 5, food.y * TILE_SIZE + 5, food.x*TILE_SIZE + TILE_SIZE - 5,
                        food.y*TILE_SIZE + TILE_SIZE - 5, fill="#802020")
    canvas_squares.append(c1)
    for i in snake.body:
        c1 = canvas.create_rectangle(i.x * TILE_SIZE + 5, i.y * TILE_SIZE + 5, i.x*TILE_SIZE + TILE_SIZE - 5, i.y*TILE_SIZE + TILE_SIZE - 5,
                                 fill="#208020")
        canvas_squares.append(c1)
    if snake.checkCollision() or snake.body[0].x < 0 or snake.body[0].x >= Game_WIDTH / TILE_SIZE or snake.body[0].y < 0 or snake.body[0].y >= Game_HEIGHT / TILE_SIZE:
        gameOver()
        return
    if snake.checkPosition(food.x, food.y):
        snake.incr()
        food.move(snake)
        global score
        score += 1
        label.config(text="Score: {}".format(score))
    snake.move()
    window.after(GAME_SPEED, updateGame, snake, food)

def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('sans_serif', 70), text="Game Over", fill="#500000")

window = Tk()
window.title("Snake Game")
window.resizable(False, False)
label = Label(window, text="Score: {}".format(score))
label.pack()
canvas = Canvas(window, bg="#000000", height=Game_HEIGHT, width=Game_WIDTH)
canvas.pack()
window.update()
x = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
y = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{x}+{y}")
drawLines()
window.bind('<Up>', lambda event: snake.changeDirection(0, -1))
window.bind('<Down>', lambda event: snake.changeDirection(0, 1))
window.bind('<Left>', lambda event: snake.changeDirection(-1, 0))
window.bind('<Right>', lambda event: snake.changeDirection(1, 0))
snake = Snake()
food = Food()
updateGame(snake, food)
window.mainloop()