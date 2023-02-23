d_money = {
        'One Hundred dollar'    : 100,
        'Twenty dollar'         : 20,
        'Ten dollar'            : 10,
        'Five dollar'           : 5,
        'One dollar'            : 1,
        'Quarter'               : 0.25,
        'Dime'                  : 0.10,     
        'Nickel'                : 0.05,
        'Penny'                 : 0.01,
        }

words = [
    'One Hundred Dollar Bills: ',
    'Twenty Dollar Bills: ',
    'Ten Dollar Bills: ',
    'Five Dollar Bills: ',
    'One Dollar Bills: ',
    'Quarters: ',
    'Dimes: ',
    'Nickels: ',
    'Pennies: ',
    
]

running = True

def countBills(val):
    
    output = []
    
    count_oneHundred = 0
    while(val >= d_money['One Hundred dollar']):
        val -= d_money['One Hundred dollar']
        count_oneHundred += 1 
    output.append(count_oneHundred)
    
    ###
        
    count_twenty = 0
    while(val >= d_money['Twenty dollar']):
        val -= d_money['Twenty dollar']
        count_twenty += 1
    output.append(count_twenty)

    ###
        
    count_ten = 0
    while(val >= d_money['Ten dollar']):
        val -= d_money['Ten dollar']
        count_ten += 1      
    output.append(count_ten)
    
    ###
       
    count_five = 0
    while(val >= d_money['Five dollar']):
        val -= d_money['Five dollar']
        count_five += 1        
    output.append(count_five)
    
    ###
        
    count_one = 0
    while(val >= d_money['One dollar']):
        val -= d_money['One dollar']
        count_one += 1      
    output.append(count_one)
        
    ###
    
    count_quarter = 0
    while(val >= d_money['Quarter']):
        val -= d_money['Quarter']
        count_quarter += 1       
    output.append(count_quarter)
    
    ###
        
    count_dime = 0
    while(val >= d_money['Dime']):
        val -= d_money['Dime']
        count_dime += 1    
    output.append(count_dime)  
    
    ###
          
    count_nickel = 0
    while(val >= d_money['Nickel']):
        val -= d_money['Nickel']
        count_nickel += 1     
    output.append(count_nickel)
    
    ###
    
    val = round(val, 2)
    
    count_penny = 0
    while(val >= d_money['Penny']):
        val -= d_money['Penny']
        count_penny += 1 
    output.append(count_penny)
        
    return output

def isDigit(val):
    if str(val).__contains__('.'):
        index = str(val).index('.') 
        if(str(val[0:index]).isdigit() and str(val[index+1:len(str(val))]).isdigit()):
            return True
    else:
        if (str(val).isdigit()):
            return True
    return False

while(running):
    
    validInput = False
    
    while(not validInput):
        cost = input("\nCost? - ")
        given = input("Given? - ")
                
        if(isDigit(cost) and isDigit(given)):
            if (float(cost) <= float(given)):
                validInput = True
            else:
                print('Not enough money :(\n')
        else:
            print('Invalid Input\n')
    
    change = round(abs(float(cost) - float(given)),2)

    array = countBills(change)

    print('\n----------------------')
    print('- RESULT -')
    print('----------------------\n')


    for i in range(0, len(array)):
        if array[i] > 0:
            print(words[i] + str(array[i]))        

    changeIndex = str(change).index('.')
    if (len(str(change)[changeIndex+1:len(str(change))]) < 2):
        change = str(change) + '0'

    print('\nTotal change: $' + str(change))
    
    if (input('\nEnter "Exit" to close program, or enter anything to run again\n').lower() == 'exit'):
        running = False
        print('Goodbye :)')
