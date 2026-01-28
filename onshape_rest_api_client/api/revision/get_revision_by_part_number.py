from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_revision_info import BTRevisionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    pnum: str,
    *,
    revision: str | Unset = UNSET,
    element_type: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["revision"] = revision

    params["elementType"] = element_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/revisions/c/{cid}/partnumber/{pnum}".format(
            cid=quote(str(cid), safe=""),
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
    cid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    revision: str | Unset = UNSET,
    element_type: int | Unset = UNSET,
) -> Response[BTRevisionInfo]:
    """Get details for the specified revision.

     If the `revision` parameter is left blank, the latest revision information is returned. See [API
    Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-latest-
    revision-info) for more details.

    Args:
        cid (str):
        pnum (str):
        revision (str | Unset):
        element_type (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRevisionInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        pnum=pnum,
        revision=revision,
        element_type=element_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    revision: str | Unset = UNSET,
    element_type: int | Unset = UNSET,
) -> BTRevisionInfo | None:
    """Get details for the specified revision.

     If the `revision` parameter is left blank, the latest revision information is returned. See [API
    Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-latest-
    revision-info) for more details.

    Args:
        cid (str):
        pnum (str):
        revision (str | Unset):
        element_type (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRevisionInfo
    """

    return sync_detailed(
        cid=cid,
        pnum=pnum,
        client=client,
        revision=revision,
        element_type=element_type,
    ).parsed


async def asyncio_detailed(
    cid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    revision: str | Unset = UNSET,
    element_type: int | Unset = UNSET,
) -> Response[BTRevisionInfo]:
    """Get details for the specified revision.

     If the `revision` parameter is left blank, the latest revision information is returned. See [API
    Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-latest-
    revision-info) for more details.

    Args:
        cid (str):
        pnum (str):
        revision (str | Unset):
        element_type (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRevisionInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        pnum=pnum,
        revision=revision,
        element_type=element_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    revision: str | Unset = UNSET,
    element_type: int | Unset = UNSET,
) -> BTRevisionInfo | None:
    """Get details for the specified revision.

     If the `revision` parameter is left blank, the latest revision information is returned. See [API
    Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-latest-
    revision-info) for more details.

    Args:
        cid (str):
        pnum (str):
        revision (str | Unset):
        element_type (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRevisionInfo
    """

    return (
        await asyncio_detailed(
            cid=cid,
            pnum=pnum,
            client=client,
            revision=revision,
            element_type=element_type,
        )
    ).parsed
