def IsSymbol(sym):
    if sym == '*' or sym == '/' or sym == '+' or sym == '-' or sym == '^' :
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
        if '0' <= input[i] <= '9':
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
    result = IntCalc(input)
    #############################
    return result

def main():
    input = "-2+5*7+19/2+1"
    result = IntegerCalc(input)
    print(result)

if __name__ == "__main__" :
    main()


print(input)