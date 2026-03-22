# 🥗 Meal Prep Tracker

A multilingual web app to plan daily meals, track macronutrient intake in real time, and compare results against personalized nutritional goals — accessible from any browser, no installation required.

🌐 **Live app:** [mpayanm-mealprep.streamlit.app](https://mpayanm-mealprep.streamlit.app)

---

## Features

- 🌍 **Multilingual** — available in Spanish, French, and English
- 🧮 **Personalized goals** — calculated automatically from your profile (weight, height, age, sex, activity level, objective) using the Mifflin-St Jeor equation
- 🍽️ **Interactive menu builder** — build your daily meals with an accent-insensitive food search
- 📊 **Live charts** — bar chart and macro pie chart update in real time as you add foods
- ✅ **Instant feedback** — color-coded indicators show whether you're within your targets

---

## Project Structure
```
mealprep/
├── app.py                   # Entry point — language selector, tabs, layout
├── data_loader.py           # Food database loader (Excel → pandas, accent-insensitive)
├── tracker.py               # Core tracking logic (DayTracker class)
├── goals.py                 # Goal calculation (TDEE + macro distribution)
├── ui/
│   ├── ui_profile.py        # Profile & Goals tab
│   ├── ui_menu.py           # Daily Menu builder
│   └── ui_charts.py        # Live Plotly charts
├── i18n/
│   └── translations.py      # All UI text in ES, FR, EN
├── macros_alimentos.xlsx    # Food database (3 sheets: es, fr, en)
├── requirements.txt
└── Historic/                # Past meal screenshots
```

---

## Installation (local)

### 1. Clone the repository
```bash
git clone https://github.com/MPayanM/mealprep.git
cd mealprep
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run
```bash
streamlit run app.py
```

---

## How It Works

1. Select your language — Spanish 🇨🇴, French 🇫🇷, or English 🇬🇧
2. Fill in your profile — the app calculates your personalized daily targets automatically
3. Build your daily menu — search foods, set portions in grams, and watch the charts update live
4. Check your results — color-coded indicators and interactive charts show your macro distribution

---

## Food Database

The food database lives in `macros_alimentos.xlsx`, which contains three sheets — one per language (`es`, `fr`, `en`) — with the same foods and nutritional values, only the names translated.

Each sheet contains the following columns:

| Column     | Description                     |
|------------|---------------------------------|
| `name`     | Food name (used for search)     |
| `calories` | kcal per 100g                   |
| `protein`  | Protein in grams per 100g       |
| `carbs`    | Carbohydrates in grams per 100g |
| `fat`      | Fat in grams per 100g           |
| `fiber`    | Fiber in grams per 100g         |
| `serving`  | Reference serving size (100g)   |

To add new foods, add a row to each of the three sheets with the translated name and the same nutritional values.

> **Note on the food database:** The multilingual Excel approach was chosen after evaluating several nutrition APIs. No free API was found that provided reliable, specific macronutrient data without IP restrictions or paywalled core fields (calories, protein). The manual database limits the food selection to items personally curated, but ensures data quality and consistency. This project can serve as a base for a more scalable version backed by a paid API such as Edamam or FatSecret.

---

## Goal Calculation

Goals are derived from your profile using the **Mifflin-St Jeor** equation:

- **BMR** → based on weight, height, age and sex
- **TDEE** → BMR × activity factor
- **Target calories** → TDEE ± objective adjustment (cut: −300, maintain: 0, bulk: +300)
- **Protein** → 1.8–2.2 g/kg bodyweight
- **Fat** → ~25% of target calories
- **Carbs** → remaining calories after protein and fat

---

## Tech Stack

| Library      | Purpose                              |
|--------------|--------------------------------------|
| `streamlit`  | Web app framework                    |
| `plotly`     | Interactive charts                   |
| `pandas`     | Food database (Excel reading)        |
| `openpyxl`   | Excel file engine for pandas         |

---

## License

Personal project — feel free to fork and adapt.