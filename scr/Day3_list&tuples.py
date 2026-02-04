car_details = ["BMW",2500000,2]#car name,price,years
print(car_details)

#tuple
coordinates=(12,3,22.3)
print(coordinates)

#list
fruit_list=("apple","banana","mango")
print(fruit_list[2])
print(type(fruit_list[2]))
#Append
fruit_list=["apple","banana","mango"]
fruit_list.append("kiwi")
print(fruit_list)
print(type(fruit_list[3]))



fruit_list=["apple","banana","mango"]
print(fruit_list[2])



#task1
#Create a list named inventory 

inventory_list=["Apples", "Bananas", "Carrots", "Dates"]
print(inventory_list)

#Append(Eggs)

inventory_list.append("Eggs")
print(inventory_list)

#Remove(Bananas bcoz it sold out)

inventory_list.remove("Bananas")
print(inventory_list)

#organize the inventory alpabets using Sort

inventory_list.sort()
print("final updated inventory:",inventory_list)




#task2
#Create a list named temperatures
Temperature=[22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
Temperature[0]
Temperature[-1]

Afternoon_peak=Temperature[3:6]
print(Afternoon_peak)
last_3_hours=Temperature[-3:]
print(last_3_hours)

print(Temperature)
print(Temperature[0],Temperature[-1])
print(Afternoon_peak)
print(last_3_hours)



#task3
screen_res=(1920, 1080)
print("Current Resolution: 1920x1080")
print(screen_res)
screen_res[0]=1280
print("Tuples cannot be modified")

