# # define a function means that we can define our own functions
# # function is a block of code which only runs when it is called
# # we can pass data into the function as parameters

# # def keyword is used to define a function
# def student_age(age):
#     if age != 10:
#         print(" He is a edult")
#     elif age == 10:
#         print(" He is a young")
#     else:
#         print("He is a chlid")

# student_age(input("Enter your age : "))

# # we can call the function multiple times

# student_age(10)

# student_age(11)

# student_age(12)

# student_age(13)

# # we can pass multiple parameters to the function

# student_age(10,11,12,13)

# we can return values from the function

def student_age(age):
    if age != 10:
        return " He is a edult"
    elif age == 10:
        return " He is a young"
    else:
        return "He is a chlid"

print(student_age(10))

# we can define a function for future use

def future_age(age):
    new_age = age + 10
    return new_age

print(future_age(10))


