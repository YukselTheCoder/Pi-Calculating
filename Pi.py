import time
import math
import decimal

First = True
while True:
    decimal.getcontext().prec = 10
    odd = True
    leibnizfirsttime = True
    var1 = 3
    if First:
        print("  !5GB###&&&###&&&&5                          Pi Calculation")
        print(" Y#PYJB@5JJJB@@5YYY7                            By Yüksel   ")
        print("~J.   P&.   P@#     ")
        print("     .&B   .#@G     ")
        print("     J@5   ^@@Y     ")
        print("    !@@?   !@@?     ")
        print("   J@@@^   ?@@5   ~?")
        print(" .G@@@P    !@@@B5PG^")
        print("  J##5.     !PB#BY: ")
        First = False
    else:
        time.sleep(2.5)
        print("-----------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        print("     Choose An Algorithm/Bir Algoritma seçin.              ")
        print(" 1-Leibniz Formula/Leibniz Formülü (Forever/Sonsuza kadar)")
        print(" 2-Pi Approximation/Pi Yaklaşımı")
        print(" 3-Pre-Loaded/Önceden Yüklenmiş")
        print(" 4-Archimedes's Tactic/Arşimet'in Taktiği")
        print(" 5-Wallis Tactic/Wallis Taktiği")
        User_input = input(":")
        User_input = int(User_input)
        if User_input == 1:
            print(
                "ENG:   Attention: Please note that this code uses Leibniz formula and can get more inaccurate by time and may not give the perfect results.")
            print(
                "TR:    Dikkat: Bu kod, Leibniz Formülünü kullandığı için zamanla yanlışlaşabilir ve mükemmel sonucu veremeyebilir.")
            time.sleep(5)
            while True:
                var2 =decimal.Decimal (4 / var1)
                if odd:
                    odd = False
                    if leibnizfirsttime:
                        varX = decimal.Decimal(var2)
                        varY = decimal.Decimal(4 - var2)
                    else:
                        varY =decimal.Decimal(varX - var2)
                else:
                    odd = True
                    varX = var2
                    varY = decimal.Decimal (varX + var2)
                print(varY)
                var1 = var1 + 2
                time.sleep(1)
        elif User_input == 2:
            print("22/7:", 22 / 7)
        elif User_input == 3:
            print(math.pi)
        elif User_input == 4:
            print("This algorithm tells the combinations on Archimedes's pi formula it may not give %100 accurate answers")
            print("Bu algoritma Arşimet'in pi formülündeki kombinasyonları gösterir.")
            language = input("Tr OR En:")
            max = decimal.Decimal(3 + (1 / 7))
            Archimedesformula = decimal.Decimal(0.14084507042)
            Guess = 0
            if language == "Tr" :
                Guessname = "Tahmin:"
            elif language == "En" :
                Guessname = "Guess:"
            while max > Archimedesformula:
                pi = math.pi
                pi = decimal.Decimal(pi)
                decimal.getcontext().prec = 10
                Guess = Guess+1
                if pi > Archimedesformula:
                    Accuracy = decimal.Decimal(pi-Archimedesformula)
                    Accuracy = decimal.Decimal(pi-Accuracy)
                elif Archimedesformula > pi:
                    Accuracy = decimal.Decimal(Archimedesformula-pi)
                    Accuracy = decimal.Decimal(pi-Accuracy)
                elif Archimedesformula == pi:
                    Accuracy = "%100"
                print(Archimedesformula,"                       ",Guessname,Guess,"     Accuracy/Doğruluk: ",Accuracy)
                Numbertoadd = decimal.Decimal(0.0000000001)
                Archimedesformula = Archimedesformula + Numbertoadd
        elif User_input == 5:
            WallisFirst=True
            while True:
                if WallisFirst:
                    A = 1
                    Pihalf = decimal.Decimal(2 / A)
                    WallisFirst = False
                else:
                    Tour = 0
                    while Tour < 5:
                        A = A + 2
                        Pihalf = decimal.Decimal(Pihalf) * decimal.Decimal(2 / A)
                        Tour=Tour+1
                    if Tour == 5:
                        Pi = decimal.Decimal(Pihalf * 2)
                        print(Pi)
        else:
            print("Error")
            time.sleep(5)
