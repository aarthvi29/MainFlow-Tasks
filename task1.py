                                        #LIST
#add an element
my_list=[1,2,3]
my_list.append(6)
print("updated list(add an element)=",my_list)

#delete an element
my_list=[1,2,3]
my_list.remove(2)
print("updated list(delete an element)=",my_list)

#modify an element
my_list=[1,2,3]
my_list[1]=5
print("modified list=",my_list)


                                        #DICTIONARY             
#add an element
my_dis={"name":"aarthvi","age":"20"}
my_dis["city"]="moradabad"
print("updated dictionary",my_dis)

#delete an element
my_dis={"name":"aarthvi","age":"20"}
my_dis.pop("age")
print("updated dictionary",my_dis)

#modify an element
my_dis={"name":"aarthvi","age":"20","city":"noida"}
my_dis["city"]="moradabad"
print("modified dictionary",my_dis)


                                        #SET
#add an element
my_set={"apple","mango","watermelon"}
my_set.add("banana")
print("updated set",my_set)

#delete an element
my_set={"apple","mango","watermelon"}
my_set.remove("watermelon")
print("updated set",my_set)

#modify an element
my_set={"apple","mango","watermelon"}
my_set.discard("watermelon")
my_set.add("banana")
print("updated set",my_set)
