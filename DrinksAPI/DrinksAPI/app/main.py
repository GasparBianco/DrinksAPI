from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routers import categories, cocktails, glasses, ingredients


app = FastAPI()

app.include_router(categories.router)
app.include_router(cocktails.router)
app.include_router(ingredients.router)
app.include_router(glasses.router)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
