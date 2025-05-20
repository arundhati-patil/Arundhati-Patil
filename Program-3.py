a = int(input("Enter a number: "))
if a % 2 == 0:
    a -= 1  # for even input, reduce by 1

odd_list = [i for i in range(1, 2*a, 2)]
print(odd_list)
