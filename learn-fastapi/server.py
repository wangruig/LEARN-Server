# 载入包
import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel


# 创建数据模型
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.get("/")
async  def root():
    return 'Hello World!'


@app.post("/test")
async def fcao_predict(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
        return item_dict


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9876)
