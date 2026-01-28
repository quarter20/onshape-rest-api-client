import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx
from dateutil.parser import isoparse

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_revision_info import BTListResponseBTRevisionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    *,
    element_type: int | Unset = UNSET,
    limit: int | Unset = 20,
    latest_only: bool | Unset = False,
    after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["elementType"] = element_type

    params["limit"] = limit

    params["latestOnly"] = latest_only

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/revisions/companies/{cid}".format(
            cid=quote(str(cid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTListResponseBTRevisionInfo:
    response_default = BTListResponseBTRevisionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTRevisionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
    element_type: int | Unset = UNSET,
    limit: int | Unset = 20,
    latest_only: bool | Unset = False,
    after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> Response[BTListResponseBTRevisionInfo]:
    """Get all revisions for a company.

     See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-all-
    revisions) for more details.
    * Returns a list of `limit` size of all objects per API call.
    * To get the next set of results, use the `next` URL from the response body.
    * Do not change any other query parameters during subsequent enumeration.
    * Persist `after` query param value and use it to begin a fresh enumeration at a later date.
    * This API can only be called by company admins.

    Args:
        cid (str):
        element_type (int | Unset):
        limit (int | Unset):  Default: 20.
        latest_only (bool | Unset):  Default: False.
        after (datetime.datetime | Unset):  Default: isoparse('2000-01-01T00:00:00Z').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTRevisionInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        element_type=element_type,
        limit=limit,
        latest_only=latest_only,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    *,
    client: AuthenticatedClient,
    element_type: int | Unset = UNSET,
    limit: int | Unset = 20,
    latest_only: bool | Unset = False,
    after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> BTListResponseBTRevisionInfo | None:
    """Get all revisions for a company.

     See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-all-
    revisions) for more details.
    * Returns a list of `limit` size of all objects per API call.
    * To get the next set of results, use the `next` URL from the response body.
    * Do not change any other query parameters during subsequent enumeration.
    * Persist `after` query param value and use it to begin a fresh enumeration at a later date.
    * This API can only be called by company admins.

    Args:
        cid (str):
        element_type (int | Unset):
        limit (int | Unset):  Default: 20.
        latest_only (bool | Unset):  Default: False.
        after (datetime.datetime | Unset):  Default: isoparse('2000-01-01T00:00:00Z').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTRevisionInfo
    """

    return sync_detailed(
        cid=cid,
        client=client,
        element_type=element_type,
        limit=limit,
        latest_only=latest_only,
        after=after,
    ).parsed


async def asyncio_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
    element_type: int | Unset = UNSET,
    limit: int | Unset = 20,
    latest_only: bool | Unset = False,
    after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> Response[BTListResponseBTRevisionInfo]:
    """Get all revisions for a company.

     See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-all-
    revisions) for more details.
    * Returns a list of `limit` size of all objects per API call.
    * To get the next set of results, use the `next` URL from the response body.
    * Do not change any other query parameters during subsequent enumeration.
    * Persist `after` query param value and use it to begin a fresh enumeration at a later date.
    * This API can only be called by company admins.

    Args:
        cid (str):
        element_type (int | Unset):
        limit (int | Unset):  Default: 20.
        latest_only (bool | Unset):  Default: False.
        after (datetime.datetime | Unset):  Default: isoparse('2000-01-01T00:00:00Z').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTRevisionInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        element_type=element_type,
        limit=limit,
        latest_only=latest_only,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    *,
    client: AuthenticatedClient,
    element_type: int | Unset = UNSET,
    limit: int | Unset = 20,
    latest_only: bool | Unset = False,
    after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> BTListResponseBTRevisionInfo | None:
    """Get all revisions for a company.

     See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/#get-all-
    revisions) for more details.
    * Returns a list of `limit` size of all objects per API call.
    * To get the next set of results, use the `next` URL from the response body.
    * Do not change any other query parameters during subsequent enumeration.
    * Persist `after` query param value and use it to begin a fresh enumeration at a later date.
    * This API can only be called by company admins.

    Args:
        cid (str):
        element_type (int | Unset):
        limit (int | Unset):  Default: 20.
        latest_only (bool | Unset):  Default: False.
        after (datetime.datetime | Unset):  Default: isoparse('2000-01-01T00:00:00Z').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTRevisionInfo
    """

    return (
        await asyncio_detailed(
            cid=cid,
            client=client,
            element_type=element_type,
            limit=limit,
            latest_only=latest_only,
            after=after,
        )
    ).parsed
