elements = input().split()
products = input().split()
store = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    store[key] = int(value)

for product in products:
    if product in store:
        print(f'We have {store[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
