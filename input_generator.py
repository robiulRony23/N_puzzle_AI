from random import randint
import math
file = open("in.txt","w")

# n = int(input("Ender value for n:"))

n=8
st=set()
file.write(str(n)+"\n")
print(n)
row = round(math.sqrt(n+1))
for i in range(row):
    for j in range(row):
        while True:
            val = randint(0,n)
            if val not in st:
                st.add(val)
                file.write(str(val)+" ")
                print(str(val),end=" ")
                break
    file.write("\n")
    print("")
file.close()