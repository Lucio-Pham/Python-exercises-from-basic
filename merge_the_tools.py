    #Một chuỗi s có độ dài n: s= c1c2c3...cn-1
    #Một số nguyên k với n chia hết cho k
    #Chia chuỗi s thành n/k nhóm nhỏ ti, với các chữ cái đứng liền kề nhau trong chuỗi s
    #sau đó dùng chuỗi nhỏ ti để tạo ra các chuỗi ui sao cho:
    #các kí tự trong ui là các chữ cái liên tiếp trong ti 
    #không có các kí tự lặp lại trong chuỗi phụ ui. nếu chuỗi ui có kí tự lặp lại thì sẽ bị xoá và không được công nhận
    #ví dụ chuỗi s= 'AAABCADDE'
    #k=3
    #Đầu ra sẽ là: AB CA AD
    
    def merge_the_tools(string, k): 
        for part in zip(*[iter(string)]*k): 
            d= dict()
            print(''.join([d.setdefault(c,c) for c in part if c not in d]))

    if __name__=='__main__': 
        string, k = input(), int(input())
        merge_the_tools(string, k)
