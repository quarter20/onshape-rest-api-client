from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_modification_request_info import BTAppModificationRequestInfo
from ...types import Response


def _get_kwargs(
    mrid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/drawings/modify/status/{mrid}".format(
            mrid=quote(str(mrid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppModificationRequestInfo:
    response_default = BTAppModificationRequestInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppModificationRequestInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mrid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTAppModificationRequestInfo]:
    """Get the status of a drawing modification operation.

    Args:
        mrid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppModificationRequestInfo]
    """

    kwargs = _get_kwargs(
        mrid=mrid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mrid: str,
    *,
    client: AuthenticatedClient,
) -> BTAppModificationRequestInfo | None:
    """Get the status of a drawing modification operation.

    Args:
        mrid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppModificationRequestInfo
    """

    return sync_detailed(
        mrid=mrid,
        client=client,
    ).parsed


async def asyncio_detailed(
    mrid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTAppModificationRequestInfo]:
    """Get the status of a drawing modification operation.

    Args:
        mrid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppModificationRequestInfo]
    """

    kwargs = _get_kwargs(
        mrid=mrid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mrid: str,
    *,
    client: AuthenticatedClient,
) -> BTAppModificationRequestInfo | None:
    """Get the status of a drawing modification operation.

    Args:
        mrid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppModificationRequestInfo
    """

    return (
        await asyncio_detailed(
            mrid=mrid,
            client=client,
        )
    ).parsed
