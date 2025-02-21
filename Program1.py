#Write a program to count the number of alphabets and number of digits in the string 'Nagpur-440010'

s = "Nagpur-440010"
s = s.split('-')
print(len(s[0]),len(s[1]))
print(type(s))