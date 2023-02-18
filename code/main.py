# main python file

# intro
print('Welcome to the "Average score counter "')
print('Version 1.0')

while True:
    enter = input('Press "Enter" to begin...')
    if enter == "":
        break
    else:
        print('Something went wrong')

# collecting info
while True:
    fiveAmount = int(input('How many "5s" do you have?\n'))
    if type(enter) != int:
        print('Something went wrong')
    else:
        break
while True:
    fourAmount = int(input('How many "4s" do you have?\n'))
    if enter == "":
        break
    else:
        print('Something went wrong')
while True:
    threeAmount = int(input('How many "3s" do you have?\n'))
    if enter == "":
        break
    else:
        print('Something went wrong')
while True:
    twoAmount = int(input('How many "2s" do you have?\n'))
    if enter == "":
        break
    else:
        print('Something went wrong')

# algorythm
def averageFn(five, four, three, two):
    five = five * 5
    four = four * 4
    three = three * 3
    two = two * 2

    result = (five + four + three + two)/2
    return result

result = averageFn(fiveAmount, fourAmount, threeAmount, twoAmount)

# info output
print(f'Your average is: {result}')

# exit
while True:
    enter = input('Press "Enter" to exit.')
    if enter == "":
        break
    else:
        print('Something went wrong')