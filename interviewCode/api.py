import fastapi

from fastapi import FastAPI

from parser import *

from pydantic import BaseModel

import uvicorn

app = FastAPI()


# Request model for POST
class UpdateRequest(BaseModel):
    new_text: str

# GET: Return the current markdown
@app.get("/")
def get_markdown():
    data_json = get_json()
    markdown_content = json_to_md(data_json)
    return {"markdown": markdown_content}

# POST: Append new text to markdown and return the updated content
@app.post("/")
def update_markdown(update: UpdateRequest):
    data_json = get_json()
    updated_markdown = update_json(update.new_text, data_json)
    return {"updated_markdown" : updated_markdown}


# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

