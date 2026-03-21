# i18n/translations.py
# All UI text in Spanish, French, and English.

TRANSLATIONS = {
    'es': {
        # General
        'app_title':   '🥗 Meal Prep Tracker',
        'app_caption': 'Sigue tus macros diarios contra tus objetivos nutricionales personalizados.',

        # Language selector
        'change_language': 'Cambiar idioma',

        # Tabs
        'tab_profile': '👤  Perfil & Objetivos',
        'tab_menu':    '🍽️  Menú Diario',

        # Profile
        'profile_title':   'Tu Perfil',
        'profile_caption': 'Completa tus datos. Tus objetivos nutricionales se calculan automáticamente.',
        'weight':          'Peso (kg)',
        'height':          'Altura (cm)',
        'age':             'Edad',
        'sex':             'Sexo biológico',
        'sex_male':        'masculino',
        'sex_female':      'femenino',
        'activity':        'Nivel de actividad',
        'goal':            'Objetivo',
        'save_profile':    '💾  Guardar perfil',
        'profile_saved':   'Perfil guardado. Tus objetivos fueron actualizados.',
        'activity_options': {
            'sedentary':   'Sedentario (trabajo de escritorio, sin ejercicio)',
            'light':       'Ligeramente activo (1–3 días/semana)',
            'moderate':    'Moderadamente activo (3–5 días/semana)',
            'active':      'Muy activo (6–7 días/semana)',
            'very_active': 'Extremadamente activo (trabajo físico + entrenamiento)',
        },
        'objective_options': {
            'cut':      'Definición (perder grasa · −300 kcal)',
            'maintain': 'Mantenimiento (peso actual)',
            'bulk':     'Volumen (ganar músculo · +300 kcal)',
        },

        # Goals
        'targets_title':   '📌 Tus objetivos diarios',
        'targets_caption': 'Calculados con la ecuación de Mifflin-St Jeor.',
        'based_on':        'Basado en tu perfil',

        # Menu
        'menu_title':   '🍽️ Construye tu menú',
        'menu_caption': 'Agrega alimentos a cada comida. Los gráficos se actualizan automáticamente.',
        'menu_tip':     '👉 Las cantidades son en gramos : 1 x 🥚 ~ 50 g',
        'search_placeholder': 'ej. pollo, avena, huevo...',
        'no_results':   'Sin resultados. Intenta con otro término.',
        'add_btn':      '＋ Agregar',
        'remove_btn':   '✕',
        'meal_labels': {
            'breakfast': '🌅 Desayuno',
            'snack_1':   '🍎 Merienda 1',
            'lunch':     '🍽️ Almuerzo',
            'snack_2':   '🥜 Merienda 2',
            'diner':     '🌙 Cena',
        },

        # Charts
        'live_results':    '📊 Resultados en vivo',
        'macros_vs_goals': 'Macros vs. Objetivos (g)',
        'macro_dist':      'Distribución de macros (% kcal)',
        'calories':        'Calorías',
        'protein':         'Proteína',
        'carbs':           'Carbohidratos',
        'fat':             'Grasa',
        'within_target':   'Dentro del objetivo',
        'below_target':    'Por debajo del objetivo',
        'over_limit':      'Por encima del límite',
        'add_foods_chart': 'Agrega alimentos para ver la distribución',
        'min_label':       'Mín',
        'max_label':       'Máx',
    },

    'fr': {
        # General
        'app_title':   '🥗 Meal Prep Tracker',
        'app_caption': 'Suivez vos macros quotidiens par rapport à vos objectifs nutritionnels personnalisés.',

        # Language selector
        'change_language': 'Changer de langue',

        # Tabs
        'tab_profile': '👤  Profil & Objectifs',
        'tab_menu':    '🍽️  Menu Quotidien',

        # Profile
        'profile_title':   'Votre Profil',
        'profile_caption': 'Remplissez vos données. Vos objectifs nutritionnels sont calculés automatiquement.',
        'weight':          'Poids (kg)',
        'height':          'Taille (cm)',
        'age':             'Âge',
        'sex':             'Sexe biologique',
        'sex_male':        'masculin',
        'sex_female':      'féminin',
        'activity':        'Niveau d\'activité',
        'goal':            'Objectif',
        'save_profile':    '💾  Sauvegarder le profil',
        'profile_saved':   'Profil sauvegardé. Vos objectifs ont été mis à jour.',
        'activity_options': {
            'sedentary':   'Sédentaire (bureau, sans sport)',
            'light':       'Légèrement actif (1–3 jours/semaine)',
            'moderate':    'Modérément actif (3–5 jours/semaine)',
            'active':      'Très actif (6–7 jours/semaine)',
            'very_active': 'Extrêmement actif (travail physique + entraînement)',
        },
        'objective_options': {
            'cut':      'Sèche (perdre de la graisse · −300 kcal)',
            'maintain': 'Maintien (poids actuel)',
            'bulk':     'Prise de masse (gagner du muscle · +300 kcal)',
        },

        # Goals
        'targets_title':   '📌 Vos objectifs quotidiens',
        'targets_caption': 'Calculés avec l\'équation de Mifflin-St Jeor.',
        'based_on':        'Basé sur votre profil',

        # Menu
        'menu_title':   '🍽️ Construisez votre menu',
        'menu_caption': 'Ajoutez des aliments à chaque repas. Les graphiques se mettent à jour automatiquement.',
        'menu_tip':     '👉 Les quantités sont en grammes : 1 x 🥚 ~ 50 g',
        'search_placeholder': 'ex. poulet, flocons d\'avoine, œuf...',
        'no_results':   'Aucun résultat. Essayez un autre terme.',
        'add_btn':      '＋ Ajouter',
        'remove_btn':   '✕',
        'meal_labels': {
            'breakfast': '🌅 Petit-déjeuner',
            'snack_1':   '🍎 Goûter 1',
            'lunch':     '🍽️ Déjeuner',
            'snack_2':   '🥜 Goûter 2',
            'diner':     '🌙 Dîner',
        },

        # Charts
        'live_results':    '📊 Résultats en direct',
        'macros_vs_goals': 'Macros vs. Objectifs (g)',
        'macro_dist':      'Distribution des macros (% kcal)',
        'calories':        'Calories',
        'protein':         'Protéines',
        'carbs':           'Glucides',
        'fat':             'Lipides',
        'within_target':   'Dans l\'objectif',
        'below_target':    'En dessous de l\'objectif',
        'over_limit':      'Au-dessus de la limite',
        'add_foods_chart': 'Ajoutez des aliments pour voir la distribution',
        'min_label':       'Min',
        'max_label':       'Max',
    },

    'en': {
        # General
        'app_title':   '🥗 Meal Prep Tracker',
        'app_caption': 'Track your daily macros against personalized nutritional goals.',

        # Language selector
        'change_language': 'Change language',

        # Tabs
        'tab_profile': '👤  Profile & Goals',
        'tab_menu':    '🍽️  Daily Menu',

        # Profile
        'profile_title':   'Your Profile',
        'profile_caption': 'Fill in your data. Your nutritional goals are calculated automatically.',
        'weight':          'Weight (kg)',
        'height':          'Height (cm)',
        'age':             'Age',
        'sex':             'Biological sex',
        'sex_male':        'male',
        'sex_female':      'female',
        'activity':        'Activity level',
        'goal':            'Goal',
        'save_profile':    '💾  Save Profile',
        'profile_saved':   'Profile saved! Your goals have been updated.',
        'activity_options': {
            'sedentary':   'Sedentary (desk job, no exercise)',
            'light':       'Lightly active (1–3 days/week)',
            'moderate':    'Moderately active (3–5 days/week)',
            'active':      'Very active (6–7 days/week)',
            'very_active': 'Extremely active (physical job + training)',
        },
        'objective_options': {
            'cut':      'Cut (lose fat · −300 kcal deficit)',
            'maintain': 'Maintain (stay at current weight)',
            'bulk':     'Bulk (gain muscle · +300 kcal surplus)',
        },

        # Goals
        'targets_title':   '📌 Your Daily Targets',
        'targets_caption': 'Calculated from your profile using the Mifflin-St Jeor equation.',
        'based_on':        'Based on your profile',

        # Menu
        'menu_title':   '🍽️ Build Your Menu',
        'menu_caption': 'Add foods to each meal. Charts update automatically.',
        'menu_tip':     '👉 Quantities are in grams : 1 x 🥚 ~ 50 g',
        'search_placeholder': 'e.g. chicken breast, oats, egg...',
        'no_results':   'No results found. Try a different search.',
        'add_btn':      '＋ Add',
        'remove_btn':   '✕',
        'meal_labels': {
            'breakfast': '🌅 Breakfast',
            'snack_1':   '🍎 Snack 1',
            'lunch':     '🍽️ Lunch',
            'snack_2':   '🥜 Snack 2',
            'diner':     '🌙 Dinner',
        },

        # Charts
        'live_results':    '📊 Live Results',
        'macros_vs_goals': 'Macros vs. Goals (g)',
        'macro_dist':      'Macro Distribution (% kcal)',
        'calories':        'Calories',
        'protein':         'Protein',
        'carbs':           'Carbs',
        'fat':             'Fat',
        'within_target':   'Within target',
        'below_target':    'Below target',
        'over_limit':      'Over limit',
        'add_foods_chart': 'Add foods to see distribution',
        'min_label':       'Min',
        'max_label':       'Max',
    },
}