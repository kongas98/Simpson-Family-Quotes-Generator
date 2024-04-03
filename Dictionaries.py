#Ασκηση 1

#Δημιουργία λεξικού
dictionary = {
    "Ιταμός":"Προκλητικός, αυθάδης, αναιδής",
    "Όνειδος":"Ντροπή, καταισχύνη",
    "Πομφόλυγες":"Αερολογίες, ανοησίες",
}

#Εμφάνιση Λεξικού
print(dictionary)

#Πρόσθεση λήμματος
dictionary["φληναφήαματα"] = "Ανοησίες, Σαχλαμάρες"

#Καταχώρηση χρήστη ενός ζεύγους κλειδιού-τιμής
key = input("Γράψε ένα κλειδι: ")
meaning = input("Γράψε τι σημαίνει: ")

#Πρόσθεση του ζεύγους στο λεξικό
dictionary[key] = meaning

#Εμφάνιση του λεξικού
print(dictionary)


#Άσκηση 2

# Define a dictionary named `worker` containing details of a worker.
worker = {
    "Name": "Themis",
    "Last name": "Kottas",
    "Father's Name": "Dimitrios",
    "Date of Birth": "13/04/1998",
    "Address": "Chrisostomou Smirnis 10, Efkarpia Thessalonikis",
    "Phone": "6947462013",
}

# Print worker's name, father's name, and last name.
print("Ονοματεπώνυμο: " + worker["Name"], worker["Father's Name"], worker["Last name"])
# Print worker's date of birth.
print("Ημερομηνία γέννησης: " + worker["Date of Birth"])
# Print worker's address.
print("Διεύθυνση: " + worker["Address"])
# Print worker's phone number.
print("Τηλέφωνο: " + worker["Phone"])

# Exercise 3

# Import required libraries.
import random
from random import randrange

# Create an empty dictionary named `dictionary`.
dictionary = {}

# Initialize keys in the dictionary from 1 to 6 with values set to 0.
for i in range(1, 7):
    dictionary[i] = 0

# Roll a dice 100 times and count occurrences of each number.
for i in range(100):
    dice = randrange(1, 7)  # Randomly generate a number between 1 and 6 (inclusive).
    dictionary[dice] += 1

# Print the dictionary showing the count of occurrences for each number.
print(dictionary)

# Calculate the probability of each number occurring and update the dictionary accordingly.
for i in range(1, 7):
    dictionary[i] = (100 - dictionary[i]) / 100

# Print the updated dictionary containing the probability of each number.
print(dictionary)

            

#Ασκηση 4
# Define a paragraph containing information about Werner Heisenberg.
paragraph = "Werner Karl Heisenberg (pronounced [vɛʁnɐ kaʁl hazn̩bɛʁk] ⓘ; 5 December 1901 1 February 1976)[2] was a German theoretical physicist, one of the main pioneers of the theory of quantum mechanics, and a principal scientist in the Nazi nuclear weapons program during World War II. He published his Umdeutung paper in 1925, a major reinterpretation of old quantum theory. In the subsequent series of papers with Max Born and Pascual Jordan, during the same year, his matrix formulation of quantum mechanics was substantially elaborated. He is known for the uncertainty principle, which he published in 1927. Heisenberg was awarded the 1932 Nobel Prize in Physics "

# Convert the paragraph into a list of characters.
paragraph_list = list(paragraph)

# Initialize an empty dictionary to store character counts.
dictionary = {}

# Iterate through each character in the paragraph.
for char in paragraph_list:
    # If the character is not already in the dictionary, add it with a count of 0.
    if char not in dictionary:
        dictionary[char] = 0
    # Otherwise, increment the count for that character.
    dictionary[char] += 1

# Iterate through the sorted values of the dictionary.
for key in sorted(dictionary):
    # Print the character and its count.
    print(str(key) + " : " + str(dictionary[key]))


#Ασκηση 5

merch = {
    "book":10.18,
    "Parsley":0.22,
    "Cement":5.17,
    "CD":0.05,
}

# Print the initial contents of the `merch` dictionary.
print(merch)

# Iterate three times to get ratings for three different customers.
for i in range(3):
    # Prompt the user to input a rating for the customer.
    rate = float(input("Write your rate for this customer: "))
    
    # Validate the input to ensure it falls within the specified range.
    while rate <= 0 or rate >= 6:
        rate = float(input("Write your rate for this customer: "))

    # Calculate new prices for the items based on the provided rate.
    new_values = {key: value * (1 + rate) for key, value in merch.items()}

    # Print the updated prices.
    print(new_values)


#Ασκηση 6

