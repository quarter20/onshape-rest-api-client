from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_api_table_list_1223 import BTApiTableList1223
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    configuration: str | Unset = UNSET,
    table_namespace: str | Unset = UNSET,
    table_type: str,
    table_parameters: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["configuration"] = configuration

    params["tableNamespace"] = table_namespace

    params["tableType"] = table_type

    params["tableParameters"] = table_parameters

    params["partId"] = part_id

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/fstable".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTApiTableList1223:
    response_default = BTApiTableList1223.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTApiTableList1223]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    table_namespace: str | Unset = UNSET,
    table_type: str,
    table_parameters: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTApiTableList1223]:
    """Compute and return a FeatureScript table for a Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        configuration (str | Unset):
        table_namespace (str | Unset):
        table_type (str):
        table_parameters (str | Unset):
        part_id (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTApiTableList1223]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        configuration=configuration,
        table_namespace=table_namespace,
        table_type=table_type,
        table_parameters=table_parameters,
        part_id=part_id,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    table_namespace: str | Unset = UNSET,
    table_type: str,
    table_parameters: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTApiTableList1223 | None:
    """Compute and return a FeatureScript table for a Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        configuration (str | Unset):
        table_namespace (str | Unset):
        table_type (str):
        table_parameters (str | Unset):
        part_id (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTApiTableList1223
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        configuration=configuration,
        table_namespace=table_namespace,
        table_type=table_type,
        table_parameters=table_parameters,
        part_id=part_id,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    table_namespace: str | Unset = UNSET,
    table_type: str,
    table_parameters: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTApiTableList1223]:
    """Compute and return a FeatureScript table for a Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        configuration (str | Unset):
        table_namespace (str | Unset):
        table_type (str):
        table_parameters (str | Unset):
        part_id (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTApiTableList1223]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        configuration=configuration,
        table_namespace=table_namespace,
        table_type=table_type,
        table_parameters=table_parameters,
        part_id=part_id,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    table_namespace: str | Unset = UNSET,
    table_type: str,
    table_parameters: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTApiTableList1223 | None:
    """Compute and return a FeatureScript table for a Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        configuration (str | Unset):
        table_namespace (str | Unset):
        table_type (str):
        table_parameters (str | Unset):
        part_id (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTApiTableList1223
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            configuration=configuration,
            table_namespace=table_namespace,
            table_type=table_type,
            table_parameters=table_parameters,
            part_id=part_id,
            link_document_id=link_document_id,
        )
    ).parsed
