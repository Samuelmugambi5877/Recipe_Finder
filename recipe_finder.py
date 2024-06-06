import json

def print_welcome_message():
    print("\nWelcome to the Recipe Finder")
    print("You can search for recipes based on ingredients and preferences.")
    print("Choose an option to get started:")
    print("1. Search for a recipe by name")
    print("2. Search for a recipe by ingredient")
    print("3. View saved searches")
    print("4. Exit")

def define_recipes():
    recipes = {
        "spaghetti_carbonara": {
            "name": "Spaghetti Carbonara",
            "ingredients": {
                "spaghetti": "200g",
                "eggs": "2",
                "bacon": "100g",
                "parmesan cheese": "50g",
                "black pepper": "to taste"
            },
            "instructions": "Cook spaghetti (10 minutes); fry bacon (5 minutes); mix eggs, parmesan cheese, and black pepper; toss together."
        },
        "caesar_salad": {
            "name": "Caesar Salad",
            "ingredients": {
                "romaine lettuce": "1 head",
                "croutons": "100g",
                "parmesan cheese": "50g",
                "caesar dressing": "100ml"
            },
            "instructions": "Toss romaine lettuce with caesar dressing (5 minutes); top with croutons and parmesan cheese."
        },
        "chicken_parmesan": {
            "name": "Chicken Parmesan",
            "ingredients": {
                "chicken breast": "2 pieces",
                "breadcrumbs": "100g",
                "tomato sauce": "200ml",
                "mozzarella cheese": "100g",
                "parmesan cheese": "50g"
            },
            "instructions": "Coat chicken in breadcrumbs (10 minutes); fry until golden (10 minutes); top with tomato sauce and cheeses; bake until bubbly (20 minutes)."
        },
        "chocolate_chip_cookies": {
            "name": "Chocolate Chip Cookies",
            "ingredients": {
                "butter": "100g",
                "sugar": "200g",
                "eggs": "2",
                "flour": "300g",
                "chocolate chips": "200g",
                "vanilla extract": "1 tsp"
            },
            "instructions": "Cream butter and sugar (5 minutes); beat in eggs and vanilla (5 minutes); mix in flour and chocolate chips (5 minutes); bake until golden (15 minutes)."
        },
        "ugali_and_fish": {
            "name": "Ugali and Fish",
            "ingredients": {
                "maize flour": "2 cups",
                "water": "4 cups",
                "tilapia fish": "1 whole",
                "tomatoes": "2",
                "onions": "2",
                "vegetable oil": "3 tbsp"
            },
            "instructions": "Prepare ugali by boiling maize flour and water until thickened (15 minutes); fry fish with tomatoes and onions (20 minutes); serve together."
        },
        "sukuma_wiki": {
            "name": "Sukuma Wiki",
            "ingredients": {
                "kale": "1 bunch",
                "tomatoes": "2",
                "onions": "1",
                "garlic": "2 cloves",
                "vegetable oil": "2 tbsp"
            },
            "instructions": "Saute onions and garlic (5 minutes); add chopped kale and tomatoes (10 minutes); cook until tender; serve as a side dish."
        },
        "nyama_choma": {
            "name": "Nyama Choma",
            "ingredients": {
                "goat meat": "1 kg",
                "salt": "to taste",
                "pepper": "to taste",
                "vegetable oil": "2 tbsp",
                "lime or lemon": "1"
            },
            "instructions": "Season meat with salt, pepper, and lime (10 minutes); grill over open flame until cooked (30 minutes); serve with vegetables and ugali."
        },
        "chapati": {
            "name": "Chapati",
            "ingredients": {
                "wheat flour": "2 cups",
                "water": "1 cup",
                "vegetable oil": "4 tbsp",
                "salt": "1 tsp"
            },
            "instructions": "Knead flour, water, and salt into dough (10 minutes); roll out into thin circles (10 minutes); fry with oil until golden brown (10 minutes)."
        },
        "mandazi": {
            "name": "Mandazi",
            "ingredients": {
                "all-purpose flour": "2 cups",
                "sugar": "1/2 cup",
                "coconut milk": "1 cup",
                "vegetable oil": "for frying",
                "baking powder": "1 tsp"
            },
            "instructions": "Mix flour, sugar, coconut milk, and baking powder (10 minutes); shape into balls and fry in hot oil until golden brown (10 minutes)."
        },
        "pilau_rice": {
            "name": "Pilau Rice",
            "ingredients": {
                "basmati rice": "2 cups",
                "beef or chicken": "300g",
                "onions": "2",
                "garlic": "2 cloves",
                "ginger": "1 tsp",
                "pilau masala": "2 tbsp",
                "vegetable oil": "3 tbsp"
            },
            "instructions": "Fry onions, garlic, and ginger (5 minutes); add meat and pilau masala (10 minutes); cook until meat is browned; add rice and water (15 minutes); cook until rice is tender."
        },
        "beef_stew": {
            "name": "Beef Stew",
            "ingredients": {
                "beef": "500g",
                "potatoes": "3",
                "carrots": "2",
                "onions": "1",
                "garlic": "2 cloves",
                "tomatoes": "2",
                "beef broth": "2 cups"
            },
            "instructions": "Brown beef in a pot (10 minutes); add chopped onions and garlic (5 minutes); add carrots and potatoes (10 minutes); add tomatoes and beef broth; simmer until tender (30 minutes)."
        },
        "fish_curry": {
            "name": "Fish Curry",
            "ingredients": {
                "fish fillets": "500g",
                "coconut milk": "1 cup",
                "curry powder": "2 tbsp",
                "tomatoes": "2",
                "onions": "1",
                "garlic": "2 cloves",
                "ginger": "1 tsp"
            },
            "instructions": "Saute onions, garlic, and ginger (5 minutes); add curry powder (2 minutes); add tomatoes and coconut milk (10 minutes); add fish fillets and simmer until cooked (10 minutes)."
        },
        "banana_bread": {
            "name": "Banana Bread",
            "ingredients": {
                "ripe bananas": "3",
                "flour": "2 cups",
                "sugar": "1 cup",
                "eggs": "2",
                "butter": "1/2 cup",
                "baking soda": "1 tsp",
                "vanilla extract": "1 tsp"
            },
            "instructions": "Mash bananas (5 minutes); mix with melted butter, sugar, and eggs (5 minutes); add flour and baking soda (5 minutes); pour into a loaf pan and bake until golden (45 minutes)."
        },
        "mango_smoothie": {
            "name": "Mango Smoothie",
            "ingredients": {
                "mango": "1",
                "yogurt": "1 cup",
                "honey": "1 tbsp",
                "milk": "1/2 cup",
                "ice cubes": "a handful"
            },
            "instructions": "Blend mango, yogurt, honey, milk, and ice cubes until smooth (5 minutes)."
        },
        "vegetable_stir_fry": {
            "name": "Vegetable Stir Fry",
            "ingredients": {
                "broccoli": "1 head",
                "carrots": "2",
                "bell peppers": "2",
                "soy sauce": "2 tbsp",
                "garlic": "2 cloves",
                "ginger": "1 tsp",
                "vegetable oil": "2 tbsp"
            },
            "instructions": "Saute garlic and ginger (2 minutes); add chopped vegetables and stir-fry until tender (10 minutes); add soy sauce and cook for another 2 minutes."
        },
        "avocado_salad": {
            "name": "Avocado Salad",
            "ingredients": {
                "avocado": "1",
                "tomatoes": "2",
                "cucumber": "1",
                "red onion": "1/2",
                "lime juice": "1 tbsp",
                "olive oil": "2 tbsp",
                "salt": "to taste",
                "pepper": "to taste"
            },
            "instructions": "Chop avocado, tomatoes, cucumber, and red onion (5 minutes); toss with lime juice, olive oil, salt, and pepper."
        },
        "spinach_and_feta_omelette": {
            "name": "Spinach and Feta Omelette",
            "ingredients": {
                "eggs": "3",
                "spinach": "1 cup",
                "feta cheese": "1/4 cup",
                "onion": "1/2",
                "olive oil": "1 tbsp",
                "salt": "to taste",
                "pepper": "to taste"
            },
            "instructions": "Saute spinach and onion (5 minutes); beat eggs and pour into pan (2 minutes); add feta cheese and cook until eggs are set (5 minutes)."
        }
    }
    return recipes

