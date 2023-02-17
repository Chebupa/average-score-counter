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
fiveAmount = int(input('How many "5s" do you have?\n'))
fourAmount = int(input('How many "4s" do you have?\n'))
threeAmount = int(input('How many "3s" do you have?\n'))
twoAmount = int(input('How many "2s" do you have?\n'))

# algorythm
def averageFn(five, four, three, two):
    result = (five + four + three + two)/2
    return result

result = averageFn(fiveAmount, fourAmount, threeAmount, twoAmount)

# info output
print(f'Your average is: {result}')

# exit
while True:
    enter = input('Press "Enter" to begin...')
    if enter == "":
        break
    else:
        print('Something went wrong')