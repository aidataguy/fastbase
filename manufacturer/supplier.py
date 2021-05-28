from fastapi import APIRouter, HTTPException
from models.supplier_model import *


api_router = APIRouter()

@api_router.get('/')
def index():
    return {'msg': "go to /docs for swagger documentation"}



@api_router.post('/supplier/register')
async def add_supplier(supplier_details: supplier_pydanticIn):
    supplier_obj = await Supplier.create(**supplier_details.dict(exclude_unset=True))
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {'status': "ok", "data": response}


@api_router.get('/suppliers')
async def get_all_suppliers():
    response = await supplier_pydantic.from_queryset(Supplier.all())
    return {'status': "ok", "data": response}

@api_router.get('/supplier/{supplier_id}')
async def get_supplier_detail(supplier_id: int):
    response = await supplier_pydantic.from_queryset_single(Supplier.get(id=supplier_id))
    return {'status': 'ok', 'data': response}

@api_router.put('/supplier/{supplier_id}')
async def update_supplier(supplier_id: int, update_info: supplier_pydanticIn):
    supplier = await Supplier.get(id=supplier_id)
    update_info = update_info.dict(exclude_unset=True)
    supplier.name = update_info['name']
    supplier.manufacturer = update_info['manufacturer']
    supplier.email = update_info['email']
    supplier.phone = update_info['phone']
 
    await supplier.save()


    response = await supplier_pydantic.from_tortoise_orm(supplier)

    return {'status': 'ok', 'data': response}


@api_router.delete('/supplier/{id}')
async def remove_supplier(supplier_id: int):
    supplier = await Supplier.get(id=supplier_id).delete

    response = await supplier_pydantic.from_tortoise_orm(supplier)
    
    return {'status': 'ok', 'data': response}


