from typing import Union, Literal
from fastapi import FastAPI
from pydantic import BaseModel
from pyroute2 import NDB

###


def get_device_property(device_id: str, prop: str):
    with NDB() as ndb:
        if device_id not in ndb.interfaces:
            return None
        with ndb.interfaces[device_id] as interface:
            return interface[prop]


def get_device_ips(device_id: str):
    return get_device_property(device_id, "address")


def get_device_status(device_id: str):
    return get_device_property(device_id, "state")


def get_device_mtu(device_id: str):
    return get_device_property(device_id, "mtu")


###

app = FastAPI()

# Query routes


@app.get("/v1/links")
async def list_all_ids_route():
    with NDB() as ndb:
        return [interface.ifname for interface in ndb.interfaces.summary()]


@app.get("/v1/links/{device_id}")
async def get_device_settings_route(device_id: str):
    return {
        device_id: {
            "ips": get_device_ips(device_id),
            "status": get_device_status(device_id),
            "mtu": get_device_mtu(device_id),
        }
    }


@app.get("/v1/links/{device_id}/ips")
async def get_device_ips_route(device_id: str):
    return {device_id: get_device_ips(device_id)}


@app.get("/v1/links/{device_id}/status")
async def get_device_status_route(device_id: str):
    return {device_id: get_device_status(device_id)}


@app.get("/v1/links/{device_id}/mtu")
async def get_device_mtu_route(device_id: str):
    return {device_id: get_device_mtu(device_id)}


# Modification routes


# class PatchDeviceInfoBody(BaseModel):
#     ip: Union[str, None]
#     status: Union[Literal["up"], Literal["down"], None]
#     mtu: int


# @app.patch("/v1/links/{device_id}")
# async def patch_device_info_route(body: PatchDeviceInfoBody, device_id: str):
#     return
