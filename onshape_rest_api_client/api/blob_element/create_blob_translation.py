from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_translate_format_params import BTTranslateFormatParams
from ...models.bt_translation_request_info import BTTranslationRequestInfo
from ...models.create_blob_translation_wv import CreateBlobTranslationWv
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wv: CreateBlobTranslationWv,
    wvid: str,
    eid: str,
    *,
    body: BTTranslateFormatParams,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/blobelements/d/{did}/{wv}/{wvid}/e/{eid}/translations".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTTranslationRequestInfo:
    response_default = BTTranslationRequestInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTTranslationRequestInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: CreateBlobTranslationWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTTranslateFormatParams,
    link_document_id: str | Unset = "",
) -> Response[BTTranslationRequestInfo]:
    """Export a blob element to another format.

     * Use `formatName` in the JSON request body to specify the export file type. Use
    [Translations/getAllTranslatorFormats]#/Translation/getAllTranslatorFormats) to get a list of valid
    export file formats.
    * Set `storeInDocument` to `false` to export to a data file. Set to `true` to export to a blob
    element in the same document.
    * See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.

    Args:
        did (str):
        wv (CreateBlobTranslationWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTTranslateFormatParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTranslationRequestInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: CreateBlobTranslationWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTTranslateFormatParams,
    link_document_id: str | Unset = "",
) -> BTTranslationRequestInfo | None:
    """Export a blob element to another format.

     * Use `formatName` in the JSON request body to specify the export file type. Use
    [Translations/getAllTranslatorFormats]#/Translation/getAllTranslatorFormats) to get a list of valid
    export file formats.
    * Set `storeInDocument` to `false` to export to a data file. Set to `true` to export to a blob
    element in the same document.
    * See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.

    Args:
        did (str):
        wv (CreateBlobTranslationWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTTranslateFormatParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTranslationRequestInfo
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        client=client,
        body=body,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: CreateBlobTranslationWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTTranslateFormatParams,
    link_document_id: str | Unset = "",
) -> Response[BTTranslationRequestInfo]:
    """Export a blob element to another format.

     * Use `formatName` in the JSON request body to specify the export file type. Use
    [Translations/getAllTranslatorFormats]#/Translation/getAllTranslatorFormats) to get a list of valid
    export file formats.
    * Set `storeInDocument` to `false` to export to a data file. Set to `true` to export to a blob
    element in the same document.
    * See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.

    Args:
        did (str):
        wv (CreateBlobTranslationWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTTranslateFormatParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTranslationRequestInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: CreateBlobTranslationWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTTranslateFormatParams,
    link_document_id: str | Unset = "",
) -> BTTranslationRequestInfo | None:
    """Export a blob element to another format.

     * Use `formatName` in the JSON request body to specify the export file type. Use
    [Translations/getAllTranslatorFormats]#/Translation/getAllTranslatorFormats) to get a list of valid
    export file formats.
    * Set `storeInDocument` to `false` to export to a data file. Set to `true` to export to a blob
    element in the same document.
    * See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.

    Args:
        did (str):
        wv (CreateBlobTranslationWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTTranslateFormatParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTranslationRequestInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            eid=eid,
            client=client,
            body=body,
            link_document_id=link_document_id,
        )
    ).parsed
