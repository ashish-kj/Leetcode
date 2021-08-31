n = int(input())

def isBadVersion(m):
    if(m >= 8):
        return True
    else:
        return False

f = 0
l = n - 1

while(f<=l):
    m = (f+l)//2
    if(isBadVersion(m)):
        l = m - 1
    else:
        f = m + 1
print(f)