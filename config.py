from pathlib import Path


SECRET_KEY = r"ex-ktvy0*txzma!ql8+)b2o3cg809u3lqa#$3da-%8rpgk-0t$"

DATABASE_PATH = Path("data.db")

USER_IMAGE_UPLOADS_PATH = Path("user_image_uploads")
if not USER_IMAGE_UPLOADS_PATH.exists():
    USER_IMAGE_UPLOADS_PATH.mkdir()
