import tkinter as tk, random
from tkinter import PhotoImage

#Variables
aces = {"name": "Aces", "buttonName": "","buttonNameLabel": "", "score": 1, "id": 0}
twos = {"name": "Twos",  "buttonName": "","buttonNameLabel": "","score": 2, "id": 1}
threes = {"name": "Threes",  "buttonName": "","buttonNameLabel": "","score": 3, "id": 2}
fours = {"name": "Fours", "buttonName": "","buttonNameLabel": "", "score": 4, "id": 3}
fives = {"name": "Fives", "buttonName": "","buttonNameLabel": "", "score": 5, "id": 4}
sixes = {"name": "Sixes", "buttonName": "","buttonNameLabel": "", "score": 6, "id": 5}
bonuses = {"name": "Bonus", "buttonName": "","buttonNameLabel": "", "score": 35, "id": 6}
three_of_kind = {"name": "Three of a Kind", "buttonName": "","buttonNameLabel": "", "score": 0, "id": 7}
four_of_kind = {"name": "Four of a Kind", "buttonName": "","buttonNameLabel": "", "score": 0, "id": 8}
full_house = {"name": "Full House",  "buttonName": "","buttonNameLabel": "","score": 25, "id": 9}
sm_straight = {"name": "Small Straight", "buttonName": "","buttonNameLabel": "", "score": 30, "id": 10}
lg_straight = {"name": "Large Straight", "buttonName": "","buttonNameLabel": "", "score": 40, "id": 11}
yahtzee = {"name": "Yahtzee",  "buttonName": "","buttonNameLabel": "","score": 50, "id": 12}
chance = {"name": "Chance",  "buttonName": "","buttonNameLabel": "","score": 0, "id": 13}

scores = [aces, twos, threes, fours, fives, sixes, bonuses, three_of_kind, four_of_kind, full_house, sm_straight, lg_straight, yahtzee,chance]
allDice = []

currentDiceNumbers = []
disabledScores = []
rollCount = 0
bonusScore = 0



window = tk.Tk()
var = tk.StringVar()

def right_click(event):
    event.widget['state'] = 'normal'
    event.widget.configure(highlightbackground = "white")

def createDice(numberPassed):

    for i in range(5):
        diceNumber = "dice"+str(i)
        imageNumber = "imageDice"+str(i)
        smallImageNumber = "smaller_image"+str(i)

        #load the image
        globals()[imageNumber] = PhotoImage(master = window, file = "*INSERT FILE PATH*" + str(numberPassed)+".png")
        globals()[smallImageNumber] = globals()[imageNumber].subsample(8,8)

        #create a label to display the image

        globals()[diceNumber] = tk.Button(window, state = 'normal', image = globals()[smallImageNumber], command = lambda var = (diceNumber):[diceRead(var)])
        globals()[diceNumber].grid(row = 1, column = i+2, padx = 2, pady = 2)
        globals()[diceNumber].bind("<Button-2>", right_click)
        allDice.append(globals()[diceNumber])



def rollDice():
    global allDice, dice0, dice1, dice2, dice3, dice4, rollCount, rollButton, scores, currentDiceNumbers, disabledScores
    c = 0
    rollCount +=1
    rollCounter.configure(text = "Roll Number: " + str(rollCount))

    if len(currentDiceNumbers) > 0:
        currentDiceNumbers.clear()

    if rollCount > 0:
        for i in scores:
            if globals()[i['buttonName']] in disabledScores:
                pass
            else:
                globals()[i['buttonName']]['state'] = 'normal'

    for i in allDice:
        randomNumber = random.randint(1,6)
        diceNumber = "dice"+str(c)
        imageNumber = "imageDice"+str(c)
        smallImageNumber = "smaller_image"+str(c)

        if globals()[diceNumber]['state'] !='disabled':
            
            # Load the image 
            globals()[imageNumber] = PhotoImage(master = window,file="*INSERT FILE PATH*" +str(randomNumber)+".png")
            globals()[smallImageNumber] = globals()[imageNumber].subsample(8,8)
            
        
        # Create a label to display the image
            globals()[diceNumber] = tk.Button(window, image=globals()[smallImageNumber], command=lambda var = str("dice"+str(c)):[diceRead(var)])
            globals()[diceNumber].grid(row = 1, column = c+2, padx = 2, pady=2)
            globals()[diceNumber].bind("<Button-2>", right_click) #Button 2 on Mac #Button 3 on Windows

            if rollCount == 3:
                rollButton['state'] = 'disabled'
        else:
            if rollCount == 3:
                rollButton['state'] = 'disabled'
            pass
        c+=1
        currentDiceNumbers.append(globals()[imageNumber].cget('file'))

def diceRead(diceName):
    global allDice, dice0, dice1, dice2, dice3, dice4, rollCount, rollButton, scores, currentDiceNumbers, disabledScores

    globals()[diceName]['state'] = 'disabled'
    globals()[diceName].configure(highlightbackground = 'red')



for i in range(len(scores)):
    c = 0
    r = 3

    buttonScore = "Button" +str(i)
    buttonScoreLabel = "ButtonLabel"+str(i)
    

    if scores[i]["name"] == 'Bonus':
        globals()[buttonScore] = tk.Label(master = window, text = str(scores[i]["name"]), width = 12)
        globals()[buttonScore].grid(row = r + i, column = c, padx = 2, pady = 2)

        globals()[buttonScoreLabel] = tk.Label(master = window, text = "0", width = 12)
        globals()[buttonScoreLabel].grid(row = r + i, column = c+1, padx = 2, pady = 2)

    else:
        globals()[buttonScore] = tk.Button(master = window, text = str(scores[i]["name"]), state = 'disabled', width = 12, command= lambda var = str(buttonScore),  var2 = str(scores[i]["name"]):[pushed(var,var2)])
        globals()[buttonScore].grid(row = r + i, column = c, padx = 2, pady = 2)

        globals()[buttonScoreLabel] = tk.Label(master = window, text = "-", width = 12)
        globals()[buttonScoreLabel].grid(row = r + i, column = c+1, padx = 2, pady = 2)
        
    scores[i]['buttonName'] = buttonScore
    scores[i]['buttonNameLabel'] = buttonScoreLabel



