# https://dmoj.ca/problem/coci08c1p2
'''
INPUT
    - Number of questions N (1<=N<=100
    - String of N letters containing answers
'''

adrian_sequence  = "ABC"
adrian_score    = 0
bruno_sequence  = "BABC"
bruno_score     = 0
goran_sequence  = "CCAABB"
goran_score     = 0

questions = int(input())
exam = input()

for i in range(questions):
    answer = exam[i]
    
    if answer == adrian_sequence[i%len(adrian_sequence)]:
        adrian_score = adrian_score + 1

    if answer == bruno_sequence[i%len(bruno_sequence)]:
        bruno_score = bruno_score + 1

    if answer == goran_sequence[i%len(goran_sequence)]:
        goran_score = goran_score + 1


max_score = max(adrian_score, bruno_score, goran_score)

print(max_score)

if adrian_score == max_score:
    print('Adrian')

if bruno_score == max_score:
    print('Bruno')

if goran_score == max_score:
    print('Goran')
