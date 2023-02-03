def getNumber():
    return int( input("Enter number: ") )

def addNumbers( num1, num2, num3 ):
    return num1 + num2 + num3

def subtractNumbers ( num1, num2 ):
    return num1 - num2

def multiplication ( num1, num2 ):
    return num1 * num2

def division (num1, num2):
    return num1 / num2


def displayResult( result ): #+
    print(num1, "+", num2, "+", num3, "=", result)

def displayResult2( result2 ): #-
    print(num1, "-", num2, "=", result2)

def displayResult3( result3 ): #*
    print(num1, "*", num2, "=", result3)

def displayResult4( result4):
    print(num1, "/", num2, "=", result4)



#programmain
num1 = ""
num2 = ""
num3 = ""

num1 = getNumber()
num2 = getNumber()
num3 = getNumber()

addNumbers( num1, num2, num3)
subtractNumbers ( num1, num2 )
multiplication ( num1, num2 )
division (num1, num2)

result = num1+num2+num3
result2 = num1-num2
result3 = num1*num2
result4 = num1/num2

displayResult(result)
displayResult2(result2)
displayResult3(result3)
displayResult4( result4)

print("Program End.")
