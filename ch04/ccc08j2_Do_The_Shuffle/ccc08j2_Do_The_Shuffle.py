# https://dmoj.ca/problem/ccc08j2
'''
playlist = [A, B, C, D, E]
4 buttons:
    - 1: move first song to the end of playlist
        [A, B, C, D, E] -> [B, C, D, E, A]
    - 2: move last song to the start
        [A, B, C, D, E] -> [E, A, B, C, D]
    - 3: swap the first two songs of the playlist
        [A, B, C, D, E] -> [B, A, C, D, E]
    - 4: just play the songs

INPUT:
    - b - button number that use press (1 <= b <= 4)
    - n - number of times pressed (1 <= n <= 10)

OUTPUT:
    When last button 4 is pressed we should display the playlist:
    B C D A E
'''

playlist = 'ABCDE'
button = 0

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

print(' '.join(playlist))
