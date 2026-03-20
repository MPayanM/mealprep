# tracker.py
# Core tracking logic. The DayTracker class manages a full day's meals
# and computes nutritional totals without relying on global state.

from data_loader import get_macros

VALID_MEALS = ['breakfast', 'snack_1', 'lunch', 'snack_2', 'diner']

EMPTY_TOTALS = {
    'calories': 0.0,
    'fat':      0.0,
    'carbs':    0.0,
    'fiber':    0.0,
    'protein':  0.0
}


class DayTracker:
    """
    Tracks all meals and their nutritional content for a single day.
    Instantiate a new DayTracker for each day — no global state, no resets needed.
    """

    def __init__(self):
        # Each meal is a list of dicts: {'food': str, 'grams': float, 'macros': dict}
        self.meals: dict[str, list] = {meal: [] for meal in VALID_MEALS}

    def add(self, meal_name: str, food: str, grams: float) -> None:
        """Adds a food item (in grams) to a specific meal."""
        if meal_name not in self.meals:
            print(f"[tracker] '{meal_name}' is not a valid meal. Options: {VALID_MEALS}")
            return

        macros = get_macros(food)
        if macros is None:
            return

        factor = grams / macros['serving']
        scaled = {key: macros[key] * factor for key in EMPTY_TOTALS}

        self.meals[meal_name].append({
            'food':   food,
            'grams':  grams,
            'macros': scaled
        })

    def get_totals(self) -> dict:
        """Returns a dict with the summed nutritional totals for the full day."""
        totals = dict(EMPTY_TOTALS)  # fresh copy

        for meal_items in self.meals.values():
            for item in meal_items:
                for key in totals:
                    totals[key] += item['macros'][key]

        return totals

    def show_meals(self) -> None:
        """Prints a readable summary of all meals and their contents."""
        for meal_name in VALID_MEALS:
            items = self.meals[meal_name]
            print(f"\n  {meal_name.upper()}:")
            if not items:
                print("    (no foods added)")
            else:
                for item in items:
                    print(f"    - {item['grams']:.0f}g of {item['food']}")