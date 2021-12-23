import json
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
 
with open("promosi.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

@app.get('/')
def home() :
    return {"Welcome to my api"}
    
@app.get('/promosi/', tags=["promosi"])
async def read_all_promosi():
    return data

@app.get('/promosi/{item_id}', tags=["promosi"])
async def read_promosi(item_id: int):
    for promosi_item in data['promosi']:
        if promosi_item['id'] ==item_id:
            return promosi_item
    raise HTTPException(
        status_code =404, detail=f'"Item not found'
    )

@app.post('/promosi',tags=["promosi"])
async def post_promosi(name:str, jumlah:int):
    id = 100
    if (len(data['promosi'])>0) :
        id=data['promosi'][len(data['promosi'])-1]['id']+1
    new_data ={'id':id, 'name':name, 'jumlah':jumlah}
    data['promosi'].append(dict(new_data))
    read_file.close()
    with open("promosi.json", "w") as write_file:
        json.dump(data,write_file,indent=4)
    write_file.close()

    return (new_data)

    raise HTTPEXCEPTION(
        status_code=500, detail=f'Internal server error'
    )

@app.put('/promosi/{item_id}',tags=["promosi"])
async def update_promosi(item_id: int, name: str, jumlah: int):
    for promosi_item in data['promosi']:
        if promosi_item['id'] == item_id:
            promosi_item['name'] = name
            promosi_item['jumlah'] = jumlah
            read_file.close()
            with open("promosi.json", "w") as write_file:
                json.dump(data,write_file,indent=4)
            write_file.close()
            
            return{"message":"Data updated"}
    raise HTTPException(
        status_code =404, detail=f'"Item not found'
    )

    
@app.delete('/promosi/{item_id}',tags=["promosi"])
async def delete_promosi(item_id: int):
    for promosi_item in data['promosi']:
        if promosi_item['id'] == item_id:
            data['promosi'].remove(promosi_item)
            read_file.close()
            with open("promosi.json", "w") as write_file:
                json.dump(data,write_file,indent=4)
            write_file.close()
            
            return{"message":"Data deleted"}
    raise HTTPException(
        status_code =404, detail=f'"Item not found'
    ) 