def search_by_name(recipes, query):
    found_recipes = []
    for key, recipe in recipes.items():
        if query.lower() in recipe['name'].lower():
            found_recipes.append(recipe)
    return found_recipes

def search_by_ingredient(recipes, query):
    found_recipes = []
    for key, recipe in recipes.items():
        for ingredient in recipe['ingredients']:
            if query.lower() in ingredient.lower():
                found_recipes.append(recipe)
                break
    return found_recipes

def display_recipes(recipes):
    for recipe in recipes:
        print("\nRecipe:", recipe['name'])
        print("Ingredients:")
        for ingredient, quantity in recipe['ingredients'].items():
            print(f"{ingredient}: {quantity}")
        print("Instructions:", recipe['instructions'])

def save_search(query, results):
    search_data = {
        "query": query,
        "results": [recipe['name'] for recipe in results]
    }
    with open("search_history.json", "a") as file:
        json.dump(search_data, file)
        file.write("\n")

def view_saved_searches():
    try:
        with open("search_history.json", "r") as file:
            for line in file:
                search_data = json.loads(line)
                print(f"\nSearch Query: {search_data['query']}")
                print("Results:")
                for result in search_data['results']:
                    print(result)
    except FileNotFoundError:
        print("No saved searches found.")

def main():
    recipes = define_recipes()
    print_welcome_message()
    
    while True:
        try:
            choice = int(input("Enter your choice (1, 2, 3, or 4): "))
            if choice == 1:
                query = input("Enter the name of the recipe you're looking for: ")
                found_recipes = search_by_name(recipes, query)
                if found_recipes:
                    display_recipes(found_recipes)
                    save_search(query, found_recipes)
                else:
                    print("No recipes found with that name.")
            elif choice == 2:
                query = input("Enter the ingredient you're looking for: ")
                found_recipes = search_by_ingredient(recipes, query)
                if found_recipes:
                    display_recipes(found_recipes)
                    save_search(query, found_recipes)
                else:
                    print("No recipes found with that ingredient.")
            elif choice == 3:
                view_saved_searches()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, 3, or 4).")

if __name__ == "__main__":
    main()
