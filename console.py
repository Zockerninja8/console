import pyautogui as pg
import webbrowser
import time
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
                while True:
                    print("Bitte wähle eine Zahl")
                    n1 = input()
                    print("Wähle eine Rechenart")
                    print("1= Plus 2= Minus 3= Geteilt 4= Mal")
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
                    else:
                        print("Bitte gib eine Zahl von 1 bis 4 ein")
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
            elif console == "/secret":
                print("Bitte Password eingeben")
                secretpw = input()
                if secretpw == "sad":
                    print("Secret befehle sind:")
                    print("/data robin/elia")
                    print("/secret.list")
                    print("/menu")
                    secrets = input()
                    if secrets == "/data robin":
                        print()
                    elif secrets == "/data elia":
                        print()
                    elif secrets == "/secret.list":
                        print("Secret befehle sind:")
                        print("/data robin/elia")
                        print("/secret.list")
                        print("/menu")
            elif console == "/quiz":
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

            elif console == "/shitstorm":
                print("Bist du sicher, dass du das machen willst?")
                print("Dann schreibe ja.")
                ss = input()
                if ss == "ja":
                    while True:
                        print("                                                                                                                                                                                                                                                                                                                                          💩")
                        print("                                                                                                                                                                                                                                                                                                                                         💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                        💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                       💩💩💩💩 ")
                        print("                                                                                                                                                                                                                                                                                                                                       💩💩💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                        💩💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                         💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                          💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                           💩")
                        print("                                                                                                                                                                                                                                                                                                                                          💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                         💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                       💩💩💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                      💩💩💩💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                       💩💩💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                        💩💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                         💩💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                          💩💩")
                        print("                                                                                                                                                                                                                                                                                                                                           💩")
            else:
                print("Unbekanter Befehl")
                print("Bitte gib einen Befehl ein")
    else:
        print("Falsch")
