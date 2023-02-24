running = True
lengthOfFloat = 3

def isDecimal(input):
            dot = str(input).index('.') + 1
            if str(input[dot:dot+1]) != '0' or len(str(input)) > lengthOfFloat:
                return True
            return False
                
def isPrime(x): 
    if x > 1:
        for i in range(2,x):
            if (x % i == 0):
                return False
        return True
    return False

while running:
    n = input('Enter value or "Exit" to stop program - ')

    if str(n).lower() == 'exit':
        running = False
        print('\nGoodbye :)')
    elif n.isdigit():
        primes = []
        for x in range(0, int(n) + 1):
            if isPrime(x):
                primes.append(x)
                
        print(primes)
        print('Prime numbers: ' + str(len(primes)))
    else:
        print('Invalid Input\n')


## COMPLETE