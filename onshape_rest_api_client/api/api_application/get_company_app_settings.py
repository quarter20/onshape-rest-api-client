from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_user_app_settings_info import BTUserAppSettingsInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    cpid: str,
    *,
    document_id: str | Unset = UNSET,
    key: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["documentId"] = document_id

    json_key: list[str] | Unset = UNSET
    if not isinstance(key, Unset):
        json_key = key

    params["key"] = json_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/applications/clients/{cid}/settings/companies/{cpid}".format(
            cid=quote(str(cid), safe=""),
            cpid=quote(str(cpid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTUserAppSettingsInfo:
    response_default = BTUserAppSettingsInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTUserAppSettingsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    cpid: str,
    *,
    client: AuthenticatedClient | Client,
    document_id: str | Unset = UNSET,
    key: list[str] | Unset = UNSET,
) -> Response[BTUserAppSettingsInfo]:
    """Get company-level preference settings for an application.

     This API is only usable with an OAuth token and only by the current user or admin.

    Args:
        cid (str):
        cpid (str):
        document_id (str | Unset):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTUserAppSettingsInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        cpid=cpid,
        document_id=document_id,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    cpid: str,
    *,
    client: AuthenticatedClient | Client,
    document_id: str | Unset = UNSET,
    key: list[str] | Unset = UNSET,
) -> BTUserAppSettingsInfo | None:
    """Get company-level preference settings for an application.

     This API is only usable with an OAuth token and only by the current user or admin.

    Args:
        cid (str):
        cpid (str):
        document_id (str | Unset):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTUserAppSettingsInfo
    """

    return sync_detailed(
        cid=cid,
        cpid=cpid,
        client=client,
        document_id=document_id,
        key=key,
    ).parsed


async def asyncio_detailed(
    cid: str,
    cpid: str,
    *,
    client: AuthenticatedClient | Client,
    document_id: str | Unset = UNSET,
    key: list[str] | Unset = UNSET,
) -> Response[BTUserAppSettingsInfo]:
    """Get company-level preference settings for an application.

     This API is only usable with an OAuth token and only by the current user or admin.

    Args:
        cid (str):
        cpid (str):
        document_id (str | Unset):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTUserAppSettingsInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        cpid=cpid,
        document_id=document_id,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    cpid: str,
    *,
    client: AuthenticatedClient | Client,
    document_id: str | Unset = UNSET,
    key: list[str] | Unset = UNSET,
) -> BTUserAppSettingsInfo | None:
    """Get company-level preference settings for an application.

     This API is only usable with an OAuth token and only by the current user or admin.

    Args:
        cid (str):
        cpid (str):
        document_id (str | Unset):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTUserAppSettingsInfo
    """

    return (
        await asyncio_detailed(
            cid=cid,
            cpid=cpid,
            client=client,
            document_id=document_id,
            key=key,
        )
    ).parsed
