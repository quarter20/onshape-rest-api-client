from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_item_info import BTItemInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    iid: str,
    *,
    document_id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["documentId"] = document_id

    params["companyId"] = company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/items/{iid}".format(
            iid=quote(str(iid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTItemInfo:
    response_default = BTItemInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTItemInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    iid: str,
    *,
    client: AuthenticatedClient,
    document_id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> Response[BTItemInfo]:
    """Get item by ID.

     Either `documentId` or `companyId` must be provided, in addition to the item ID.

    Args:
        iid (str):
        document_id (str | Unset):
        company_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTItemInfo]
    """

    kwargs = _get_kwargs(
        iid=iid,
        document_id=document_id,
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    iid: str,
    *,
    client: AuthenticatedClient,
    document_id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> BTItemInfo | None:
    """Get item by ID.

     Either `documentId` or `companyId` must be provided, in addition to the item ID.

    Args:
        iid (str):
        document_id (str | Unset):
        company_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTItemInfo
    """

    return sync_detailed(
        iid=iid,
        client=client,
        document_id=document_id,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    iid: str,
    *,
    client: AuthenticatedClient,
    document_id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> Response[BTItemInfo]:
    """Get item by ID.

     Either `documentId` or `companyId` must be provided, in addition to the item ID.

    Args:
        iid (str):
        document_id (str | Unset):
        company_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTItemInfo]
    """

    kwargs = _get_kwargs(
        iid=iid,
        document_id=document_id,
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    iid: str,
    *,
    client: AuthenticatedClient,
    document_id: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
) -> BTItemInfo | None:
    """Get item by ID.

     Either `documentId` or `companyId` must be provided, in addition to the item ID.

    Args:
        iid (str):
        document_id (str | Unset):
        company_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTItemInfo
    """

    return (
        await asyncio_detailed(
            iid=iid,
            client=client,
            document_id=document_id,
            company_id=company_id,
        )
    ).parsed
