X = input().split()
Y, Z, P = X[0], X[1], X[2]


suffix = ""
min_length = min(len(Y), len(Z), len(P))

for i in range(1, min_length + 1):
    if Y[-i] == Z[-i] == P[-i]: 
        suffix = Y[-i] + suffix
    else:
        break

print("Longest common suffix:", suffix)
