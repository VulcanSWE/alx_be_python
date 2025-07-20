#Prompt the user for the weather condition and provide advice based on the input
weather = input("Enter the weather condition (sunny, rainy, snowy): ").strip().lower()

# Check the weather condition and provide appropriate advice
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "snowy":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
