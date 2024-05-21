from constants import HTTP_CODE_401_MSG, HTTP_CODE_401, HTTP_CODE_500, HTTP_CODE_500_MSG
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from controller.auth import authRouter
from controller.exceptions import UnAuthorizedException

app = FastAPI()

app.include_router(authRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):

    if type(exc) is UnAuthorizedException:
        return JSONResponse(
            status_code=HTTP_CODE_401,
            content={"error": HTTP_CODE_401_MSG},
        )
    else:
        return JSONResponse(
            status_code=HTTP_CODE_500,
            content={"error": HTTP_CODE_500_MSG},
        )