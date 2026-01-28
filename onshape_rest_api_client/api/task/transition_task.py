from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_task_info import BTTaskInfo
from ...types import Response


def _get_kwargs(
    tid: str,
    transition: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tasks/{tid}/{transition}".format(
            tid=quote(str(tid), safe=""),
            transition=quote(str(transition), safe=""),
        ),
    }

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
    transition: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTTaskInfo]:
    """Execute a workflow transition.

    Args:
        tid (str):
        transition (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTaskInfo]
    """

    kwargs = _get_kwargs(
        tid=tid,
        transition=transition,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tid: str,
    transition: str,
    *,
    client: AuthenticatedClient,
) -> BTTaskInfo | None:
    """Execute a workflow transition.

    Args:
        tid (str):
        transition (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTaskInfo
    """

    return sync_detailed(
        tid=tid,
        transition=transition,
        client=client,
    ).parsed


async def asyncio_detailed(
    tid: str,
    transition: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTTaskInfo]:
    """Execute a workflow transition.

    Args:
        tid (str):
        transition (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTaskInfo]
    """

    kwargs = _get_kwargs(
        tid=tid,
        transition=transition,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tid: str,
    transition: str,
    *,
    client: AuthenticatedClient,
) -> BTTaskInfo | None:
    """Execute a workflow transition.

    Args:
        tid (str):
        transition (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTaskInfo
    """

    return (
        await asyncio_detailed(
            tid=tid,
            transition=transition,
            client=client,
        )
    ).parsed
