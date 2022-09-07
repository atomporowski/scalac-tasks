from fastapi import FastAPI

import scraper

app = FastAPI()


@app.get("/")
async def read_list():
    return scraper.jokes_list


@app.get("/{id}")
async def read_item(id: int):
    for i in scraper.jokes_list:
        if int(i['id']) == id:
            return i
