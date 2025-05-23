# podwojna petla do tabliczki mnozenia
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
        
print()  #dla lepszej czytelnosci


# int nie dziala na decimal numbers
# float pozwalana decimal numbers - wiec float jest lepszy od int