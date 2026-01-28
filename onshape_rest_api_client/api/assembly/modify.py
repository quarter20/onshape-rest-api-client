from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_assembly_modification_params import BTAssemblyModificationParams
from ...models.modify_response_default import ModifyResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTAssemblyModificationParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/assemblies/d/{did}/w/{wid}/e/{eid}/modify".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ModifyResponseDefault:
    response_default = ModifyResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModifyResponseDefault]:
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
    body: BTAssemblyModificationParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> Response[ModifyResponseDefault]:
    """Modify an assembly.

     This endpoint can include multiple modifications to an assembly with one change. For example, it can
    delete/suppress/unsuppress/transform multiple instances. It creates one history entry in the
    document history list.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTAssemblyModificationParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModifyResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
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
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTAssemblyModificationParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> ModifyResponseDefault | None:
    """Modify an assembly.

     This endpoint can include multiple modifications to an assembly with one change. For example, it can
    delete/suppress/unsuppress/transform multiple instances. It creates one history entry in the
    document history list.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTAssemblyModificationParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModifyResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        client=client,
        body=body,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTAssemblyModificationParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> Response[ModifyResponseDefault]:
    """Modify an assembly.

     This endpoint can include multiple modifications to an assembly with one change. For example, it can
    delete/suppress/unsuppress/transform multiple instances. It creates one history entry in the
    document history list.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTAssemblyModificationParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModifyResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTAssemblyModificationParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> ModifyResponseDefault | None:
    """Modify an assembly.

     This endpoint can include multiple modifications to an assembly with one change. For example, it can
    delete/suppress/unsuppress/transform multiple instances. It creates one history entry in the
    document history list.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTAssemblyModificationParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModifyResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            client=client,
            body=body,
            link_document_id=link_document_id,
        )
    ).parsed
