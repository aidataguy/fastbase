from tortoise.models import Model
from tortoise import fields

from tortoise.contrib.pydantic import pydantic_model_creator

class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30, nullable=False)
    quantity = fields.IntField(default=0)
    quantity_sold = fields.IntField(default=10)
    price_per_unit = fields.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    revenue = fields.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    supplier = fields.ForeignKeyField("models.Supplier", related_name="supplier")


class Supplier(Model):
    id =fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    manufacturer = fields.CharField(max_length=25)
    email = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=15)


product_pydantic = pydantic_model_creator(Product, name="Product")
product_pydanticIn = pydantic_model_creator(Product, name="ProductIn", exclude_readonly=True)

supplier_pydantic = pydantic_model_creator(Supplier, name="Supplier")
supplier_pydanticIn = pydantic_model_creator(Supplier, name="SupplierIn", exclude_readonly=True)
