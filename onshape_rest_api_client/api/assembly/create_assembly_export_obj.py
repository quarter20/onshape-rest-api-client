from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_translation_request_info import BTTranslationRequestInfo
from ...models.btb_obj_export_params import BTBObjExportParams
from ...types import Response


def _get_kwargs(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
    *,
    body: BTBObjExportParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/assemblies/d/{did}/{wv}/{wvid}/e/{eid}/export/obj".format(
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
    client: AuthenticatedClient,
    body: BTBObjExportParams,
) -> Response[BTTranslationRequestInfo]:
    """Export the assembly to OBJ.

     Creates an asynchronous export of the assembly. See [API Guide: Import & Export](https://onshape-
    public.github.io/docs/api-adv/translation/#export-an-assembly-to-gltf-obj-solidworks-or-step) for
    details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):
        body (BTBObjExportParams): Options for exporting elements to OBJ.

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
    client: AuthenticatedClient,
    body: BTBObjExportParams,
) -> BTTranslationRequestInfo | None:
    """Export the assembly to OBJ.

     Creates an asynchronous export of the assembly. See [API Guide: Import & Export](https://onshape-
    public.github.io/docs/api-adv/translation/#export-an-assembly-to-gltf-obj-solidworks-or-step) for
    details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):
        body (BTBObjExportParams): Options for exporting elements to OBJ.

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
    client: AuthenticatedClient,
    body: BTBObjExportParams,
) -> Response[BTTranslationRequestInfo]:
    """Export the assembly to OBJ.

     Creates an asynchronous export of the assembly. See [API Guide: Import & Export](https://onshape-
    public.github.io/docs/api-adv/translation/#export-an-assembly-to-gltf-obj-solidworks-or-step) for
    details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):
        body (BTBObjExportParams): Options for exporting elements to OBJ.

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
    client: AuthenticatedClient,
    body: BTBObjExportParams,
) -> BTTranslationRequestInfo | None:
    """Export the assembly to OBJ.

     Creates an asynchronous export of the assembly. See [API Guide: Import & Export](https://onshape-
    public.github.io/docs/api-adv/translation/#export-an-assembly-to-gltf-obj-solidworks-or-step) for
    details.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):
        body (BTBObjExportParams): Options for exporting elements to OBJ.

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
