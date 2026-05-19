import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_object_workflow_info import BTObjectWorkflowInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_id: str,
    *,
    request_id: str | Unset = UNSET,
    after_date_time: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["requestId"] = request_id

    json_after_date_time: str | Unset = UNSET
    if not isinstance(after_date_time, Unset):
        json_after_date_time = after_date_time.isoformat()
    params["afterDateTime"] = json_after_date_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workflow/obj/{object_id}".format(
            object_id=quote(str(object_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTObjectWorkflowInfo:
    response_default = BTObjectWorkflowInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTObjectWorkflowInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient,
    request_id: str | Unset = UNSET,
    after_date_time: datetime.datetime | Unset = UNSET,
) -> Response[BTObjectWorkflowInfo]:
    """Lightweight information about the current state of a workflowable object like release package.

     Caller must be a company admin as this api allows access to all company owned workflowable objects.

    Args:
        object_id (str):
        request_id (str | Unset):
        after_date_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTObjectWorkflowInfo]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        request_id=request_id,
        after_date_time=after_date_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_id: str,
    *,
    client: AuthenticatedClient,
    request_id: str | Unset = UNSET,
    after_date_time: datetime.datetime | Unset = UNSET,
) -> BTObjectWorkflowInfo | None:
    """Lightweight information about the current state of a workflowable object like release package.

     Caller must be a company admin as this api allows access to all company owned workflowable objects.

    Args:
        object_id (str):
        request_id (str | Unset):
        after_date_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTObjectWorkflowInfo
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
        request_id=request_id,
        after_date_time=after_date_time,
    ).parsed


async def asyncio_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient,
    request_id: str | Unset = UNSET,
    after_date_time: datetime.datetime | Unset = UNSET,
) -> Response[BTObjectWorkflowInfo]:
    """Lightweight information about the current state of a workflowable object like release package.

     Caller must be a company admin as this api allows access to all company owned workflowable objects.

    Args:
        object_id (str):
        request_id (str | Unset):
        after_date_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTObjectWorkflowInfo]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        request_id=request_id,
        after_date_time=after_date_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: str,
    *,
    client: AuthenticatedClient,
    request_id: str | Unset = UNSET,
    after_date_time: datetime.datetime | Unset = UNSET,
) -> BTObjectWorkflowInfo | None:
    """Lightweight information about the current state of a workflowable object like release package.

     Caller must be a company admin as this api allows access to all company owned workflowable objects.

    Args:
        object_id (str):
        request_id (str | Unset):
        after_date_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTObjectWorkflowInfo
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
            request_id=request_id,
            after_date_time=after_date_time,
        )
    ).parsed
