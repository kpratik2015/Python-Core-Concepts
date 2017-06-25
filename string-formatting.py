str1 = "Some text"
str2 = " Some other text"
concatenate_str = "Concatenation: " + str1 + str2
print(concatenate_str)

format_str = "firs the tab \t then the new line \nthis format takes effect only after using in \'print\' \
inline break which isn't \"line break\" ".lower()

cap_str = "\ncapitalized".upper()

print(format_str)

print(cap_str)

print("-----------------")

some_text = "Splitting to get words, or with comma"

print(some_text.split())

print(some_text.split(","))

print("Length of some_text: " + str(len(some_text)))

print("\n-----------------")

print("SUBSTITUTION\n")

subst_text = "With {variable} substitution.".format(variable="variable") 
print(subst_text)

subst_text = "With {0} {1}.".format("positional", "substitution") 
print(subst_text)

subst_text = "With %%s %s." %("substitution")
print(subst_text)

subst_text = "n decimal place float substitution where n=2 here: %.2f" %(20.196343)
print(subst_text)

print("\n-----------------")

print("DATE TIME\n")

import datetime

today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)

text = today.strftime("%d/%m/%y")
print(text)

now = datetime.datetime.utcnow() #utc time
text = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(text)

now = datetime.datetime.now() #local time
date_text = now.strftime('%Y/%m/%d %H:%M:%S.%f') #[:-3]
text = "Time is: %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%B %d, %Y %H:%M:%S.%f %p')
text = "Time is %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%x')
text = "Time is %s" %(date_text)
print(text)



