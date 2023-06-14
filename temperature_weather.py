# Weather application

# The user can add a temperature and this will give back a message.

temperature = int(input("What is the temperature in celsius? "))

if temperature <= 0:
    print("It is freezing! Get a coat!")
elif 0 < temperature <= 15:
    print("It is chilly... A jacket will do")
elif 16 < temperature <= 20:
    print("It's warming up... Perfect weather!")
elif 21 < temperature <= 30:
    print("Summer is here! Get the ice-cream!")
else:
    print("It is hellish outside... Send help")