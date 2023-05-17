# solution 1 for the interview question
import operator
import time
# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1
start = time.time()
my_list = [['poster', 99999990227], ['framed poster', 100], ['Whiteboard', 1360],['Canvas', 22227]]
print(max(my_list, key=lambda x: x[1]))
def search(arr, m, y):
    for j in range(0, m):
        if arr[j] == y:
            return j
    return -1

# Driver Code
X = ["Poster", "Framed Poster", 'whiteboard']
Y = ["canvas", "Framed Poster"]
Z = ["Canvas", "Poster"]
y = str(input("Enter the maximam product name:"))
m = len(X)
result = search(X, m, y)
if result == -1:
    print("X print house  doesnot produces it")
else:
    print("X print house produces it")
m = len(Y)
result1 = search(Y, m, y)
if result1 == -1:
    print("Y print house  doesnot produces it")
else:
    print("Y print house produces it")
m = len(Z)
result2 = search(Z, m, y)
if result2 == -1:
    print("Z print house  doesnot produces it")
else:
    print("Z print house produces it")
end= time.time()
print( end-start )

