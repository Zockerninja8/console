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
        print("/joke 1-4")
        print("/spam")
        print("/pw")
        print("/kaka")
        print("/spamm_whatsapp")
        print("/spamm_discord")
        print("/quiz")
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
                print("/joke 1-4")
                print("/spam")
                print("/pw")
                print("/kaka")
                print("/spamm_whatsapp")
                print("/spamm_discord")
                print("/quiz")
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
            elif console == "/spam":
                while True:
                    print("Spam")
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
                                print("to start pres enter to stop tippe /stop_spamm if you start there is no return")
                                chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                                webbrowser.get('chrome').open_new_tab("web.whatsapp.com")
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
                chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab("https://discord.com/channels/@me/857922893265502231")
                time.sleep(15)
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
            elif console == "/calculator":
                print("Bitte gebe eine Zahl ein")
                n1 = input()
                print("Wähle eine rechen art aus")
                print("1= Plus")
                print("2= Minus")
                print("3= Mal")
                print("4= Geteilt")
                rechnen = input()
                if rechnen == "1":
                    print("Wähle eine zweite Zahl aus")
                    n2 = input()

                elif rechnen == "1":
                    print("Wähle eine zweite Zahl aus")
                    n2 = input()


                elif rechnen == "1":
                    print("Wähle eine zweite Zahl aus")
                    n2 = input()

                elif rechnen == "1":
                    print("Wähle eine zweite Zahl aus")
                    n2 = input()



            elif console == "/shitstorm":
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