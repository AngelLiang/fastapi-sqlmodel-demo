from fastapi import APIRouter, FastAPI

router: APIRouter = APIRouter()

from .apis import *  # noqa


def init_user_router(api: FastAPI, prefix=''):
    api.include_router(router, prefix=prefix)
