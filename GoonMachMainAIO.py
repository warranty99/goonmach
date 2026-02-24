# The following code was optimized by CHATGPT, however it is based on an entirely hand written code by me.
# Yes this is exactly what you think it is.
# No Im not sorry.

# This program was created by SkibidiToiletMaster9900
# Where are the epstein files??

# python -m PyInstaller --onefile "C:\Users\Usuario\Desktop\gang shit\python\GoonMachMainGPTver.py"
# I know this is in the source code, I dont care!!

import re
import webbrowser
import time
import os
import sys
import subprocess

version = "1.0-AIO"
fuckass = 33 + 1
r3 = r"https://rule"+str(fuckass)+".xxx/index.php?page=post&s=view&id="
ng = r"https://www.newgrounds.com/" # This is useless but will remain.
watermark = r"&tags=GOONMACH" 
parantheses = r"^([A-Z]+)\(([^()]*)\)\(([^()]*)\)$" # This is the craziest fucking regex ive ever seen... oh my god..
AMOUNT_OF_USERLISTS = 0

# Oh my god... It even has a watermark...
                                        
# ++==++****@*. ..+%:.     .::.*=..=.-:*-..:::::::::::::::: 
# ===-=-::+@#:  -. : .- .. .=. . .*:.::#...::::::::-.::.::: 
#.@%###@@@@-:...  -  :               @=@-..::::::.:-::::::- 
#.#*+**==@.   ...   +=@@@@@@@@@%#+.  ..%@...::::--:::::--:: 
#.******@- .-......::-=*===+#*@@@@%+%%+  @:::-:.:::.:::-::: 
#  +***+%:@@+ ....:::+--*+=-::-+*%#%%##@=#* ....:::::::::::: 
#.+===-@@@   ....  ..:.=++*++=-:--==:-@%*:..:::--:::::---:: 
#:@@@@%@-.  .... -+=-=+%*****%@@#***-%@*  ::::-:::-:::::::: 
# ====-@--:.... :=-=+*++*##%%*#***#=*@@::..::::::::-::::::: 
# +++*+@--==:.:+#*:.         .-=*+%@@@@...:::.::::::....::: 
#.**++*@#.--@: .==##%#         -#     ...:---=-::-===+=--=- 
#:@#@@@***+=:==:=:=+#%@@@@@@%*-%@   -@# .:-=-====+++-===+=+ 
# +++=%:  @--.===:::--=--==-*+.-@@@@@@ .*... .  .   ..-  :. 
# ++*=@ @   *-=+:....====*+=*=:-%*::@+     ::--------:----: 
# =-=:@ @   *-+:.....::-+= ...:+#*:@+ @@@@@.        ..-:::: 
# ####@-    *::..:::-=++#@#    --*++ -@*+#@@@@@@@@@@ :::::: 
# =+@@@  - .+:-::::-:-:-+*%#%*@@@@  .@@%%@%#%####@@ .:-:::- 
# @@@   @@+@-:::-=--: .   .%@%:. +@@%+-#@*+#*###%@# .:::-:: 
#-#   .   +=-.::..:==.+@@@+:....     .==@@@@##%@@@. ::::::: 
#  .:.... -@:-:-... ::@........+#%#@@.  .=@@@@@@@+ :::::::: 
#  .:....  *#.::::::  = :%#####*+-.:=@#          :::::-:::: 
# :.:.....  @##:::::. @@-*---:. +:++%#  :::....: #=:::::::: 
# ..:......  #*==... .@  :=++==+*#%#+@= :.:...:. %::::::::: 
# ...:......  ##:    %@..***=:::    .-  : .:..-  @.:::::::: 
# :..:..:....  =:%@@#@% :..-=*###@@@@@+ :..:..: .@:.::--::: 

