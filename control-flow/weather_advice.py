weather = str(input("Enter the weather condition (sunny, rainy, snowy): ")).lower()

if weather == "sunny":
    print(f" Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print(f" Don't forget your umbrella and a raincoat..")
elif weather == "snowy":
    print(f" Make sure to wear a warm coat and a scarf..")
else:
    print(f" Sorry, I don't have recommendations for this weather.")
