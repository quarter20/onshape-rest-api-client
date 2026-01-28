from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    content_disposition: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["contentDisposition"] = content_disposition

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/blobelements/d/{did}/w/{wid}/e/{eid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> File:
    response_default = File(payload=BytesIO(response.content))

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    content_disposition: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> Response[File]:
    """Download a file from a blob element for the specified workspace/version/microversion.

     See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        content_disposition (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        link_document_id=link_document_id,
        content_disposition=content_disposition,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    content_disposition: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> File | None:
    """Download a file from a blob element for the specified workspace/version/microversion.

     See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        content_disposition (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        content_disposition=content_disposition,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    content_disposition: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> Response[File]:
    """Download a file from a blob element for the specified workspace/version/microversion.

     See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        content_disposition (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        link_document_id=link_document_id,
        content_disposition=content_disposition,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    content_disposition: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> File | None:
    """Download a file from a blob element for the specified workspace/version/microversion.

     See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        content_disposition (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
            content_disposition=content_disposition,
            if_none_match=if_none_match,
        )
    ).parsed
