import re

locations = input()
pattern = r'(=|/)([A-Z][A-Za-z]{2,})\1'
matches = re.finditer(pattern, locations)
destination = []
length = 0

for match in matches:
    destination.append(match.group(2))
    length += int(len(match.group(2)))
print(f"Destinations: {', '.join(destination)}")
print(f"Travel Points: {length}")
