from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_assembly_instance_definition_params import BTAssemblyInstanceDefinitionParams
from ...models.create_instance_response_default import CreateInstanceResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTAssemblyInstanceDefinitionParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/assemblies/d/{did}/w/{wid}/e/{eid}/instances".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateInstanceResponseDefault:
    response_default = CreateInstanceResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateInstanceResponseDefault]:
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
    client: AuthenticatedClient,
    body: BTAssemblyInstanceDefinitionParams | Unset = UNSET,
) -> Response[CreateInstanceResponseDefault]:
    """Insert an instance of a part, sketch, assembly, or Part Studio into an assembly.

     Part Studio instances may include multiple parts.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAssemblyInstanceDefinitionParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateInstanceResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
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
    client: AuthenticatedClient,
    body: BTAssemblyInstanceDefinitionParams | Unset = UNSET,
) -> CreateInstanceResponseDefault | None:
    """Insert an instance of a part, sketch, assembly, or Part Studio into an assembly.

     Part Studio instances may include multiple parts.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAssemblyInstanceDefinitionParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateInstanceResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTAssemblyInstanceDefinitionParams | Unset = UNSET,
) -> Response[CreateInstanceResponseDefault]:
    """Insert an instance of a part, sketch, assembly, or Part Studio into an assembly.

     Part Studio instances may include multiple parts.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAssemblyInstanceDefinitionParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateInstanceResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTAssemblyInstanceDefinitionParams | Unset = UNSET,
) -> CreateInstanceResponseDefault | None:
    """Insert an instance of a part, sketch, assembly, or Part Studio into an assembly.

     Part Studio instances may include multiple parts.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAssemblyInstanceDefinitionParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateInstanceResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            client=client,
            body=body,
        )
    ).parsed
