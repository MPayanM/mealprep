# data_loader.py
# Loads food database from Excel based on selected language sheet.

import pandas as pd
import unicodedata
import streamlit as st

EXCEL_PATH = 'macros_alimentos.xlsx'


def normalize(text: str) -> str:
    """Removes accents and lowercases text for accent-insensitive comparison."""
    return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode().lower()


@st.cache_data
def load_data(lang: str) -> pd.DataFrame:
    """Loads the food database for the given language sheet (es, fr, en)."""
    df = pd.read_excel(EXCEL_PATH, sheet_name=lang)
    df['name'] = df['name'].str.strip()
    df['name_normalized'] = df['name'].apply(normalize)
    return df


def list_foods(lang: str) -> list[str]:
    """Returns all food names for the given language."""
    return load_data(lang)['name'].tolist()


def get_macros(food: str, lang: str) -> dict | None:
    """Returns macros for a food item. Accent-insensitive. Returns None if not found."""
    df  = load_data(lang)
    row = df[df['name_normalized'] == normalize(food)]

    if row.empty:
        return None

    return {
        'calories': row['calories'].values[0],
        'fat':      row['fat'].values[0],
        'carbs':    row['carbs'].values[0],
        'fiber':    row['fiber'].values[0],
        'protein':  row['protein'].values[0],
        'serving':  row['serving'].values[0],
    }