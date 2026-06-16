setx = {"pizza", "waffle"}
sety = {"pizza", "alfredo pasta"}
print("Original ste elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.symmetric_difference(sety)
print(setz)
seta = sety.difference(setx)
print(seta)
