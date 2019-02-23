import math

def IsSymbol(sym):
    if sym == '*' or sym == '/' or sym == '+' or sym == '-' or sym == '^' :
        return True
    return False

def IsDigit(ch):
    if (ch >= '0' and ch <= '9') or (ch >= 'A' and ch <= 'F') or (ch == 'x') or (ch == 'b') or (ch == '.'):
        return True
    return False

def IntCalc(input) :
    strNum=""
    numStack = []
    # -나 +로 수식이 시작되면 맨 앞에 0 삽입
    if input[0] == '-' or input[0] == '+':
        input = '0'+input

    # 숫자 추출
    PlusMinus = 1
    for i in range(len(input)) :
        if IsDigit(input[i]):
            strNum = strNum + input[i]
        else :
            if not strNum == "":
                numStack.append(str(int(strNum)*PlusMinus))

            if IsSymbol(numStack[-1]) :
                if input[i] == '-':
                    PlusMinus = 1
                else:
                    PlusMinus = -1
            else:
                numStack.append(input[i])
            strNum=""
    if not strNum == "":
        numStack.append(str(int(strNum)*PlusMinus))

    #곱하기, 나누기 처리
    calcStack = []
    nLen = len(numStack)
    for i in range(nLen) :
        item = numStack.pop(-1)
        if IsSymbol(item):
            calcStack.append(item)
        else:
            if len(calcStack) > 0 and calcStack[-1] == "*":
                num2 = int(item)
                calcStack.pop(-1)
                num1 = int(calcStack.pop(-1))
                calcStack.append(str(num1*num2))
            elif len(calcStack) > 0 and calcStack[-1] == "/":
                num2 = int(item)
                calcStack.pop(-1)
                num1 = int(calcStack.pop(-1))
                if num1 == 0:
                    return "INF"
                calcStack.append(str(int(num2/num1)))
            else:
                calcStack.append(item)

    # 더하기, 빼기 처리
    while True:
        if len(calcStack) == 1:
            result = calcStack.pop(-1)
            break;
        num1 = int(calcStack.pop())
        sym = calcStack.pop()
        num2 = int(calcStack.pop())
        total = 0
        if sym == "+":
            total = num1+num2
        elif sym == "-":
            total=num1-num2
        calcStack.append(str(total))
    return result

def IntegerCalc(input) :
    result = ""
    #############################
    # 괄호 처리
    charStack=[]
    inBrace=""
    for i in range(len(input)):
        if input[i] == ')':
            while True:
                temp=charStack.pop(-1)
                if temp == '(':
                    dc=IntCalc(inBrace)
                    charStack+=dc
                    inBrace=""
                    break
                else:
                    inBrace=temp+inBrace
        else:
            charStack+=input[i]
    strR=""
    for i in range(len(charStack)):
        strR=strR+charStack[i]

    result = IntCalc(strR)
    #############################
    return result

def Conv10(strNum) :
    decNum = 0
    if len(strNum)  > 1 and strNum[0] == '0' and strNum[1]  == 'x':
        hexNum = strNum[2:]
        decNum += int(hexNum, 16)
        return str(decNum)
    elif len(strNum) > 1 and strNum[len(strNum)-1] == 'b':
        binNum = strNum[:-1]
        decNum += int(binNum, 2)
        return str(decNum)
    else:
        return strNum

def ProgrammerCalc(input):
    result = ""
    #############################
    numQ = ""
    strNum = ""

    # 숫자 추출 & 10 진수 변환
    for i in range(len(input)):
        if IsDigit(input[i]):
            strNum += input[i]
        else:
            if not strNum == "":
                numQ = numQ + Conv10(strNum)
            numQ = numQ + input[i]
            strNum = ""

    if not strNum == "":
        numQ = numQ + Conv10(strNum);

    decRes = IntegerCalc(numQ);
    if decRes =="INF":
        return "INF"
    resNum = int(decRes)
    hexRes = "0x" + hex(resNum)[2:].upper()
    binRes = bin(resNum)[2:] + "b"
    result = decRes + " " + hexRes + " " + binRes;

    #############################
    return result

