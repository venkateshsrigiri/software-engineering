t = int(input("give the input of temperature: "))
h = int(input('give the input of humidity: '))
w = int(input('give the input of wind speed: '))
we = 0.5*t**2-0.2*h+0.1*w-15
print(we)
if we > 300:
    print("sunny")
elif 200<we<=300:
    print("cloudy")
elif 100<we <200:
    print("rainy")
elif we<= 100:
    print("stormy")

