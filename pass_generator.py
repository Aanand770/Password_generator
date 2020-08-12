import random

# To get lower case letters
lcase = "abcdefghijklmnopqrstuvwxyz"

# To get upper case letters
ucase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# To get Numbers
no = "0123456789"

# To get Special Character
spchar = "{}[]@#$!~%^&*()_/?.<,>*"

# To combine lower case, upper case, numbers and special character
a = lcase + ucase + no + spchar

# Fixing The length of password
leng = 16

# Generating the password by combining lower case, upper case, numbers and special character randomly
pwd = "".join(random.sample(a, leng))


# To print the generated Password
print(pwd)
