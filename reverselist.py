# Reverse a list using slicig operator
lst=[1,2,3,6,7,9]
rvslst=lst[::-1]
print ("Lst ", lst)
print ("Reverse Lst ", rvslst)

#Reverse a string using slicing operator 
str1="brindasahoo"
revstr1=str1[::-1]
print ("Reverse of " + str1 + " is " + revstr1)

#Reverse a string using for loop
str2="sahoobrinda"
revstr2=""
for elem in str2:
	revstr2 = elem+revstr2
print ("Reverse of " + str2 + " is " + revstr2)

#Reverse words in a sentense using spilt opertor
str3="Hi  name How are You "
words=str3.split(" ")
output=words[-1::-1]
str4=" " .join(output)
print ("Reverse of  [" + str3 + "] is [" + str4 +"]")