def GetTriValue(strNum):
    dNum = 0.0
    if strNum[0] == 'S':
        dNum = float(strNum[1:])
        dNum = math.sin(dNum * math.pi / 180.0)
    elif strNum[0] == 'C':
        dNum = float(strNum[1:])
        dNum = math.cos(dNum * math.PI / 180.0)
    elif strNum[0] == 'T':
        dNum = float(strNum[1:])
        dNum = math.tan(dNum * math.PI / 180.0)
    elif strNum[0] == 'L':
        dNum = float(strNum[1:])
        dNum = math.log10(dNum)
    else:
        dNum = float(strNum)
    return dNum


def DoubleCalc(input):
    result = ""
    numStack = []
    strNum = ""

    if input[0] == '-' or input[0] == '+':
        input = "0" + input

    # 숫자 추출 & factorial 처리
    for i in range(len(input)):
        if IsDigit(input[i]) or input[i] == 'S' or input[i] == 'C' or input[i] == 'T' or input[i] == 'L':
            strNum += input[i]
        elif input[i] == '!':
            nNum = math.factorial(int(strNum));
            strNum = ""
            numStack.append(nNum)
        else: # +- * / 기호
            dNum = 0.0;
            if not strNum == "":
                dNum = GetTriValue(strNum)
            numStack.append(dNum)
            strNum = "";
            numStack.append(input[i]);
    if not strNum == "":
        dNum = GetTriValue(strNum)
        numStack.append(dNum)

    # 곱하기, 나누기, 거듭제곱 처리
    calcStack = []
    nLen = len(numStack)
    for i in range(nLen):
        item = numStack.pop(-1)
        if IsSymbol(item):
            calcStack.append(item)
        elif len(calcStack) > 0 and calcStack[-1] == "*":
            num2 = float(item)
            str = calcStack.pop(-1)
            str = calcStack.pop(-1)
            num1 = float(str)
            calcStack.append(num1 * num2)
        elif len(calcStack) > 0 and calcStack[-1] == "/":
            num2 = float(item)
            str = calcStack.pop(-1)
            str = calcStack.pop(-1)
            num1 = float(str)
            if num1 == 0:
                return "INF"
            calcStack.append(num2 / num1)
        elif len(calcStack) and calcStack[-1] == "^":
            num1 = float(item)
            str = calcStack.pop(-1)
            str = calcStack.pop(-1)
            num2 = float(str)
            calcStack.append(math.pow(num1, num2))
        else:
            calcStack.append(item)

    # 더하기, 빼기 처리
    while True:
        if len(calcStack) == 1:
            result = calcStack.pop(-1)
            break

        strTemp = calcStack.pop(-1)
        num1 = float(strTemp)
        sym = calcStack.pop(-1)
        strTemp = calcStack.pop(-1)
        num2 = float(strTemp)

        total = 0.0
        if sym == "+":
            total = num1 + num2
        elif sym == "-":
            total = num1 - num2;
        calcStack.append(total)

    return result

def EngineeringCalc(input):
    result = ""
    ###############################################
    input = input.replace("SIN", "S")
    input = input.replace("COS", "C")
    input = input.replace("TAN", "T")
    input = input.replace("LOG", "L")

    # 괄호 처리
    charStack = []
    inBrace = ""
    for i in range(len(input)):
        if input[i] == ')':
            while True:
                temp = charStack.pop(-1)
                if temp[0] == '(':
                    dc = DoubleCalc(inBrace)
                    if dc =="INF":
                        return "INF"

                    charStack+=str(dc)
                    inBrace = ""
                    break
                else:
                    inBrace = temp + inBrace
        else:
            charStack.append(input[i])

    strTemp = "";
    for item in charStack:
        strTemp = strTemp + item

    result = DoubleCalc(strTemp)
    if result == "INF":
        return "INF"
    dRes = float(result)
    result = ("%.3f" % dRes)
    #######################################################
    return result

def main():
    input = "12+3*(7+3*2)+19/(3*(3/2))"
    result = IntegerCalc(input)
    print(result)
    input = "11b+(0x11*10b+1)-9"
    result = ProgrammerCalc(input)
    print(result)
    input="-0.123+2^(1/2)+SIN((40+5)*SIN(89+SIN(90)))+LOG(2*3+4)+5!"
    result = EngineeringCalc(input)
    print(result)

if __name__ == "__main__" :
    main()

print(input)