createDice(1)
rollButton = tk.Button(window, text = "Roll", width = 12, command=lambda:[rollDice()])
rollButton.grid(row = 1, column = 0)

rollCounter = tk.Label(window, text = "Roll Number: " + str(rollCount), width = 12)
rollCounter.grid(row = 0, column = 1, columnspan = 5)



def pushed(scoreBox, nameOfScore):
    global rollCount,rollCounter,rollButton, allDice,currentDiceNumbers,scores,disabledScores, bonusScore

    #Resets back to start

    total = 0
    rollCount = 0
    rollCounter.configure (text = "Roll Number: " + str(rollCount))
    rollButton['state'] = 'normal'
    #END


#Counters for Calculating Score
    counter1 = currentDiceNumbers.count("/Users/tuckerwalden/Desktop/Pyahtzee_Windows/dice/1.png")
    counter2 = currentDiceNumbers.count("/Users/tuckerwalden/Desktop/Pyahtzee_Windows/dice/2.png")
    counter3 = currentDiceNumbers.count("/Users/tuckerwalden/Desktop/Pyahtzee_Windows/dice/3.png")
    counter4 = currentDiceNumbers.count("/Users/tuckerwalden/Desktop/Pyahtzee_Windows/dice/4.png")
    counter5 = currentDiceNumbers.count("/Users/tuckerwalden/Desktop/Pyahtzee_Windows/dice/5.png")
    counter6 = currentDiceNumbers.count("/Users/tuckerwalden/Desktop/Pyahtzee_Windows/dice/6.png")

    counters = [counter1,counter2,counter3,counter4,counter5,counter6]
    print(counters)
#END

    #Scoring 1 - 6 & Bonus:

    #One
    if nameOfScore == 'Aces':
        if counter1 > 0:
            total = counter1*1
        else:
            total = 0
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel0.configure(text = str(total))
        bonusScore += total

    #Two
    if nameOfScore == 'Twos':
        if counter2 > 0:
            total = counter2*2
        else:
            total = 0
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel1.configure(text = str(total))
        bonusScore += total

    #Three
    if nameOfScore == 'Threes':
        if counter3 > 0:
            total = counter3*3
        else:
            total = 0
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel2.configure(text = str(total))
        bonusScore += total
            
    #Four
    if nameOfScore == 'Fours':
        if counter4 > 0:
            total = counter4*4
        else:
            total = 0
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel3.configure(text = str(total))
        bonusScore += total

    #Five
    if nameOfScore == 'Fives':
        if counter5 > 0:
            total = counter5*5
        else:
            total = 0
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel4.configure(text = str(total))
        bonusScore += total

    #Six
    if nameOfScore == 'Sixes':
        if counter6 > 0:
            total = counter6*6
        else:
            total = 0
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel5.configure(text = str(total))
        bonusScore += total

    #Bonus
    if bonusScore >= 63:
        ButtonLabel6.configure(text = str(35))
    else:
        ButtonLabel6.configure(text = str(0))
#END

    #Rest of Scoring

    #3 of kind
    if nameOfScore == 'Three of a Kind': 

        if 3 in counters or 4 in counters or 5 in counters:
            number = 1
            for num in counters:
                if num == 0:
                    pass
                else:
                    total += number *num
                number +=1
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel7.configure(text = str(total))

    #4 of kind
    if nameOfScore == 'Four of a Kind': 

        if 4 in counters or 5 in counters:
            number = 1
            for num in counters:
                if num == 0:
                    pass
                else:
                    total += number *num
                number +=1
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel8.configure(text = str(total))

    #Full House
    if nameOfScore == 'Full House':

        if 3 in counters and 2 in counters:
            for num in counters:
                if num == 0:
                    pass
                else:
                    total = 25
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel9.configure(text = str(total))        
    

    #Small Straight
    if nameOfScore == 'Small Straight':
        if counter1 >= 1 and counter2 >= 1 and counter3 >= 1 and counter4 >=1 or counter2 >= 1 and counter3 >=1 and counter4 >=1 and counter5 >=1 or counter6 >= 1 and counter5 >= 1 and counter4 >=1 and counter3 >=1:
           for num in counters:
               if num == 0:
                   pass            
               else:
                   total = 30
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel10.configure(text = str(total))

    #Large Straight
    if nameOfScore == 'Large Straight':
        if counter1 >= 1 and counter2 >= 1 and counter3 >= 1 and counter4 >=1  and counter5 >= 1 or counter2 >= 1 and counter3 >=1 and counter4 >=1 and counter5 >=1 and counter6 >= 1:
            for num in counters:
                if num == 0:
                    pass
                else:
                    total = 40
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel11.configure(text = str(total))

    if nameOfScore == 'Yahtzee':
        if 5 in counters:
            for num in counters:
                if num == 0:
                    pass
                else:
                    total = 50
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel12.configure(text = str(total))

    #Chance
    if nameOfScore == 'Chance':
        number = 1
        for num in counters:
           if num == 0:
               pass
           else:
               total += number *num
           number +=1        
        globals()[scoreBox]['state'] = 'disabled'
        disabledScores.append(globals()[scoreBox])
        ButtonLabel13.configure(text = str(total))   
    createDice(1)
    print(total)    















window.mainloop()
