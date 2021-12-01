# Cesar Hernandez
# 1835494

def get_age(): #Checking if the age is valid. Cannot be under 18 or above 75
    Age = int(input())
    if 18 <= Age <= 75:
        return Age
    raise ValueError("Invalid age.")

def fat_burning_heart_rate(Age): #Calculate the fat burn rate 70% * (220 - age)
    return (220 - Age) * 0.7

if __name__ == "__main__": #print out if age is valid or not valid with message
    try:
        Age = get_age()
        print("Fat burning heart rate for a", Age, "year-old:", fat_burning_heart_rate(Age), "bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.")