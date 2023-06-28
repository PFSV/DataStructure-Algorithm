def push(item):  # 삽입 연산
    stack.append(item)


def pop():  # 삭제 연산
    if len(stack) != 0:
        item = stack.pop(-1)
        return item


stack = []
push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리  push 후:\t', end='')
print(stack, '\t<- top')
push('pear')
print('배 push 후:\t\t\t\t\t', end='')
print(stack, '\t<- top')
pop()
push('grape')
print('pop(), 포도 push 후:\t\t\t', end='')
print(stack, '\t<- top')
