from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_publication_item_response_default import DeletePublicationItemResponseDefault
from ...types import Response


def _get_kwargs(
    pid: str,
    iid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/publications/{pid}/item/{iid}".format(
            pid=quote(str(pid), safe=""),
            iid=quote(str(iid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeletePublicationItemResponseDefault:
    response_default = DeletePublicationItemResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeletePublicationItemResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pid: str,
    iid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeletePublicationItemResponseDefault]:
    """Remove an item from a publication.

    Args:
        pid (str):
        iid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletePublicationItemResponseDefault]
    """

    kwargs = _get_kwargs(
        pid=pid,
        iid=iid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pid: str,
    iid: str,
    *,
    client: AuthenticatedClient,
) -> DeletePublicationItemResponseDefault | None:
    """Remove an item from a publication.

    Args:
        pid (str):
        iid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletePublicationItemResponseDefault
    """

    return sync_detailed(
        pid=pid,
        iid=iid,
        client=client,
    ).parsed


async def asyncio_detailed(
    pid: str,
    iid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeletePublicationItemResponseDefault]:
    """Remove an item from a publication.

    Args:
        pid (str):
        iid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletePublicationItemResponseDefault]
    """

    kwargs = _get_kwargs(
        pid=pid,
        iid=iid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pid: str,
    iid: str,
    *,
    client: AuthenticatedClient,
) -> DeletePublicationItemResponseDefault | None:
    """Remove an item from a publication.

    Args:
        pid (str):
        iid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletePublicationItemResponseDefault
    """

    return (
        await asyncio_detailed(
            pid=pid,
            iid=iid,
            client=client,
        )
    ).parsed
