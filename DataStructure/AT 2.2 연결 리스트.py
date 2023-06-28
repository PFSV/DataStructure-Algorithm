class SList:
    class Node:
        def __init__(self, item, link):  # 노드 생성자
            self.item = item
            self.next = link

    def __init__(self):  # 연결 리스트 생성자
        self.head = None
        self.size = 0

    def insert_front(self, item):  # 연결 리스트의 맨 앞에 새 노드 삽입
        if self.size == 0:
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def delete_front(self):  # 연결 리스트의 맨 앞 노드 삭제
        if self.size == 0:
            print('리스트 empty')
        else:
            self.head = self.head.next
            self.size -= 1

    def search(self, target):  # item 이 target 인 노드 탐색
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None

    def print_list(self):  # 연결 리스트 출력
        p = self.head
        while p:
            print(p.item, ' -> ', end=' ')
            p = p.next
        print()


s = SList()  # 연결 리스트 만들기
s.insert_front('orange')
s.insert_front('apple')
s.insert_front('pear')
s.print_list()
print('배는  %d번째 노드에 있다.' % s.search('pear'))
print('키위는', s.search('kiwi'))
s.print_list()
print('첫 노드를 삭제한 후:\t', end=' ')
s.delete_front()
s.print_list()

