# ASSIGNMENT 
array1 = [["names", "Eng", "Math", "chemistry"], ["jude", 70, 90, 80], ["kate", 50, 60, 90], ["caleb", 90, 77, 70]]

def student_average(array, student):
  a = []
  for i in array:
    if student in i:
      a = i[1:]
  b = 0
  for n in a:
    b += n
  average = round(b/len(a),2)
  return average

def subject_average(array, subject):
  array2 = []
  for k in range(0, len(array)):
    y = []
    for m in array:
      y.append(m[k])
    array2.append(y)
  for i in array2:
    if subject in i:
      scores = i[1:]
  total = 0
  for p in scores:
    total += p
  average = round(total/len(scores), 2)
  return average

e = student_average(array1, "caleb")
d = subject_average(array1, "chemistry")
print(f'Average score of the student {e}')
print(f'Average score of the subject is {d}')
