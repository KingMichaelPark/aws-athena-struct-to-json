# AWS Athena Table Schema to JSON

Two scripts to assist you in converting a massive struct blob of text to
something sortable and "diff-erable."

I'll get around to packaging this later, for now just add the convert.py to your
project, it has no dependencies.

## Usage

```py
from convert import clean_struct

import boto3

session = boto3.session.Session(profile_name="YOUR_AWS_CREDENTIALS_PROFILE")


client = session.client("athena")
table_metadata_columns = client.get_table_metadata(
    CatalogName="AwsDataCatalog", DatabaseName="DatabaseName", TableName="TableName"
)["TableMetadata"]["Columns"]
struct_field = table_metadata_columns[0]["Type"]
json_field = clean_struct(struct_field)
```
