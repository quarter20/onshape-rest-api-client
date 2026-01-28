from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_instance_response_default import DeleteInstanceResponseDefault
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    nid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/assemblies/d/{did}/w/{wid}/e/{eid}/instance/nodeid/{nid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
            nid=quote(str(nid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteInstanceResponseDefault:
    response_default = DeleteInstanceResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteInstanceResponseDefault]:
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
    nid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteInstanceResponseDefault]:
    """Delete an instance of an assembly.

    Args:
        did (str):
        wid (str):
        eid (str):
        nid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteInstanceResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        nid=nid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    nid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteInstanceResponseDefault | None:
    """Delete an instance of an assembly.

    Args:
        did (str):
        wid (str):
        eid (str):
        nid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteInstanceResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        nid=nid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    nid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteInstanceResponseDefault]:
    """Delete an instance of an assembly.

    Args:
        did (str):
        wid (str):
        eid (str):
        nid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteInstanceResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        nid=nid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    nid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteInstanceResponseDefault | None:
    """Delete an instance of an assembly.

    Args:
        did (str):
        wid (str):
        eid (str):
        nid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteInstanceResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            nid=nid,
            client=client,
        )
    ).parsed
