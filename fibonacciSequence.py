running = True

while running:
    answer = input('Enter steps or "Exit" to close program - ')

    if answer.isdigit():
        output = []

        for i in(range(0, int(answer))):
            if i == 0 or i == 1:
                output.append(i)
            else:
                output.append(output[i-1] + output[i-2])

        print(str(output) + '\n')
        
    elif answer.lower == 'exit':
        running = False
        print('\nGoodbye :)')
    else:
        print('Invalid Input\n')

# COMPLETE