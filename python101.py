# VARIABLES ===============================================
# Create a variable named `x`

x=1
print(x)

jasonsays = 'when youre stoned you are the string'
print(jasonsays)

# Have multiple words? Snake case it!


# Create another variable, assign it to a Boolean
octopus = True
print(octopus)

Donald_Trump= False
print(Donald_Trump)
# Variables are case sensitive
# BASIC MATH ===============================================
# Simple math between numbers
result = 5*5
print(result)
# Math with variables
print (4*4)


# STRINGS ===============================================
# Simple string
x ='1. but i already made a string'
y =' 2. are you sure?'
result2 = x+" " +y

#you can add spaces within the first or 2nd string best practise is to never add spaces within the strings though but to append them as they are and put a space in the middle (as line 32 shows.)

print(result2)
# String concatenation

# you can add variables with actual numbers i.e
three = 3
result3 = 10 + three
print (result3)

# LIST ===============================================
# A list of fruits

# All the data types in this list! Try to include at least:
# 1) Number (Integer)
# 2) String
# 3) Variable
# 4) Boolean

numbers = [1,3,5,7,9]
print (numbers)

#you can mix your lists / (arrays in ruby lists here) with different data types

mixed_list= [50,'three thousand',False,numbers,jasonsays]
print (mixed_list)

# Get the first item from the list
mixed_list[0]
# Get the third item from the list
mixed_list[2]
# Get the last item from the list
mixed_list[-1]
# Append another item to the end of the list
print(mixed_list[1])
# Add an item at the beginning of the list with `insert`
# `.insert(index, val)`
mixed_list.append('apple')
mixed_list.insert(0,"strawberry")
print(mixed_list)
mixed_list[3]="apple"
print(mixed_list)
# LIST // Loops
# Print each item in the list
# for _ in _

fruits = ["watermelon","kidneys","cheese"]

for item in fruits:
  print("my item is" +" "+ item)

for jump in mixed_list:
  print (jump)
print("aarrrr i'm a pirate , I'm actually not all that badass cause I'd have scurvey ")


#Strings can not be next to numbers unless you cast it to a string which

# DICTIONARY ===============================================
# Create a car. It should have a few properties:

# 1) name - string
car = {
  "name": "Jason",
  "brand": "Tesla",
  "wheels": 3,
  "passengers": ["jason" , "DEPRESSION", "Daniel I guess"],
  "park": False
}
# 2) brand - string
# 3) wheels - integer
# 4) passengers - list
# 5) park - boolean

# Access values from the car
# Use square bracket notation & `.get`

print(car ['brand'])
print(car.get("passengers"))

# Update a the 'colour' property's value

# Use square bracket notation & '.update' for more props in one go!

car["brand"] = "brand change Lexus"
print(car)

new_car_values= {
  "wheels": 4,
  "park": True,
  "poop": False

}

car.update(new_car_values)
print(car)


# FLOW CONTROL // If/else ===============================================
# Set the temperature

temperature= 0
print(temperature)

# Print out if the temperature is cold, average, or hot
if temperature <=0:
  print ("cold")
elif temperature  <=24:
  print ('lovin that averageness')
else :
  print("It's spicy outside")





















