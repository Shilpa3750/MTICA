def printSunday():
    print('Sunday')
    return
def printMonday():
    print('Monday')
def printTuesday():
    print('Tuesday')
def printWednesday():
    print('Wednesday')
def printThursday():
    print('Thursaday')
def printFriday():
    print('Friday')
def printSaturday():
    print('Saturday')
def choice():
        print("Enter day number between 1-7")
dayDict={1:printSunday,2:printMonday, 3:printTuesday, 4:printWednesday
        ,5:printThursday,6:printFriday,7:printSaturday}
##selection=0
##while True:
##    if selection==6:break
##    choice()
##    selection=int(input("select a Day option:"))
##    if (selection>=0)and(selection<4):
##        dayNumSelect[selection]()
##
dayNo=int(input())
if dayNo<=1 and dayNo<=7:
    dayDict[dayNo]()
else:
    print("INVALID")
        

        
          
    


