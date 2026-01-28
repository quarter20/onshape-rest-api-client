from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_modification_request_info import BTAppModificationRequestInfo
from ...models.bt_drawing_modification_params import BTDrawingModificationParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTDrawingModificationParams,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/drawings/d/{did}/w/{wid}/e/{eid}/modify".format(
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppModificationRequestInfo:
    response_default = BTAppModificationRequestInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppModificationRequestInfo]:
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
    body: BTDrawingModificationParams,
    link_document_id: str | Unset = "",
) -> Response[BTAppModificationRequestInfo]:
    """Modify a drawing via JSON payload.

     See [API Guide: Drawings](https://onshape-public.github.io/docs/api-adv/drawings/) for more
    information.When polling for drawing modifications to complete, use a reasonable interval (e.g.,
    avoid polling multiple times a second, use an exponential backoff strategy, etc.). See [Rate
    Limiting](/docs/api-adv/errors/#429) and [API Limits](/docs/auth/limits) for more information.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTDrawingModificationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppModificationRequestInfo]
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
    body: BTDrawingModificationParams,
    link_document_id: str | Unset = "",
) -> BTAppModificationRequestInfo | None:
    """Modify a drawing via JSON payload.

     See [API Guide: Drawings](https://onshape-public.github.io/docs/api-adv/drawings/) for more
    information.When polling for drawing modifications to complete, use a reasonable interval (e.g.,
    avoid polling multiple times a second, use an exponential backoff strategy, etc.). See [Rate
    Limiting](/docs/api-adv/errors/#429) and [API Limits](/docs/auth/limits) for more information.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTDrawingModificationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppModificationRequestInfo
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
    body: BTDrawingModificationParams,
    link_document_id: str | Unset = "",
) -> Response[BTAppModificationRequestInfo]:
    """Modify a drawing via JSON payload.

     See [API Guide: Drawings](https://onshape-public.github.io/docs/api-adv/drawings/) for more
    information.When polling for drawing modifications to complete, use a reasonable interval (e.g.,
    avoid polling multiple times a second, use an exponential backoff strategy, etc.). See [Rate
    Limiting](/docs/api-adv/errors/#429) and [API Limits](/docs/auth/limits) for more information.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTDrawingModificationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppModificationRequestInfo]
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
    body: BTDrawingModificationParams,
    link_document_id: str | Unset = "",
) -> BTAppModificationRequestInfo | None:
    """Modify a drawing via JSON payload.

     See [API Guide: Drawings](https://onshape-public.github.io/docs/api-adv/drawings/) for more
    information.When polling for drawing modifications to complete, use a reasonable interval (e.g.,
    avoid polling multiple times a second, use an exponential backoff strategy, etc.). See [Rate
    Limiting](/docs/api-adv/errors/#429) and [API Limits](/docs/auth/limits) for more information.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTDrawingModificationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppModificationRequestInfo
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
