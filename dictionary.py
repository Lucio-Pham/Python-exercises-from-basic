#đảo ngược dictionary 
#đảo vị trí key:value cho nhau 
my_dict= { "name": "Lucio", "car":"Lamborghini", "pet":"Mo", "book": "War&Peace"}
my_inverted_dict = dict(map(reversed, my_dict.items()))
print ("original dictionary", my_dict)
print ("inverted dictionary", my_inverted_dict)

#cách khác để đảo vị trí key:value trong dict 
my_inverted_dict_2= {value:key for key, value in my_dict.items()} 
print ("other way to create inverted dict",my_inverted_dict_2)

#chuyển đổi 2 list vào 1 dictionary (gộp 2 list thành 1 dict) 
list_1= ["name", "car", "pet", "book"] 
list_2= ["Lucio", "Lamborghini", "Mo", "War&Peace"]

combine_dict = dict (zip(list_1, list_2)) #list đặt trước là key, đặt sau là value
print ("gộp 2 list thành 1 dict", combine_dict)

#cách khác để gộp 2 list thành 1 dictionary
combine_list = {key:value for key, value in zip(list_1, list_2)}
print ("cách khác gộp 2 list thành 1 dict\n", combine_list)

#sắp xếp 1 list các dictionary
csv_mapping_list= [ {'name': 'Lucio', 'car': 'Lamborghini', 'pet': 'Mo'},
                    {'name': 'Anna', 'car': 'Ferrari', 'pet': 'Jini'},
                    {'name': 'Kevin', 'car': 'Nissan GTR', 'pet': 'Klivan'},
                    {'name': 'Maximilian', 'car': 'Audi', 'pet':'Mitt'}] 
size= len (csv_mapping_list)
for i in range (size):
  min_index =i 
  for j in range (i+1, size): 
    if csv_mapping_list [min_index]['name']>csv_mapping_list[j]['name']: 
      min_index=j
      csv_mapping_list[i], csv_mapping_list[min_index] = csv_mapping_list[ min_index], csv_mapping_list[i]
      
#gộp 2 dictionary 
dict_1= {'name': 'Lucio', 'car': 'Lamborghini', 'pet': 'Mo'}
dict_2= {'name': 'Anna', 'car': 'Ferrari', 'pet': 'Jini'}
powers= dict()

for dict in (dict_1, dict_2): 
    for key, value in dict.items(): 
        powers[key]= value
        print("Gộp dictionary\n", powers)
#cách khác để gộp dictionary---dictionary comprehension
powers = {key:value for d in (dict_1, dict_2) for key, val in d.items()}
print ("cách khác để gộp dictionary\n", powers) 