formattedlistPG1 = {
    "1) " : "Tomboy Solar Flare by Moour",
    "2) " : "Juri-Han by Rechiru",
    "3) " : "Juri-Han FJ v1 by Rechiru",
    "4) " : "Juri-Han FJ v2 by Rechiru",
    "5) " : "Lammy by Rechiru",
    "6) " : "Lammy BJ by Rechiru",
    "7) " : "ENA CG (?) by Rechiru",
    "8) " : "Cheelai BBJ by Ariademon",
    "9) " : "Sweaty Mixi by Vixycore",
    "10) " : "Jane Doe BJ FMDM by NekoNSFW",
    "11) " : "Halloween by Atkoart", 
    "12)" : "Maid CG by Atkoart (shorter)"
}    

formattedlistPG2 = {
    "13) " : "Maid CG by Atkoart (longer)",
    "14) " : "Yandere Dev Foursome by AnnaAnon",
    "15) " : "Sakura Kasugano by Rtil", # UPLOAD THE VICEB NG ONE
    "16) " : "Omori Slime Girls by Shizuka",
    "17) " : "Ryuuko by litsilium",
    "18) " : "Ryuuko Anim by litsilium",
    "19) " : "Power and Kobeni by litsilium",
    "20) " : "Power by jeffmiga",
    "21) " : "Kobeni BJ by Rtil",
    "22) " : "Ranni the Witch v1 by Flou",
    "23) " : "Ranni the Witch v2 by Flou",
    "24) " : "Kagura basketball by jeffmiga"
}

formattedlistPG3 = {
    "25) " : "Kagura waitress by jeffmiga",
    "26) " : "Fuuka and Kotone by jeffmiga",
    "27) " : "Persona 4 gals by jeffmiga"
}

userlist = {

}



generalist = {
    "Tomboy Solar Flare by Moour" : "16419703", 
    "Juri-Han by Rechiru" : "14650960",
    "Juri-Han FJ v1 by Rechiru" : "14651011",
    "Juri-Han FJ v2 by Rechiru" : "15411089",
    "Lammy by Rechiru" : "14539899",
    "Lammy BJ by Rechiru" : "11902760",
    "ENA CG (?) by Rechiru" : "11057300",
    "Cheelai BBJ by Ariademon" : "15144146",
    "Sweaty Mixi by Vixycore" : "16218063",
    "Jane Doe BJ FMDM by NekoNSFW" : "11339083",
    "Halloween by Atkoart" : "15547588",
    "Maid CG by Atkoart (shorter)" : "15343576",
    "Maid CG by Atkoart (longer)" : "15655822",
    "Yandere Dev Foursome by AnnaAnon" : "13904572", # referencia
    "Sakura Kasugano by Rtil" : "4561996",
    "Omori Slime Girls by Shizuka" : "7916031",
    "Ryuuko by litsilium" : "6561291",
    "Ryuuko Anim by litsilium" : "15356961",
    "Power and Kobeni by litsilium" : "7702343",
    "Power by jeffmiga" : "15507907",
    "Kobeni BJ by Rtil" : "7070711",
    "Ranni the Witch v1 by Flou" : "6019115",
    "Ranni the Witch v2 by Flou" : "11261285",
    "Kagura basketball by jeffmiga" : "14645473",
    "Kagura waitress by jeffmiga" : "9935659",
    "Fuuka and Kotone by jeffmiga" : "15301150",
    "Persona 4 gals by jeffmiga" : "13755506"
}

def GETTO(specimen):
    if sys.platform.startswith("win"):
        chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([chrome, "--incognito", r3+specimen+watermark])

    elif sys.platform == "darwin":  # macOS 
        subprocess.Popen(["open", "-na", "Google Chrome", "--args", "--incognito", r3+specimen+watermark])

    else:  # Linux
        subprocess.Popen(["google-chrome", "--incognito", r3+specimen+watermark])

