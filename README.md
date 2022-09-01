# Network service

TODO application briefing.

# Usage

TODO

# Examples

TODO

# API route specification:

## IP Queries and settings

### `GET /ip?v=[PROTOCOL]`

List all IP addresses of all devices/interfaces.

Optional parameters:

- PROTOCOL: `4` | `6` = Pick IPv4 or IPv6 addresses. Omit to receive both.

Returned JSON schema:

```
{
  devices: {
    [DEVICE_ID]: string[]
  }
}
```


### `GET /ip/[DEVICE_ID]`

Read IP address of a specific device.

Required parameters:

- DEVICE_ID: string = device string identifier

Returned schema:

```
{
  [DEVICE_ID]: string[]
}
```

### `POST /ip/[DEVICE_ID]/[ADDRESS]?append`

Assign an IP address and mask to a device/interface.

Required parameters:

- DEVICE_ID: string = device string identifier
- ADDRESS: string = IP address with a mask

Optional parameters:

- append: boolean = Instead of assigning, append the address and keep any existing addresses.

Returned schema (representing success or failure of the operation):

```
{
  [DEVICE_ID]: boolean
}
```

### `DEL /ip/[DEVICE_ID]/[ADDRESS]`

Remove an IP address from a device.

Required parameters:

- DEVICE_ID: string = device string identifier
- ADDRESS: string = IP address with a mask

Returned schema (representing success or failure of the operation):

```
{
  [DEVICE_ID]: boolean
}
```

## Device status queries and settings

### `GET /status/[DEVICE_ID]`

Check the status (up/down) of a device.

Required parameters:

- DEVICE_ID: string = device string identifier

Returned schema:

```
{
  [DEVICE_ID]: "up" | "down"
}
```

### `POST /status/[DEVICE_ID]/[STATUS]`

Set the status (up/down) of a device.

Required parameters:

- DEVICE_ID: string = device string identifier
- STATUS: "up" | "down" = status to be set

Returned schema (representing success or failure of the operation)

```
{
  [DEVICE_ID]: boolean
}
```

## Device Maximum Transmission Unit (MTU)

### `GET /mtu/[DEVICE_ID]`

Read the MTU size of a device in bytes.

Required parameters:

- DEVICE_ID: string = device string identifier

Returned schema:

```
{
  [DEVICE_ID]: number
}
```

### `POST /mtu/[DEVICE_ID]/[MTU_BYTES]`

Set the MTU size of a device in bytes.

Required parameters:

- DEVICE_ID: string = device string identifier
- MTU_BYTES: number = MTU size to be set


Returned schema (representing success or failure of the operation)

```
{
  [DEVICE_ID]: boolean
}
```