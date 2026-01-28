from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_attachments_response_default import DeleteAttachmentsResponseDefault
from ...types import Response


def _get_kwargs(
    cid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/comments/{cid}/attachment".format(
            cid=quote(str(cid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteAttachmentsResponseDefault:
    response_default = DeleteAttachmentsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteAttachmentsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteAttachmentsResponseDefault]:
    """Delete all attachments from a comment.

    Args:
        cid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAttachmentsResponseDefault]
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
    client: AuthenticatedClient,
) -> DeleteAttachmentsResponseDefault | None:
    """Delete all attachments from a comment.

    Args:
        cid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAttachmentsResponseDefault
    """

    return sync_detailed(
        cid=cid,
        client=client,
    ).parsed


async def asyncio_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteAttachmentsResponseDefault]:
    """Delete all attachments from a comment.

    Args:
        cid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAttachmentsResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteAttachmentsResponseDefault | None:
    """Delete all attachments from a comment.

    Args:
        cid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAttachmentsResponseDefault
    """

    return (
        await asyncio_detailed(
            cid=cid,
            client=client,
        )
    ).parsed
