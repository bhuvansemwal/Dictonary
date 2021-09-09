"""
Create a dictionary and take input from the user and return the meaning of the word from the dictionary.
"""
d1= {"Bhuvan": "The World, One of the three worlds", "Ananya" : "Unique, having no equivalent", "Anjali": "divine,love offering"}

print("Select a Name to know its meaning:")
print("Bhuvan\nAnjali\nAnanya")

name=input()

print("The meaning of the name", name, "is:")
print(d1[name])