# Define a dictionary named `buildings` containing buildings and their respective countries.
buildings = {
    "Burj Khalifa": "United Arab Emirates",
    "Shanghai Tower": "China",
    "Abraj Al-Bait Clock Tower": "Saudi Arabia",
    "Ping An Finance Center": "China",
    "Lotte World Tower": "South Korea",
    "One World Trade Center": "United States",
    "Guangzhou CTF Finance Center": "China",
    "Tianjin CTF Finance Center": "China",
    "Zun Taipei": "Taiwan",
    "Shanghai World Financial Center": "China",
    "Central Park Tower": "United States",
    "Lakhta Center": "Russia",
    "Landmark": "Vietnam",
    "Changsha IFS Tower": "China",
    "Petronas Tower 1": "Malaysia",
    "Petronas Tower 2": "Malaysia",
    "Zifeng Tower": "China",
    "Suzhou IFS": "China",
    "The Exchange": "Malaysia",
    "Willis Tower": "United States",
    "KK100": "China",
    "Guangzhou International Finance Center": "China",
    "Wuhan Center": "China",
    "111 West 57th Street": "United States",
    "One Vanderbilt": "United States",
    "Dongguan International Trade Center": "China",
    "432 Park Avenue": "United States",
    "Marina 101": "United Arab Emirates",
    "Trump International Hotel and Tower": "United States",
    "Jin Mao Tower": "China",
    "Princess Tower": "United Arab Emirates",
    "Al Hamra Tower": "Kuwait",
    "International Finance Centre": "China",
    "Haeundae LCT The Sharp Landmark Tower": "South Korea",
    "Nanning China Resources Tower": "China",
    "Guiyang Financial Center Tower": "China",
    "China Resources Headquarters": "China",
    "23 Marina": "United Arab Emirates",
    "Shun Hing Square": "China",
    "Eton Place Dalian Tower 1": "China"
}

# Initialize an empty dictionary to store buildings grouped by country.
country_buildings = {}

# Iterate through each key-value pair in the `buildings` dictionary.
for key, value in buildings.items():
    # If the country is not already in `country_buildings`, add it as a key with a list containing the building.
    if value not in country_buildings:
        country_buildings[value] = [key]
    # If the country already exists in `country_buildings`, append the building to the existing list.
    else:
        country_buildings[value].append(key)

# Iterate through each country and its corresponding list of buildings.
for key, value in country_buildings.items():
    # Print the country followed by its list of buildings.
    print(key + str(value), end="\n\n")


#Ασκηση 7
# Import the required libraries.
import random
from random import choice

# Define a dictionary named `family` containing information about the Simpson family.
family = {
    "father": {
        "name": "Homer Simpson",
        "occupation": "nuclear safety inspector",
        "quotes": [
            "Lord Help Me, I’m Just Not That Bright",
            "Kids, You Tried Your Best And You Failed Miserably. The Lesson Is, Never Try.",
            "It Takes Two To Lie; One To Lie, And One To Listen.",
            "To Alcohol! The Cause Of, And Solution To, All Of Life's Problems.",
            "I Am So Smart! I Am So Smart! S-M-R-T! I Mean S-M-A-R-T!",
            "D'Oh!"
        ]
    },
    "mother": {
        "name": "Marge Simpson",
        "occupation": "housewife",
        "quotes": [
            "Am I Pregnant?",
            "And all this time I thought 'Googling yourself' meant the other thing.",
            "Homer, we have to do something. Today he's drinking people's blood. Tomorrow he could be smoking.",
            "I guess one person can make a difference. But most of the time, they probably shouldn't."
        ]
    },
    "children": [
        {
            "name": "Bart Simpson",
            "quotes": [
                "Eat My Shorts!", 
                "I'm Bart Simpson, who the hell are you?", 
                "You got the brains and talent to go as far as you want and when you do I'll be right there to borrow money"
                ]
                },
        {
            "name": "Lisa Simpson", 
            "quotes": [
                "Does It Make You Feel Superior To Tear Down People’s Dreams?", 
                "Pablo Neruda Said, 'Laughter Is The Language Of The Soul.'", 
                "I Just Think It's A Fantasy. If You Believe In Angels, Why Not Sea Monsters, Unicorns Or Leprechauns?"
                ]
                },
        {"name": "Maggie Simpson", 
         "quotes": [
             "(sucking noise)", 
             "(crying)", 
             "Daddy!"
             ]
             }
    ]
}

# Iterate through each key-value pair in the `family` dictionary.
for family_key, family_value in family.items():
    # If the key is not "children", iterate through the key-value pairs of the parent dictionary.
    if family_key != "children":
        for parents_key, parents_value in family_value.items():
            # If the key is "name", print the name of the parent.
            if parents_key == "name":
                print(parents_value)
            # If the key is "quotes", randomly choose and print a quote from the list of quotes.
            elif parents_key == "quotes":
                print(choice(parents_value))
    # If the key is "children", iterate through each child dictionary.
    else:
        for child_dict in family_value:
            for children_key, children_value in child_dict.items():
                # If the key is "name", print the name of the child.
                if children_key == "name":
                    print(children_value)
                # If the key is "quotes", randomly choose and print a quote from the list of quotes.
                else:
                    print(choice(children_value))

