import pygame
import accessories as acc
import computer_algo as algo

pygame.init()

w, h = 700, 700

win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Tic Tac Toe")
clck = pygame.time.Clock()

Player1 = {"name": "Player 1", "symbol": "cross", "sym_color": (0, 200, 0), "move": False, "wins": 0}
Player2 = {"name": "Player 2", "symbol": "circle", "sym_color": (0, 0, 200), "move": False, "wins": 0}
Computer = True
animation = False

run = True
drawn = 0

win_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],# straight sets
            [0, 4, 8], [2, 4, 6]]# diagonal sets

grid_color = (255, 255, 255)

game_count = 0
vals = []
grid = []


def initialize():
    global vals, grid, game_count
    vals = []
    grid = []
    for i in range(0, 3):  # emptying
        for j in range(0, 3):
            grid.append(pygame.Rect(200 + j * 100, 200 + i * 100, 100, 100))
            vals.append("")
    game_count = Player1["wins"] + Player2["wins"] + drawn + 1
    if Computer:
        Player2["name"] = "Computer"
        Player2["sym_color"] = (200, 0, 0)
    else:
        Player2["name"] = "Player 2"
        Player2["sym_color"] = (0, 200, 200)
    if game_count % 2 == 1:
        Player1["move"] = True
        Player2["move"] = False
    else:
        Player1["move"] = False
        Player2["move"] = True
    pygame.display.update()


initialize()


def anim_cross(c):
    size = 20
    for i in range(0, 61, 5):
        acc.msg("YOUR TURN", (0, 0, 0), 60, 120)
        pygame.draw.line(win, Player1["sym_color"], (c.x + size, c.y + size), (c.x + size + i, c.y + size + i), 2)
        pygame.draw.line(win, Player1["sym_color"], (c.x + c.width - size, c.y + size),
                         (c.x + c.width - size - i, c.y + size + i), 2)
        pygame.display.update()
        clck.tick(20)


def win_anim(a, player):
    global vals
    n = 0
    for v in vals:
        if v != "" and vals.count(v) > 0:
            vals[vals.index(v)] = ""
    while n < 10:
        n += 1
        if player == Player1:
            # Player1["sym_color"] == acc.random_colors()
            for i in a:
                acc.draw_cross(grid[i], color=Player1["sym_color"], size=20)
        else:
            # Player2["sym_color"] == acc.random_colors()
            for i in a:
                acc.draw_circle(grid[i], color=Player2["sym_color"], size=30)
                pygame.display.update()

        clck.tick(10)


def anim_circle(c):
    for i in range(3, 30, 2):
        acc.msg("YOUR TURN", (0, 0, 0), 560, 120)
        pygame.draw.circle(win, Player2["sym_color"], (c.x + 50, c.y + 50), i, 2)
        pygame.draw.circle(win, (0, 0, 0), (c.x + 50, c.y + 50), i - 2)
        pygame.display.update()
        clck.tick(20)


def draw_grid():
    pygame.draw.line(win, grid_color, (300, 200), (300, 500), 3)
    pygame.draw.line(win, grid_color, (400, 200), (400, 500), 3)
    pygame.draw.line(win, grid_color, (200, 300), (500, 300), 3)
    pygame.draw.line(win, grid_color, (200, 400), (500, 400), 3)


def check_win():
    global drawn
    for i in win_list:
        for Player in [Player1, Player2]:
            if vals[i[0]] == Player["symbol"] and vals[i[1]] == Player["symbol"] and vals[i[2]] == Player["symbol"]:
                acc.msg_2(Player["name"] + " WINS", (Player["sym_color"]), 300, 120)
                Player["wins"] += 1
                win_anim(i, Player)
                pygame.time.delay(1000)
                initialize()
                # break
    if vals.count("") == 0:
        drawn += 1
        acc.msg_2("GAME DRAWN", (255, 255, 255), 300, 120)
        pygame.display.update()
        pygame.time.delay(1000)
        initialize()


