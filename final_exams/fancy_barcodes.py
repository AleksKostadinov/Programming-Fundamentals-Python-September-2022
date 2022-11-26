import re

number_of_barcodes = int(input())
pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'

for barcode in range(number_of_barcodes):
    text = input()
    matches = re.search(pattern, text)
    number_pattern = r'(\d+)'
    if matches:
        number_matches = re.findall(number_pattern, matches.group())
        if number_matches:
            print(f"Product group: {''.join(number_matches)}")
        else:
            print('Product group: 00')
    else:
        print("Invalid barcode")
