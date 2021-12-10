from fastapi import HTTPException, status
from firebase import db
from uuid import uuid4

# 特定の登録情報を取得
async def get_member(uuid: str):
    docs = db.collection("members").where("uuid", "==", uuid).stream()
    data = []
    for doc in docs:
        post = {"id": doc.id, **doc.to_dict()}
        data.append(post)
    if len(data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="このIDは見つかりません")
    return data

# メンバー登録
async def create_member(name: str) -> str:
    uuid = str(uuid4())
    doc_ref = db.collection("members").document()
    doc_ref.set({
        "uuid": uuid,
        "name": name,
    })
    return uuid