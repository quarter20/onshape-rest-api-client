from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.un_share_document_response_default import UnShareDocumentResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    eid: str,
    *,
    entry_type: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["entryType"] = entry_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/documents/{did}/share/{eid}".format(
            did=quote(str(did), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UnShareDocumentResponseDefault:
    response_default = UnShareDocumentResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UnShareDocumentResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    entry_type: int | Unset = 0,
) -> Response[UnShareDocumentResponseDefault]:
    """Remove document View permissions from a user or other entity.

     Specify the ID of the entity to unshare with in the `eid` field, and specify the type of entity
    being identified in the `entryType` field. For example, to unshare a document with a company, you
    would use `1` as the `entryType` value and the `companyId` as the `entityId`.

    Args:
        did (str):
        eid (str):
        entry_type (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnShareDocumentResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        eid=eid,
        entry_type=entry_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    entry_type: int | Unset = 0,
) -> UnShareDocumentResponseDefault | None:
    """Remove document View permissions from a user or other entity.

     Specify the ID of the entity to unshare with in the `eid` field, and specify the type of entity
    being identified in the `entryType` field. For example, to unshare a document with a company, you
    would use `1` as the `entryType` value and the `companyId` as the `entityId`.

    Args:
        did (str):
        eid (str):
        entry_type (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnShareDocumentResponseDefault
    """

    return sync_detailed(
        did=did,
        eid=eid,
        client=client,
        entry_type=entry_type,
    ).parsed


async def asyncio_detailed(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    entry_type: int | Unset = 0,
) -> Response[UnShareDocumentResponseDefault]:
    """Remove document View permissions from a user or other entity.

     Specify the ID of the entity to unshare with in the `eid` field, and specify the type of entity
    being identified in the `entryType` field. For example, to unshare a document with a company, you
    would use `1` as the `entryType` value and the `companyId` as the `entityId`.

    Args:
        did (str):
        eid (str):
        entry_type (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnShareDocumentResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        eid=eid,
        entry_type=entry_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    entry_type: int | Unset = 0,
) -> UnShareDocumentResponseDefault | None:
    """Remove document View permissions from a user or other entity.

     Specify the ID of the entity to unshare with in the `eid` field, and specify the type of entity
    being identified in the `entryType` field. For example, to unshare a document with a company, you
    would use `1` as the `entryType` value and the `companyId` as the `entityId`.

    Args:
        did (str):
        eid (str):
        entry_type (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnShareDocumentResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            eid=eid,
            client=client,
            entry_type=entry_type,
        )
    ).parsed
