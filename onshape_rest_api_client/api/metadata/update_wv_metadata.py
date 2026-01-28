from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.update_wv_metadata_response_default import UpdateWVMetadataResponseDefault
from ...types import Response


def _get_kwargs(
    did: str,
    wv: str,
    wvid: str,
    *,
    body: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/metadata/d/{did}/{wv}/{wvid}".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
        ),
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateWVMetadataResponseDefault:
    response_default = UpdateWVMetadataResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateWVMetadataResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
    body: str,
) -> Response[UpdateWVMetadataResponseDefault]:
    """Update the metadata for a workspace or version.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWVMetadataResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
    body: str,
) -> UpdateWVMetadataResponseDefault | None:
    """Update the metadata for a workspace or version.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWVMetadataResponseDefault
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
    body: str,
) -> Response[UpdateWVMetadataResponseDefault]:
    """Update the metadata for a workspace or version.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWVMetadataResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
    body: str,
) -> UpdateWVMetadataResponseDefault | None:
    """Update the metadata for a workspace or version.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWVMetadataResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            client=client,
            body=body,
        )
    ).parsed
