#input values
n = int(input())

#random no return function for testing

def isBadVersion(m):
    if(m >= 8):
        return True
    else:
        return False

#binary search algo

f = 0
l = n - 1

while(f<=l):
    m = (f+l)//2
    if(isBadVersion(m)):
        l = m - 1
    else:
        f = m + 1
print(f)