from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_revision_info import BTRevisionInfo
from ...types import UNSET, Response


def _get_kwargs(
    cd: str,
    cdid: str,
    pnum: str,
    *,
    et: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["et"] = et

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/revisions/{cd}/{cdid}/p/{pnum}/latest".format(
            cd=quote(str(cd), safe=""),
            cdid=quote(str(cdid), safe=""),
            pnum=quote(str(pnum), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTRevisionInfo:
    response_default = BTRevisionInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTRevisionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cd: str,
    cdid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    et: str,
) -> Response[BTRevisionInfo]:
    """Get the latest revision information for a part.

     See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-
    latest-revision-info) for more details. Returns 204 if no revisions are found.

    Args:
        cd (str):
        cdid (str):
        pnum (str):
        et (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRevisionInfo]
    """

    kwargs = _get_kwargs(
        cd=cd,
        cdid=cdid,
        pnum=pnum,
        et=et,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cd: str,
    cdid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    et: str,
) -> BTRevisionInfo | None:
    """Get the latest revision information for a part.

     See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-
    latest-revision-info) for more details. Returns 204 if no revisions are found.

    Args:
        cd (str):
        cdid (str):
        pnum (str):
        et (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRevisionInfo
    """

    return sync_detailed(
        cd=cd,
        cdid=cdid,
        pnum=pnum,
        client=client,
        et=et,
    ).parsed


async def asyncio_detailed(
    cd: str,
    cdid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    et: str,
) -> Response[BTRevisionInfo]:
    """Get the latest revision information for a part.

     See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-
    latest-revision-info) for more details. Returns 204 if no revisions are found.

    Args:
        cd (str):
        cdid (str):
        pnum (str):
        et (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRevisionInfo]
    """

    kwargs = _get_kwargs(
        cd=cd,
        cdid=cdid,
        pnum=pnum,
        et=et,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cd: str,
    cdid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    et: str,
) -> BTRevisionInfo | None:
    """Get the latest revision information for a part.

     See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-
    latest-revision-info) for more details. Returns 204 if no revisions are found.

    Args:
        cd (str):
        cdid (str):
        pnum (str):
        et (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRevisionInfo
    """

    return (
        await asyncio_detailed(
            cd=cd,
            cdid=cdid,
            pnum=pnum,
            client=client,
            et=et,
        )
    ).parsed
