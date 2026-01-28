from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bt_assembly_feature_list_response_1174 import BTAssemblyFeatureListResponse1174
from ...models.get_features_wvm import GetFeaturesWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    feature_id: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["explodedViewId"] = exploded_view_id

    json_feature_id: list[str] | Unset = UNSET
    if not isinstance(feature_id, Unset):
        json_feature_id = feature_id

    params["featureId"] = json_feature_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assemblies/d/{did}/{wvm}/{wvmid}/e/{eid}/features".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTAssemblyFeatureListResponse1174 | None:
    if response.status_code == 200:
        response_200 = BTAssemblyFeatureListResponse1174.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAssemblyFeatureListResponse1174]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    feature_id: list[str] | Unset = UNSET,
) -> Response[BTAssemblyFeatureListResponse1174]:
    """Get the definitions of the specified features in an assembly.

    Args:
        did (str):
        wvm (GetFeaturesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        feature_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyFeatureListResponse1174]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        exploded_view_id=exploded_view_id,
        feature_id=feature_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    feature_id: list[str] | Unset = UNSET,
) -> BTAssemblyFeatureListResponse1174 | None:
    """Get the definitions of the specified features in an assembly.

    Args:
        did (str):
        wvm (GetFeaturesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        feature_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyFeatureListResponse1174
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
        exploded_view_id=exploded_view_id,
        feature_id=feature_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    feature_id: list[str] | Unset = UNSET,
) -> Response[BTAssemblyFeatureListResponse1174]:
    """Get the definitions of the specified features in an assembly.

    Args:
        did (str):
        wvm (GetFeaturesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        feature_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyFeatureListResponse1174]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        exploded_view_id=exploded_view_id,
        feature_id=feature_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetFeaturesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    feature_id: list[str] | Unset = UNSET,
) -> BTAssemblyFeatureListResponse1174 | None:
    """Get the definitions of the specified features in an assembly.

    Args:
        did (str):
        wvm (GetFeaturesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        feature_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyFeatureListResponse1174
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
            exploded_view_id=exploded_view_id,
            feature_id=feature_id,
        )
    ).parsed
