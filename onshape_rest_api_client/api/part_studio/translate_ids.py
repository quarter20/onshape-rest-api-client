from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_id_translation_info import BTIdTranslationInfo
from ...models.bt_id_translation_params import BTIdTranslationParams
from ...types import Response


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    body: BTIdTranslationParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/idtranslations".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTIdTranslationInfo:
    response_default = BTIdTranslationInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTIdTranslationInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTIdTranslationParams,
) -> Response[BTIdTranslationInfo]:
    """Find corresponding deterministic IDs from a source document microversion at the target version.

     * Deterministic IDs are only valid for one microversion.
    * This maps deterministic IDs between microversions in an attempt to find the corresponding entities
    in each version.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTIdTranslationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTIdTranslationInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTIdTranslationParams,
) -> BTIdTranslationInfo | None:
    """Find corresponding deterministic IDs from a source document microversion at the target version.

     * Deterministic IDs are only valid for one microversion.
    * This maps deterministic IDs between microversions in an attempt to find the corresponding entities
    in each version.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTIdTranslationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTIdTranslationInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTIdTranslationParams,
) -> Response[BTIdTranslationInfo]:
    """Find corresponding deterministic IDs from a source document microversion at the target version.

     * Deterministic IDs are only valid for one microversion.
    * This maps deterministic IDs between microversions in an attempt to find the corresponding entities
    in each version.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTIdTranslationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTIdTranslationInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTIdTranslationParams,
) -> BTIdTranslationInfo | None:
    """Find corresponding deterministic IDs from a source document microversion at the target version.

     * Deterministic IDs are only valid for one microversion.
    * This maps deterministic IDs between microversions in an attempt to find the corresponding entities
    in each version.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTIdTranslationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTIdTranslationInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            body=body,
        )
    ).parsed
