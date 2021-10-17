from fastapi import Request, FastAPI

app = FastAPI()
DATA = 'Standard response'

@app.get('/')
async def root():
    return DATA

@app.post('/')
async def post_data(request: Request):
    global DATA
    DATA = await request.body()
    return 'Everything is OK!'

#Uruchami sie poleceniem:
# uvicorn main:app --reload