from fastapi import APIRouter, FastAPI

router: APIRouter = APIRouter()

from .apis import *  # noqa


def init_course_router(api: FastAPI, prefix=''):
    api.include_router(router, prefix=prefix)
