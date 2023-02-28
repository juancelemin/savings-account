from fastapi import APIRouter, status


router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={
        404: {"description": "Not found"},
        401: {"description": "Unauthorized"},
    },
)


@router.get("/", status_code=status.HTTP_200_OK)
async def account():
    """

    """
    return {"message": "Hello World"}