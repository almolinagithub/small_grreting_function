# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
  print("Hi there")
  print("Ciao, come va?")
  print("Howdy")

greet()

def greet_w_name(name):
    print("Hi there "+name)
    print("Ciao "+name)
    print("Howdy" + name)

greet_w_name("Alex") 

def greet_with(name,location):
  print("ciao "+ name +"vai pure a "+ location)

greet_with("Alex ","CAlcutta")