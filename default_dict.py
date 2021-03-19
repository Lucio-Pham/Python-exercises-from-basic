#Bạn được cho trước 2 số tự nhiên m và n
#Có n chữ có thể bị lặp lại trong nhóm chữ A
#Có m chữ thuộc về nhóm chữ B 
#Người ta muốn kiểm tra xem m chữ này có đồng thời xuất hiện trong nhóm chữ A hay không
#Nếu có xuất hiện thì in ra vị trí và số lần xuất hiện
#Nếu không có xuất hiện thì in ra giá trị -1

from collections import defaultdict

d= defaultdict(list)
list_word= []
n, m = map(int, input().split())

for k in range (0, n): 
    d[input()].append(i+1)

for i in range (0, m): 
    list_word= list_word + [input()]

for v in list_word:
    if v in d:
        print(''.join(map(str, d[v])))
    else: 
        print('-1')