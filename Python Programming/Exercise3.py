#%%
name = "His name is Conan O'Brien"
cat = 'My cat name is "Butters"'
print (name)
print (cat)

both = "My cat's name is \"Butters\""
print (cat2)

#%%
def fahrenheit_to_celsius(temp):
    """ Converts Fahrenheit temperature to Celsius
        Formula is 5/9 of temp minus 32 """
        
    newTemp = 5*(temp-32)/9
    print("The Fahrenheit temperature",temp,"is equivalent to",newTemp,end='')
    print (" degrees Celsius")
     
#%%
def celsius_to_fahrenheit(temp):
        """ Converts Celsius temperature to Fahrenheit
        Formula is 9/5 of temp plus 32 """
    newTemp = (9*temp/5)+32
    print("The Celsius temprature",temp,"is equivalent to",newTemp,end='')
    print(" degree Farenheit.")
   
#%%