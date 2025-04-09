def get_first_element(lst):
    print(lst[0])  # list ka pehla element print hoga

# Neeche wala code user se input lega
n = int(input("Kitne elements chahiye list mein? "))
lst = []
for i in range(n):
    element = input(f"Element #{i + 1}: ")
    lst.append(element)

get_first_element(lst)
