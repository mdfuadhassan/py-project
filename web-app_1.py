print("My Page".center(50))
print()
def isname():
    name = input("Name ")
    pas = input("Pasword ")
    can_next = input("Cancel or Next ")
    print()

    if can_next == "next" or can_next == "Next" or can_next == "NEXT":
        print("AppsGallery".center(50))
        print()
        def task1():
            apps=["Facebook","Instagram","YouTube","Messenger","WhatsApp","Google","calculator","RockPaperScissor Game","Multiplication-calculator","Ludo Random Number"]
            for i in apps:
                print(i)
        #goback = input("Go or Back ")
        #if goback == "go" or goback == "Go" or goback == "GO":
            choose = input("Enter any app >...")
            if choose == "fb" or choose == "Fb" or choose == "FB" or choose == "facebook" or choose == "Facebook" or  choose == "FACEBOOK":
                def func1():
                    print("loading page.....")
                    print("https://m.facebook.com")
                    print()
                    # print("Go or Back")   
                    goback2 = input("Go or Back ")
                    if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                        func1()
                    elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                        task1()
                    else:
                        func1()
                    func1()
                func1()
            elif choose == "in" or  choose == "In" or choose == "IN" or choose == "instagram" or choose == "Instagram" or choose == "INSTAGRAM":
                def func2():
                    print("loading page.....")
                    print("https://www.instagram.com")
                    print()
                    #print("Go or Back")
                    goback2 = input("Go or Back ")
                    if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                        func2()
                    elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                        task1()
                    else:
                        func2()
                    func2()
                func2()
            elif choose == "yt" or choose == "Yt" or choose == "YT" or choose == "youtube" or choose == "Youtube" or choose == "YouTube" or choose == "YOUTUBE":
                def func3():
                    print("loading page.....")
                    print("https://m.youtube.com")
                    print()
                    # print("Go or Back")
                    goback2 = input("Go or Back ")
                    if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                        func3()
                    elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                        task1()
                    else:
                        func3()
                    func3()
                func3()                             
            elif choose == "mg" or choose == "Mg" or choose == "MG" or choose == "messenger" or choose == "Messenger" or choose == "MESSENGER":
                def func4():
                    print("loading page.....")
                    print("https://www.messenger.com")
                    print()
                    # print("Go or Back")
                    goback2 = input("Go or Back ")
                    if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                        func4()
                    elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                        task1()
                    else:
                        func4()
                    func4()
                func4()
            elif choose == "wa" or choose == "Wa" or choose == "WA" or choose == "whatsapp" or choose == "WhatsApp" or choose == "WHATSAPP":
                def func5():
                    print("loading page.....")
                    print("https://www.whatsapp.com")
                    print()
                    # print("Go or Back")
                    goback2 = input("Go or Back ")
                    if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                        func5()
                    elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                        task1()
                    else:
                        func5()
                    func5()
                func5()
            elif choose == "gg" or  choose == "Gg" or choose == "GG" or choose == "google" or  choose == "Google" or choose == "GOOGLE":
                def func6():
                    print("loading page.....")
                    print("https://www.google.com")
                    print()
                    # print("Go or Back")
                    goback2 = input("Go or Back ")
                    if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                        func6()
                    elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                        task1()
                    else:
                        func6()
                    func6()
                func6()
            elif choose == "cl" or choose == "Cl" or choose == "CL" or choose == "calculator" or  choose == "Calculator" or choose == "CALCULATOR":
                # print("loading page.....")
                # print()
                # print("Go or Back")
                def task2():                       
                    goback3 = input("Go or Back ")
                    if goback3 == "go" or goback3 == "Go" or goback3 == "GO":
                            num1 = int(input("Enter a frirst value: "))   
                            symble = input("Enter a symble: ")
                            num2 = int(input("Enter a second value: "))  
                            if symble == "+":
                                print(f"{num1} + {num2} = {num1+num2}")
                            elif symble == "-":
                                print(f"{num1} - {num2} = {num1-num2}")
                            elif symble == "*": 
                                print(f"{num1} * {num2} = {num1*num2}")
                            elif symble == "/":
                                print(f"{num1} / {num2} = {num1/num2}")
                            elif symble == "**": 
                                print(f"{num1} ** {num2} = {num1**num2}")
                            elif symble == "%%":
                                print(f"{num1} %% {num2} = {num1%num2}")
                            elif symble == "//": 
                                print(f"{num1} // {num2} = {num1//num2}")
                            elif symble == "%": 
                                print(f"{num1} % {num2} = {num1*num2/100}")
                            else:
                                task1()
                    elif goback3 == "back" or goback3 == "Back" or goback3 == "BRACK":      
                        print()
                        # print("Go or Back")
                        goback3 = input("Go or Back ")
                        if goback3 == "go" or goback3 == "Go" or goback3 == "GO":
                            task2()
                        elif goback3 == "back" or goback3 == "Back" or goback3 == "BACK":
                            task1()
                        else:
                            task2()
                    else:
                        task2()
                    task2()
                task2()
            elif choose == "rps" or choose == "Rps" or choose == "RPS" or choose == "rockpaperscissor" or choose == "ROCKPAPERSCISSOR" or choose == "rock paper scissor" or choose == "ROCK PAPER SCISSOR":
                # print("loading page.....")
                def task3():
                    print("Rock,Paper,Scissor")
                    goback10 = input("Go or Back ")
                    if goback10 == "go" or goback10 == "Go" or goback10 == "GO":
                        def rps():
                            import random
                            player = input("My choice is : ")
                            choices = ["rock","paper","scissors"]
                            computer = random.choice(choices)
                            print("Computer :", computer)
                            
                            print()
                            print("Back")
                            if player == "back":
                                task3()
                            rps()
                        rps()
                    elif goback10 == "back" or goback10 == "Back" or goback10 == "BACK":                               
                        print()
                        # print("Go or Back")
                        goback2 = input("Go or Back ")
                        if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                            task3()
                        elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                            task1()
                        else:
                            task3()
                    else:
                        task3()
                    task3()
                task3()
            elif choose == "mc" or choose == "Mc" or choose == "MC" or choose == "multiplicationcalculator" or choose == "Multiplicationcalculator" or choose == "MULTIPLICATIONCALCULATOR" or choose == "multiplication calculator" or choose == "Multiplication calculator" or choose == "Multiplication Calculator" or choose == "MULTIPLICATION CALCULATOR":
                # print("loading page.....")                      
                def task4():
                    goback2 = input("Go or Back ")
                    if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                        num = int(input("Enter a number: "))
                        a = 0 
                        while a <10:
                            a += 1
                            print(f"{num} x {a} = {num*a}")
                            # if num == "s" or num == "stop":
                            #     break 
                            # print()    
                    elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                        print()
                        # print("Go or Back")
                        goback2 = input("Go or Back ")
                        if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                            task4()
                        elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                            task1()
                        else:
                            task4()
                    else:
                        task4()
                    task4()
                task4()
            elif choose == "lrn" or choose == "Lrn" or choose == "LRN" or choose == "ludorandomnumber" or choose == "Ludorandomnumber" or choose == "LUDORANDOMNUMBER" or choose == "ludo random number" or choose == "Ludo random number" or choose == "Ludo Random Number" or choose == "LUDO RANDOM NUMBER":
                # print("loading page.....")
                def task5():
                    import random
                    decision = input("y = you, t = team-mate,pp = pass playyer : ")
                    if decision == "y":
                        player = [1,2,4,5,6]
                        choices = random.choice(player)
                        print("Your choice :",choices)
                        print()
                        print("Back")
                    elif decision == "t":      
                        teammate = [1,2,4,5,6]
                        choices = random.choice(teammate)
                        print("Teammate choice:",choices)
                        print()
                        print("Back")
                    elif decision == "pp":
                        print("pass player")
                        print()
                        print("Back")
                    elif decision == "back" or decision == "Back" or decision == "BACK":         
                        print()
                        # print("Go or Back")
                        goback2 = input("Go or Back ")
                        if goback2 == "go" or goback2 == "Go" or goback2 == "GO":
                            task5()
                        elif goback2 == "back" or goback2 == "Back" or goback2 == "BACK":
                            task1()
                        else:
                            task5()
                    else:
                        task5()
                    task5()
                task5()
            elif choose == "go" or choose == "Go" or choose == "GO":
                task1()
            elif choose == "back" or choose == "Back" or choose == "BACK":
                isname()
            else:
                print("Try again.....")  
        #elif goback == "back" or goback == "Back" or goback == "BACK":
        #    isname()
        #else:
        #    print("Try again.....")
        #task()         
            
        task1()

    elif can_next == "cancel" or can_next == "Cancel" or can_next == "CANCEL":
        # name = input("Name ")
        # pas = input("Pasword ")
        isname()
    else:
        print("Try again.....")
    isname()
isname()


