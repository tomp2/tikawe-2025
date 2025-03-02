from pathlib import Path

POSTS_PER_PAGE = 9

USERNAME_MIN_LEN = 3
USERNAME_MAX_LEN = 16

PASSWORD_MIN_LEN = 8
PASSWORD_MAX_LEN = 128

SECRET_KEY = r"ex-ktvy0*txzma!ql8+)b2o3cg809u3lqa#$3da-%8rpgk-0t$"

DATABASE_PATH = Path("data.db")

USER_IMAGE_UPLOADS_PATH = Path("user_image_uploads")
if not USER_IMAGE_UPLOADS_PATH.exists():
    USER_IMAGE_UPLOADS_PATH.mkdir()
