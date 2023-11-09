globlaValue = ""

def echo(inputValue):
    return inputValue+" echo " + globlaValue

def echoEdit(inputValue):
    globlaValue = "Bob" #local variable
    return inputValue+" Bob " + globlaValue

def echoEditGlobal(inputValue):
    global globlaValue #here is using the global variable
    globlaValue = "carl"
    return inputValue+" carl " + globlaValue

    
firstValue = input("Enter a value: ")
print(echo(firstValue))
print(globlaValue)
print(echoEdit(firstValue))
print(globlaValue)
print(echoEditGlobal(firstValue))
print(globlaValue)

globlaValue = "global"

secondValue = input("Enter a value: ")
print(echo(secondValue))
print(globlaValue)
print(echoEdit(secondValue))
print(globlaValue)
print(echoEditGlobal(secondValue))
print(globlaValue)