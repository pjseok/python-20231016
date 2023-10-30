class Score:
    a = 100

    def __init__(self, kor, eng, math, sci):#생성자(초기화자)-객체가 생성될 때 자동으로 호출되는 메서드
        print("안녕하세요 저는 생성자입니다!!!!")
        print("변수 초기화를 시작합니다!!")
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sci = sci

    def test(self):
        self.a

    def aver(self):
        ave = (self.kor + self.eng + self.math + self.sci) / 4
        return ave

    def sum(self):
        sum = self.kor + self.eng + self.math + self.sci
        return sum

sc1 = Score(60, 100, 70, 20)

averScore = sc1.aver()
sumScore = sc1.sum()

print(averScore)
print(sumScore)

class ScorePlus(Score):

    def maxScore(self):
        maxScore = max(self.kor, self.sci, self.eng, self.math)
        return maxScore

sp1 = ScorePlus(1,2,3,4)
print(sp1.aver())
print(sp1.maxScore()) # maxScore메서드가 추가됨
