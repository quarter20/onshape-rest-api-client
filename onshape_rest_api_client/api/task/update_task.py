from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_task_info import BTTaskInfo
from ...models.bt_update_task_params import BTUpdateTaskParams
from ...types import Response


def _get_kwargs(
    tid: str,
    *,
    body: BTUpdateTaskParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tasks/{tid}".format(
            tid=quote(str(tid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTTaskInfo:
    response_default = BTTaskInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTTaskInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateTaskParams,
) -> Response[BTTaskInfo]:
    """Update the task and its properties.

    Args:
        tid (str):
        body (BTUpdateTaskParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTaskInfo]
    """

    kwargs = _get_kwargs(
        tid=tid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateTaskParams,
) -> BTTaskInfo | None:
    """Update the task and its properties.

    Args:
        tid (str):
        body (BTUpdateTaskParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTaskInfo
    """

    return sync_detailed(
        tid=tid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateTaskParams,
) -> Response[BTTaskInfo]:
    """Update the task and its properties.

    Args:
        tid (str):
        body (BTUpdateTaskParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTaskInfo]
    """

    kwargs = _get_kwargs(
        tid=tid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateTaskParams,
) -> BTTaskInfo | None:
    """Update the task and its properties.

    Args:
        tid (str):
        body (BTUpdateTaskParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTaskInfo
    """

    return (
        await asyncio_detailed(
            tid=tid,
            client=client,
            body=body,
        )
    ).parsed
