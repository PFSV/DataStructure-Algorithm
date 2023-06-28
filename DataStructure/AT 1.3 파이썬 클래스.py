class Student:
    def __init__(self, x, y):   # Student 객체 생성자
        self.name = x           # 이름을 저장할 변수
        self.id = y             # id를 저장할 변수

    def get_name(self):  # 객체의 name 을 리턴하는 메소드
        return self.name

    def get_id(self):  # 객체의 id를 리턴하는 메소드
        return self.id


best = Student('John Doe', 20210934)
print(best.get_name(), end=', ')   # best 학생의 이름 출력
print(best.get_id())               # best 학생의 id 출력
honor = Student('Jane Doe', 20210980)
print(honor.get_name(), end=', ')  # honor 학생의 이름 출력
print(honor.get_id())              # honor 학생의 id 출력
print(best)
print(honor)

