number = int(input())
day = int(input())
month = int(input())
year = int(input())
hours = int(input())
minutes = int(input())
size_bytes = int(input())
width = int(input())
height = int(input())
orientation = ''

if size_bytes >= 1000000:
    mb_bytes = size_bytes / 1000000
    if size_bytes % 1000000 == 0:
        size_bytes = f'{int(mb_bytes)}MB'
    else:
        size_bytes = f'{mb_bytes}MB'
elif size_bytes >= 1000:
    kb_bytes = size_bytes / 1000
    size_bytes = f'{int(kb_bytes)}KB'
elif size_bytes < 1000:
    size_bytes = f'{int(size_bytes)}B'

if width == height:
    orientation = 'square'
elif width > height:
    orientation = 'landscape'
else:
    orientation = 'portrait'

print(f'Name: DSC_{number:04d}.jpg')
print(f'Date Taken: {day:02d}/{month:02d}/{year} {hours:02d}:{minutes:02d}')
print(f'Size: {size_bytes}')
print(f'Resolution: {width}x{height} ({orientation})')
