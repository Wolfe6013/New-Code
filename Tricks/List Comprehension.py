people: list[str] = ['James','Charlotte','Stephany','Mario','Sandra']

# long_names: list[str] = []
# for person in people:
#     if len(person) > 7:
#         long_names.append(person)
# print(f'{long_names = }')

long_names: list[str] = [p for p in people if len(p) > 7]
print(f'{long_names = }')