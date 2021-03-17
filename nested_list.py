#Tìm sinh viên có điểm trung bình cao thứ 2 trong danh sách
#nếu có nhiều hơn 2 sinh viên có số điểm trung bình cao thứ hai
#thì sắp xếp sinh viên theo tên, thứ tự alphabet

marksheet= [] #danh sach bang diem
score_list=[] #danh sach diem 
if __name__ == '__main__': 
    for _ in range (int(input())): 
        name= input()
        score= float(input()) 
        marksheet += [[name, score]]
        score_list += [score]
    b= sorted(list(set(score_list)))[1]
    for a,c in sorted(marksheet):
        if c==b: 
            print(a) 
            