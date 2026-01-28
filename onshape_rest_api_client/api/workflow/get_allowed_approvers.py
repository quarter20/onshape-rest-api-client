from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_workflow_observer_option_info import BTListResponseBTWorkflowObserverOptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    q: str | Unset = "",
    expand_teams: bool | Unset = True,
    include_self: bool | Unset = True,
    exclude_connections: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["expandTeams"] = expand_teams

    params["includeSelf"] = include_self

    params["excludeConnections"] = exclude_connections

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workflow/c/{company_id}/approvers".format(
            company_id=quote(str(company_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTListResponseBTWorkflowObserverOptionInfo:
    response_default = BTListResponseBTWorkflowObserverOptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTWorkflowObserverOptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = "",
    expand_teams: bool | Unset = True,
    include_self: bool | Unset = True,
    exclude_connections: bool | Unset = False,
) -> Response[BTListResponseBTWorkflowObserverOptionInfo]:
    """Get all identities allowed to be approvers on a workflow object.

     * Identities can be users and/or teams.
    * For Enterprise accounts, also includes roles and any aliases that contain allowed users/teams.
    * Not object- or property-specific.
    * Used for delegation and company settings.

    Args:
        company_id (str):
        q (str | Unset):  Default: ''.
        expand_teams (bool | Unset):  Default: True.
        include_self (bool | Unset):  Default: True.
        exclude_connections (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTWorkflowObserverOptionInfo]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        q=q,
        expand_teams=expand_teams,
        include_self=include_self,
        exclude_connections=exclude_connections,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = "",
    expand_teams: bool | Unset = True,
    include_self: bool | Unset = True,
    exclude_connections: bool | Unset = False,
) -> BTListResponseBTWorkflowObserverOptionInfo | None:
    """Get all identities allowed to be approvers on a workflow object.

     * Identities can be users and/or teams.
    * For Enterprise accounts, also includes roles and any aliases that contain allowed users/teams.
    * Not object- or property-specific.
    * Used for delegation and company settings.

    Args:
        company_id (str):
        q (str | Unset):  Default: ''.
        expand_teams (bool | Unset):  Default: True.
        include_self (bool | Unset):  Default: True.
        exclude_connections (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTWorkflowObserverOptionInfo
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        q=q,
        expand_teams=expand_teams,
        include_self=include_self,
        exclude_connections=exclude_connections,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = "",
    expand_teams: bool | Unset = True,
    include_self: bool | Unset = True,
    exclude_connections: bool | Unset = False,
) -> Response[BTListResponseBTWorkflowObserverOptionInfo]:
    """Get all identities allowed to be approvers on a workflow object.

     * Identities can be users and/or teams.
    * For Enterprise accounts, also includes roles and any aliases that contain allowed users/teams.
    * Not object- or property-specific.
    * Used for delegation and company settings.

    Args:
        company_id (str):
        q (str | Unset):  Default: ''.
        expand_teams (bool | Unset):  Default: True.
        include_self (bool | Unset):  Default: True.
        exclude_connections (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTWorkflowObserverOptionInfo]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        q=q,
        expand_teams=expand_teams,
        include_self=include_self,
        exclude_connections=exclude_connections,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = "",
    expand_teams: bool | Unset = True,
    include_self: bool | Unset = True,
    exclude_connections: bool | Unset = False,
) -> BTListResponseBTWorkflowObserverOptionInfo | None:
    """Get all identities allowed to be approvers on a workflow object.

     * Identities can be users and/or teams.
    * For Enterprise accounts, also includes roles and any aliases that contain allowed users/teams.
    * Not object- or property-specific.
    * Used for delegation and company settings.

    Args:
        company_id (str):
        q (str | Unset):  Default: ''.
        expand_teams (bool | Unset):  Default: True.
        include_self (bool | Unset):  Default: True.
        exclude_connections (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTWorkflowObserverOptionInfo
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            q=q,
            expand_teams=expand_teams,
            include_self=include_self,
            exclude_connections=exclude_connections,
        )
    ).parsed
