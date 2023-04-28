"""
####isalpha()-> Method is used to check whether all characters in the String is an alphabet.
Syntax:  string.isalpha()
Parameters: isalpha() does not take any parameters

Errors and Exceptions:

It contains no arguments, therefore an error occurs if a parameter is passed
Both uppercase and lowercase alphabets return “True”
Space is not considered to be the alphabet, therefore it returns “False”
"""
# checking for alphabets
str = "HelloPUNNA"
string="welcome"
n="1224"
m="Kusa@143"
a= "$*%!!!"
s = 'python-123'
print(str.isalpha() ,string.isalpha() ,n.isalpha() ,m.isalpha() ,a.isalpha() ,s.isalpha())
print(m[0:4].isalpha())
print()
# checking if space is an alphabet
mystr="Hello Kusa kumar"
print(mystr.isalpha())

### Count the number of alphabets in the string by string methods
string="kusa kumar punnana"
count=0
for a in string:
    if (a.isalpha()) == True:
        count+=1
print(count)
"""
##isdecimal()
isdecimal() function returns true if all characters in a string are decimal, else it returns False
Syntax: string_name.isdecimal()
Parameters:This method does not takes any parameters .
Return: boolean value. True – all characters are decimal, False – one or more than one character is not decimal.
"""
print()
print("isdecimal() Method:")
p="123 678 "
print(str.isdecimal() ,string.isdecimal() ,n.isdecimal() ,m.isdecimal() ,a.isdecimal() ,s.isdecimal())
print(m[5:7].isdecimal())
print()
print(p.isdecimal())
print("1.43".isdecimal())
print()

### difference between isdigit and is decimal and isnumeric
"""
By definition, isdecimal() ⊆ isdigit() ⊆ isnumeric() . That is, if a string is decimal , then it'll also be digit and numeric
isnumeric()-> all the characters in the string must be numeric, and the - and the . are not.
isdecimal() method supports only Decimal Numbers. 
isdigit() method supports Decimals, Subscripts, Superscripts. 
isnumeric() method supports Digits(0-90, Vulgar Fractions, Subscripts, Superscripts, Roman Numerals, Currency Numerators.
"""
c="_user_123"
k='   kk'
d='0123'  #base10 values
e= 'ↁ' # Roman numbers
f=	'⅔' #Uni code fraction part for numeric is true, fractional part retun false
g='2²'  #fractions and Superscripts

print(c.isdecimal() ,c.isdigit() ,c.isnumeric())
print(k.isdecimal() ,k.isdigit() ,k.isnumeric())
print(d.isdecimal() ,d.isdigit() ,d.isnumeric())
print(e.isdecimal() ,e.isdigit() ,e.isnumeric())
print(f.isdecimal() ,f.isdigit() ,f.isnumeric())
print(g.isdecimal() ,g.isdigit() ,g.isnumeric())

"""
##islower() -> islower() method checks if all characters in the string are lowercase. 
This method returns True if all alphabets in a string are lowercase alphabets. 
If the string contains at least one uppercase alphabet, it returns False.
Syntax:  string.islower()
Returns:True: If all the letters in the string are in lower case and
        False: If even one of them is in upper case
        
##isupper ->
Syntax: string.isupper()
Returns:    True if all the letters in the string are in the upper case and 
            False if even one of them is in the lower case. 
"""
x="KUSAKUMAR"
y='kusakumarPUNNANA'
z= "KusaKumar123_@#$"
r="_user_123"
q=" KUSA iS GOOD HUMUN BEING"
print()
print("Method of isupper and islower:")
print(x.isupper() , x.islower())
print(y.isupper() , y.islower())
print(z.isupper() , z.islower())
print(r.isupper() , r.islower())
print(q.isupper() , q.islower())  # spaces are present return false
"""
##isalnum() ->Method checks whether all the characters in a given string are either alphabet or numeric (alphanumeric) characters.

Syntax:  string_name.isalnum() 
Parameter:  isalnum() method takes no parameters 
"""
print()
string = "abc123"
print(string.isalnum())
print()
string = "abc 123"
print(string, "is alphanumeric?", string.isalnum())
string = "abc_123"
print(string, "is alphanumeric?", string.isalnum())
string = "kus123*"
print(string, "is alphanumeric?", string.isalnum())
string = "aaaa"
print(string, "is alphanumeric?", string.isalnum())