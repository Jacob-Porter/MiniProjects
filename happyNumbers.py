import math

running = True

def parseNum(val):
    output = []
    for i in range(0, len(str(val))):
        output.append(str(val)[i:i+1])
    return output
        
def doMath(array):
    output = 0 
    for i in range(0, len(array)):
        output = output + math.pow(int(array[i]), 2)
    return output

def deleteDecimals(val):
    index = str(val).index('.')
    parsedNum = str(val)[0:index]
    return str(parsedNum)


while(running):
    num = input('\nEnter the potential Happy number or enter "Exit" to close program - ')

    if num.lower() == 'exit':
        running = False
        print('\nGoodbye :)')
        
    elif num.isdigit():  
        
        final = 0
        prev = num
        count = 0

        while(final != 1):
            final = doMath(parseNum(int(prev)))
            prev = final
            count += 1
                
            if (len(deleteDecimals(final)) == 1 and final != 1):
                break
            
        if (final == 1):
            print('\n' + str(num) + ' IS a Happy Number :)')
            print('It took ' + str(count) + ' cycles...')
        else:
            print('\n' + str(num) + ' IS NOT a Happy Number :(')
            print('It took ' + str(count) + ' cycles...')
    else:
        print('Invalid Input\n')
      
        
# COMPLETE
    