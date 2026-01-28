from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_export_rule_valid_options_info import BTExportRuleValidOptionsInfo
from ...models.get_valid_rule_options_cu import GetValidRuleOptionsCu
from ...types import Response


def _get_kwargs(
    cu: GetValidRuleOptionsCu,
    cuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exportrules/options/{cu}/{cuid}".format(
            cu=quote(str(cu), safe=""),
            cuid=quote(str(cuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTExportRuleValidOptionsInfo:
    response_default = BTExportRuleValidOptionsInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTExportRuleValidOptionsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cu: GetValidRuleOptionsCu,
    cuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTExportRuleValidOptionsInfo]:
    """Get a list of valid export rule options for the user or company.

     Does NOT get the rules themselves; it gets the information used to create them.

    Args:
        cu (GetValidRuleOptionsCu):
        cuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTExportRuleValidOptionsInfo]
    """

    kwargs = _get_kwargs(
        cu=cu,
        cuid=cuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cu: GetValidRuleOptionsCu,
    cuid: str,
    *,
    client: AuthenticatedClient,
) -> BTExportRuleValidOptionsInfo | None:
    """Get a list of valid export rule options for the user or company.

     Does NOT get the rules themselves; it gets the information used to create them.

    Args:
        cu (GetValidRuleOptionsCu):
        cuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTExportRuleValidOptionsInfo
    """

    return sync_detailed(
        cu=cu,
        cuid=cuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    cu: GetValidRuleOptionsCu,
    cuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTExportRuleValidOptionsInfo]:
    """Get a list of valid export rule options for the user or company.

     Does NOT get the rules themselves; it gets the information used to create them.

    Args:
        cu (GetValidRuleOptionsCu):
        cuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTExportRuleValidOptionsInfo]
    """

    kwargs = _get_kwargs(
        cu=cu,
        cuid=cuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cu: GetValidRuleOptionsCu,
    cuid: str,
    *,
    client: AuthenticatedClient,
) -> BTExportRuleValidOptionsInfo | None:
    """Get a list of valid export rule options for the user or company.

     Does NOT get the rules themselves; it gets the information used to create them.

    Args:
        cu (GetValidRuleOptionsCu):
        cuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTExportRuleValidOptionsInfo
    """

    return (
        await asyncio_detailed(
            cu=cu,
            cuid=cuid,
            client=client,
        )
    ).parsed
