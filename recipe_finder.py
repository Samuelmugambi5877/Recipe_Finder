# recipe_finder.py

def print_welcome_message():
    print("Welcome to the Recipe Finder")
    print("You can search for recipes based on ingredients and preferences.")
    print("Choose an option to get started:")

def define_recipes():
    recipes = {
        "spaghetti_carbonara": {
            "name": "Spaghetti Carbonara",
            "ingredients": ["spaghetti", "eggs", "bacon", "parmesan cheese", "black pepper"],
            "instructions": "Cook spaghetti; fry bacon; mix eggs, parmesan cheese, and black pepper; toss together."
        },
        "caesar_salad": {
            "name": "Caesar Salad",
            "ingredients": ["romaine lettuce", "croutons", "parmesan cheese", "caesar dressing"],
            "instructions": "Toss romaine lettuce with caesar dressing; top with croutons and parmesan cheese."
        },
        "chicken_parmesan": {
            "name": "Chicken Parmesan",
            "ingredients": ["chicken breast", "breadcrumbs", "tomato sauce", "mozzarella cheese", "parmesan cheese"],
            "instructions": "Coat chicken in breadcrumbs; fry until golden; top with tomato sauce and cheeses; bake until bubbly."
        },
        "chocolate_chip_cookies": {
            "name": "Chocolate Chip Cookies",
            "ingredients": ["butter", "sugar", "eggs", "flour", "chocolate chips", "vanilla extract"],
            "instructions": "Cream butter and sugar; beat in eggs and vanilla; mix in flour and chocolate chips; bake until golden."
        },
        "ugali_and_fish": {
            "name": "Ugali and Fish",
            "ingredients": ["maize flour", "water", "tilapia fish", "tomatoes", "onions", "vegetable oil"],
            "instructions": "Prepare ugali by boiling maize flour and water until thickened; fry fish with tomatoes and onions; serve together."
        },
        "sukuma_wiki": {
            "name": "Sukuma Wiki",
            "ingredients": ["kale", "tomatoes", "onions", "garlic", "vegetable oil"],
            "instructions": "Saute onions and garlic; add chopped kale and tomatoes; cook until tender; serve as a side dish."
        },
        "nyama_choma": {
            "name": "Nyama Choma",
            "ingredients": ["goat meat", "salt", "pepper", "vegetable oil", "lime or lemon"],
            "instructions": "Season meat with salt, pepper, and lime; grill over open flame until cooked; serve with vegetables and ugali."
        },
        "chapati": {
            "name": "Chapati",
            "ingredients": ["wheat flour", "water", "vegetable oil", "salt"],
            "instructions": "Knead flour, water, and salt into dough; roll out into thin circles; fry with oil until golden brown."
        },
        "mandazi": {
            "name": "Mandazi",
            "ingredients": ["all-purpose flour", "sugar", "coconut milk", "vegetable oil", "baking powder"],
            "instructions": "Mix flour, sugar, coconut milk, and baking powder; shape into balls and fry in hot oil until golden brown."
        },
        "pilau_rice": {
            "name": "Pilau Rice",
            "ingredients": ["basmati rice", "beef or chicken", "onions", "garlic", "ginger", "pilau masala", "vegetable oil"],
            "instructions": "Fry onions, garlic, and ginger; add meat and pilau masala; cook until meat is browned; add rice and water; cook until rice is tender."
        },
        # Add more recipes as needed
    }
    return recipes

print_welcome_message()

recipes = define_recipes()
print(recipes)
