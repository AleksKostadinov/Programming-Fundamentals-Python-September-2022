old_version = input()
new_version = (int(old_version.replace('.', ''))) + 1
# print('.'.join(str(new_version)))
print(*(str(new_version)), sep=".")
