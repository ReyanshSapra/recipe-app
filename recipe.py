import streamlit as st
import requests

st.set_page_config(page_title="Dish Generator", page_icon="🍴")

st.markdown("""
    <style>
        .bottom-right {
            position: fixed;
            bottom: 10px;
            right: 10px;
            background-color: white;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Display static text within the bottom right container
st.markdown("<div class='bottom-right'>Reyansh Sapra</div>", unsafe_allow_html=True)

def get_recipes_by_ingredients(ingredients, offset=0, number=10000):
    api_endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
    api_key = "4d490bbdedff409d9f1eaade0aff5676"
    params = {
        "ingredients": ",".join(ingredients),
        "apiKey": api_key,
        "number": number,
        "offset": offset
    }
    response = requests.get(api_endpoint, params=params)
    return response.json()

def main():
    st.title("Dish Generator")

    st.header("Search by Ingredients")
    ingredients_input = st.text_input("Enter the ingredients you have, separated by commas")
    if st.button("Find Recipes"):
        if ingredients_input:
            ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
            recipes = get_recipes_by_ingredients(ingredients)
            if recipes:
                st.subheader("Recipes you can make:")
                for recipe in recipes:
                    st.subheader(recipe['title'])
                    st.image(recipe['image'])
                    missed_ingredients = [ingredient['name'] for ingredient in recipe['missedIngredients']]
                    st.write("Missing ingredients:", ", ".join(missed_ingredients))
                    st.write("---")
            else:
                st.write("No recipes found with the given ingredients.")
                st.subheader("☹️")

if __name__ == "__main__":
    main()
