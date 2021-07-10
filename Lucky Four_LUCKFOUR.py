# https://www.codechef.com/problems/LUCKFOUR

t = int(input())


for _ in range(t):
    count = 0
    
    n = input()
    for i in range(len(n)):
        if n[i] == "4":
            count += 1
    print(count)