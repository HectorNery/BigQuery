#Para familiarizarse más con BigQuery, ahora emitirás una consulta 
#en el conjunto de datos públicos de GitHub . 
#Encontrarás los mensajes de confirmación más comunes en GitHub. 
#También usarás la consola web de BigQuery para obtener una vista previa 
#y ejecutar consultas ad-hoc.

#Para ver como se ven os datos abre el conjunto de datos Github
#En la la vista gráfica de BigQueary
#https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=github_repos&t=commits&page=table

#Para ver cómo se ven los datos, abra el conjunto de datos 
#de GitHub en la IU web de BigQuery:
    
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

print(f'{"Anio":<10} | {"CategoriaPrincipal":<25} | {"Distrito":<25} | {"TotalDelitos":>15}')
print("-" * 90)

for row in results:
    Anio = row['Anio']
    CategoriaPrincipal = row['CategoriaPrincipal']
    Distrito = row['Distrito']
    TotalDelitos = row['TotalDelitos']
    print(f'{Anio:<10} | {CategoriaPrincipal:<25} | {Distrito:<25} | {TotalDelitos:>15,}')
