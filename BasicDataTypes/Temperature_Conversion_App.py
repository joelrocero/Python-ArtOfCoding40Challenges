#Basic Data Types Challenge 3: Temperature Conversion App

print("Welcome to the Temperature Conversion App")

#Gather user input
temp_f = float(input("\nWhat is your given temperature in degrees Fahrenheit: "))

#Convert temps
temp_c = (5/9)*(temp_f - 32)
temp_k = temp_c + 273.15

#Round temps
temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)
temp_k = round(temp_k, 4)

#Summary table
print("\nDegrees Fahreinheit:\t" + str(temp_f))
print("Degree Celsius:\t" + str(temp_c))
print("Degreees Kelvin:\t" + str(temp_k))
