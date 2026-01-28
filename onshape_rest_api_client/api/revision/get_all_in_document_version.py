from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_revision_info import BTListResponseBTRevisionInfo
from ...types import Response


def _get_kwargs(
    did: str,
    vid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/revisions/d/{did}/v/{vid}".format(
            did=quote(str(did), safe=""),
            vid=quote(str(vid), safe=""),
        ),
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
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTListResponseBTRevisionInfo]:
    """Get all revisions for a version.

     Retrieve a list of all revisions that exist in a document version and are owned by the document's
    owning company.  See [API Guide: Release Management](https://onshape-public.github.io/docs/api-
    adv/relmgmt/#get-all-revisions) for more details.

    Args:
        did (str):
        vid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTRevisionInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        vid=vid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
) -> BTListResponseBTRevisionInfo | None:
    """Get all revisions for a version.

     Retrieve a list of all revisions that exist in a document version and are owned by the document's
    owning company.  See [API Guide: Release Management](https://onshape-public.github.io/docs/api-
    adv/relmgmt/#get-all-revisions) for more details.

    Args:
        did (str):
        vid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTRevisionInfo
    """

    return sync_detailed(
        did=did,
        vid=vid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTListResponseBTRevisionInfo]:
    """Get all revisions for a version.

     Retrieve a list of all revisions that exist in a document version and are owned by the document's
    owning company.  See [API Guide: Release Management](https://onshape-public.github.io/docs/api-
    adv/relmgmt/#get-all-revisions) for more details.

    Args:
        did (str):
        vid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTRevisionInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        vid=vid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
) -> BTListResponseBTRevisionInfo | None:
    """Get all revisions for a version.

     Retrieve a list of all revisions that exist in a document version and are owned by the document's
    owning company.  See [API Guide: Release Management](https://onshape-public.github.io/docs/api-
    adv/relmgmt/#get-all-revisions) for more details.

    Args:
        did (str):
        vid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTRevisionInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            vid=vid,
            client=client,
        )
    ).parsed
