from typing import Union, Literal
from fastapi import FastAPI
from pydantic import BaseModel
from pyroute2 import NDB

app = FastAPI()


@app.get("/v1/links")
async def list_all_ids():
    with NDB() as ndb:
        print(ndb.interfaces.summary())
        return [interface[3] for interface in ndb.interfaces.summary()]


# @app.get("/v1/links/{device_id}/ip")
# async def list_device_ips(device_id: str):
#     print(device_id)
#     return ["ip1", "ip2"]


# class PostIPBody(BaseModel):
#     address: str
#     append: Union[bool, None]


# @app.post("/v1/links/{device_id}/ip")
# async def set_device_ip(body: PostIPBody, device_id: str):
#     print(body)
#     print(device_id)
#     return {device_id: True}


# class DelIPBody(BaseModel):
#     address: str


# @app.delete("/v1/links/{device_id}/ip")
# async def del_device_ip(body: DelIPBody, device_id: str):
#     print(body)
#     print(device_id)
#     return {device_id: True}


# @app.get("/v1/links/{device_id}/status")
# async def get_device_status(device_id: str):
#     print(device_id)
#     return {device_id: "up"}


# class PostStatusBody(BaseModel):
#     status: Union[Literal["up"], Literal["down"]]


# @app.post("/v1/links/{device_id}/status")
# async def set_device_status(body: PostStatusBody, device_id: str):
#     print(body)
#     print(device_id)
#     return {device_id: True}


# @app.get("/v1/links/{device_id}/mtu")
# async def get_device_mtu(device_id: str):
#     print(device_id)
#     return {device_id: 123}


# class PostMTUBody(BaseModel):
#     mtu: int


# @app.post("/v1/links/{device_id}/mtu")
# async def set_device_mtu(body: PostMTUBody, device_id: str):
#     print(body)
#     print(device_id)
#     return {device_id: True}
