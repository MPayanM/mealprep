# data_loader.py
# Queries the API Ninjas Nutrition API for food macros.

import requests
import streamlit as st

BASE_URL = "https://api.api-ninjas.com/v1/nutrition"
API_KEY  = st.secrets["API_NINJAS_KEY"]


def search_foods(query: str, max_results: int = 10) -> list[dict]:
    """
    Searches API Ninjas for foods matching the query.
    Returns a list of dicts with 'name' and 'macros'.
    """
    if not query:
        return []

    response = requests.get(
        BASE_URL,
        headers={'X-Api-Key': API_KEY},
        params={'query': query}
    )

    if response.status_code != 200:
        return []

    foods   = response.json()
    results = []

    for food in foods[:max_results]:
        results.append({
            'name':   food['name'].title(),
            'macros': {
                'calories': food.get('calories',      0),
                'protein':  food.get('protein_g',     0),
                'carbs':    food.get('carbohydrates_total_g', 0),
                'fat':      food.get('fat_total_g',   0),
                'fiber':    food.get('fiber_g',        0),
                'serving':  food.get('serving_size_g', 100),
            }
        })

    return results