#Kiểm tra mã bưu chính có hợp lệ hay không
#Mã bưu chính P thoả mãn các yêu cầu sau:
#P phải là một số trong khoảng từ 100000 đến 999999
#P phải không chứa hơn 1 chữ số lặp lại xen kẽ

regex_integer_in_range= r'^[1-9][0-9]{5}$'
regex_alternating_repetitive_pair= r'(?=(\d)\d\1)'

import re

P= input()
print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_pair, P))<2)
