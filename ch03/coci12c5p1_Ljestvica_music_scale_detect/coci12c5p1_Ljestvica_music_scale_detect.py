# https://dmoj.ca/problem/coci12c5p1_Ljestvica_music_scale_detect

measures = input()
measures = measures.split("|")

main_tones_a_minor = ("A", "D", "E")
main_tones_c_major = ("C", "F", "G")

a_minor_count = 0
c_major_count = 0

for measure in measures:
    note = measure[0]

    if note in main_tones_a_minor:
        a_minor_count = a_minor_count + 1

    if note in main_tones_c_major:
        c_major_count = c_major_count + 1


if a_minor_count == c_major_count:
    if measures[-1][-1] == 'A':
        a_minor_count = a_minor_count + 1
    else:
        c_major_count = c_major_count + 1

if a_minor_count > c_major_count:
    print("A-mol")
else:
    print("C-dur")


'''
CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GA|GF|EC|CG|C|CG|AF|EG|AC|DF|EG|C
CD|EC|CD|EC|EF|G|EF|G|GAGF|GA|GF|EC|CG|C|CG|AF|EG|AC|DF|EG|CD|A

TEST CASES
AEB|C
CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GAGF|EC|CG|C|CG|C
EFDCDF|GDA
'''
