#Cửa hàng giày muốn tính toán doanh thu cho từng đôi giày bán ra
#Chủ cửa hàng có danh sách kích cỡ các đôi giày trong shop
#Gọi X là số đôi giày trong shop
#Gọi N là số khách hàng bỏ ra x đồng mua 1 đôi giày có kích cỡ cụ thể 
#Tính doanh thu mà cửa hàng thu được 

import collections

#Nhập số đôi giày có trong shop
num_Shoes = int(input()) 
#Danh sách các kích cỡ giày có trong shop
shoes = collections.Counter(map(int, input().split()))
#số lượng khách hàng đến mua
num_Cust = int(input())

income = 0

for i in range(num_Cust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print (income)