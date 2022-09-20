bpm = int(input())
beats = int(input())

seconds = 60 / (bpm / beats)
m = int(seconds // 60)
s = int(seconds % 60)

num_bars = beats // 4
if beats % 4 != 0:
    num_bars = beats / 4
    print(f'{num_bars:.1f} bars - {m}m {s}s')
else:
    print(f'{num_bars} bars - {m}m {s}s')