from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_variable_studio_reference_list_info import BTVariableStudioReferenceListInfo
from ...models.set_variable_studio_references_response_default import SetVariableStudioReferencesResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTVariableStudioReferenceListInfo,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/variables/d/{did}/w/{wid}/e/{eid}/variablestudioreferences".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SetVariableStudioReferencesResponseDefault:
    response_default = SetVariableStudioReferencesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SetVariableStudioReferencesResponseDefault]:
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
    body: BTVariableStudioReferenceListInfo,
    link_document_id: str | Unset = "",
) -> Response[SetVariableStudioReferencesResponseDefault]:
    """Set the Variable Studio references for an element.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTVariableStudioReferenceListInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetVariableStudioReferencesResponseDefault]
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
    body: BTVariableStudioReferenceListInfo,
    link_document_id: str | Unset = "",
) -> SetVariableStudioReferencesResponseDefault | None:
    """Set the Variable Studio references for an element.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTVariableStudioReferenceListInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetVariableStudioReferencesResponseDefault
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
    body: BTVariableStudioReferenceListInfo,
    link_document_id: str | Unset = "",
) -> Response[SetVariableStudioReferencesResponseDefault]:
    """Set the Variable Studio references for an element.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTVariableStudioReferenceListInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetVariableStudioReferencesResponseDefault]
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
    body: BTVariableStudioReferenceListInfo,
    link_document_id: str | Unset = "",
) -> SetVariableStudioReferencesResponseDefault | None:
    """Set the Variable Studio references for an element.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTVariableStudioReferenceListInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetVariableStudioReferencesResponseDefault
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
