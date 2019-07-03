operator = '+'
password = '1235678'
num = 23
numTwo = 25
parameter = 21
string1 = "hello"
string2 = " My name is Charlotte"
my_list_3_5 = []
answer = 0
def function_one(password):
    if len( password ) <8 :
        print("Password is too short")
    else:
        print (password)

def function_two(num):
    if num % 3 == 0:
        print ("This number is divisible by 3")
    elif num % 5 == 0:
        print ("This number is divisible by 5")
    else :
        print("This number is not disvisible by 3 or 5")

def function_three(numTwo):
    if numTwo % 3 == 0:
        if numTwo % 5 == 0:
            print("fizz buzz")
        else :
            print ("fizz")
    elif numTwo % 5 == 0:
        print ("buzz")
    else :
        print( numTwo )

def function_four(num):
    print( num + 1)

def function_five(num, numTwo, operator):
    print ( num, operator, numTwo)
    if operator == '+':
        answer = num + numTwo
    elif operator == '-':
        answer = num - numTwo
    elif operator == 'x':
        answer = num * numTwo
    elif operator == "/":
        answer = num / numTwo
    print(answer)

def function_six(string1,string2):
    print (string1, string2)

def function_seven(answer):
    for i in range(1000):
        if i%3 ==0:
            if i%5 == 0:
                my_list_3_5.append(i)
                answer = answer + (i)
            else:
                my_list_3_5.append(i)
                answer = answer + (i)
        elif i %5 ==0:
            my_list_3_5.append(i)
            answer = answer + (i)
    print(answer)
        



# function_one(password)
# function_two(num)
# function_three(numTwo)
# function_four(num)
# function_five(num, numTwo, operator)
# function_six(string1,string2)
function_seven(answer)
