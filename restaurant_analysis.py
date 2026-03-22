"""
Restaurant Data Analysis
========================
A combined analysis pipeline covering:
  - Task 1: Data loading, cleaning & rating distribution
  - Task 2: Statistical summary & categorical distributions
  - Task 3: Geospatial mapping & location-rating correlation
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────

data = pd.read_csv("Dataset .csv")


# ══════════════════════════════════════════════
# TASK 1 — Data Exploration & Cleaning
# ══════════════════════════════════════════════

print("=" * 55)
print("TASK 1: Data Exploration & Cleaning")
print("=" * 55)

# Basic info
print("\n--- Dataset Preview (first 10 rows) ---")
print(data.head(10))

print("\n--- Dataset Info ---")
data.info()

print(f"\nNumber of rows    : {data.shape[0]}")
print(f"Number of columns : {data.shape[1]}")

# Missing values
print("\n--- Missing Values per Column ---")
print(data.isnull().sum())

# Handle missing 'Cuisines'
missing_before = data[data['Cuisines'].isnull()].index.tolist()
print(f"\nRows with missing 'Cuisines' (before): {missing_before}")

data.fillna({'Cuisines': 'Not Specified'}, inplace=True)

missing_after = data[data['Cuisines'].isnull()].index.tolist()
print(f"Rows with missing 'Cuisines' (after) : {missing_after}")

# Rating distribution plot
plt.figure(figsize=(10, 6))
sns.countplot(x='Aggregate rating', data=data, palette='viridis')
plt.title('Distribution of Aggregate Rating')
plt.xlabel('Aggregate Rating')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=55)
plt.tight_layout()
plt.savefig("task1_rating_distribution.png", dpi=150)
plt.show()
print("\nAggregate Rating value counts:")
print(data['Aggregate rating'].value_counts())


# ══════════════════════════════════════════════
# TASK 2 — Statistical Summary & Distributions
# ══════════════════════════════════════════════

print("\n" + "=" * 55)
print("TASK 2: Statistical Summary & Categorical Distributions")
print("=" * 55)

print("\n--- Descriptive Statistics ---")
print(data.describe())

# Top 20 distributions for key categorical columns
categorical_vars = ['Country Code', 'City', 'Cuisines']

for col in categorical_vars:
    plt.figure(figsize=(10, 4))
    value_counts = data[col].value_counts().head(20)
    sns.barplot(x=value_counts.values, y=value_counts.index, palette='viridis')
    plt.title(f"Top 20 {col} Distribution")
    plt.xlabel("Count")
    plt.ylabel(col)
    plt.tight_layout()
    plt.savefig(f"task2_{col.lower().replace(' ', '_')}_distribution.png", dpi=150)
    plt.show()

# Print top counts
print("\nTop 20 Cuisines by Number of Restaurants:")
print(data['Cuisines'].value_counts().head(20))

print("\nTop 20 Cities by Number of Restaurants:")
print(data['City'].value_counts().head(20))


# ══════════════════════════════════════════════
# TASK 3 — Geospatial Mapping & Correlation
# ══════════════════════════════════════════════

print("\n" + "=" * 55)
print("TASK 3: Geospatial Mapping & Location-Rating Correlation")
print("=" * 55)

# Interactive map
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=2)

for _, row in data.iterrows():
    if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=2,
            popup=row['Restaurant Name'],
            color='blue',
            fill=True,
            fill_opacity=0.4
        ).add_to(restaurant_map)

restaurant_map.save("restaurant_locations_map.html")
print("\nInteractive map saved → restaurant_locations_map.html")

# Top cities bar chart
top_cities = data['City'].value_counts().head(15)
plt.figure(figsize=(10, 6))
sns.barplot(y=top_cities.index, x=top_cities.values, palette='mako')
plt.title("Top 15 Cities with Most Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("task3_top_cities.png", dpi=150)
plt.show()

# Top countries bar chart
top_countries = data['Country Code'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y=top_countries.index, x=top_countries.values, palette='rocket')
plt.title("Top 10 Countries by Restaurant Count")
plt.xlabel("Number of Restaurants")
plt.ylabel("Country Code")
plt.tight_layout()
plt.savefig("task3_top_countries.png", dpi=150)
plt.show()

# Correlation: location vs rating
correlation = data[['Latitude', 'Longitude', 'Aggregate rating']].corr()
print("\nCorrelation between Location (Lat/Lon) and Aggregate Rating:")
print(correlation)

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap: Location vs Rating")
plt.tight_layout()
plt.savefig("task3_correlation_heatmap.png", dpi=150)
plt.show()

print("\n✅ Analysis complete. All plots saved as PNG files.")
