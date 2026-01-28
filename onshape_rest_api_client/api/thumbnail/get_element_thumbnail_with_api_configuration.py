from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_element_thumbnail_with_api_configuration_response_default import (
    GetElementThumbnailWithApiConfigurationResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    cid: str,
    sz: str,
    *,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
    require_config_match: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["t"] = t

    params["skipDefaultImage"] = skip_default_image

    params["rejectEmpty"] = reject_empty

    params["requireConfigMatch"] = require_config_match

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/thumbnails/d/{did}/w/{wid}/e/{eid}/ac/{cid}/s/{sz}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
            cid=quote(str(cid), safe=""),
            sz=quote(str(sz), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetElementThumbnailWithApiConfigurationResponseDefault:
    response_default = GetElementThumbnailWithApiConfigurationResponseDefault.from_dict(response.content)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetElementThumbnailWithApiConfigurationResponseDefault]:
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
    cid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
    require_config_match: bool | Unset = False,
) -> Response[GetElementThumbnailWithApiConfigurationResponseDefault]:
    """Get the thumbnail image with the given configuration for an element.

     Returns the thumbnail image for an element at a specified version, with the given configuration.

    Args:
        did (str):
        wid (str):
        eid (str):
        cid (str):
        sz (str):
        link_document_id (str | Unset):  Default: ''.
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.
        reject_empty (bool | Unset):  Default: False.
        require_config_match (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetElementThumbnailWithApiConfigurationResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        cid=cid,
        sz=sz,
        link_document_id=link_document_id,
        t=t,
        skip_default_image=skip_default_image,
        reject_empty=reject_empty,
        require_config_match=require_config_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    cid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
    require_config_match: bool | Unset = False,
) -> GetElementThumbnailWithApiConfigurationResponseDefault | None:
    """Get the thumbnail image with the given configuration for an element.

     Returns the thumbnail image for an element at a specified version, with the given configuration.

    Args:
        did (str):
        wid (str):
        eid (str):
        cid (str):
        sz (str):
        link_document_id (str | Unset):  Default: ''.
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.
        reject_empty (bool | Unset):  Default: False.
        require_config_match (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetElementThumbnailWithApiConfigurationResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        cid=cid,
        sz=sz,
        client=client,
        link_document_id=link_document_id,
        t=t,
        skip_default_image=skip_default_image,
        reject_empty=reject_empty,
        require_config_match=require_config_match,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    cid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
    require_config_match: bool | Unset = False,
) -> Response[GetElementThumbnailWithApiConfigurationResponseDefault]:
    """Get the thumbnail image with the given configuration for an element.

     Returns the thumbnail image for an element at a specified version, with the given configuration.

    Args:
        did (str):
        wid (str):
        eid (str):
        cid (str):
        sz (str):
        link_document_id (str | Unset):  Default: ''.
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.
        reject_empty (bool | Unset):  Default: False.
        require_config_match (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetElementThumbnailWithApiConfigurationResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        cid=cid,
        sz=sz,
        link_document_id=link_document_id,
        t=t,
        skip_default_image=skip_default_image,
        reject_empty=reject_empty,
        require_config_match=require_config_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    cid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
    require_config_match: bool | Unset = False,
) -> GetElementThumbnailWithApiConfigurationResponseDefault | None:
    """Get the thumbnail image with the given configuration for an element.

     Returns the thumbnail image for an element at a specified version, with the given configuration.

    Args:
        did (str):
        wid (str):
        eid (str):
        cid (str):
        sz (str):
        link_document_id (str | Unset):  Default: ''.
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.
        reject_empty (bool | Unset):  Default: False.
        require_config_match (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetElementThumbnailWithApiConfigurationResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            cid=cid,
            sz=sz,
            client=client,
            link_document_id=link_document_id,
            t=t,
            skip_default_image=skip_default_image,
            reject_empty=reject_empty,
            require_config_match=require_config_match,
        )
    ).parsed
