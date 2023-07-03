# Qestion

class question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def chekAnswer(self, answer):
        return self.answer == answer

#Quiz
class quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionindex = 0  

    def getQuestion(self):
        return self.questions[self.questionindex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"soru {self.questionindex + 1}: {question.text}")

        for q in question.choices:
            print("-"+ q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.chekAnswer(answer):
            self.score += 1
        self.questionindex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionindex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("score: ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionindex + 1

        if questionNumber > totalQuestion:
            print("quiz bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))

q1 = question("en iyi programlama dili hangisidir?", ['C#','python','javascript','java'], 'python')
q2 = question("en popüler programlama dili hangisidir?", ['python','javascript','C#','java'], 'python')
q3 = question("en kazandıran programlama dili hangisidir?", ['C#','javascript','java','python'], 'python')
questions = [q1,q2,q3]

quiz = quiz(questions)

quiz.loadQuestion()







