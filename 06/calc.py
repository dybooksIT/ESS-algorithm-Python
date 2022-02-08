def calc(expression):
    stack = []
    for i in expression.split(' '):
        # 現在のスタックの内容を表示
        print(stack)
        if i == '+':
            # +のときはスタックから2つ取り出して加算し、再度格納する
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif i == '-':
            # -のときはスタックから2つ取り出して減算し、再度格納する
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif i == '*':
            # *のときはスタックから2つ取り出して乗算し、再度格納する
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif i == '/':
            # *のときはスタックから2つ取り出して除算し、再度格納する
            b, a = stack.pop(), stack.pop()
            stack.append(a // b)
        else:
            # 演算子以外（数字）のときはその値を格納する
            stack.append(int(i))
    return stack[0]

print(calc('4 6 2 + * 3 1 - 5 * -'))
