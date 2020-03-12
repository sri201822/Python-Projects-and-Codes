# Query to get region wise total wine reviews
reviews.region_1=reviews.region_1.fillna('Unknown')
reviews_per_region = reviews.groupby('region_1').size().sort_values(ascending=False)

# Alternate way
reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
