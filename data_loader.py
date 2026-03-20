# data_loader.py
# Responsible for loading and querying the food database from the Excel file.

import pandas as pd

_excel_data = pd.read_excel('macros_alimentos.xlsx')
_excel_data['name'] = _excel_data['name'].str.strip()


def get_macros(food: str) -> dict | None:
    """
    Returns a dict with the macros of a food item (per its serving size).
    Returns None if the food is not found in the database.
    """
    row = _excel_data[_excel_data['name'].str.lower() == food.lower()]

    if row.empty:
        print(f"[data_loader] '{food}' not found in database.")
        return None

    return {
        'calories': row['calories'].values[0],
        'fat':      row['fat'].values[0],
        'carbs':    row['carbs'].values[0],
        'fiber':    row['fiber'].values[0],
        'protein':  row['protein'].values[0],
        'serving':  row['serving'].values[0]
    }


def list_foods() -> list[str]:
    """Returns a list of all available food names in the database."""
    return _excel_data['name'].tolist()