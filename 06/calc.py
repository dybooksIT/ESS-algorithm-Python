def calc(expression):
    stack = []
    for i in expression.split(' '):
        # 현재 스택의 내용을 표시
        print(stack)

        if i == '+':
            # +의 경우 스택에서 요소 두 개를 꺼내 더한 뒤 다시 저장
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif i == '-':
            # -의 경우 스택에서 요소 두 개를 꺼내 뺀 뒤 다시 저장
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif i == '*':
            # *의 경우 스택에서 요소 두 개를 꺼내 곱한 뒤 다시 저장
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif i == '/':
            # *의 경우 스택에서 요소 두 개를 꺼내 나눈 뒤 다시 저장
            b, a = stack.pop(), stack.pop()
            stack.append(a // b)
        else:
            # 연산자 이외(숫자)인 경우 그 값을 저장
            stack.append(int(i))
    return stack[0]

print(calc('4 6 2 + * 3 1 - 5 * -'))