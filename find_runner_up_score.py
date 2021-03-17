#cho một danh sách n sinh viên gồm tên và điểm số
#tìm ra sinh viên có số điểm cao thứ 2
n= int(input())
arr= list(map(int, input().split()))
z = max(arr) 

i=0 
while (i<n): 
    if z ==max(arr): 
        arr.remove(max(arr))
    i+=1
print(max(arr))

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())