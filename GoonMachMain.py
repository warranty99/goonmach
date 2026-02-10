# Yes this is exactly what you think it is.
# No Im not sorry.

# This program was created by SkibidiToiletMaster9900
# Where are the epstein files??

import webbrowser
import time
import os
import sys
import subprocess

version = "1.21"
r3 = r"https://rule34.xxx/index.php?page=post&s=view&id="
ng = r"https://www.newgrounds.com/" # This is useless but will remain.
watermark = r"&tags=GOONMACH" 

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
    "20) " : "Kobeni BJ by Rtil",
    "21) " : "Ranni the Witch v1 by Flou",
    "22) " : "Ranni the Witch v2 by Flou"
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
    "Kobeni BJ by Rtil" : "7070711",
    "Ranni the Witch HJ by Flou" : "6019115",
    "Ranni the Witch BJ by Flou" : "11261285"
}

def GETTO(specimen):
    if sys.platform.startswith("win"):
        chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([chrome, "--incognito", r3+specimen+watermark])

    elif sys.platform == "darwin":  # macOS 
        subprocess.Popen(["open", "-na", "Google Chrome", "--args", "--incognito", r3+specimen])

    else:  # Linux
        subprocess.Popen(["google-chrome", "--incognito", r3+specimen+watermark])

def START(firstmessage=True):
    if firstmessage == True:
        print(r"Welcome to the system! respond with 'LIST' to access the list, or 'INFO' for some information on this program!")
    answer = input(r"(GOON MACHINE) >>> ")
    if "LIST" in answer:
        print("")
        for i, (key, value) in enumerate(formattedlistPG1.items(), start=1):
            print(f"{i}) {value}")
        print("PAGE 1/2")    
        print("")
        print(r"Type the number of the specimen you'd like to access, to go back, simply type 'BACK', for next page, type 'NEXT' ")    
        answer = input(r"(GOON MACHINE) >>> ")
        if "BACK" in answer:
            START(firstmessage=False)

        elif "NEXT" in answer:
            print("")
            for i, (key, value) in enumerate(formattedlistPG2.items(), start=13):
                print(f"{i}) {value}")
            print("PAGE 2/2")    
            print("")
            print(r"Type the number of the specimen you'd like to access, to go back, simply type 'BACK', for next page, type 'NEXT' ")  
            answer = input(r"(GOON MACHINE) >>> ")
            if "BACK" in answer:
                START(firstmessage=False)
            else:
                specimen = generalist[formattedlistPG2[str(answer + ") ")]]    # It is way too late to make this a function of its own, so layers it is...
                print("En route to the specimen!")
                GETTO(specimen) # If you're snooping through this code for whatever reason, you're a bitch!
                START() # Unless you're a friend of mine, then you're good dw.
        else:
            specimen = generalist[formattedlistPG1[str(answer + ") ")]]    
            print("En route to the specimen!")
            GETTO(specimen)
            START()
    elif "INFO" in answer:
        print("This program was developed in early 2026 by a very handsome and smart guy, it is currently in version", version)
        print("This program has not been tested on a MAC, but should work. This program is NOT meant for mobile.")
        print("And yes, it does actually have a watermark.") # https://c.tenor.com/Dc-4lEQkfz8AAAAd/tenor.gif
        START(firstmessage=False)


print("Hello user, please enter a password to access this program. Make sure its in all caps.")
password = input(">>> ")
if "GOON" in password:
    START()
elif "JERK" in password:
    START()
elif "MASTURB" in password:
    START()
elif "CRANK" in password:
    START()
elif "BEAT" in password:
    START()
else:
    print("Sorry, but I dont think you will find this program to be of use to you.")
    time.sleep(1)
    print("Goodbye.")
    time.sleep(0.5)
    quit()
