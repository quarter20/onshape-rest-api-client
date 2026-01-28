from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_document_info import BTDocumentInfo
from ...models.bt_document_params import BTDocumentParams
from ...types import Response


def _get_kwargs(
    *,
    body: BTDocumentParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTDocumentInfo:
    response_default = BTDocumentInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTDocumentInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BTDocumentParams,
) -> Response[BTDocumentInfo]:
    """Create and upload a document.

     The `name` field is required in the `BTDocumentParams` schema when creating a new document.

    Args:
        body (BTDocumentParams): Parameters for creating and updating documents.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDocumentInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BTDocumentParams,
) -> BTDocumentInfo | None:
    """Create and upload a document.

     The `name` field is required in the `BTDocumentParams` schema when creating a new document.

    Args:
        body (BTDocumentParams): Parameters for creating and updating documents.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDocumentInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BTDocumentParams,
) -> Response[BTDocumentInfo]:
    """Create and upload a document.

     The `name` field is required in the `BTDocumentParams` schema when creating a new document.

    Args:
        body (BTDocumentParams): Parameters for creating and updating documents.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDocumentInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BTDocumentParams,
) -> BTDocumentInfo | None:
    """Create and upload a document.

     The `name` field is required in the `BTDocumentParams` schema when creating a new document.

    Args:
        body (BTDocumentParams): Parameters for creating and updating documents.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDocumentInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
