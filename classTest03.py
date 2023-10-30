class Father:
    def __init__(self, job):
        self.jobName = job

    age = 60 #클래스 변수
    name = "홍길동" #클래스 변수

    def test(self):
        testV = 100

father1 = Father("회사원")

print(father1.name)

father2 = Father("군인")

print(father2.name)

father1.name = "김유신"

father1.jobName = "비행사"

print(father1.name)
print(father2.name)
print(father1.jobName)
print(father2.jobName)

