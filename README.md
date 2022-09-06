# Network service

TODO application briefing.

# Usage

TODO

# Examples

TODO

# API route specification:

## IP Queries and settings

### `GET /v1/links/ips?v=[PROTOCOL]`

List all IP addresses of all devices/interfaces.

Optional parameters:

- PROTOCOL: `4` | `6` = Pick IPv4 or IPv6 addresses. Omit to receive both.

Returned JSON schema:

```
{
  devices: {
    [DEVICE_ID]: string[]
  } = Object with every device ID with its corresponding IP list.
}
```


### `GET /v1/links/[DEVICE_ID]/ip`

Read IP address of a specific device.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Returned JSON schema:

```
{
  [DEVICE_ID]: string[] = List of IP addresses.
}
```

### `POST /v1/links/[DEVICE_ID]/ip`

Assign an IP address and mask to a device/interface.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Body JSON schema:
```
{
  address: string = IP address with a mask.
  append: boolean = Instead of assigning, append the address and keep any existing addresses.
}
```

Returned JSON schema:

```
{
  [DEVICE_ID]: boolean = Operation success/failure.
}
```

### `DEL /v1/links/[DEVICE_ID]/ip`

Remove an IP address from a device.

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

## Device status queries and settings

### `GET /v1/links/[DEVICE_ID]/status`

Check the status (up/down) of a device.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Returned JSON schema:

```
{
  [DEVICE_ID]: "up" | "down" = Status to be set.
}
```

### `POST /v1/links/[DEVICE_ID]/status`

Set the status (up/down) of a device.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Body JSON schema:
```
{
  status: "up" | "down" = IP address with a mask.
}
```

Returned JSON schema:

```
{
  [DEVICE_ID]: boolean = Operation success/failure.
}
```

## Device Maximum Transmission Unit (MTU)

### `GET /v1/links/[DEVICE_ID]/mtu`

Read the MTU size of a device in bytes.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Returned JSON schema:

```
{
  [DEVICE_ID]: number = MTU size in bytes.
}
```

### `POST /v1/links/[DEVICE_ID]/mtu`

Set the MTU size of a device in bytes.

Required parameters:

- DEVICE_ID: string = Device string identifier.

Body JSON schema:
```
{
  mtu: number = MTU size in bytes.
}
```

Returned JSON schema:

```
{
  [DEVICE_ID]: boolean = Operation success/failure.
}
```