l=[2,3,5,6,10,34,12]
search = int(input("Enter the element:"))

for i in range(len(l)):
    if l[i]==search:
        print(f"{search} is found at index-{i}")
        break
else:
    print(f'{search}is not found')