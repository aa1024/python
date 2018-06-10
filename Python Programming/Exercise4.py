#%%
def name():
    """ Ask the first name and last name, concatenate and print. 
        Also ask the city and state and print"""
    fname = input("Enter your first name:")
    lname = input("Enter your last name:")
    city = input("Enter the city you live in:")
    state = input("Enter the state you live in:")

    fullname = fname+ " "+ lname
    city_state = city +", " +state
    print("Your name is:",fullname)
    print("You live in:",city_state)
#%%