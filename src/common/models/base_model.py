from tortoise import fields


class BaseModel:
    id = fields.CharField(pk=True, max_length=40)
    created_date = fields.DateField(auto_now_add=True)
    created_time = fields.TimeField(auto_now_add=True)
    modified_date = fields.DateField(auto_now=True)
    modified_time = fields.TimeField(auto_now=True)