def nav():
    global Computer
    for g in grid:
        if event.type == pygame.MOUSEMOTION:
            if g.collidepoint(event.pos):
                pygame.draw.rect(win, (0, 200, 0) if vals[grid.index(g)] == "" else (200, 0, 0), g, 3)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if g.collidepoint(pos) and vals[grid.index(g)] == "" and event.button == 1:
                if Player1["move"]:
                    vals[grid.index(g)] = "cross"
                    anim_cross(g)
                    Player1["move"] = False
                    Player2["move"] = True
                elif Player2["move"] and not Computer:
                    vals[grid.index(g)] = "circle"
                    anim_circle(g)
                    Player1["move"] = True
                    Player2["move"] = False

    if Computer and Player2["move"]:
        check_win()
        computer_move()


def computer_move():
    index = algo.computer(vals)
    anim_circle(grid[index])
    vals[index] = "circle"

    Player1["move"] = True
    Player2["move"] = False


def gamewindow():
    global button, Computer
    win.fill((0, 0, 0))
    acc.background()
    acc.msg_heading("TIC TAC TOE", (200, 0, 0), 200, 0)

    button = acc.buttons("Computer", 550, 0, Computer)
    for i in range(len(vals)):
        if vals[i] == "cross":
            acc.draw_cross(grid[i], color=Player1["sym_color"], size=20)
        if vals[i] == "circle":
            acc.draw_circle(grid[i], color=Player2["sym_color"], size=30)

    # pygame.draw.rect(win, (255, 255, 255), (40, 100, 150, 500))
    # pygame.draw.rect(win, (255, 255, 255), (540, 100, 150, 500))

    acc.msg_2("Game " + str(game_count), (255, 255, 255), 350, 50)
    acc.msg_2(Player1["name"], (0, 200, 0), 50, 250)
    acc.msg_2(Player2["name"], (200, 0, 0), 550, 250)
    pygame.draw.rect(win, (200, 200, 200), (40, 100, 150, 500), 2)
    pygame.draw.rect(win, (200, 200, 200), (540, 100, 150, 500), 2)
    acc.msg("Wins: " + str(Player1["wins"]), Player1["sym_color"], 50, 450)
    acc.msg("Wins: " + str(Player2["wins"]), Player2["sym_color"], 550, 450)

    acc.msg("Drawn: " + str(drawn), (255, 255, 0), 300, 600)
    acc.draw_cross(pygame.Rect(50, 300, 100, 100), color=Player1["sym_color"], size=20)
    acc.draw_circle(pygame.Rect(550, 300, 100, 100), color=Player2["sym_color"], size=30)

    if Player1["move"]:
        acc.msg("YOUR TURN", (0, 0, 0), 60, 120)
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        pygame.draw.rect(win, acc.random_colors(), (40, 100, 150, 500), 3)
    elif Player2["move"]:
        acc.msg("YOUR TURN", (0, 0, 0), 560, 120)
        pygame.mouse.set_cursor(*pygame.cursors.ball)
        pygame.draw.rect(win, acc.random_colors(), (540, 100, 150, 500), 3)

    acc.msg("MOVING FIRST", (200, 0, 0), 50 if game_count % 2 == 1 else 550, 400)

    draw_grid()
    check_win()


while run:
    clck.tick(15)
    for event in pygame.event.get(pump=True):
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if pygame.Rect(50, 250, 100, 25).collidepoint(pos):
                nm = acc.textbox((50, 250), 100)
                Player1["name"] = nm if nm != "" else "Player 1"
            if not Computer and pygame.Rect(550, 250, 100, 25).collidepoint(pos):
                nm = acc.textbox((550, 250), 100)
                Player2["name"] = nm if nm != "" else "Player 2"
            if button.collidepoint(pos):
                Computer = False if Computer else True
                initialize()
    gamewindow()
    nav()
    pygame.display.update()

pygame.display.quit()
