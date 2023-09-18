from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items")
async def read_items(page: int = Query(1, gt=0), limit: int = Query(10, gt=0)):
    # Fake pagination by slicing a list
    items = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]

    start = (page - 1) * limit
    end = start + limit

    total = 7
    has_next_page = limit * page < total
    return {
        "data": items[start:end],
        "total": total,
        "page_no": page,
        "page_size": limit,
        "has_next_page": has_next_page
    }
