#công ty X có khoảng 100 công nhân
#Công ty muốn tạo mã số định danh (UID) cho nhân viên
#Một mã định danh phải thoả mãn các yêu cầu sau: 
#Phải chứa ít nhất 2 chữ cái alphabet viết hoa
#phải chứa ít nhất 3 chữ số từ 0-9
#chỉ có thể chứa các kí tự chữ số và chữ cái, viết thường hoặc viết hoa [0-9], [a-z], [A-Z]
#không có kí tự nào được lặp lại 
#phải có chính xác 10 kí tự trong một mã số định danh hợp lệ

import re
for i in range (int(input())): 
    N= input().strip()
    if N.isalnum() and len(N) ==10: 
        if bool(re.search(r'(.*[A-Z]){2,}', N) and bool(re.search(r'(.*[0-9]){3,}', N)): 
            if re.search(r'.*(.).*\1+.*', N): 
                print('Invalid')
            else: 
                print('Valid')
        else: 
            print('Invalid')
    else: 
        print('Invalid') 