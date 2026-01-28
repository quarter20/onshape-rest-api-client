from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_next_part_numbers_param import BTNextPartNumbersParam
from ...models.update_next_numbers_response_default import UpdateNextNumbersResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BTNextPartNumbersParam,
    cid: str | Unset = UNSET,
    did: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["cid"] = cid

    params["did"] = did

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/partnumber/nextnumbers",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateNextNumbersResponseDefault:
    response_default = UpdateNextNumbersResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateNextNumbersResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BTNextPartNumbersParam,
    cid: str | Unset = UNSET,
    did: str | Unset = UNSET,
) -> Response[UpdateNextNumbersResponseDefault]:
    """Send the items to generate numbers for, and return the next valid available part numbers.

     Get the next available part number. See [API Guide: Release Management](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#get-the-next-available-part-number) for more details.

    Args:
        cid (str | Unset):
        did (str | Unset):
        body (BTNextPartNumbersParam):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateNextNumbersResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        cid=cid,
        did=did,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BTNextPartNumbersParam,
    cid: str | Unset = UNSET,
    did: str | Unset = UNSET,
) -> UpdateNextNumbersResponseDefault | None:
    """Send the items to generate numbers for, and return the next valid available part numbers.

     Get the next available part number. See [API Guide: Release Management](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#get-the-next-available-part-number) for more details.

    Args:
        cid (str | Unset):
        did (str | Unset):
        body (BTNextPartNumbersParam):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateNextNumbersResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
        cid=cid,
        did=did,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BTNextPartNumbersParam,
    cid: str | Unset = UNSET,
    did: str | Unset = UNSET,
) -> Response[UpdateNextNumbersResponseDefault]:
    """Send the items to generate numbers for, and return the next valid available part numbers.

     Get the next available part number. See [API Guide: Release Management](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#get-the-next-available-part-number) for more details.

    Args:
        cid (str | Unset):
        did (str | Unset):
        body (BTNextPartNumbersParam):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateNextNumbersResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        cid=cid,
        did=did,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BTNextPartNumbersParam,
    cid: str | Unset = UNSET,
    did: str | Unset = UNSET,
) -> UpdateNextNumbersResponseDefault | None:
    """Send the items to generate numbers for, and return the next valid available part numbers.

     Get the next available part number. See [API Guide: Release Management](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#get-the-next-available-part-number) for more details.

    Args:
        cid (str | Unset):
        did (str | Unset):
        body (BTNextPartNumbersParam):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateNextNumbersResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            cid=cid,
            did=did,
        )
    ).parsed
