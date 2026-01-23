# https://dmoj.ca/problem/ecoo17r1p1
'''
13:35:00
14:30:00
Y1  12
Y2  10
Y3  7
Y4  5

0.5 Running the brunch
0.5 Trip

INPUT:
    cost - Cost of the trip (integer)
    Y1, Y2, Y3, Y4 - precentages of total number of students (float)
    N - Totalnumber of students (integer)

THE CATCH!!
1.8 people is the same as i person
Any missing or extra people should be removed from or added to
the group with the highest percentage
'''

YEAR_CHARGE = [12, 10, 7, 5]

for dataset in range(10):
    trip_cost               = int(input())
    attendance_percentages  = [float(data) for data in input().split(" ")]
    total_students          = int(input())

    attendees = []
    for percentage in attendance_percentages:
        attendees.append(int(percentage * total_students))

    # Missing (+int) or Extra (-int) person
    missing = total_students - sum(attendees)
    if missing > 0:
        most_attendees = max(attendees)
        index_most = attendees.index(most_attendees)
        attendees[index_most] += missing

    total_proceeds = 0
    for i in range(len(attendees)):
        total_proceeds += (attendees[i] * YEAR_CHARGE[i])

    if (trip_cost <= (int(total_proceeds/2))):
        print("NO")
    else:
        print("YES")

