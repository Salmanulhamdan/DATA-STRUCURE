pantry = {
    "chicken": 500,"lemon": 2, "cumin": 24, "paprika": 18, "chilli powder": 7,
    "yogurt": 300,"oil": 450,"onion": 5,"garlic": 9,
    "ginger": 2,"tomato puree": 125,"almonds": 75, "rice": 500,
    "coriander": 20,"lime": 3,"pepper": 8,"egg": 6,"pizza": 2,"spam": 1,
}
recipes = {
    "Butter chicken": [
        "chicken", "lemon","cumin","paprika","chilli powder","yogurt",
        "oil","onion", "garlic","ginger", "tomato puree", "almonds","rice", "coriander","lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}
while True:
    print("Menu:")
    for i, recipe in enumerate(recipes):
        print(f"{i+1}. {recipe}")
    print("0. Quit")
    choice = int(input("Enter the number of the recipe you want to make, or 0 to quit: "))
    if choice == 0:
        print("Goodbye!")
        break
    elif choice < 1 or choice > len(recipes):
        print("Invalid input. Please enter a number between 1 and", len(recipes))
        continue

    recipe_name = list(recipes.keys())[choice-1]
    recipe_ingredients = recipes[recipe_name]

    for ingredient in recipe_ingredients:
        if ingredient not in pantry or pantry[ingredient] == 0:
            print(f"Sorry, you don't have enough {ingredient} to make {recipe_name}.")
            break
    else:
        print(f"Making {recipe_name}...")
        for ingredient in recipe_ingredients:
            pantry[ingredient] -= 1
        print(f"{recipe_name} is ready!")
