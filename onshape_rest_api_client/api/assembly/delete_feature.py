from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bt_feature_api_base_1430 import BTFeatureApiBase1430
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    fid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/assemblies/d/{did}/w/{wid}/e/{eid}/features/featureid/{fid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
            fid=quote(str(fid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTFeatureApiBase1430 | None:
    if response.status_code == 200:
        response_200 = BTFeatureApiBase1430.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTFeatureApiBase1430]:
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
    fid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTFeatureApiBase1430]:
    """Delete a feature from an assembly.

    Args:
        did (str):
        wid (str):
        eid (str):
        fid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureApiBase1430]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        fid=fid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    fid: str,
    *,
    client: AuthenticatedClient,
) -> BTFeatureApiBase1430 | None:
    """Delete a feature from an assembly.

    Args:
        did (str):
        wid (str):
        eid (str):
        fid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureApiBase1430
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        fid=fid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    fid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTFeatureApiBase1430]:
    """Delete a feature from an assembly.

    Args:
        did (str):
        wid (str):
        eid (str):
        fid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureApiBase1430]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        fid=fid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    fid: str,
    *,
    client: AuthenticatedClient,
) -> BTFeatureApiBase1430 | None:
    """Delete a feature from an assembly.

    Args:
        did (str):
        wid (str):
        eid (str):
        fid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureApiBase1430
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            fid=fid,
            client=client,
        )
    ).parsed
