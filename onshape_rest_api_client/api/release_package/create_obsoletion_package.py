from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_obsoletion_package_response_default import CreateObsoletionPackageResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wfid: str,
    *,
    revision_id: str,
    debug_mode: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["revisionId"] = revision_id

    params["debugMode"] = debug_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/releasepackages/obsoletion/{wfid}".format(
            wfid=quote(str(wfid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateObsoletionPackageResponseDefault:
    response_default = CreateObsoletionPackageResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateObsoletionPackageResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wfid: str,
    *,
    client: AuthenticatedClient,
    revision_id: str,
    debug_mode: bool | Unset = False,
) -> Response[CreateObsoletionPackageResponseDefault]:
    """Create an obsoletion package to make an existing revision obsolete.

    Args:
        wfid (str):
        revision_id (str):
        debug_mode (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateObsoletionPackageResponseDefault]
    """

    kwargs = _get_kwargs(
        wfid=wfid,
        revision_id=revision_id,
        debug_mode=debug_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wfid: str,
    *,
    client: AuthenticatedClient,
    revision_id: str,
    debug_mode: bool | Unset = False,
) -> CreateObsoletionPackageResponseDefault | None:
    """Create an obsoletion package to make an existing revision obsolete.

    Args:
        wfid (str):
        revision_id (str):
        debug_mode (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateObsoletionPackageResponseDefault
    """

    return sync_detailed(
        wfid=wfid,
        client=client,
        revision_id=revision_id,
        debug_mode=debug_mode,
    ).parsed


async def asyncio_detailed(
    wfid: str,
    *,
    client: AuthenticatedClient,
    revision_id: str,
    debug_mode: bool | Unset = False,
) -> Response[CreateObsoletionPackageResponseDefault]:
    """Create an obsoletion package to make an existing revision obsolete.

    Args:
        wfid (str):
        revision_id (str):
        debug_mode (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateObsoletionPackageResponseDefault]
    """

    kwargs = _get_kwargs(
        wfid=wfid,
        revision_id=revision_id,
        debug_mode=debug_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wfid: str,
    *,
    client: AuthenticatedClient,
    revision_id: str,
    debug_mode: bool | Unset = False,
) -> CreateObsoletionPackageResponseDefault | None:
    """Create an obsoletion package to make an existing revision obsolete.

    Args:
        wfid (str):
        revision_id (str):
        debug_mode (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateObsoletionPackageResponseDefault
    """

    return (
        await asyncio_detailed(
            wfid=wfid,
            client=client,
            revision_id=revision_id,
            debug_mode=debug_mode,
        )
    ).parsed
