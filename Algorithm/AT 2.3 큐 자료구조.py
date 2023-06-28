def add(item):  # 삽입 연산
    q.append(item)


def remove():   # 삭제 연산
    if len(q) != 0:
        item = q.pop(0)
        return item


q = []
add('apple')
add('orange')
add('cherry')
add('pear')
print('사과, 오렌지, 체리, 배 삽입 후: \t', end='')
print(q)
remove()
print('remove 후:\t\t\t', end='')
print(q)
remove()
print('remove 후:\t\t\t', end='')
print(q)
add('grape')
print('포도 삽입 후:\t\t', end='')
print(q)
