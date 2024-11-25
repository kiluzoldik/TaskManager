from fastapi import FastAPI


def create_app() -> FastAPI:
    return FastAPI(
        title='Task Manager',
        description='A simple task manager with redis & celery & mongoDB',
        docs_url='/api/docs',
    )