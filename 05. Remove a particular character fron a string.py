# write a program which can remove a particular character from a string

s=input("enter the string :")
term=input("what would like to remove from string:")

result = " "

for i in s:
  if i !=term:
    result=result + i
print(result)    
