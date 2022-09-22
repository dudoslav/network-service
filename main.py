from typing import Union, Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pyroute2 import NDB

###


def get_device_property(device_id: str, prop: str):
    with NDB() as ndb:
        if device_id not in ndb.interfaces:
            raise HTTPException(
                status_code=404, detail=f"Device ID: {device_id} not found"
            )
        with ndb.interfaces[device_id] as interface:
            return interface[prop]


def get_device_ips(device_id: str):
    return [get_device_property(device_id, "address")]


def get_device_status(device_id: str):
    return get_device_property(device_id, "state")


def get_device_mtu(device_id: str):
    return get_device_property(device_id, "mtu")


###


def set_device_status(device_id: str, status: Union[Literal["up"], Literal["down"]]):
    with NDB() as ndb:
        if device_id not in ndb.interfaces:
            raise HTTPException(
                status_code=404, detail=f"Device ID: {device_id} not found"
            )
        with ndb.interfaces[device_id] as interface:
            interface.set(state=status)
            interface.commit()
    return True


def set_device_ip(device_id: str, ip: str):
    with NDB() as ndb:
        if device_id not in ndb.interfaces:
            raise HTTPException(
                status_code=404, detail=f"Device ID: {device_id} not found"
            )
        with ndb.interfaces[device_id] as interface:
            # (ndb.addresses.create(address='10.0.0.1', prefixlen=24, index=interface['index']).commit())
            set_device_status(device_id, "down")
            interface.add_ip(ip)
            set_device_status(device_id, "up")
    return True


# def set_device_mtu(device_id: str, mtu: int):
#     with NDB() as ndb:
#         if device_id not in ndb.interfaces:
#             raise HTTPException(
#                 status_code=404, detail=f"Device ID: {device_id} not found"
#             )
#         with ndb.interfaces[device_id] as interface:
#             pass
#     return True


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


class PatchDeviceInfoBody(BaseModel):
    ip: Union[str, None]
    status: Union[Literal["up"], Literal["down"], None]
    mtu: Union[int, None]


@app.patch("/v1/links/{device_id}")
async def patch_device_info_route(body: PatchDeviceInfoBody, device_id: str):

    if body.ip is not None:
        set_device_ip(device_id, body.ip)

    # if body.mtu is not None:
    #     set_device_mtu(device_id, body.mtu)

    if body.status is not None:
        set_device_status(device_id, body.status)

    return {device_id: True}
