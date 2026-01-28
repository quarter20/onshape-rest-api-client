from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_feature_list_response_2457 import BTFeatureListResponse2457
from ...models.get_part_studio_features_wvm import GetPartStudioFeaturesWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetPartStudioFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    include_geometry_ids: bool | Unset = True,
    feature_id: list[str] | Unset = UNSET,
    no_sketch_geometry: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["rollbackBarIndex"] = rollback_bar_index

    params["elementMicroversionId"] = element_microversion_id

    params["includeGeometryIds"] = include_geometry_ids

    json_feature_id: list[str] | Unset = UNSET
    if not isinstance(feature_id, Unset):
        json_feature_id = feature_id

    params["featureId"] = json_feature_id

    params["noSketchGeometry"] = no_sketch_geometry

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTFeatureListResponse2457:
    response_default = BTFeatureListResponse2457.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTFeatureListResponse2457]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetPartStudioFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    include_geometry_ids: bool | Unset = True,
    feature_id: list[str] | Unset = UNSET,
    no_sketch_geometry: bool | Unset = False,
) -> Response[BTFeatureListResponse2457]:
    """Get a list of features instantiated in the Part Studio.

     See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wvm (GetPartStudioFeaturesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        include_geometry_ids (bool | Unset):  Default: True.
        feature_id (list[str] | Unset):
        no_sketch_geometry (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureListResponse2457]
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
        include_geometry_ids=include_geometry_ids,
        feature_id=feature_id,
        no_sketch_geometry=no_sketch_geometry,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetPartStudioFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    include_geometry_ids: bool | Unset = True,
    feature_id: list[str] | Unset = UNSET,
    no_sketch_geometry: bool | Unset = False,
) -> BTFeatureListResponse2457 | None:
    """Get a list of features instantiated in the Part Studio.

     See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wvm (GetPartStudioFeaturesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        include_geometry_ids (bool | Unset):  Default: True.
        feature_id (list[str] | Unset):
        no_sketch_geometry (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureListResponse2457
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
        include_geometry_ids=include_geometry_ids,
        feature_id=feature_id,
        no_sketch_geometry=no_sketch_geometry,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetPartStudioFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    include_geometry_ids: bool | Unset = True,
    feature_id: list[str] | Unset = UNSET,
    no_sketch_geometry: bool | Unset = False,
) -> Response[BTFeatureListResponse2457]:
    """Get a list of features instantiated in the Part Studio.

     See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wvm (GetPartStudioFeaturesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        include_geometry_ids (bool | Unset):  Default: True.
        feature_id (list[str] | Unset):
        no_sketch_geometry (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureListResponse2457]
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
        include_geometry_ids=include_geometry_ids,
        feature_id=feature_id,
        no_sketch_geometry=no_sketch_geometry,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetPartStudioFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    include_geometry_ids: bool | Unset = True,
    feature_id: list[str] | Unset = UNSET,
    no_sketch_geometry: bool | Unset = False,
) -> BTFeatureListResponse2457 | None:
    """Get a list of features instantiated in the Part Studio.

     See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wvm (GetPartStudioFeaturesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        include_geometry_ids (bool | Unset):  Default: True.
        feature_id (list[str] | Unset):
        no_sketch_geometry (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureListResponse2457
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
            include_geometry_ids=include_geometry_ids,
            feature_id=feature_id,
            no_sketch_geometry=no_sketch_geometry,
        )
    ).parsed
