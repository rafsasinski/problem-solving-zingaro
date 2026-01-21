'''
The C3MPlaya

5 songs ABCDE

4 Buttons
 b1: first song to end of playlist
 b2: last song to the beginning of playlist
 b3: swapp two first songs
 b4: play the playlist - end of program

INPUT:
Always comes in two line pairs
    b - button number
        1 <= b <= 4
    n - number of presses
        1 <= n <= 10
'''

playlist = 'ABCDE'
button = 0
presses = 0

while button != 4:
    button = int(input())
    presses = int(input())

    for i in range(presses):

        if button == 1:
            playlist = playlist[1:] + playlist[0]
        elif button == 2:
            playlist = playlist[-1] + playlist[0:-1]
        elif button == 3:
            playlist = playlist[1] + playlist[0] + playlist[2:]

print(" ".join(playlist))
