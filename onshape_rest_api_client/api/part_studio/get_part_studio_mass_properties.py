from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_mass_properties_bulk_info import BTMassPropertiesBulkInfo
from ...models.get_part_studio_mass_properties_wvm import GetPartStudioMassPropertiesWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetPartStudioMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_id: list[str] | Unset = UNSET,
    mass_as_group: bool | Unset = True,
    use_mass_property_overrides: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["rollbackBarIndex"] = rollback_bar_index

    params["elementMicroversionId"] = element_microversion_id

    json_part_id: list[str] | Unset = UNSET
    if not isinstance(part_id, Unset):
        json_part_id = part_id

    params["partId"] = json_part_id

    params["massAsGroup"] = mass_as_group

    params["useMassPropertyOverrides"] = use_mass_property_overrides

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/massproperties".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTMassPropertiesBulkInfo:
    response_default = BTMassPropertiesBulkInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTMassPropertiesBulkInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetPartStudioMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_id: list[str] | Unset = UNSET,
    mass_as_group: bool | Unset = True,
    use_mass_property_overrides: bool | Unset = False,
) -> Response[BTMassPropertiesBulkInfo]:
    """Get the mass properties for a Part Studio.

     Parts must have density. The returned schema includes the same information as in the Onshape [Mass
    Properties Tool](https://cad.onshape.com/help/Content/massprops-ps.htm).

    When three values are returned:
     * The first is the calculated value.
     * The second is the minimum possible value, considering tolerance.
     * The third is the maximum possible value, considering tolerance.

     See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wvm (GetPartStudioMassPropertiesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        part_id (list[str] | Unset):
        mass_as_group (bool | Unset):  Default: True.
        use_mass_property_overrides (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMassPropertiesBulkInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        part_id=part_id,
        mass_as_group=mass_as_group,
        use_mass_property_overrides=use_mass_property_overrides,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetPartStudioMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_id: list[str] | Unset = UNSET,
    mass_as_group: bool | Unset = True,
    use_mass_property_overrides: bool | Unset = False,
) -> BTMassPropertiesBulkInfo | None:
    """Get the mass properties for a Part Studio.

     Parts must have density. The returned schema includes the same information as in the Onshape [Mass
    Properties Tool](https://cad.onshape.com/help/Content/massprops-ps.htm).

    When three values are returned:
     * The first is the calculated value.
     * The second is the minimum possible value, considering tolerance.
     * The third is the maximum possible value, considering tolerance.

     See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wvm (GetPartStudioMassPropertiesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        part_id (list[str] | Unset):
        mass_as_group (bool | Unset):  Default: True.
        use_mass_property_overrides (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMassPropertiesBulkInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        part_id=part_id,
        mass_as_group=mass_as_group,
        use_mass_property_overrides=use_mass_property_overrides,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetPartStudioMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_id: list[str] | Unset = UNSET,
    mass_as_group: bool | Unset = True,
    use_mass_property_overrides: bool | Unset = False,
) -> Response[BTMassPropertiesBulkInfo]:
    """Get the mass properties for a Part Studio.

     Parts must have density. The returned schema includes the same information as in the Onshape [Mass
    Properties Tool](https://cad.onshape.com/help/Content/massprops-ps.htm).

    When three values are returned:
     * The first is the calculated value.
     * The second is the minimum possible value, considering tolerance.
     * The third is the maximum possible value, considering tolerance.

     See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wvm (GetPartStudioMassPropertiesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        part_id (list[str] | Unset):
        mass_as_group (bool | Unset):  Default: True.
        use_mass_property_overrides (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMassPropertiesBulkInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        part_id=part_id,
        mass_as_group=mass_as_group,
        use_mass_property_overrides=use_mass_property_overrides,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetPartStudioMassPropertiesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_id: list[str] | Unset = UNSET,
    mass_as_group: bool | Unset = True,
    use_mass_property_overrides: bool | Unset = False,
) -> BTMassPropertiesBulkInfo | None:
    """Get the mass properties for a Part Studio.

     Parts must have density. The returned schema includes the same information as in the Onshape [Mass
    Properties Tool](https://cad.onshape.com/help/Content/massprops-ps.htm).

    When three values are returned:
     * The first is the calculated value.
     * The second is the minimum possible value, considering tolerance.
     * The third is the maximum possible value, considering tolerance.

     See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wvm (GetPartStudioMassPropertiesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        part_id (list[str] | Unset):
        mass_as_group (bool | Unset):  Default: True.
        use_mass_property_overrides (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMassPropertiesBulkInfo
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
            rollback_bar_index=rollback_bar_index,
            element_microversion_id=element_microversion_id,
            part_id=part_id,
            mass_as_group=mass_as_group,
            use_mass_property_overrides=use_mass_property_overrides,
        )
    ).parsed
