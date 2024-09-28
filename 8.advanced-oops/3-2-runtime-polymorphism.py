# runtime (or dynamic) polymorphism -> overriding
class Country: 
    def official_language(self): 
        return "No official language specified" 
 
class USA(Country): 
    def official_language(self): 
        return "English" 
 
class China(Country): 
    def official_language(self): 
        return "Mandarin" 
 
class Germany(Country): 
    def official_language(self): 
        return "German" 
 
# Creating instances of the subclasses 
country = Country() 
usa = USA() 
china = China() 
germany = Germany() 
 
# Calling the overridden official_language method 
print(country.official_language())  # Output: No official language specified 
print(usa.official_language())      # Output: English 
print(china.official_language())    # Output: Mandarin 
print(germany.official_language())  # Output: German 