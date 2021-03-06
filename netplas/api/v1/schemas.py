import coreapi
import coreschema
from rest_framework.schemas import ManualSchema


RegisterSchema = ManualSchema(fields=[
    coreapi.Field(
        'name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'surname',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'type',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'password',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'password_again',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'secret_answer',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


LoginSchema = ManualSchema(fields=[
    coreapi.Field(
        'email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'password',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


ProductInfoSchema = ManualSchema(fields=[
    coreapi.Field(
        'product_name',
        required=True,
        location="query",
        schema=coreschema.String()
    ),
])


RawInfoSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw_name',
        required=True,
        location="query",
        schema=coreschema.String()
    ),
])


CreateProductStockSchema = ManualSchema(fields=[
    coreapi.Field(
        'product_stock_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])

UpdateProductStockSchema = ManualSchema(fields=[
    coreapi.Field(
        'name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])

CreateRawStockSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw_stock_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])

ProductAttrCreateSchema = ManualSchema(fields=[
    coreapi.Field(
        'product_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'value',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


CreateProductSchema = ManualSchema(fields=[
    coreapi.Field(
        name='product_stock_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='product_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'unit_price',
        required=True,
        location="form",
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        'amount',
        required=False,
        location="form",
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        'product_attr',
        required=False,
        location='form',
        schema=coreschema.Array()
    )
])


UpdateProductSchema = ManualSchema(fields=[
    coreapi.Field(
        name='product_stock_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'unit_price',
        required=True,
        location="form",
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        'amount',
        required=False,
        location="form",
        schema=coreschema.Integer()
    )
])

CreateProductTemplateSchema = ManualSchema(fields=[
    coreapi.Field(
        name='product_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='raw_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        name='quantity',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


CreateRawSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw_stock_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'raw_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'unit_price',
        required=True,
        location="form",
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        'amount',
        required=True,
        location="form",
        schema=coreschema.Integer()
    ),
])

UpdateRawSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw_stock_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'unit_price',
        required=True,
        location="form",
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        'amount',
        required=True,
        location="form",
        schema=coreschema.Integer()
    ),
])


CreateClientSchema = ManualSchema(fields=[
    coreapi.Field(
        'email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'surname',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'phone',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'address',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'company',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


CreateSupplierSchema = ManualSchema(fields=[
    coreapi.Field(
        'email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'surname',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'phone',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'address',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'company',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


CreateProductOrderSchema = ManualSchema(fields=[
    coreapi.Field(
        'client_email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'product_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'user_email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'order_title',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'quantity',
        required=True,
        location="form",
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        'status',
        required=False,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'delivery_date',
        required=False,
        location="form",
        schema=coreschema.String()
    )
])


CreateRawOrderSchema = ManualSchema(fields=[
    coreapi.Field(
        'supplier_email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'raw_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'user_email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'order_title',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'quantity',
        required=True,
        location="form",
        schema=coreschema.Integer()
    ),
    coreapi.Field(
        'status',
        required=False,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'delivery_date',
        required=False,
        location="form",
        schema=coreschema.String()
    )
])


DamagedCreateRawOrderSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


DamagedCreateProductOrderSchema = ManualSchema(fields=[
    coreapi.Field(
        'product_name',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


UpdatePassword = ManualSchema(fields=[
    coreapi.Field(
        'email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'secret_answer',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'new_password',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'new_password_again',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])


NotAuthenticatedUpdatePassword = ManualSchema(fields=[
    coreapi.Field(
        'email',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'secret_answer',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'new_password',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'new_password_again',
        required=True,
        location="form",
        schema=coreschema.String()
    ),
])
