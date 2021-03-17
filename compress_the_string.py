#Nhập vào 1 chuỗi các chữ số hoặc chữ cái
#In ra màn hình dạng tuple với số lần xuất hiện của từng phần tử khác nhau trong chuỗi
from itertools import groupby
'''
for k, s in groupby(input()):
    print (*[" ".join(2) (len(list(s)), int(k))])
'''
print(*[(len(list(s)), int(k)) for k, s in groupby(input())])