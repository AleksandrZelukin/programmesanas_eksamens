from ckanapi import RemoteCKAN

rc = RemoteCKAN('https://data.gov.lv/dati/lv/', apikey=API_TOKEN)
result = rc.action.datastore_search_sql(
    sql="""SELECT * from "132dc234-4240-47af-a711-673e58a8a894" WHERE title LIKE 'jones'"""
)
print(result['records'])
