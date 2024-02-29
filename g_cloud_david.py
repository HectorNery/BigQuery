from google.cloud import bigquery

client = bigquery.Client()

query = """
    SELECT
  year AS Anio,
  major_category AS CategoriaPrincipal,
  borough AS Distrito,
  SUM(value) AS TotalDelitos
FROM
  bigquery-public-data.london_crime.crime_by_lsoa
WHERE
  year IS NOT NULL
  AND major_category IS NOT NULL
  AND borough IS NOT NULL
GROUP BY
  Anio, CategoriaPrincipal, Distrito
ORDER BY
  Anio, TotalDelitos DESC;
"""

results = client.query(query)

for row in results:
    state = row['state']
    gender = row['gender']
    total_people = row['total_people']
    print(f'{state:<2} | {gender:<6} | {total_people:>9,}')