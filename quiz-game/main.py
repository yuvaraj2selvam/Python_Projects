from data import question_data
from question_model import question 
from quiz_brain import quizbrain

question_bank=[]

for x in question_data:
	question_bank.append(question(x["text"],x["answer"]))

obj=quizbrain(question_bank)

n=len(question_bank)

while n:
	obj.next_question()
	n=n-1