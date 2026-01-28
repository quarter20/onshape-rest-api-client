from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_document_response_default import DeleteDocumentResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    *,
    forever: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["forever"] = forever

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/documents/{did}".format(
            did=quote(str(did), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteDocumentResponseDefault:
    response_default = DeleteDocumentResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteDocumentResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    forever: bool | Unset = False,
) -> Response[DeleteDocumentResponseDefault]:
    """Delete document by document ID.

    Args:
        did (str):
        forever (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDocumentResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        forever=forever,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient,
    forever: bool | Unset = False,
) -> DeleteDocumentResponseDefault | None:
    """Delete document by document ID.

    Args:
        did (str):
        forever (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDocumentResponseDefault
    """

    return sync_detailed(
        did=did,
        client=client,
        forever=forever,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    forever: bool | Unset = False,
) -> Response[DeleteDocumentResponseDefault]:
    """Delete document by document ID.

    Args:
        did (str):
        forever (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDocumentResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        forever=forever,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient,
    forever: bool | Unset = False,
) -> DeleteDocumentResponseDefault | None:
    """Delete document by document ID.

    Args:
        did (str):
        forever (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDocumentResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
            forever=forever,
        )
    ).parsed
