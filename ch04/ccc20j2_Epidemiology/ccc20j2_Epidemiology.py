# https://dmoj.ca/problem/ccc20j2

'''
Disease Person infect (R) people only next day.
No Person is infected more than 1
We want total of more than (P) people have disease

INPUT:
    - (P) value
    - (N) Number of disease people on day 0
    - (R) value - infection rate

OUTPUT:
    - First day number on which the total number of disease people is > (P)
'''

infected_target = int(input())
infected        = int(input())
infection_rate  = int(input())
day             = 0
newly_infected  = infected

while infected <= infected_target:
    day = day + 1
    newly_infected = newly_infected * infection_rate
    infected = infected + newly_infected
    print(f"day: {day}\t infected: {infected}\t newly infected {newly_infected}")

print(day)

'''
D 0
i = 1
r = 5
ni = i

D 1
ni = ni * r = 1 * 5 = 5
i = i + ni = 1 + 5 = 6

D2
ni = ni * r = 5 * 5 = 25
i = i + ni = 6 + 25 = 31

'''
