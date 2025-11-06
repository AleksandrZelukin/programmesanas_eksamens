from ckanapi import RemoteCKAN

rc = RemoteCKAN('https://data.gov.lv/dati/lv/')
result = rc.action.datastore_search(
    resource_id="277165b4-1a1c-4ebf-a7f4-364f36347128",
    filters={
      "subject": ["watershed", "survey"],
      "stage": "active",
    },
)
print(result['records'])