
# Challenge-1: Creating the question class

class Question:

    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer

new_q=Question("How are you?","I am fine")
print(new_q.text,new_q.answer)

