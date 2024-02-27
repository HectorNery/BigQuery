from google.cloud import bigquery

client = bigquery.Client()

query = """
    SELECT state, gender, COUNT(*) AS total_people
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    GROUP BY state, gender
    ORDER BY state, gender
"""

results = client.query(query)

for row in results:
    state = row['state']
    gender = row['gender']
    total_people = row['total_people']
    print(f'{state:<2} | {gender:<6} | {total_people:>9,}')