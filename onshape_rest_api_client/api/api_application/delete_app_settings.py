from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    uid: str,
    *,
    key: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_key: list[str] | Unset = UNSET
    if not isinstance(key, Unset):
        json_key = key

    params["key"] = json_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/applications/clients/{cid}/settings/users/{uid}".format(
            cid=quote(str(cid), safe=""),
            uid=quote(str(uid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    uid: str,
    *,
    client: AuthenticatedClient | Client,
    key: list[str] | Unset = UNSET,
) -> Response[Any]:
    """Delete a user's application preference settings.

     This API is only usable with an OAuth token and only by the current user or admin.

    Args:
        cid (str):
        uid (str):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        cid=cid,
        uid=uid,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    cid: str,
    uid: str,
    *,
    client: AuthenticatedClient | Client,
    key: list[str] | Unset = UNSET,
) -> Response[Any]:
    """Delete a user's application preference settings.

     This API is only usable with an OAuth token and only by the current user or admin.

    Args:
        cid (str):
        uid (str):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        cid=cid,
        uid=uid,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
