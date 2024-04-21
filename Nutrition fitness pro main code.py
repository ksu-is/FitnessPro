def nutrition_facts(recipe, portion_size):
    # Nutrition facts for each recipe
    nutrition_data = 
        {Veggie and Cheese Omelette_B: {"calories": 300, "carbs": 10, "protein": 20, "fat": 15},
        Protein Pancakes_B: {"calories": 250, "carbs": 30, "protein": 20, "fat": 8},
        Chia Seed Pudding_B: {"calories": 180, "carbs": 20, "protein": 5, "fat": 10},

        Chicken & Tzatziki Wraps_L: {"calories": 400, "carbs": 35, "protein": 30, "fat": 18},
        Pesto Spinach Penne_L: {"calories": 350, "carbs": 45, "protein": 12, "fat": 14},
        Veggie Bacon Club Sandwich_L: {"calories": 450, "carbs": 40, "protein": 15, "fat": 25},
        Chicken, Spinach & Feta Wrap_L: {"calories": 380, "carbs": 30, "protein": 25, "fat": 20},

        Sheet-Pan Salmon with Crispy Quinoa_D: {"calories": 420, "carbs": 30, "protein": 35, "fat": 18},
        Chickpea Pasta with Mushrooms & Kale_D: {"calories": 350, "carbs": 40, "protein": 15, "fat": 12},
        Chicken Tikka Masala with Rice_D: {"calories": 400, "carbs": 45, "protein": 25, "fat": 16},

        Chicken Caesar Salad_S: {"calories": 320, "carbs": 15, "protein": 30, "fat": 18},
        Apple & Peanut Butter Toast_S: {"calories": 200, "carbs": 25, "protein": 5, "fat": 10},
        Acai Bowl_S: {"calories": 280, "carbs": 40, "protein": 8, "fat": 12}}

# Calculate nutrition facts based on portion size
    facts = nutrition_data[recipe]
    for key in facts:
        facts[key] *= portion_size
    
    return facts

def choose_recipe():
    print("Welcome to Fitness Pro!")
    meal_option = input("Select a meal option - breakfast, lunch, or dinner: ")
    print("Choose from the following recipes:")
    
    recipes = []
    if meal_option.lower() == "breakfast":
        recipes = [
            "Veggie and Cheese Omelette",
            "Protein Pancakes",
            "Chia Seed Pudding"
        ]
    elif meal_option.lower() == "lunch":
        recipes = [
            "Chicken & Tzatziki Wraps",
            "Pesto Spinach Penne",
            "Veggie Bacon Club Sandwich",
            "Chicken, Spinach & Feta Wrap"
        ]
    elif meal_option.lower() == "dinner":
        recipes = [
            "Sheet-Pan Salmon with Crispy Quinoa",
            "Chickpea Pasta with Mushrooms & Kale",
            "Chicken Tikka Masala with Rice"
        ]
    else:
        print("Invalid meal option. Please choose breakfast, lunch, or dinner.")
        return
    
    index = 1
    for recipe in recipes:
        print(f"{index}. {recipe}")
        index += 1
    
    recipe_index = int(input("Enter the number corresponding to your choice: ")) - 1
    portion_size = int(input("Enter the portion size (in servings): "))
    
    selected_recipe = recipes[recipe_index]
    nutrition_info = nutrition_facts(selected_recipe, portion_size)
    
    print("\nNutrition Facts:")
    for key, value in nutrition_info.items():
        print(f"{key.capitalize()}: {value}g")

choose_recipe()
