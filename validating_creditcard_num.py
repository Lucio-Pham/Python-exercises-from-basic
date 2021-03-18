#bạn được cấp một mã số thẻ tín dụng N. bạn phải kiểm tra xem số thẻ tín dụng có hợp lệ hay không
#Số thẻ tín dụng phải thoả mãn các điều kiện sau: 
#Chuỗi số phải bắt đầu bằng 4, 5 hoặc 6
#Chuỗi số chỉ bao gồm 16 chữ số
#Chuỗi số chỉ tạo thành bởi các chữ số từ 0-9
#Chuỗi số được phân tách thành các nhóm 4 chữ số, phân cách nhau bằng dấu "-"
#Không được chứa các kí tự đặc biệt như ''(kí tự trống), _ , etc.
#Không được chứa 4 chữ số giống nhau liên tiếp 
#ví dụ: 42536258796157867 ---->  có 17 chữ số→ Invalid 
#4444424442444   ---->   Có chứa các chữ số giống nhau lặp lại liên tiếp quá 4 lần → Invalid
#5122-2368-7954 - 3214   ----> có chứa kí tự đặc biệt → Invalid
#44244x4424442444   ----> có chứa kí tự không phải là chữ số → Invalid
#0525362587961578    ----> không bắt đầu bằng các chữ số 4, 5 và 6 → Invalid

import re
card_number= re.compile (
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$"
)

for _ in range (int(input().strip())):
    print("valid" if card_number.search(input().strip()) else "Invalid") 