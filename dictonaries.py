#Dictionaries are used to store data values in key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
   123:"Legit"
}

#Retrieving items from dictionaries
print(thisdict)
print(thisdict["brand"])
print(thisdict[123])

#Adding new items to dictionary
thisdict["color"] = "red"
print(thisdict)

#updating the items in the dictionary
thisdict.update({"airbags":"yes"})
print(thisdict)

#pop/del through a dictionary(removes a specified item)
thisdict.pop(123)
print(thisdict)

#popitem() removes the last item from the dictionary
thisdict.popitem()
print(thisdict)

#loop through a dictionary
print("loop is:")
for key in thisdict:
    print(key)
    print(thisdict[key])

#nesting in dictionary
capital={
    "France":"Paris",
    "Germany":"Berlin"
}

#nesting a dictionary in a dictionary
travel_log={
    "France":{"cities_visited": ["Paris","Lille","Dijon"],"total_visits":13},
    "Canada":{"cities_visited":["Brampton","Barrie","Montreal"],"total_visits":56},
    "United Kingdom":{"cities_visited":["London","Edingburg","Birmingham"],"total_visits":23}
}

#nesting a dictionary in a list
travel_log=[
    {
      "country":"France",
      "cities_visited": ["Paris","Lille","Dijon"],
      "total_visits":13
    },

    {
      "country":"Canada", 
      "cities_visited":["Brampton","Barrie","Montreal"],
      "total_visits":56
    },

    {
        "country":"United Kingdom",
        "cities_visited":["London","Edingburg","Birmingham"],
        "total_visits":23
    }
]
