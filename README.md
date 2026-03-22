# 🍽️ Restaurant Data Analysis

A Python-based data analysis project that explores a restaurant dataset across **three levels of analysis** — from data cleaning and EDA to geospatial visualization and correlation analysis.

---

## 📋 Project Overview

| Task | Focus |
|------|-------|
| **Task 1** | Data loading, cleaning & rating distribution |
| **Task 2** | Statistical summary & categorical distributions |
| **Task 3** | Geospatial mapping & location-rating correlation |

---

## ✨ Features

- 🧹 **Data Cleaning** — Handles missing values in the `Cuisines` column gracefully
- 📊 **EDA** — Distribution plots for ratings, cuisines, cities, and countries
- 🗺️ **Interactive Map** — Folium-based world map of all restaurant locations
- 🔥 **Correlation Heatmap** — Analyzes relationship between location and ratings
- 💾 **Auto-saves** all plots as PNG files for easy reporting

---

## 📂 Project Structure

```
restaurant-data-analysis/
├── restaurant_analysis.py     # Main combined analysis script
├── Dataset .csv               # Input dataset (add your own)
├── requirements.txt           # Dependencies
└── outputs/                   # Auto-generated on run
    ├── task1_rating_distribution.png
    ├── task2_country_code_distribution.png
    ├── task2_city_distribution.png
    ├── task2_cuisines_distribution.png
    ├── task3_top_cities.png
    ├── task3_top_countries.png
    ├── task3_correlation_heatmap.png
    └── restaurant_locations_map.html
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-data-analysis.git
cd restaurant-data-analysis
```

### 2. Set Up a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the Dataset

Place your `Dataset .csv` file in the project root directory.

### 5. Run the Analysis

```bash
python restaurant_analysis.py
```

All plots will be displayed and saved automatically.

---

## 📦 Requirements

```
pandas
matplotlib
seaborn
folium
```

---

## 📊 Sample Outputs

- **Rating Distribution** — Count plot showing how restaurants are distributed across rating values
- **Top 20 Cuisines / Cities / Countries** — Horizontal bar charts for categorical insights
- **Interactive World Map** — HTML map with blue circle markers for every restaurant
- **Correlation Heatmap** — Shows whether latitude/longitude has any influence on ratings

---

## 🛠️ Built With

- [Pandas](https://pandas.pydata.org/) — Data manipulation
- [Matplotlib](https://matplotlib.org/) — Plotting
- [Seaborn](https://seaborn.pydata.org/) — Statistical visualization
- [Folium](https://python-visualization.github.io/folium/) — Interactive maps

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
