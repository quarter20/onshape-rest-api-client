from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_mass_properties_info import BTMassPropertiesInfo
from ...models.get_assembly_mass_properties_wvm import GetAssemblyMassPropertiesWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetAssemblyMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assemblies/d/{did}/{wvm}/{wvmid}/e/{eid}/massproperties".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTMassPropertiesInfo:
    response_default = BTMassPropertiesInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTMassPropertiesInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetAssemblyMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
) -> Response[BTMassPropertiesInfo]:
    """Get the mass properties for the assembly.

     The assembly must contain parts that have density. The returned schema includes the same information
    as in the Onshape [Mass Properties Tool](https://cad.onshape.com/help/Content/massprops-asmb.htm).
    When three values are returned:
     * The first is the calculated value.
     * The second is the minimum possible value, considering tolerance.
     * The third is the maximum possible value, considering tolerance.

    Args:
        did (str):
        wvm (GetAssemblyMassPropertiesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMassPropertiesInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetAssemblyMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
) -> BTMassPropertiesInfo | None:
    """Get the mass properties for the assembly.

     The assembly must contain parts that have density. The returned schema includes the same information
    as in the Onshape [Mass Properties Tool](https://cad.onshape.com/help/Content/massprops-asmb.htm).
    When three values are returned:
     * The first is the calculated value.
     * The second is the minimum possible value, considering tolerance.
     * The third is the maximum possible value, considering tolerance.

    Args:
        did (str):
        wvm (GetAssemblyMassPropertiesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMassPropertiesInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetAssemblyMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
) -> Response[BTMassPropertiesInfo]:
    """Get the mass properties for the assembly.

     The assembly must contain parts that have density. The returned schema includes the same information
    as in the Onshape [Mass Properties Tool](https://cad.onshape.com/help/Content/massprops-asmb.htm).
    When three values are returned:
     * The first is the calculated value.
     * The second is the minimum possible value, considering tolerance.
     * The third is the maximum possible value, considering tolerance.

    Args:
        did (str):
        wvm (GetAssemblyMassPropertiesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMassPropertiesInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetAssemblyMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
) -> BTMassPropertiesInfo | None:
    """Get the mass properties for the assembly.

     The assembly must contain parts that have density. The returned schema includes the same information
    as in the Onshape [Mass Properties Tool](https://cad.onshape.com/help/Content/massprops-asmb.htm).
    When three values are returned:
     * The first is the calculated value.
     * The second is the minimum possible value, considering tolerance.
     * The third is the maximum possible value, considering tolerance.

    Args:
        did (str):
        wvm (GetAssemblyMassPropertiesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMassPropertiesInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
            configuration=configuration,
        )
    ).parsed
