
def nums(num):
    if num < 10:
        if num == 1:
            return "₁"
        elif num == 2:
            return "₂"
        elif num == 3:
            return "₃"
        elif num == 4:
            return "₄"
        elif num == 5:
            return "₅"
        elif num == 6:
            return "₆"
        elif num == 7:
            return "₇"
        elif num == 8:
            return "₈"
        elif num == 9:
            return "₉"
    else:
        return "n"

def myround(num):
    return round(num, 3)


A = [
     [0.00, 0.08, -0.23, 0.32],
     [0.16, -0.23, 0.18, 0.16],
     [0.15, 0.12, 0.32, -0.18],
     [0.25, 0.21, -0.16, 0.03]]
B = [1.34, -2.33, 0.34, 0.63]
e = 0.001
X = [B.copy(), [0,0,0,0]]
X1 = B.copy()
c = 1
while (e < abs(X[0][0] - X[1][0]) or e < abs(X[0][1] - X[1][1]) or e < abs(X[0][2] - X[1][2]) or e < abs(X[0][3] - X[1][3])):
    print("Итерация - ", c)
    for i in range(len(X[0])):
        sum = 0
        for j in range(len(A)):
            sum += A[i][j] * X1[j]
        sum += B[i]
        X1[i] = sum
    X[1] = X[0].copy()
    X[0] = X1.copy()
    for i in range(len(X[1])):
        print(f"X{nums(i+1)} = {myround(X[1][i])}")
    print()
    c += 1

print("Итерация - ", c)

for i in range(len(X[1])):
    print(f"X{nums(i+1)} = {myround(X[1][i])}")