print("Please enter a positive integer: ")
N = int(input())
numlist = []
for i in range(0, N):
    print("Please enter an integer: ")
    numlist.append(input())
def ask():
    print("Please enter an integer: ")
    X = input()
    if X in numlist:
        indx = numlist.index(X)
        print(indx+1)
    else:
        print(-1)
ask()