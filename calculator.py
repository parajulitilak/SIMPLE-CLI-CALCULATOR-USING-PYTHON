import re

print("Simple mathematical calculator ")
print("Type 'quit' to exit ")

previous=0
run=True

def perform_math():

    global run
    global previous
    equation=""


    if previous==0:
        equation=input("\nEnter mathematical equation :\n")


    else:
        equation=input(str(previous))


    if equation=='quit':
        print("Goodbye!!! Human Being")
        run=False


    else:
        equation=re.sub('[a-zA-Z,.:()" "]','',equation)

        if previous==0:
            previous=eval(equation)

        else:
            previous=eval(str(previous)+equation)

while run:
    perform_math()