import random

arrayLength = 100
maxNum = 1000
array = []

bubbling = True

for i in range(0, random.randint(arrayLength * 0.5,arrayLength)):
    array.append(random.randint(0,maxNum))
    
print(str(array) + '\n')    
    
cycles = 0
swaps = 0

while(bubbling):
    bubbling = False
    for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            bubbling = True
            swaps += 1
    cycles += 1      
            
print(array)
print('Cycles: ' + str(cycles))
print('Swaps: ' + str(swaps))
                
                
    