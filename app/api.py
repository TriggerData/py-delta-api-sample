import json

import pyarrow as pa
from pydantic import BaseModel
from deltalake import DeltaTable
from deltalake.writer import write_deltalake
from fastapi import FastAPI

app = FastAPI()

# Azurite configuration
storage_options = {
    "AZURE_STORAGE_USE_EMULATOR": "true",
    "AZURE_ACCOUNT_NAME": "devstoreaccount1",
    "AZURE_ACCESS_KEY": "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==",
}

# Pre-requisite: "sandbox" is a container in your devstoreaccount1
table_uri = "az://sandbox/delta_table"


class Dataset(BaseModel):
    x: int
    y: int


def persist_table(item: Dataset, mode: str):
    request_df = pa.Table.from_pylist([item.model_dump()])

    write_deltalake(table_or_uri=table_uri,
                    data=request_df,
                    mode=mode,
                    overwrite_schema=True,
                    storage_options=storage_options)

    return json.loads(item.model_dump_json())


@app.post("/create")
def create_delta_table(item: Dataset):
    return persist_table(item, "overwrite")


@app.get("/read")
def read_delta_table():
    df_json = DeltaTable(table_uri=table_uri, 
                         storage_options=storage_options).to_pandas().to_json(orient="records")

    return json.loads(df_json)


@app.post("/append")
def append_delta_table(item: Dataset):
    return persist_table(item, "append")
