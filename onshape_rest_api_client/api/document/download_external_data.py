from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    did: str,
    fid: str,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/externaldata/{fid}".format(
            did=quote(str(did), safe=""),
            fid=quote(str(fid), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.json()))

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    fid: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[File]:
    """Download external data file(s) associated with the document.

     * See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.
    * If downloading an exported file, poll the `requestState` in the translation response and wait for
    a result of `DONE` before attempting to download the file.
    * Use the `resultExternalDataIds` from the translation response as the foreign id (`{fid}`) in this
    API.

    Args:
        did (str):
        fid (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        did=did,
        fid=fid,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    fid: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> File | None:
    """Download external data file(s) associated with the document.

     * See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.
    * If downloading an exported file, poll the `requestState` in the translation response and wait for
    a result of `DONE` before attempting to download the file.
    * Use the `resultExternalDataIds` from the translation response as the foreign id (`{fid}`) in this
    API.

    Args:
        did (str):
        fid (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        did=did,
        fid=fid,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    did: str,
    fid: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[File]:
    """Download external data file(s) associated with the document.

     * See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.
    * If downloading an exported file, poll the `requestState` in the translation response and wait for
    a result of `DONE` before attempting to download the file.
    * Use the `resultExternalDataIds` from the translation response as the foreign id (`{fid}`) in this
    API.

    Args:
        did (str):
        fid (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        did=did,
        fid=fid,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    fid: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> File | None:
    """Download external data file(s) associated with the document.

     * See [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for
    more details.
    * If downloading an exported file, poll the `requestState` in the translation response and wait for
    a result of `DONE` before attempting to download the file.
    * Use the `resultExternalDataIds` from the translation response as the foreign id (`{fid}`) in this
    API.

    Args:
        did (str):
        fid (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            did=did,
            fid=fid,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
