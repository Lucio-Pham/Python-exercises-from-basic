#trang trí hoạ tiết thảm 
#yêu cầu: thảm trang trí kích thước n*m 
#n là số tự nhiên lẻ. m gấp 3 lần n. 
#mẫu thiết kế phải có chữ WELCOME ở giữa
#các hoạ tiết còn lại được vẽ bằng dấu | , .  và - 
#  Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
#   Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

import string 

def print_rangoli(size): 
    alpha= string.ascii_lowercase
    l=[]
    for i in range (n):
        s= '-'.join(alpha[i:n]) 
        l.append((s[::-1] + s[1:]).center(4*n-3, '-'))
    print('\n'.join(l[:0:-1]+l))

if __name__=="__main__": 
    n= int(input())
    print_rangoli(n) 

n, m = map(int,input().split())
pattern_draw = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern_draw + ['WELCOME'.center(m, '-')] + pattern_draw[::-1]))