from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
from typing import List

app = FastAPI()

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017")
db = client["VerseDB"]

# Define Pydantic model for the collection 
class Item(BaseModel):

    surah: int
    ayah: int
    arabic: str
    english: str
    

# Create operation for Anger,Disgust.fear,joy and sad collections
@app.post("/anger/", response_model=dict)
def create_anger_item(item: Item):
    collection1 = db["Anger"]
    inserted_item = collection1.insert_one(item.dict())
    return {"id": str(inserted_item.inserted_id), **item.dict()}

@app.post("/disgust/", response_model=dict)
def create_disgust_item(item: Item):
    collection2 = db["Disgust"]
    inserted_item = collection2.insert_one(item.dict())
    return {"id": str(inserted_item.inserted_id), **item.dict()}

@app.post("/fear/", response_model=dict)
def create_fear_item(item: Item):
    collection3 = db["Fear"]
    inserted_item = collection3.insert_one(item.dict())
    return {"id": str(inserted_item.inserted_id), **item.dict()}

@app.post("/joy/", response_model=dict)
def create_fear_item(item: Item):
    collection4 = db["Joy"]
    inserted_item = collection4.insert_one(item.dict())
    return {"id": str(inserted_item.inserted_id), **item.dict()}

@app.post("/sad/", response_model=dict)
def create_sad_item(item: Item):
    collection5 = db["Sad"]
    inserted_item = collection5.insert_one(item.dict())
    return {"id": str(inserted_item.inserted_id), **item.dict()}


# Delete operation for  Anger,Disgust.fear,joy and sad collections

@app.delete("/anger/{item_id}/", response_model=dict)
def delete_anger_item(item_id: str):
    collection1 = db["Anger"]
    deleted_item = collection1.find_one_and_delete({"_id": ObjectId(item_id)})
    if deleted_item:
        return {"message": "Item deleted successfully", **deleted_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/disgust/{item_id}/", response_model=dict)
def delete_disgust_item(item_id: str):
    collection2 = db["Disgust"]
    deleted_item = collection2.find_one_and_delete({"_id": ObjectId(item_id)})
    if deleted_item:
        return {"message": "Item deleted successfully", **deleted_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
    
@app.delete("/fear/{item_id}/", response_model=dict)
def delete_fear_item(item_id: str):
    collection3 = db["Fear"]
    deleted_item = collection3.find_one_and_delete({"_id": ObjectId(item_id)})
    if deleted_item:
        return {"message": "Item deleted successfully", **deleted_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/joy/{item_id}/", response_model=dict)
def delete_joy_item(item_id: str):
    collection4 = db["Joy"]
    deleted_item = collection4.find_one_and_delete({"_id": ObjectId(item_id)})
    if deleted_item:
        return {"message": "Item deleted successfully", **deleted_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/sad/{item_id}/", response_model=dict)
def delete_sad_item(item_id: str):
    collection5 = db["Sad"]
    deleted_item = collection5.find_one_and_delete({"_id": ObjectId(item_id)})
    if deleted_item:
        return {"message": "Item deleted successfully", **deleted_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
    

# Update operation for  Anger,Disgust.fear,joy and sad collections

@app.put("/anger/{item_id}/", response_model=dict)
def update_anger_item(item_id: str, item: Item):
    collection1 = db["Anger"]
    updated_item = collection1.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": item.dict()},
        return_document="after",
    )
    if updated_item:
        return {"message": "Item updated successfully", **updated_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    

@app.put("/disgust/{item_id}/", response_model=dict)
def update_disgust_item(item_id: str, item: Item):
    collection2 = db["Disgust"]
    updated_item = collection2.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": item.dict()},
        return_document="after",
    )
    if updated_item:
        return {"message": "Item updated successfully", **updated_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
    
    
@app.put("/fear/{item_id}/", response_model=dict)
def update_fear_item(item_id: str, item: Item):
    collection3 = db["Fear"]
    updated_item = collection3.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": item.dict()},
        return_document="after",
    )
    if updated_item:
        return {"message": "Item updated successfully", **updated_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
    
@app.put("/joy/{item_id}/", response_model=dict)
def update_joy_item(item_id: str, item: Item):
    collection4 = db["Joy"]
    updated_item = collection4.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": item.dict()},
        return_document="after",
    )
    if updated_item:
        return {"message": "Item updated successfully", **updated_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
     
@app.put("/sad/{item_id}/", response_model=dict)
def update_sad_item(item_id: str, item: Item):
    collection5 = db["Sad"]
    updated_item = collection5.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": item.dict()},
        return_document="after",
    )
    if updated_item:
        return {"message": "Item updated successfully", **updated_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


# Read operation to retrieve all items from the "Anger" collection

@app.get("/anger/", response_model=List[Item])
def get_all_anger_items():
    collection1 = db["Anger"]
    items = list(collection1.find())
    return items

# Read operation to retrieve all items from the "Disgust" collection

@app.get("/disgust/", response_model=List[Item])
def get_all_disgust_items():
    collection2 = db["Disgust"]
    items = list(collection2.find())
    return items


# Read operation to retrieve all items from the "Fear" collection

@app.get("/fear/", response_model=List[Item])
def get_all_fear_items():
    collection3 = db["Fear"]
    items = list(collection3.find())
    return items

# Read operation to retrieve all items from the "joy" collection

@app.get("/joy/", response_model=List[Item])
def get_all_joy_items():
    collection4 = db["Joy"]
    items = list(collection4.find())
    return items

# Read operation to retrieve all items from the "sad" collection

@app.get("/sad/", response_model=List[Item])
def get_all_sad_items():
    collection4 = db["Sad"]
    items = list(collection4.find())
    return items


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
