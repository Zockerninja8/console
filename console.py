import pyautogui as pg
import webbrowser
import time
from tkinter import *
from math import sqrt
from random import shuffle
print("Gib bitte deinen Namen an.")
name = input()
print("loading...")
time.sleep(5)
print("system: online")
time.sleep(1)
print("Willkommen")
print(name)
time.sleep(0.5)
while True:
    erstes = input("Password")
    if erstes == "2008":
        print("Richtig")
        print("Mögliche Befehle sind:")
        print("/stop")
        print("/name")
        print("/help")
        print("/joke 1-5")
        print("/spam")
        print("/pw")
        print("/kaka")
        print("/spamm_whatsapp")
        print("/spamm_discord")
        print("/quiz")
        print("/shitstorm")
        print("/url")
        print("/film")
        print("/calculator")
        while True:
            console = input()
            if console == '/stop':
                print("System wird gestoppt...")
                print("Stopping...")
                time.sleep(3)
                exit(0)
            elif console == "/name":
                print("Du hast gesagt das du")
                print(name)
                print("heist")
            elif console == "/help":
                print("Mögliche Befehle sind:")
                print("/stop")
                print("/name")
                print("/help")
                print("/joke 1-5")
                print("/spam")
                print("/pw")
                print("/kaka")
                print("/spamm_whatsapp")
                print("/spamm_discord")
                print("/quiz")
                print("/shitstorm")
                print("/url")
                print("/film")
                print("/calculator")
            elif console == "/joke 1":
                print("Wie lautet der Vorname vom Reh?")
                time.sleep(5)
                print("Kartoffelpüree")
            elif console == "/joke 2":
                print("Auf einer Skala von 1 bis 10 wie deutsch sind sie?")
                time.sleep(5)
                print("Dürfte ich erstmal ihren Umfrageberechtigungsschein sehen?")
            elif console == "/joke 3":
                print("Wie nennt man ein helles Mammut?")
                time.sleep(5)
                print("Hellmut")
            elif console == "/joke 4":
                print("Meine Frau will mit mir über mein kindisches Verhalten reden.")
                time.sleep(5)
                print("Tja, aber ohne das Geheimwort kommt sie nicht in meine Kissenburg.")
            elif console == "/joke 5":
                print("Frau: Herr Doktor, kann ich mit Durchfall baden gehen?")
                time.sleep(5)
                print("Doktor: Ja klar, wenn Sie die Wanne voll kriegen.")
            elif console == "/spam":
                while True:
                    print("Spam")
            elif console == "/film":
                print("Das war unser mit Abstand länstes Projekt!!")
                time.sleep(3)
                webbrowser.open("https://www.youtube.com/watch?v=A506ihAuYlQ")
            elif console == "/url":
                print("Bitte gebe eine URL ein...")
                url = input()
                webbrowser.open("https://"+url)
            elif console == "/calculator":
                print("Bitte wähle eine Zahl")
                n1 = input()
                print("Wähle eine Rechenart")
                print("1= Plus 2= Minus 3= Geteilt 4= Mal")
                while True:
                    calculator = input("/stop zum beenden")
                    if calculator == "1":
                        print("Wähle eine zweite Zahl")
                        n2 = input()
                        print(int(n2) + int(n1))
                        time.sleep(4)
                        continue
                    elif calculator == "2":
                        print("Wähle eine zweite Zahl")
                        n2 = input()
                        print(int(n2) - int(n1))
                        time.sleep(4)
                        continue
                    elif calculator == "3":
                        print("Wähle eine zweite Zahl")
                        n2 = input()
                        print(int(n2) / int(n1))
                        time.sleep(4)
                        continue
                    elif calculator == "4":
                        print("Wähle eine zweite Zahl")
                        n2 = input()
                        print(int(n2) * int(n1))
                        time.sleep(4)
                        continue
                    elif calculator == "/stop":
                        continue
            elif console == "/pw":
                password = input("Bitte Code eingeben...")
                if password == "1234":
                    print("So einfach ist der Code jetzt auch nicht...")
                else:
                    print("Falscher Code...")
                    exit(0)
            elif console == "/kaka":
                print("💩")
            elif console == "/spamm_whatsapp":
                webbrowser.open("https://web.whatsapp.com")
                time.sleep(15)
                pg.press("tab")
                pg.press("tab")
                while True:
                    time.sleep(10)
                    pg.press("h")
                    pg.press("a")
                    pg.press("l")
                    pg.press("l")
                    pg.press("o")
                    pg.press("space")
                    pg.press("i")
                    pg.press("c")
                    pg.press("h")
                    pg.press("space")
                    pg.press("b")
                    pg.press("i")
                    pg.press("n")
                    pg.press("space")
                    pg.press("e")
                    pg.press("i")
                    pg.press("n")
                    pg.press("space")
                    pg.press("b")
                    pg.press("o")
                    pg.press("t")
                    pg.press("enter")
            elif console == "/spamm_discord":
                webbrowser.open("https://web.whatsapp.com")
                while True:
                    pg.press("h")
                    pg.press("a")
                    pg.press("l")
                    pg.press("l")
                    pg.press("o")
                    pg.press("space")
                    pg.press("i")
                    pg.press("c")
                    pg.press("h")
                    pg.press("space")
                    pg.press("b")
                    pg.press("i")
                    pg.press("n")
                    pg.press("space")
                    pg.press("e")
                    pg.press("i")
                    pg.press("n")
                    pg.press("space")
                    pg.press("b")
                    pg.press("o")
                    pg.press("t")
                    pg.press("enter")
            elif console == "/game 1":
                print("Work in procres")
            elif console == "/quiz":
                while True:
                    while True:
                        print("Wie alt ist Elia?")
                        quiz = input()
                        if quiz == "13":
                            print("Richtig")
                            print("1/?")
                            time.sleep(3)
                            while True:
                                quiz2 = input("Wie viele Haustiere hat Elia?")
                                if quiz2 == "2":
                                    print("Richtig")
                                    print("2/?")
                                    time.sleep(3)
                                    while True:
                                        quiz3 = input("Mag Elia Caffe")
                                        if quiz3 == "ja":
                                            print("Richtig")
                                            print("3/?")
                                            print("Gut gemacht")

                                        else:
                                            print("Falsch")
                                else:
                                    print("Falsch")
                        else:
                            print("Falsch")
            elif console == "/bubble":
                HEIGHT = 768
                WIDTH = 1366
                window = Tk()
                colors = ["darkred", "green", "blue", "purple", "pink", "lime"]
                health = {
                    "ammount": 3,
                    "color": "green"
                }
                window.title("Bubble Blaster")
                c = Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
                c.pack()
                ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill="red")
                ship_id2 = c.create_oval(0, 0, 30, 30, outline="red")
                SHIP_R = 15
                MID_X = WIDTH / 2
                MID_Y = HEIGHT / 2
                c.move(ship_id, MID_X, MID_Y)
                c.move(ship_id2, MID_X, MID_Y)
                ship_spd = 10
                score = 0


                def move_ship(event):
                    if event.keysym == "Up":
                        c.move(ship_id, 0, -ship_spd)
                        c.move(ship_id2, 0, -ship_spd)
                    elif event.keysym == "Down":
                        c.move(ship_id, 0, ship_spd)
                        c.move(ship_id2, 0, ship_spd)
                    elif event.keysym == "Left":
                        c.move(ship_id, -ship_spd, 0)
                        c.move(ship_id2, -ship_spd, 0)
                    elif event.keysym == "Right":
                        c.move(ship_id, ship_spd, 0)
                        c.move(ship_id2, ship_spd, 0)
                    elif event.keysym == "P":
                        score += 10000


                c.bind_all('<Key>', move_ship)
                from random import randint

                bub_id = list()
                bub_r = list()
                bub_speed = list()
                bub_id_e = list()
                bub_r_e = list()
                bub_speed_e = list()
                min_bub_r = 10
                max_bub_r = 40
                max_bub_spd = 20
                gap = 1000


                def create_bubble():
                    x = WIDTH + gap
                    y = randint(0, HEIGHT)
                    r = randint(min_bub_r, max_bub_r)
                    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="red", fill="black")
                    bub_id.append(id1)
                    bub_r.append(r)
                    bub_speed.append(randint(5, max_bub_spd))


                def move_bubbles():
                    for i in range(len(bub_id)):
                        c.move(bub_id[i], -bub_speed[i], 0)
                    for i in range(len(bub_id_e)):
                        c.move(bub_id_e[i], -bub_speed_e[i], 0)


                from time import sleep, time

                bub_chance = 30


                def get_coords(id_num):
                    pos = c.coords(id_num)
                    x = (pos[0] + pos[2]) / 2
                    y = (pos[1] + pos[3]) / 2
                    return x, y


                def del_bubble(i):
                    del bub_r[i]
                    del bub_speed[i]
                    c.delete(bub_id[i])
                    del bub_id[i]


                def clean():
                    for i in range(len(bub_id) - 1, -1, -1):
                        x, y = get_coords(bub_id[i])
                        if x < -gap:
                            del_bubble(i)


                def distance(id1, id2):
                    x1, y1 = get_coords(id1)
                    x2, y2 = get_coords(id2)
                    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


                def collision():
                    points = 0
                    for bub in range(len(bub_id) - 1, -1, -1):
                        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
                            points += (bub_r[bub] + bub_speed[bub])
                            del_bubble(bub)
                    return points


                def cleanAll():
                    for i in range(len(bub_id) - 1, -1, -1):
                        x, y = get_coords(bub_id[i])
                        del_bubble(i)


                def collision_e():
                    for bub in range(len(bub_id_e) - 1, -1, -1):
                        if distance(ship_id2, bub_id_e[bub]) < (SHIP_R + bub_r_e[bub]):
                            window.destroy()
                            print("You were killed by a red bubble...")
                            print("You got ", score, " score!")
                            sleep(100)


                c.create_text(50, 30, text="SCORE", fill="white")
                st = c.create_text(50, 50, fill="white")
                c.create_text(100, 30, text="TIME", fill="white")
                tt = c.create_text(100, 50, fill="white")


                def show(score):
                    c.itemconfig(st, text=str(score))


                evil_bub = 50
                # MAIN GAME LOOP
                while True:
                    if randint(1, bub_chance) == 1:
                        create_bubble()
                    move_bubbles()
                    collision_e()
                    clean()
                    score += collision()
                    if score >= 400:
                        evil_bub = 40
                        bub_chance = 25
                        if score >= 1000:
                            evil_bub = 30
                            bub_chance = 20
                    show(score)
                    window.update()
                    shuffle(colors)
                    sleep(0.01)
            elif console == "/shitstorm":
                print("Möchtest du es einmal sehen oder gespammt werden")
                print("Wenn du es einmal sehen möchtest gebe 1 ein wenn du gespammt werden möchtest gib spamm ein")
                ss = input()
                if ss == "spamm":
                    while True:
                        print("💩💩💩💩💩💩💩💩💩")
                        print(" 💩💩💩💩💩💩💩💩")
                        print("  💩💩💩💩💩💩💩")
                        print("   💩💩💩💩💩💩")
                        print("    💩💩💩💩💩")
                        print("     💩💩💩💩")
                        print("      💩💩💩")
                        print("       💩💩")
                        print("        💩")
                elif ss == "1":
                    print("💩💩💩💩💩💩💩💩💩")
                    print(" 💩💩💩💩💩💩💩💩")
                    print("  💩💩💩💩💩💩💩")
                    print("   💩💩💩💩💩💩")
                    print("    💩💩💩💩💩")
                    print("     💩💩💩💩")
                    print("      💩💩💩")
                    print("       💩💩")
                    print("        💩")

            else:
                print("Unbekanter Befehl")
                print("Bitte gib einen Befehl ein")
    else:
        print("Falsch")
