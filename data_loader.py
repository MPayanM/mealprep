# data_loader.py
# Queries the FatSecret Platform API for food macros.

import requests
import streamlit as st

TOKEN_URL = "https://oauth.fatsecret.com/connect/token"
BASE_URL  = "https://platform.fatsecret.com/rest/server.api"

CLIENT_ID     = st.secrets["FATSECRET_CLIENT_ID"]
CLIENT_SECRET = st.secrets["FATSECRET_CLIENT_SECRET"]


def _get_token() -> str:
    """Gets an OAuth2 access token from FatSecret."""
    response = requests.post(
        TOKEN_URL,
        data={
            'grant_type':    'client_credentials',
            'scope':         'basic',
            'client_id':     CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }
    )
    return response.json().get('access_token', '')


def search_foods(query: str, max_results: int = 10) -> list[dict]:
    """
    Searches FatSecret for foods matching the query.
    Returns a list of dicts with 'food_id' and 'name'.
    """
    if not query:
        return []

    token = _get_token()

    response = requests.get(
        BASE_URL,
        headers={'Authorization': f'Bearer {token}'},
        params={
            'method':           'foods.search',
            'search_expression': query,
            'max_results':       max_results,
            'format':           'json',
        }
    )

    if response.status_code != 200:
        return []

    data  = response.json()
    foods = data.get('foods', {}).get('food', [])

    if isinstance(foods, dict):
        foods = [foods]

    results = []
    for food in foods:
        results.append({
            'food_id': food['food_id'],
            'name':    food['food_name']
        })

    return results


def get_macros_by_id(food_id: str) -> dict | None:
    """
    Fetches nutritional data for a food by its FatSecret food_id.
    Returns macros per 100g.
    """
    token = _get_token()

    response = requests.get(
        BASE_URL,
        headers={'Authorization': f'Bearer {token}'},
        params={
            'method':  'food.get.v2',
            'food_id': food_id,
            'format':  'json',
        }
    )

    if response.status_code != 200:
        return None

    food      = response.json().get('food', {})
    servings  = food.get('servings', {}).get('serving', [])

    if isinstance(servings, dict):
        servings = [servings]

    # Find the 100g serving or use the first one
    serving = next(
        (s for s in servings if s.get('serving_description') == '100 g'),
        servings[0] if servings else None
    )

    if not serving:
        return None

    # Scale to 100g if needed
    metric_amount = float(serving.get('metric_serving_amount', 100) or 100)
    factor        = 100 / metric_amount

    return {
        'calories': float(serving.get('calories', 0) or 0) * factor,
        'protein':  float(serving.get('protein',  0) or 0) * factor,
        'carbs':    float(serving.get('carbohydrate', 0) or 0) * factor,
        'fat':      float(serving.get('fat',      0) or 0) * factor,
        'fiber':    float(serving.get('fiber',    0) or 0) * factor,
        'serving':  100
    }