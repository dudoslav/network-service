from typing import Union, Literal
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/v1/links/ips")
async def list_all_ips(v: Union[Literal["4"], Literal["6"], None] = None):
    print(v)
    return {"eth0": ["ip1", "ip2"], "eth1": ["ip1", "ip2"]}


@app.get("/v1/links/{device_id}/ip")
async def list_device_ips(device_id: str):
    print(device_id)
    return ["ip1", "ip2"]


class PostIPBody(BaseModel):
    address: str
    append: Union[bool, None]


@app.post("/v1/links/{device_id}/ip")
async def set_device_ip(body: PostIPBody, device_id: str):
    print(body)
    print(device_id)
    return {device_id: True}


class DelIPBody(BaseModel):
    address: str


@app.delete("/v1/links/{device_id}/ip")
async def del_device_ip(body: DelIPBody, device_id: str):
    print(body)
    print(device_id)
    return {device_id: True}


@app.get("/v1/links/{device_id}/status")
async def get_device_status(device_id: str):
    print(device_id)
    return {device_id: "up"}


class PostStatusBody(BaseModel):
    status: Union[Literal["up"], Literal["down"]]


@app.post("/v1/links/{device_id}/status")
async def set_device_status(body: PostStatusBody, device_id: str):
    print(body)
    print(device_id)
    return {device_id: True}


@app.get("/v1/links/{device_id}/mtu")
async def get_device_mtu(device_id: str):
    print(device_id)
    return {device_id: 123}


class PostMTUBody(BaseModel):
    mtu: int


@app.post("/v1/links/{device_id}/mtu")
async def set_device_mtu(body: PostMTUBody, device_id: str):
    print(body)
    print(device_id)
    return {device_id: True}
