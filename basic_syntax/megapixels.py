width = int(input())
height = int(input())

megapixels = (width * height) / 1000000
integer_megapixels = (width * height) % 1000000
if integer_megapixels != 0:
    print(f'{width}x{height} => {megapixels:.1f}MP')
else:
    print(f'{width}x{height} => {int(megapixels)}MP')