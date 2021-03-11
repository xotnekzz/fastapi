from typing import Optional

from fastapi.responses import StreamingResponse
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI
import pandas as pd
import io

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items2/{item_id}", response_class=PlainTextResponse)
def read_item(item_id: int, q: Optional[str] = None):
    df = pd.DataFrame({'id':[1,2], 'name':['ts','yj']})
    stream = io.StringIO()

    df.to_csv(stream, index = False)

    response = StreamingResponse(iter([stream.getvalue()]),
                        media_type="text/csv"
    )

    response.headers["Content-Disposition"] = "attachment; filename=export.csv"

    return response
