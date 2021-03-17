    #Một chuỗi s có độ dài n: s= c1c2c3...cn-1
    #Một số nguyên k với n chia hết cho k
    #Chia chuỗi s thành n/k nhóm nhỏ ti, 

    def merge_the_tools(string, k): 
        for part in zip(*[iter(string)]*k): 
            d= dict()
            print(''.join([d.setdefault(c,c) for c in part if c not in d]))

    if __name__=='__main__': 
        string, k = input(), int(input())
        merge_the_tools(string, k)