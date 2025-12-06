# https://dmoj.ca/problem/ccc11s2

student_responses = int(input())
answers = []
correct = 0

for i in range(student_responses*2):
    answers.append(input())
    if (i >= student_responses):
        if answers[i-student_responses] == answers[i]:
            correct = correct + 1

print(correct)
