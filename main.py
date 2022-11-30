from apify_client import ApifyClient
import os
import pandas as pd

if __name__ == '__main__':
    client = ApifyClient(os.environ['APIFY_TOKEN'], api_url=os.environ['APIFY_API_BASE_URL'])
    dataset_id = client.datasets().get_or_create(name="tryout-dataset")["id"]
    dataset_client = client.dataset(dataset_id)
    counter = 0
    items = []
    for e in range(10):
        items.append({
            "name": f"name_{e}",
            "value": e if e % 2 == 0 else None
        })

    dataframe = pd.DataFrame(items)
    dataset_client.push_items(dataframe.to_dict(orient='records'))
