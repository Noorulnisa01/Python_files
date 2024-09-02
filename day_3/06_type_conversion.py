                               
                                 # Type Conversion

# type conversion is the process of converting one data type to another data type
# 1. int to float
# 2. float to int
# 3. int to string
# 4. float to string
# 5. string to int
# 6. string to float

                # implicit type conversion

x = 2    # int      
y = 2.0  # float
z = x/y  # float

# z data type is float because when intergal number is divided by float number it gives float number
# float is always superior than intergal number

print(z, type(z))

# 2. float to int
x = 2.0  # float
y = 2    # int
z = x/y  # float    

# z data type is float because when float number is divided by intergal number it gives float number
# int is always inferior than float number

print(z, type(z))

            # explict type conversion


age = input("Enter your age : ")

print(int(age), type(int(age)))

# here z is string but it convert it into intergal number
# we can change data type of variable by putting data type in front of variable

