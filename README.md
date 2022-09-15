# Network service

TODO application briefing.

# Usage

TODO

# Examples

TODO

# API route specification:

## Query routes

### `GET /v1/links`

List all link identifiers.

Returned JSON schema:

```
{
  links: string[] = List of string identifiers.
}
```

### `GET /v1/links/[DEVICE_ID]`

Read every property of a specific device.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Returned JSON schema:

```
{
  [DEVICE_ID]: {
    ips: string[] = List of IP addresses.
    status: "up" | "down" = Status of the device (running/stopped).
    mtu: number = Size of MTU (Maximum Transmission Unit) in bytes.
  }
}
```

### `GET /v1/links/[DEVICE_ID]/ips`

Read all IP addresses of a specific link.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Returned JSON schema:

```
{
  [DEVICE_ID]: string[] = List of IP addresses.
}
```

### `GET /v1/links/[DEVICE_ID]/status`

Check the status (up/down) of a device.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Returned JSON schema:

```
{
  [DEVICE_ID]: "up" | "down" = Status of device.
}
```

### `GET /v1/links/[DEVICE_ID]/mtu`

Read the MTU size of a device in bytes.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Returned JSON schema:

```
{
  [DEVICE_ID]: number = Size of MTU (Maximum Transmission Unit) in bytes.
}
```

## Modifications routes

### `PATCH /v1/links/[DEVICE_ID]`

Change settings of a specific device.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Optional body JSON schema (include only desired attributes):
```
{
  ip: string = Exclusive IP address with a mask to bet set.
  status: "up" | "down" = Status of the device (running/stopped) to be set.
  mtu: number = Size of MTU (Maximum Transmission Unit) in bytes to be set.
}
```

Returned JSON schema:

```
{
  [DEVICE_ID]: boolean = Operation success/failure.
}
```

### `POST /v1/links/[DEVICE_ID]/ips`

Add an IP address and mask to a device.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Body JSON schema:
```
{
  address: string = IP address with a mask.
}
```

Returned JSON schema:

```
{
  [DEVICE_ID]: boolean = Operation success/failure.
}
```

### `DEL /v1/links/[DEVICE_ID]/ips`

Remove an IP address and mask from a device.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Body JSON schema:
```
{
  ip: string = IP address with a mask to be removed.
}
```

Returned JSON schema:

```
{
  [DEVICE_ID]: boolean = Operation success/failure.
}
```