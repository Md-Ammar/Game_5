import pygame
import random
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

pygame.init()
w, h = 700, 700
win = pygame.display.set_mode((w, h), HWSURFACE | DOUBLEBUF | RESIZABLE)

clock = pygame.time.Clock()

font1 = pygame.font.SysFont('CHILLER', 35)
font2 = pygame.font.SysFont('system', 25, True)
fontbutton = pygame.font.SysFont('chiller', 25, True)
fonts = pygame.font.get_fonts()


def draw_circle(c, color, size):
    pygame.draw.circle(win, color, (c.x + 50, c.y + 50), size, size//5)

def draw_cross(c, color, size):
    pygame.draw.line(win, color, (c.x + size, c.y + size), (c.x + c.width - size, c.y + c.height - size),
                     size//5)
    pygame.draw.line(win, color, (c.x + size, c.y + c.height - size), (c.x + c.width - size, c.y + size),
                     size//5)

def random_colors():
    return random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)

bg_rects = []
for i in range(w//50):
    bg_rects.append([random.randrange(0, w), random.randrange(0, h), random_colors(), random.randrange(0, 2)])

def background():
    for i in bg_rects:
        i[1] += 10
        if i[1] >= h:
            bg_rects.pop(bg_rects.index(i))
            bg_rects.append([random.randrange(0, w), 0, random_colors(), random.randrange(0, 2)])
        else:
            # pygame.draw.circle(win, random_colors(), (i[0], i[1]), i[2], 1)
            # pygame.draw.rect(win, i[2], (i[0], i[1], 10, 10))
            if i[3] == 0: draw_circle(pygame.Rect(i[0], i[1], 0, 0), i[2], size=10)
            elif i[3] == 1: draw_cross(pygame.Rect(i[0], i[1], 0, 0), i[2], size=10)



def msg_heading(m, color, x, y):  # large text(mid)
    # text = font1.render(m, 1, color)
    # win.blit(text, ((w - text.get_width()) // 2, y - text.get_height() // 2))
    for i in range(len(m)):
        F = pygame.font.SysFont(fonts[random.randrange(0, len(fonts))], 25, True)
        text = F.render(m[i], 1, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        win.blit(text, (x + i * 30, y))


def msg_2(m, color, x, y):  # large text(mid)
    text = font1.render(m, 1, color)
    win.blit(text, (x, y))


def msg(m, color, x, y):  # small text
    text = font2.render(m, 1, color)
    win.blit(text, (x, y))


def textbox(c, wid):
    global font2
    font2 = pygame.font.SysFont('Chiller', 25, True)
    s = ""
    n = True
    while n:
        pygame.draw.rect(win, (255, 255, 255), (c[0], c[1], wid, 30))
        pygame.draw.rect(win, (0, 200, 0), (c[0], c[1], wid, 30), 2)

        if s == "":
            win.blit(font2.render("<NAME>", 1, (100, 100, 100)), c)
        if len(s) > 0: s = s[0].upper() + s[1:]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return s

            if event.type == pygame.KEYDOWN:
                l = str(pygame.key.name(event.key))
                if l == "backspace": s = s[0:len(s) - 1]
                if l == "space": s += " "
                if l == "return": return s
                if len(l) == 1: s += l
        txt = font2.render(s, 1, (0, 0, 0))
        win.blit(txt, c)

        if wid < txt.get_width():
            wid = txt.get_width()
        pygame.display.update()
        clock.tick(10)


def buttons(msg, x, y, state):  # button
    global font2
    text = fontbutton.render(msg, 1, (0, 255, 0))
    wid_button, ht_button = text.get_width(), text.get_height()
    color = (0, 200, 0) if state else (200, 0, 0)

    pygame.draw.rect(win, (0, 0, 0), (x, y, wid_button, ht_button), 0)
    pygame.draw.rect(win, color, (x, y, wid_button, ht_button), 3)

    win.blit(text, (x, y))
    dim = pygame.Rect(x, y, wid_button, ht_button)
    return dim


