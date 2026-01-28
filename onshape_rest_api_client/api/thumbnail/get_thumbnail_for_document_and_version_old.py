from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_thumbnail_info import BTThumbnailInfo
from ...types import Response


def _get_kwargs(
    did: str,
    vid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/thumbnails/document/{did}/version/{vid}".format(
            did=quote(str(did), safe=""),
            vid=quote(str(vid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTThumbnailInfo:
    response_default = BTThumbnailInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTThumbnailInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTThumbnailInfo]:
    """This endpoint will be deprecated soon. Use `getThumbnailForDocumentAndVersion` instead.

     This API exists for historical reasons. It uses `/document/` in the path, rather than the standard
    `/d/` to specify the document.

    Args:
        did (str):
        vid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTThumbnailInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        vid=vid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
) -> BTThumbnailInfo | None:
    """This endpoint will be deprecated soon. Use `getThumbnailForDocumentAndVersion` instead.

     This API exists for historical reasons. It uses `/document/` in the path, rather than the standard
    `/d/` to specify the document.

    Args:
        did (str):
        vid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTThumbnailInfo
    """

    return sync_detailed(
        did=did,
        vid=vid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTThumbnailInfo]:
    """This endpoint will be deprecated soon. Use `getThumbnailForDocumentAndVersion` instead.

     This API exists for historical reasons. It uses `/document/` in the path, rather than the standard
    `/d/` to specify the document.

    Args:
        did (str):
        vid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTThumbnailInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        vid=vid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
) -> BTThumbnailInfo | None:
    """This endpoint will be deprecated soon. Use `getThumbnailForDocumentAndVersion` instead.

     This API exists for historical reasons. It uses `/document/` in the path, rather than the standard
    `/d/` to specify the document.

    Args:
        did (str):
        vid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTThumbnailInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            vid=vid,
            client=client,
        )
    ).parsed
