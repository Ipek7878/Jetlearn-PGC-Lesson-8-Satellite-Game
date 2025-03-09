
tupleX=("red","orange","yellow","green")
tupleY=(18,False,7)

print(tupleX+tupleY)

print(len(tupleY))

tuple7=(31,False)
print(tuple7*7)

tupleE=("computer science",False,28,"apples",True,7.8,"dentist",True,6.8)
print(tupleE[:3])
print(tupleE[0:-6])
print(tupleE[3:6])
print(tupleE[6:])

print(tupleE[0:-2])

user_input = input("Please tell us about yourself: ")

tuple5 = ("a", "e", "i", "o", "u")
ip = user_input.lower()

vowel_count = 0  # Counter for vowels

for i in ip:
    if i in tuple5:
        vowel_count += 1  # Increment count when a vowel is found

print(f"Number of vowels present: {vowel_count}")



