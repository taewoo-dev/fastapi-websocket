from tortoise import fields
from tortoise.models import Model


class RefreshToken(Model):
    refresh_token_id = fields.BigIntField(pk=True)


class User(Model):
    user_id = fields.BinaryField(pk=True, max_length=16)
    allow_notification = fields.BooleanField(null=True)
    birth_date = fields.CharField(max_length=8, null=True)
    created_time = fields.DatetimeField(auto_now_add=True)
    gender = fields.CharField(max_length=16, null=True)
    job = fields.IntField()
    mbti = fields.CharField(max_length=8, null=True)
    nickname = fields.CharField(max_length=16)
    purpose = fields.CharField(max_length=16)
    push_token = fields.CharField(max_length=255, null=True)
    social_id = fields.CharField(max_length=255)
    social_login_type = fields.CharField(max_length=16)
    user_status = fields.BooleanField()
    withdraw_period = fields.DatetimeField(null=True)
    refresh_token = fields.ForeignKeyField(
        "models.RefreshToken", related_name="users", null=True
    )
    is_premium = fields.BooleanField()
    profile_url = fields.CharField(
        max_length=255,
        default="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*dh7Xy5tFvRj7n2wf1UweAw.png",
    )
    premium_started_at = fields.DatetimeField(null=True)
    user_exp = fields.IntField(null=True)
    user_level = fields.IntField(null=True)

    class Meta:
        table = "users"
