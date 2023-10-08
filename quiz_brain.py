

class quizbrain:

	def __init__(self,questions):
		self.question_no=0
		self.question_list=questions
		self.score=0

	def next_question(self):
		currq=self.question_list[self.question_no]
		self.question_no+=1
		ans=input(f"Q{self.question_no} {currq.text} (True/False) :")
		if ans==currq.answer:
			self.score+=1
			print("Yes,you are right !!")
		else:
			print(f"Sorry,answer is {currq.answer}")
		print(f"your score is {self.score}/{self.question_no}\n")		


