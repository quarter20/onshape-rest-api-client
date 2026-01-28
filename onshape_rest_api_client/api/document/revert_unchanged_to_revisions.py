from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_revert_unchanged_params import BTRevertUnchangedParams
from ...models.bt_unchanged_element_info import BTUnchangedElementInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    *,
    body: BTRevertUnchangedParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/d/{did}/w/{wid}/revertunchangedtorevisions".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BTUnchangedElementInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTUnchangedElementInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTUnchangedElementInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTRevertUnchangedParams | Unset = UNSET,
) -> Response[list[BTUnchangedElementInfo]]:
    """
    Args:
        did (str):
        wid (str):
        body (BTRevertUnchangedParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTUnchangedElementInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTRevertUnchangedParams | Unset = UNSET,
) -> list[BTUnchangedElementInfo] | None:
    """
    Args:
        did (str):
        wid (str):
        body (BTRevertUnchangedParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTUnchangedElementInfo]
    """

    return sync_detailed(
        did=did,
        wid=wid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTRevertUnchangedParams | Unset = UNSET,
) -> Response[list[BTUnchangedElementInfo]]:
    """
    Args:
        did (str):
        wid (str):
        body (BTRevertUnchangedParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTUnchangedElementInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTRevertUnchangedParams | Unset = UNSET,
) -> list[BTUnchangedElementInfo] | None:
    """
    Args:
        did (str):
        wid (str):
        body (BTRevertUnchangedParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTUnchangedElementInfo]
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
            body=body,
        )
    ).parsed
