# Introducing ENV
import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from manufacturer.supplier import api_router


from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

app = FastAPI()

app.include_router(api_router, prefix='')



register_tortoise(
    app,
    db_url =os.environ.get("DB_URI"),
    modules={'models':['models.supplier_model',]},
    generate_schemas=True,
    add_exception_handlers=True
)