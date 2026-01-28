from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_translation_request_info import BTTranslationRequestInfo
from ...models.btb_solidworks_export_params import BTBSolidworksExportParams
from ...types import Response


def _get_kwargs(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
    *,
    body: BTBSolidworksExportParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/partstudios/d/{did}/{wv}/{wvid}/e/{eid}/export/solidworks".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
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
    wv: str,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
    body: BTBSolidworksExportParams,
) -> Response[BTTranslationRequestInfo]:
    """Asynchronously export a Part Studio to Solidworks.

     Creates an asynchronous export of a Part Studio to Solidworks. See [API Guide: Asynchronous
    Exports](https://onshape-public.github.io/docs/api-adv/translation/#export-a-part-studio-to-gltf-
    obj-solidworks-or-step) for more details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):
        body (BTBSolidworksExportParams): Options for exporting elements to Solidworks.

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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
    body: BTBSolidworksExportParams,
) -> BTTranslationRequestInfo | None:
    """Asynchronously export a Part Studio to Solidworks.

     Creates an asynchronous export of a Part Studio to Solidworks. See [API Guide: Asynchronous
    Exports](https://onshape-public.github.io/docs/api-adv/translation/#export-a-part-studio-to-gltf-
    obj-solidworks-or-step) for more details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):
        body (BTBSolidworksExportParams): Options for exporting elements to Solidworks.

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
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
    body: BTBSolidworksExportParams,
) -> Response[BTTranslationRequestInfo]:
    """Asynchronously export a Part Studio to Solidworks.

     Creates an asynchronous export of a Part Studio to Solidworks. See [API Guide: Asynchronous
    Exports](https://onshape-public.github.io/docs/api-adv/translation/#export-a-part-studio-to-gltf-
    obj-solidworks-or-step) for more details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):
        body (BTBSolidworksExportParams): Options for exporting elements to Solidworks.

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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
    body: BTBSolidworksExportParams,
) -> BTTranslationRequestInfo | None:
    """Asynchronously export a Part Studio to Solidworks.

     Creates an asynchronous export of a Part Studio to Solidworks. See [API Guide: Asynchronous
    Exports](https://onshape-public.github.io/docs/api-adv/translation/#export-a-part-studio-to-gltf-
    obj-solidworks-or-step) for more details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):
        body (BTBSolidworksExportParams): Options for exporting elements to Solidworks.

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
        )
    ).parsed
