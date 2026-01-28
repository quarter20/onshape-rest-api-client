from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_model_format_info import BTModelFormatInfo
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/drawings/d/{did}/w/{wid}/e/{eid}/translationformats".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BTModelFormatInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTModelFormatInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTModelFormatInfo]]:
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
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[BTModelFormatInfo]]:
    """Get a list of all valid formats the drawing can be translated (exported) to.

     See [API Guide: Translations](https://onshape-public.github.io/docs/api-adv/translation/#export-a-
    drawing-as-a-json) for more information.

    Args:
        did (str):
        wid (str):
        eid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTModelFormatInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[BTModelFormatInfo] | None:
    """Get a list of all valid formats the drawing can be translated (exported) to.

     See [API Guide: Translations](https://onshape-public.github.io/docs/api-adv/translation/#export-a-
    drawing-as-a-json) for more information.

    Args:
        did (str):
        wid (str):
        eid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTModelFormatInfo]
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[BTModelFormatInfo]]:
    """Get a list of all valid formats the drawing can be translated (exported) to.

     See [API Guide: Translations](https://onshape-public.github.io/docs/api-adv/translation/#export-a-
    drawing-as-a-json) for more information.

    Args:
        did (str):
        wid (str):
        eid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTModelFormatInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[BTModelFormatInfo] | None:
    """Get a list of all valid formats the drawing can be translated (exported) to.

     See [API Guide: Translations](https://onshape-public.github.io/docs/api-adv/translation/#export-a-
    drawing-as-a-json) for more information.

    Args:
        did (str):
        wid (str):
        eid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTModelFormatInfo]
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            client=client,
        )
    ).parsed
