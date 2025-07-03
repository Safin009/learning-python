#  write a python program to convert a string to title case without using the title()

#string - spilt by a loop - converting -append into list
s= input("enter the string:")

L=[]

for i in s.split():
 L.append(i[0].upper()+ i[1:].lower())  #converting 1st letter into upper letter 
                                      # and 2nd to last converting lower letter
                                      #append into a list and store then into a new empty variable {L}  
print(L)
