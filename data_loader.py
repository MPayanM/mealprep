# data_loader.py
# Queries the USDA FoodData Central API for food macros.

import requests
import streamlit as st

BASE_URL = "https://api.nal.usda.gov/fdc/v1"
API_KEY  = st.secrets["USDA_API_KEY"]


def search_foods(query: str, max_results: int = 8) -> list[dict]:
    """
    Searches USDA for foods matching the query.
    Returns a list of dicts with 'fdc_id' and 'name'.
    """
    if not query:
        return []

    response = requests.get(
        f"{BASE_URL}/foods/search",
        params={
            'api_key':  API_KEY,
            'query':    query,
            'pageSize': max_results,
            'dataType': 'SR Legacy,Foundation'
        }
    )

    if response.status_code != 200:
        return []

    results = []
    for food in response.json().get('foods', []):
        results.append({
            'fdc_id': food['fdcId'],
            'name':   food['description'].title()
        })

    return results


def get_macros_by_id(fdc_id: int) -> dict | None:
    """
    Fetches full nutritional data for a food by its USDA fdc_id.
    Returns a dict with calories, protein, carbs, fat, fiber (per 100g).
    """
    response = requests.get(
        f"{BASE_URL}/food/{fdc_id}",
        params={'api_key': API_KEY}
    )

    if response.status_code != 200:
        return None

    nutrients = response.json().get('foodNutrients', [])

    NUTRIENT_MAP = {
        1008: 'calories',
        1003: 'protein',
        1005: 'carbs',
        1004: 'fat',
        1079: 'fiber',
    }

    macros = {'calories': 0, 'protein': 0, 'carbs': 0,
              'fat': 0, 'fiber': 0, 'serving': 100}

    for n in nutrients:
        nutrient_id = n.get('nutrient', {}).get('id')
        if nutrient_id in NUTRIENT_MAP:
            key = NUTRIENT_MAP[nutrient_id]
            macros[key] = n.get('amount', 0)

    return macros