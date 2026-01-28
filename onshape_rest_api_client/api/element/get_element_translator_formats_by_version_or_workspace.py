from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_model_format_info import BTModelFormatInfo
from ...models.get_element_translator_formats_by_version_or_workspace_wv import (
    GetElementTranslatorFormatsByVersionOrWorkspaceWv,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wv: GetElementTranslatorFormatsByVersionOrWorkspaceWv,
    wvid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    check_content: bool | Unset = True,
    configuration: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["checkContent"] = check_content

    params["configuration"] = configuration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/elements/translatorFormats/{did}/{wv}/{wvid}/{eid}".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BTModelFormatInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTModelFormatInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTModelFormatInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: GetElementTranslatorFormatsByVersionOrWorkspaceWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
    link_document_id: str | Unset = "",
    check_content: bool | Unset = True,
    configuration: str | Unset = "",
) -> Response[list[BTModelFormatInfo]]:
    """Gets the list of formats an element can be translated to or from.

     See the [Translation API Guide](https://onshape-public.github.io/docs/api-adv/translation/) for
    additional details.

    Args:
        did (str):
        wv (GetElementTranslatorFormatsByVersionOrWorkspaceWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        check_content (bool | Unset):  Default: True.
        configuration (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTModelFormatInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        link_document_id=link_document_id,
        check_content=check_content,
        configuration=configuration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: GetElementTranslatorFormatsByVersionOrWorkspaceWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
    link_document_id: str | Unset = "",
    check_content: bool | Unset = True,
    configuration: str | Unset = "",
) -> list[BTModelFormatInfo] | None:
    """Gets the list of formats an element can be translated to or from.

     See the [Translation API Guide](https://onshape-public.github.io/docs/api-adv/translation/) for
    additional details.

    Args:
        did (str):
        wv (GetElementTranslatorFormatsByVersionOrWorkspaceWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        check_content (bool | Unset):  Default: True.
        configuration (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTModelFormatInfo]
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        check_content=check_content,
        configuration=configuration,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: GetElementTranslatorFormatsByVersionOrWorkspaceWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
    link_document_id: str | Unset = "",
    check_content: bool | Unset = True,
    configuration: str | Unset = "",
) -> Response[list[BTModelFormatInfo]]:
    """Gets the list of formats an element can be translated to or from.

     See the [Translation API Guide](https://onshape-public.github.io/docs/api-adv/translation/) for
    additional details.

    Args:
        did (str):
        wv (GetElementTranslatorFormatsByVersionOrWorkspaceWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        check_content (bool | Unset):  Default: True.
        configuration (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTModelFormatInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        link_document_id=link_document_id,
        check_content=check_content,
        configuration=configuration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: GetElementTranslatorFormatsByVersionOrWorkspaceWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
    link_document_id: str | Unset = "",
    check_content: bool | Unset = True,
    configuration: str | Unset = "",
) -> list[BTModelFormatInfo] | None:
    """Gets the list of formats an element can be translated to or from.

     See the [Translation API Guide](https://onshape-public.github.io/docs/api-adv/translation/) for
    additional details.

    Args:
        did (str):
        wv (GetElementTranslatorFormatsByVersionOrWorkspaceWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        check_content (bool | Unset):  Default: True.
        configuration (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTModelFormatInfo]
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
            check_content=check_content,
            configuration=configuration,
        )
    ).parsed
