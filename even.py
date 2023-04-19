# for i in range(2,101,2):
#     print(i)

# num = int(input("enter how many times"))
# for i in range(num):
#     print(f"My name is hello world {i}")

count=0
a = float(input("a= "))
r = float(input("r= "))
n = int(input("n= "))

for i in range(n):
    count = count + (a*(r**i))

print(f"Output: {count}")
