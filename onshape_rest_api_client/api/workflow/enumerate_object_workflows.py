import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx
from dateutil.parser import isoparse

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_object_workflow_info import BTListResponseBTObjectWorkflowInfo
from ...models.btapi_workflowable_type import BTAPIWorkflowableType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    *,
    object_types: list[BTAPIWorkflowableType] | Unset = UNSET,
    states: list[str] | Unset = UNSET,
    limit: int | Unset = 20,
    modified_after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_object_types: list[str] | Unset = UNSET
    if not isinstance(object_types, Unset):
        json_object_types = []
        for object_types_item_data in object_types:
            object_types_item = object_types_item_data.value
            json_object_types.append(object_types_item)

    params["objectTypes"] = json_object_types

    json_states: list[str] | Unset = UNSET
    if not isinstance(states, Unset):
        json_states = states

    params["states"] = json_states

    params["limit"] = limit

    json_modified_after: str | Unset = UNSET
    if not isinstance(modified_after, Unset):
        json_modified_after = modified_after.isoformat()
    params["modifiedAfter"] = json_modified_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workflow/companies/{cid}/objects".format(
            cid=quote(str(cid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTListResponseBTObjectWorkflowInfo:
    response_default = BTListResponseBTObjectWorkflowInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTObjectWorkflowInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
    object_types: list[BTAPIWorkflowableType] | Unset = UNSET,
    states: list[str] | Unset = UNSET,
    limit: int | Unset = 20,
    modified_after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> Response[BTListResponseBTObjectWorkflowInfo]:
    """Enumerate all of a company's workflowable objects.

     * For example, you can enumerate RELEASES, TASKS, etc in a company by last modified time.
    * Caller must be a company admin.
    * Specify `modifiedAfter` and use the `next` URI for complete enumeration.

    Args:
        cid (str):
        object_types (list[BTAPIWorkflowableType] | Unset):
        states (list[str] | Unset):
        limit (int | Unset):  Default: 20.
        modified_after (datetime.datetime | Unset):  Default: isoparse('2000-01-01T00:00:00Z').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTObjectWorkflowInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        object_types=object_types,
        states=states,
        limit=limit,
        modified_after=modified_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    *,
    client: AuthenticatedClient,
    object_types: list[BTAPIWorkflowableType] | Unset = UNSET,
    states: list[str] | Unset = UNSET,
    limit: int | Unset = 20,
    modified_after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> BTListResponseBTObjectWorkflowInfo | None:
    """Enumerate all of a company's workflowable objects.

     * For example, you can enumerate RELEASES, TASKS, etc in a company by last modified time.
    * Caller must be a company admin.
    * Specify `modifiedAfter` and use the `next` URI for complete enumeration.

    Args:
        cid (str):
        object_types (list[BTAPIWorkflowableType] | Unset):
        states (list[str] | Unset):
        limit (int | Unset):  Default: 20.
        modified_after (datetime.datetime | Unset):  Default: isoparse('2000-01-01T00:00:00Z').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTObjectWorkflowInfo
    """

    return sync_detailed(
        cid=cid,
        client=client,
        object_types=object_types,
        states=states,
        limit=limit,
        modified_after=modified_after,
    ).parsed


async def asyncio_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
    object_types: list[BTAPIWorkflowableType] | Unset = UNSET,
    states: list[str] | Unset = UNSET,
    limit: int | Unset = 20,
    modified_after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> Response[BTListResponseBTObjectWorkflowInfo]:
    """Enumerate all of a company's workflowable objects.

     * For example, you can enumerate RELEASES, TASKS, etc in a company by last modified time.
    * Caller must be a company admin.
    * Specify `modifiedAfter` and use the `next` URI for complete enumeration.

    Args:
        cid (str):
        object_types (list[BTAPIWorkflowableType] | Unset):
        states (list[str] | Unset):
        limit (int | Unset):  Default: 20.
        modified_after (datetime.datetime | Unset):  Default: isoparse('2000-01-01T00:00:00Z').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTObjectWorkflowInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        object_types=object_types,
        states=states,
        limit=limit,
        modified_after=modified_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    *,
    client: AuthenticatedClient,
    object_types: list[BTAPIWorkflowableType] | Unset = UNSET,
    states: list[str] | Unset = UNSET,
    limit: int | Unset = 20,
    modified_after: datetime.datetime | Unset = isoparse("2000-01-01T00:00:00Z"),
) -> BTListResponseBTObjectWorkflowInfo | None:
    """Enumerate all of a company's workflowable objects.

     * For example, you can enumerate RELEASES, TASKS, etc in a company by last modified time.
    * Caller must be a company admin.
    * Specify `modifiedAfter` and use the `next` URI for complete enumeration.

    Args:
        cid (str):
        object_types (list[BTAPIWorkflowableType] | Unset):
        states (list[str] | Unset):
        limit (int | Unset):  Default: 20.
        modified_after (datetime.datetime | Unset):  Default: isoparse('2000-01-01T00:00:00Z').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTObjectWorkflowInfo
    """

    return (
        await asyncio_detailed(
            cid=cid,
            client=client,
            object_types=object_types,
            states=states,
            limit=limit,
            modified_after=modified_after,
        )
    ).parsed