def START(firstmessage=True):
    if firstmessage == True:
        print(r"Welcome to the system! respond with 'LIST' to access the list, or 'INFO' for some information on this program!")

    while True:
        answer = input(r"(GOON MACHINE) >>> ").strip()

        if answer.upper() == "LIST":
            current_page = 1

            while True:
                print("")

                if current_page == 1:
                    page_dict = formattedlistPG1
                    start_index = 1
                    print("PAGE 1/3")
                elif current_page == 2:
                    page_dict = formattedlistPG2
                    start_index = 13
                    print("PAGE 2/3")
                else:
                    page_dict = formattedlistPG3
                    start_index = 25
                    print("PAGE 3/3")

                for i, value in enumerate(page_dict.values(), start=start_index):
                    print(f"{i}) {value}")

                print("")
                print(r"Type the number of the specimen you'd like to access, to go back, simply type 'BACK', for next page, type 'NEXT' ")

                choice = input(r"(GOON MACHINE) >>> ").strip().upper()

                if choice == "BACK":
                    break

                elif choice == "NEXT":
                    if current_page < 3:
                        current_page += 1
                    else:
                        print("Sorry bro, this is the last page as of version " + version)

                elif choice.isdigit():
                    selected_number = int(choice)

                    # Merge all pages into one ordered list
                    all_items = (
                        list(formattedlistPG1.values()) +
                        list(formattedlistPG2.values()) +
                        list(formattedlistPG3.values())
                    )

                    if 1 <= selected_number <= len(all_items):
                        title = all_items[selected_number - 1]
                        specimen = generalist.get(title)

                        if specimen:
                            print("En route to the specimen!")
                            GETTO(specimen)
                            START(firstmessage=False)
                        else:
                            print("I dont think we have that one, brah.")
                    else:
                        print("Invalid selection, broski.")
                else:
                    print("Invalid input, brah.")

        elif answer.upper() == "INFO":
            print("This program was developed in early 2026 by a very handsome and smart guy, it is currently in version", version)
            print("The -AIO stands for Artifical Intelligence Optimized, as this was semi-written by AI, based on my beautiful work.")
            print("This program has not been tested on a MAC, but should work. This program is NOT meant for mobile.")
            print("And yes, it does actually have a watermark.")

        elif answer.upper().startswith("ADD"):
            match = re.search(parantheses, answer)
            if match is not None:
                TITLE = match.group(2)
                ID = match.group(3)
                generalist[TITLE] = ID
                print("Added successfully.")
            else:
                print(r"Sorry dude, To use the ADD you have to structure it like this: ")
                print(r"ADD(TITLE)(ID)")
                print("There can be spaces.")

        elif answer.isdigit():
            selected_number = int(answer)

            all_items = (
                list(formattedlistPG1.values()) +
                list(formattedlistPG2.values()) +
                list(formattedlistPG3.values())
            )

            if 1 <= selected_number <= len(all_items):
                title = all_items[selected_number - 1]
                specimen = generalist.get(title)

                if specimen:
                    print("En route to the specimen!")
                    GETTO(specimen)
                    START(firstmessage=False)
                else:
                    print("Specimen ID not found in generalist.")
            else:
                print("Invalid number.")

        else:
            print("Sorry dude, I dont really get what you mean, try again?")
            print("Remember, 'LIST' for the list, and 'INFO' for info.. not that hard.. bro..")

print("Welcome, bro. Please input a password, brah.")
password = input(">>> ")
if "GOON" in password:
    print("Heh.. Well ill be damned..")
    START()
elif "JERK" in password:
    print("Heh.. Well ill be damned..")
    START()    
elif "MASTURB" in password:
    print("Heh.. Well ill be damned..")
    START()
elif "CRANK" in password:
    print("Heh.. Well ill be damned..")
    START()
else:
    print("MOTHERFUCKER!")
    time.sleep(0.2)
    if sys.platform.startswith("win"):
        chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([chrome, "--incognito", "https://www.youtube.com/watch?v=NXfm5ockkVo"])

    elif sys.platform == "darwin":  # macOS 
        subprocess.Popen(["open", "-na", "Google Chrome", "--args", "--incognito", "https://www.youtube.com/watch?v=NXfm5ockkVo"])

    else:  # Linux
        subprocess.Popen(["google-chrome", "--incognito", "https://www.youtube.com/watch?v=NXfm5ockkVo"])
