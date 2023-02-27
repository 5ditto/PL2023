import sys

state = True # estado True = on; False = off
counter = 0
data = ''
number = ''
on_off = ''

# ler do stdin
for line in sys.stdin:
    data += line

for char in data:
    if (char.isdigit() and state):
        number += char
    else:
        if(char.lower() == 'o'):
            on_off = 'o'
        elif(char.lower() == 'n' and on_off == 'o'):
            print("on")
            on_off = ''
        elif(char.lower() == 'f' and on_off == 'o'):
            on_off += 'f'
        elif(char.lower() == 'f' and on_off == 'of'):
            state = False
            on_off = ''
        elif(char == '='):
            if number == '': 
                number = '0'
            counter += int(number)
            number = ''
            print('\nCounter: ' + str(counter))
            on_of = ''
        else:
            if(number != ''):
                counter += int(number)
                number = ''
            on_off = ''
            