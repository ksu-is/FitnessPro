def nutrition_facts(recipe, portion_size):
    # Nutrition facts for each recipe
    nutrition_data = {
        Veggie and Cheese Omelette_B: {"calories": 300, "carbs": 10, "protein": 20, "fat": 15},
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
        Acai Bowl_S: {"calories": 280, "carbs": 40, "protein": 8, "fat": 12}
    }

# Calculate nutrition facts based on portion size
    facts = nutrition_data[recipe]
    for key in facts:
        facts[key] *= portion_size
    
    return facts