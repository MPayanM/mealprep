# tracker.py
# Core tracking logic. The DayTracker class manages a full day's meals
# and computes nutritional totals without relying on global state.

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
    Macros are scaled by grams entered relative to the 100g serving base.
    """

    def __init__(self):
        self.meals: dict[str, list] = {meal: [] for meal in VALID_MEALS}

    def add(self, meal_name: str, food: str, grams: float,
            macros_per_100g: dict) -> None:
        """
        Adds a food item to a meal.
        macros_per_100g: dict with calories, protein, carbs, fat, fiber
        (all values are per 100g, serving field is ignored)
        """
        if meal_name not in self.meals:
            print(f"[tracker] '{meal_name}' is not a valid meal.")
            return

        factor = grams / 100.0
        scaled = {key: macros_per_100g.get(key, 0) * factor
                  for key in EMPTY_TOTALS}

        self.meals[meal_name].append({
            'food':   food,
            'grams':  grams,
            'macros': scaled
        })

    def get_totals(self) -> dict:
        """Returns summed nutritional totals for the full day."""
        totals = dict(EMPTY_TOTALS)
        for meal_items in self.meals.values():
            for item in meal_items:
                for key in totals:
                    totals[key] += item['macros'][key]
        return totals

    def show_meals(self) -> None:
        """Prints a readable summary of all meals."""
        for meal_name in VALID_MEALS:
            items = self.meals[meal_name]
            print(f"\n  {meal_name.upper()}:")
            if not items:
                print("    (no foods added)")
            else:
                for item in items:
                    print(f"    - {item['grams']:.0f}g of {item['food']}")