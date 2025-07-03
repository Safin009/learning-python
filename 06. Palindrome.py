# Write a program that can check whether a given string is palindrome or not.

##like abba: to solve check 1st and last character(n) then 2nd and (n-1) character and so on are they simillar or not

s=input("enter the string:")


flag= True
for i in range(0,len(s)//2):
  if s[i] != s[len(s)-(i+1)]:
    flag=False
    print("not a palindrome")
    break
if flag:
    print("palindrome") 
