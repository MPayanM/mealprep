# goals.py
# Calculates personalized nutritional goals based on user profile.
# Formula: Mifflin-St Jeor for TDEE + macro distribution by objective.

ACTIVITY_FACTORS = {
    'sedentary':   1.2,
    'light':       1.375,
    'moderate':    1.55,
    'active':      1.725,
    'very_active': 1.9,
}

OBJECTIVE_ADJUSTMENTS = {
    'cut':      -300,
    'maintain':    0,
    'bulk':     +300,
}


def calculate_bmr(weight_kg: float, height_cm: float, age: int, sex: str) -> float:
    """Basal Metabolic Rate — Mifflin-St Jeor. sex: 'male' or 'female'"""
    if sex == 'male':
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161


def calculate_goals(profile: dict) -> dict:
    """
    Takes a user profile dict and returns personalized daily nutritional goals
    as min/max ranges — same structure as the original user_goals dict.

    Profile keys: weight_kg, height_cm, age, sex, activity, objective
    """
    bmr    = calculate_bmr(profile['weight_kg'], profile['height_cm'],
                           profile['age'], profile['sex'])
    tdee   = bmr * ACTIVITY_FACTORS[profile['activity']]
    target = tdee + OBJECTIVE_ADJUSTMENTS[profile['objective']]

    # Calorie range: ±100 kcal around target
    cal_min  = round(target - 100)
    cal_max  = round(target + 100)

    # Protein: 1.8–2.2 g/kg bodyweight
    w        = profile['weight_kg']
    prot_min = round(w * 1.8)
    prot_max = round(w * 2.2)

    # Fat: 25% of target calories
    fat_cals = target * 0.25
    fat_min  = round(fat_cals * 0.9 / 9)
    fat_max  = round(fat_cals * 1.1 / 9)

    # Carbs: remaining calories after protein and fat
    prot_mid  = (prot_min + prot_max) / 2
    fat_mid   = (fat_min  + fat_max)  / 2
    remaining = target - (prot_mid * 4) - (fat_mid * 9)
    carb_min  = round((remaining - 50) / 4)
    carb_max  = round((remaining + 50) / 4)

    return {
        'calories_min': cal_min,
        'calories_max': cal_max,
        'protein_min':  prot_min,
        'protein_max':  prot_max,
        'fat_min':      fat_min,
        'fat_max':      fat_max,
        'carbs_min':    carb_min,
        'carbs_max':    carb_max,
    }


def evaluate_totals(totals: dict, user_goals: dict) -> list[str]:
    """
    Compares the day's totals against user_goals.
    Returns a list of status messages, one per nutrient.
    """
    messages = []
    checks = [
        ('calories', 'Calories',      'kcal', '.0f'),
        ('protein',  'Protein',       'g',    '.1f'),
        ('fat',      'Fat',           'g',    '.1f'),
        ('carbs',    'Carbohydrates', 'g',    '.1f'),
    ]
    for key, label, unit, fmt in checks:
        value     = totals[key]
        min_v     = user_goals[f'{key}_min']
        max_v     = user_goals[f'{key}_max']
        formatted = format(value, fmt)

        if value < min_v:
            messages.append(f"{label} below target: {formatted}{unit} (min {min_v})")
        elif value > max_v:
            messages.append(f"{label} over limit:   {formatted}{unit} (max {max_v})")
        else:
            messages.append(f"{label} within target ({formatted}{unit})")

    return messages