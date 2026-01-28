from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_task_list_response import BTTaskListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: str | Unset = UNSET,
    status: int | Unset = 2,
    role: int | Unset = 1,
    order: int | Unset = 1,
    type_: list[str] | Unset = UNSET,
    document_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userId"] = user_id

    params["status"] = status

    params["role"] = role

    params["order"] = order

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params["documentId"] = document_id

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTTaskListResponse:
    response_default = BTTaskListResponse.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTTaskListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str | Unset = UNSET,
    status: int | Unset = 2,
    role: int | Unset = 1,
    order: int | Unset = 1,
    type_: list[str] | Unset = UNSET,
    document_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> Response[BTTaskListResponse]:
    """Lists tasks assigned to the specified user

     Returns a list of tasks assigneed to the userId specified in the request. Only company admins can
    view tasks that were not created by them and are not assigned to them.

    Args:
        user_id (str | Unset):
        status (int | Unset):  Default: 2.
        role (int | Unset):  Default: 1.
        order (int | Unset):  Default: 1.
        type_ (list[str] | Unset):
        document_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTaskListResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        status=status,
        role=role,
        order=order,
        type_=type_,
        document_id=document_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: str | Unset = UNSET,
    status: int | Unset = 2,
    role: int | Unset = 1,
    order: int | Unset = 1,
    type_: list[str] | Unset = UNSET,
    document_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> BTTaskListResponse | None:
    """Lists tasks assigned to the specified user

     Returns a list of tasks assigneed to the userId specified in the request. Only company admins can
    view tasks that were not created by them and are not assigned to them.

    Args:
        user_id (str | Unset):
        status (int | Unset):  Default: 2.
        role (int | Unset):  Default: 1.
        order (int | Unset):  Default: 1.
        type_ (list[str] | Unset):
        document_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTaskListResponse
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        status=status,
        role=role,
        order=order,
        type_=type_,
        document_id=document_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str | Unset = UNSET,
    status: int | Unset = 2,
    role: int | Unset = 1,
    order: int | Unset = 1,
    type_: list[str] | Unset = UNSET,
    document_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> Response[BTTaskListResponse]:
    """Lists tasks assigned to the specified user

     Returns a list of tasks assigneed to the userId specified in the request. Only company admins can
    view tasks that were not created by them and are not assigned to them.

    Args:
        user_id (str | Unset):
        status (int | Unset):  Default: 2.
        role (int | Unset):  Default: 1.
        order (int | Unset):  Default: 1.
        type_ (list[str] | Unset):
        document_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTaskListResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        status=status,
        role=role,
        order=order,
        type_=type_,
        document_id=document_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: str | Unset = UNSET,
    status: int | Unset = 2,
    role: int | Unset = 1,
    order: int | Unset = 1,
    type_: list[str] | Unset = UNSET,
    document_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> BTTaskListResponse | None:
    """Lists tasks assigned to the specified user

     Returns a list of tasks assigneed to the userId specified in the request. Only company admins can
    view tasks that were not created by them and are not assigned to them.

    Args:
        user_id (str | Unset):
        status (int | Unset):  Default: 2.
        role (int | Unset):  Default: 1.
        order (int | Unset):  Default: 1.
        type_ (list[str] | Unset):
        document_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTaskListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            status=status,
            role=role,
            order=order,
            type_=type_,
            document_id=document_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
