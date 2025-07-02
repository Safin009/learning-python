#Extract username from a given email.
#Eg if the email is safin.221635@s.pust.ac.bd
#then the username shuld be safin.221635

s=input("enter the email: ")
pos=s.index("@")   #find out the position of (@) and store it in a variable
print(s[0:pos])    #slicing from starting to the position and display
