from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_named_views_info import BTNamedViewsInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    skip_perspective: bool | Unset = True,
    include_section_cut_views: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["skipPerspective"] = skip_perspective

    params["includeSectionCutViews"] = include_section_cut_views

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assemblies/d/{did}/e/{eid}/namedViews".format(
            did=quote(str(did), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTNamedViewsInfo:
    response_default = BTNamedViewsInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTNamedViewsInfo]:
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
    link_document_id: str | Unset = "",
    skip_perspective: bool | Unset = True,
    include_section_cut_views: bool | Unset = False,
) -> Response[BTNamedViewsInfo]:
    """Get the view data for all named views for the specified element.

    Args:
        did (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        skip_perspective (bool | Unset):  Default: True.
        include_section_cut_views (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTNamedViewsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        eid=eid,
        link_document_id=link_document_id,
        skip_perspective=skip_perspective,
        include_section_cut_views=include_section_cut_views,
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
    link_document_id: str | Unset = "",
    skip_perspective: bool | Unset = True,
    include_section_cut_views: bool | Unset = False,
) -> BTNamedViewsInfo | None:
    """Get the view data for all named views for the specified element.

    Args:
        did (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        skip_perspective (bool | Unset):  Default: True.
        include_section_cut_views (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTNamedViewsInfo
    """

    return sync_detailed(
        did=did,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        skip_perspective=skip_perspective,
        include_section_cut_views=include_section_cut_views,
    ).parsed


async def asyncio_detailed(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    skip_perspective: bool | Unset = True,
    include_section_cut_views: bool | Unset = False,
) -> Response[BTNamedViewsInfo]:
    """Get the view data for all named views for the specified element.

    Args:
        did (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        skip_perspective (bool | Unset):  Default: True.
        include_section_cut_views (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTNamedViewsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        eid=eid,
        link_document_id=link_document_id,
        skip_perspective=skip_perspective,
        include_section_cut_views=include_section_cut_views,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    skip_perspective: bool | Unset = True,
    include_section_cut_views: bool | Unset = False,
) -> BTNamedViewsInfo | None:
    """Get the view data for all named views for the specified element.

    Args:
        did (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        skip_perspective (bool | Unset):  Default: True.
        include_section_cut_views (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTNamedViewsInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
            skip_perspective=skip_perspective,
            include_section_cut_views=include_section_cut_views,
        )
    ).parsed
