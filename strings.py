name = "Mudasir"
print(name[0:3])
print(name[-4: -1])

# Strings Cases

# title case
title = name.title()
print(title)


# lowercase

lower = name.lower()
print(lower)

# uppercase

upper = name.upper()
print(upper)

# f-string

myNum = 4
message = "My Favourite number is: "
print(f"{message} {myNum}")

# ==================> id card exercise: <===========================

fullname = "Mudasir Chandio"
fname = "Bashir Ahmed"
section = "A"
batch = 1
rollNo = 459946

print(f"""
    FullName: {fullname}
    Father's Name: {fname}
    Section: {section}
    Batch: {batch}
    RollNo: {rollNo}
""")


# =======> Whitespaces and methods in string <=========

myName = "\n\tMudasir\t\n"
print(myName)

# lstrip(): removes the left side spaces of string

print(myName.lstrip())

# rstrip(): removes the right side spaces of string

print(myName.rstrip())

# strip(): removes the spaces of string

print(myName.strip())



# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

personName = "Eric"
mess = f"Hello {personName}, would you like to learn some Python today?"
print(mess)

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

print(personName.lower())
print(personName.upper())
print(personName.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”

author = "Albert Einstein"

print(f"{author} once said, “A person who never made a mistake never tried anything new.”")


# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
# famous person’s name using a variable called famous_person. Then compose
# your message and represent it with a new variable called message. Print your
# message.

famous_person = author
messsage = "“A person who never made a mistake never tried anything new.”"
print(f"{famous_person} once said, {messsage}")

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include
# some whitespace characters at the beginning and end of the name. Make sure
# you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

person_name = "\n\teinstein\t\n"
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())
