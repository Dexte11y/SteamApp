from fastapi import APIRouter

router = APIRouter(
    prefix="users",
    tags="Users"
)

router.get(
    "/get_users"
)
async def get_users():
    pass
