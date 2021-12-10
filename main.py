from fastapi import FastAPI, Form, status
from fastapi.responses import JSONResponse
import crud
import uvicorn

app = FastAPI()

# ルート
@app.get("/")
async def root():
    return {"message": "this is root"}

# 特定の登録情報を取得
@app.get("/member")
async def get_member(uuid: str):
    member = await crud.get_member(uuid)
    resp = {
        "status": "ok",
        "data": member
    }
    return resp

# メンバー登録
@app.post("/member")
async def post_member(
    name: str = Form(...)
):
    uuid = await crud.create_member(name)
    return JSONResponse(content={"status": "ok", "uuid": uuid, "name": name}, status_code=status.HTTP_201_CREATED)

# 起動
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
