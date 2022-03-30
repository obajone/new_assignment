# ASSIGNMENT 
from array import array


array1 = [["names", "Eng", "Math", "chemistry"], 
["jude", 70, 90, 80],
 ["kate", 50, 60, 90], 
 ["caleb", 90, 77, 70]]

class student:
  def __init__(self, student, array, subject):
    self.student = student 
    self.array = array
    self.subject = subject 
    
  def student_average(self):
    score_new = []
    for score in self.array:
      if self.student in score:
        score_new = score[1:]
    b = 0
    for n in score_new:
      b += n
    average = round(b/len(score_new),2)
    return average

  def subject_average(self):
    array2 = []
    for k in range(0, len(self.array)):
      y = []
      for m in self.array:
        y.append(m[k])
      array2.append(y)
    for i in array2:
      if self.subject in i:
        scores = i[1:]
    total = 0
    for p in scores:
      total += p
    average = round(total/len(scores), 2)
    return average

student_1 = student("kate", array1, "Eng")
e = student_1.student_average()
d = student_1.subject_average()
print(f'Average score of the student is {e}')
print(f'Average score of the subject is {d}')
