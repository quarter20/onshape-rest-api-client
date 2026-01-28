from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_bounding_box_info import BTBoundingBoxInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    include_hidden: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includeHidden"] = include_hidden

    params["configuration"] = configuration

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/parts/d/{did}/{wvm}/{wvmid}/e/{eid}/partid/{partid}/boundingboxes".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            partid=quote(str(partid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTBoundingBoxInfo:
    response_default = BTBoundingBoxInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTBoundingBoxInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    include_hidden: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTBoundingBoxInfo]:
    """Get a part's bounding box details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        include_hidden (bool | Unset):  Default: False.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTBoundingBoxInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        include_hidden=include_hidden,
        configuration=configuration,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    include_hidden: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTBoundingBoxInfo | None:
    """Get a part's bounding box details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        include_hidden (bool | Unset):  Default: False.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTBoundingBoxInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        client=client,
        include_hidden=include_hidden,
        configuration=configuration,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    include_hidden: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTBoundingBoxInfo]:
    """Get a part's bounding box details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        include_hidden (bool | Unset):  Default: False.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTBoundingBoxInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        include_hidden=include_hidden,
        configuration=configuration,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    include_hidden: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTBoundingBoxInfo | None:
    """Get a part's bounding box details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        include_hidden (bool | Unset):  Default: False.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTBoundingBoxInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            partid=partid,
            client=client,
            include_hidden=include_hidden,
            configuration=configuration,
            link_document_id=link_document_id,
        )
    ).parsed
