city_names = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "New Orleans"]
resturaunts = ["Chipotle", "McDonalds", "Popeyes", "WingStop", "Starbucks", "Taco Bell", "Subway", "Chick-fil-A"]
resturaunts[5] = "In-N-Out"

#print (resturaunts[1])

#list slicing
three_cities = city_names [0:3]
#print (three_cities)
four_resturaunts = resturaunts [0:4]
#print (four_resturaunts)

#change
city_names [0] = "San Francisco"
city_names [2] = "Brooklyn" 
city_names [7] = "Hollywood" 
city_names [5] = "Tampa"

#add
city_names.append("New Jersey")
city_names.extend(["Santa Cruz", "Selma", "Chicago"])
city_names.insert(7, "Washington, D.C.")
#print (city_names)

#delete
del city_names [0]
city_names.pop (4)
city_names.remove ("Chicago")
#print (city_names)

#function
def printlist (list):
    counter = 0
    while counter < len(list):
        print (list[counter])
        counter +=1
    return "completed"

#printlist (city_names)

#function 2
def organize_list(list1):
    for index in range(len(list1)-1):
        if list1[index] >= list1[index + 1]:
            continue
        else:
            x = list1[index]
            list1.pop(index)
            list1.append(x)
    return list1
    return "done"

print (city_names)
newlist = organize_list(city_names)
print (newlist)