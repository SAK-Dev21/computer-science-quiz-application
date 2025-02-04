import File_B
import random

Waffle_questions = File_B.Topic1.FODR_EasyQuestions + File_B.Topic1.FODR_MediumQuestions + File_B.Topic1.FODR_HardQuestions + File_B.Topic1.FODR_TryhardQuestions

print(f"\n {Waffle_questions} ")

random.shuffle(Waffle_questions)

print(f"\n {Waffle_questions}")