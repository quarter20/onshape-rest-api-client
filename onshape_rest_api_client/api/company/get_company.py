from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_company_info import BTCompanyInfo
from ...types import Response


def _get_kwargs(
    cid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/{cid}".format(
            cid=quote(str(cid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTCompanyInfo:
    response_default = BTCompanyInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTCompanyInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BTCompanyInfo]:
    """Get company information by company ID.

    Args:
        cid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTCompanyInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    *,
    client: AuthenticatedClient | Client,
) -> BTCompanyInfo | None:
    """Get company information by company ID.

    Args:
        cid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTCompanyInfo
    """

    return sync_detailed(
        cid=cid,
        client=client,
    ).parsed


async def asyncio_detailed(
    cid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BTCompanyInfo]:
    """Get company information by company ID.

    Args:
        cid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTCompanyInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    *,
    client: AuthenticatedClient | Client,
) -> BTCompanyInfo | None:
    """Get company information by company ID.

    Args:
        cid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTCompanyInfo
    """

    return (
        await asyncio_detailed(
            cid=cid,
            client=client,
        )
    ).parsed
