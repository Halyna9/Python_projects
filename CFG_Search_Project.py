import requests
from pprint import pprint


# creating a function to get the recipes based on asked ingredient and diet requirements
app_id = "453ce7d2" 
app_key = "e7dce04b937a1760b73317b824ce227d"

def get_recipes(ingredient):
    if dietry_requirement == "1":
        url = f"https://api.edamam.com/search?q={user_ingredient}&app_id={app_id}&app_key={app_key}&mealType={meal_type}"
    else:
        url = f"https://api.edamam.com/search?q={user_ingredient}&app_id={app_id}&app_key={app_key}&health={diet}&mealType={meal_type}"
    response = requests.get(url)
    #pprint(response)
    recipe_database = response.json()
    return recipe_database


#printing the recipes and saving it into the recipes.txt file
def display_recipes ():
  with open('recipes.txt', 'w+', encoding='utf-8') as text_file:
    for recipe in results["hits"]:
        print("\n")
        print("*" * 100)
        text_file.write("*" * 100)
        text_file.write("\n")
        print(recipe["recipe"]["label"])
        text_file.write(f"Recipe: {recipe['recipe']['label']}\n")
        text_file.write("*" * 100)
        text_file.write("\n")

        print("*" * 100)
        print(recipe["recipe"]["url"])
        text_file.write(f"Link: {recipe['recipe']['url']}\n")
        text_file.write("\n")
        print("\n")

        ingredients_list = recipe["recipe"]["ingredientLines"]
        formated_ingr_list = "\n".join(ingredients_list)
        print(formated_ingr_list)
        text_file.write(f"Ingredients: \n{formated_ingr_list} \n")
        text_file.write("\n")
        print("\n")

        instruction = recipe["recipe"]["instructionLines"]
        formated_instruction = "\n".join(instruction)
        print(formated_instruction)
        text_file.write(f"Instruction: \n{formated_instruction} \n")
        text_file.write("\n")
        print("\n")



# asking user for any diet requirements
print("1. None \n2. Vegan \n3. Vegetarian \n4. Gluten-free")
print("5. Dairy-free \n6. Peanut-free \n")
dietry_requirement = input("Do you have any dietary requirement (Choose the number from above): ")

diet = ""
if dietry_requirement == "2":
    diet += "vegan"
elif dietry_requirement == "3":
    diet += "vegetarian"
elif dietry_requirement == "4":
    diet += "gluten-free"
elif dietry_requirement == "5":
    diet += "dairy-free"   
elif dietry_requirement == "6":
    diet += "peanut-free"
elif int(dietry_requirement) < 1 or int(dietry_requirement) > 6:
    print("Sorry, we could find any recipes. Please, try again. ")
  

# asking user for the meal type they want
print("\n")
print("1. Breakfast \n2. Brunch \n3. Lunch \n4. Dinner \n5. Snacks \n")
meal = input("What meal would you like? (Choose the number from above): ")

meal_type = ""
if meal == "1":
    meal_type += "breakfast"
elif meal == "2":
    meal_type += "brunch"
elif meal == "3":
    meal_type += "lunch"
elif meal == "4":
    meal_type += "dinner"
elif meal == "5":
    meal_type += "snack"
else:
    print("Meal type not found. Please, try again.")
   

# asking user for the ingredient 
print("\n")
user_ingredient = input("What are the ingredients you are interested in?: ")
results = get_recipes(user_ingredient)
#pprint(results)
display_recipes ()
