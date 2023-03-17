correctans = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
openfile = open("Answers.txt", 'r')
studentans = []

for i in range(len(correctans)):
    a = (openfile.readline())
    studentans.append(a.strip("\n"))

correct_count = 0
wrong_count = 0

grade = ""
index = []

for a in range(len(correctans)):
    if(studentans[a] == correctans[a]):
        correct_count = correct_count + 1
    
    else:
        wrong_count = wrong_count + 1
        index.append(a)

if(correct_count >= 15):
    grade = "PASS"

else:
    grade = "FAIL"

print("Student Test Report")
print("Status: ", grade)
print("Answers Correct: ", correct_count)
print("Answers Wrong: ", wrong_count)   
print("Question No. of Wrong Answered Questions: ", *index)

