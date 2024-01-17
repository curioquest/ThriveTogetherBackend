from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
# SessionLocal
# import os
from dotenv import load_dotenv


from authenticator import authenticator
from api.messages.routers import messages
from api.accounts.routers import accounts
from api.peers.routers import peers
from api.matching.routers import matching
from api.tags.routers import tags
from database import initialize_database, close_engine


load_dotenv()


class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(f"Incoming request: {request.method} {request.url.path}")
        return await call_next(request)


app = FastAPI()

# db_engine = create_database_engine()

# initialize_database()

# origins = ["https://hammerhead-app-2-du6ba.ondigitalocean.app",
#            "https://hammerhead-app-2-du6ba.ondigitalocean.app:443",
#            "https://hammerhead-app-2-du6ba.ondigitalocean.app/",
#            "http://localhost:3000",]

app.add_middleware(LoggerMiddleware)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
#     expose_headers=["*"],
# )

app.include_router(authenticator.router)
app.include_router(messages.messages_router)
app.include_router(accounts.router)
app.include_router(peers.router)
app.include_router(matching.router)
app.include_router(tags.router)


@app.get("/")
def root():
    return {"message": "You hit the root path!"}


@app.on_event("startup")
async def startup():
    # app.db_connection = connect_to_db()
    initialize_database()


@app.on_event("shutdown")
async def shutdown():
    close_engine()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# async def get_database():
#     return app.db_connection


# @app.get("/api/launch-details")
# def launch_details():
#     return {
#         "launch_details": {
#             "module": 3,
#             "week": 17,
#             "day": 5,
#             "hour": 19,
#             "min": "00",
#         }
#     }
