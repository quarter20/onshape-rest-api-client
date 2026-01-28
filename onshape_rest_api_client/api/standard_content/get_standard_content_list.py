from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_standard_content_hierarchy_item import BTStandardContentHierarchyItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    standard: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["standard"] = standard

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/standardcontent/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[BTStandardContentHierarchyItem]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTStandardContentHierarchyItem.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTStandardContentHierarchyItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    standard: str | Unset = "",
) -> Response[list[BTStandardContentHierarchyItem]]:
    """List all standard content.

    Args:
        standard (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTStandardContentHierarchyItem]]
    """

    kwargs = _get_kwargs(
        standard=standard,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    standard: str | Unset = "",
) -> list[BTStandardContentHierarchyItem] | None:
    """List all standard content.

    Args:
        standard (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTStandardContentHierarchyItem]
    """

    return sync_detailed(
        client=client,
        standard=standard,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    standard: str | Unset = "",
) -> Response[list[BTStandardContentHierarchyItem]]:
    """List all standard content.

    Args:
        standard (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTStandardContentHierarchyItem]]
    """

    kwargs = _get_kwargs(
        standard=standard,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    standard: str | Unset = "",
) -> list[BTStandardContentHierarchyItem] | None:
    """List all standard content.

    Args:
        standard (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTStandardContentHierarchyItem]
    """

    return (
        await asyncio_detailed(
            client=client,
            standard=standard,
        )
    ).parsed
