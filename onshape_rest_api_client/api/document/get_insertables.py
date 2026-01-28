from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_insertables_list_response import BTInsertablesListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wv: str,
    wvid: str,
    *,
    element_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    include_sketches: bool | Unset = False,
    include_reference_features: bool | Unset = False,
    include_assemblies: bool | Unset = False,
    include_feature_studios: bool | Unset = False,
    include_blobs: bool | Unset = False,
    allowed_blob_mime_types: str | Unset = "",
    exclude_newer_fs_versions: bool | Unset = False,
    max_feature_script_version: int | Unset = UNSET,
    include_part_studios: bool | Unset = False,
    include_features: bool | Unset = False,
    include_meshes: bool | Unset = False,
    include_wires: bool | Unset = False,
    include_flattened_bodies: bool | Unset = False,
    include_applications: bool | Unset = False,
    allowed_application_mime_types: str | Unset = "",
    include_composite_parts: bool | Unset = False,
    include_fs_tables: bool | Unset = False,
    include_fs_computed_part_property_functions: bool | Unset = False,
    include_variables: bool | Unset = False,
    include_variable_studios: bool | Unset = False,
    allowed_blob_extensions: str | Unset = "",
    is_obsoletion: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["elementId"] = element_id

    params["configuration"] = configuration

    params["linkDocumentId"] = link_document_id

    params["includeParts"] = include_parts

    params["includeSurfaces"] = include_surfaces

    params["includeSketches"] = include_sketches

    params["includeReferenceFeatures"] = include_reference_features

    params["includeAssemblies"] = include_assemblies

    params["includeFeatureStudios"] = include_feature_studios

    params["includeBlobs"] = include_blobs

    params["allowedBlobMimeTypes"] = allowed_blob_mime_types

    params["excludeNewerFSVersions"] = exclude_newer_fs_versions

    params["maxFeatureScriptVersion"] = max_feature_script_version

    params["includePartStudios"] = include_part_studios

    params["includeFeatures"] = include_features

    params["includeMeshes"] = include_meshes

    params["includeWires"] = include_wires

    params["includeFlattenedBodies"] = include_flattened_bodies

    params["includeApplications"] = include_applications

    params["allowedApplicationMimeTypes"] = allowed_application_mime_types

    params["includeCompositeParts"] = include_composite_parts

    params["includeFSTables"] = include_fs_tables

    params["includeFSComputedPartPropertyFunctions"] = include_fs_computed_part_property_functions

    params["includeVariables"] = include_variables

    params["includeVariableStudios"] = include_variable_studios

    params["allowedBlobExtensions"] = allowed_blob_extensions

    params["isObsoletion"] = is_obsoletion

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/{wv}/{wvid}/insertables".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTInsertablesListResponse:
    response_default = BTInsertablesListResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTInsertablesListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
    element_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    include_sketches: bool | Unset = False,
    include_reference_features: bool | Unset = False,
    include_assemblies: bool | Unset = False,
    include_feature_studios: bool | Unset = False,
    include_blobs: bool | Unset = False,
    allowed_blob_mime_types: str | Unset = "",
    exclude_newer_fs_versions: bool | Unset = False,
    max_feature_script_version: int | Unset = UNSET,
    include_part_studios: bool | Unset = False,
    include_features: bool | Unset = False,
    include_meshes: bool | Unset = False,
    include_wires: bool | Unset = False,
    include_flattened_bodies: bool | Unset = False,
    include_applications: bool | Unset = False,
    allowed_application_mime_types: str | Unset = "",
    include_composite_parts: bool | Unset = False,
    include_fs_tables: bool | Unset = False,
    include_fs_computed_part_property_functions: bool | Unset = False,
    include_variables: bool | Unset = False,
    include_variable_studios: bool | Unset = False,
    allowed_blob_extensions: str | Unset = "",
    is_obsoletion: bool | Unset = False,
) -> Response[BTInsertablesListResponse]:
    """Retrieve insertables by document ID and workspace or version ID.

    Args:
        did (str):
        wv (str):
        wvid (str):
        element_id (str | Unset):
        configuration (str | Unset):
        link_document_id (str | Unset):
        include_parts (bool | Unset):  Default: False.
        include_surfaces (bool | Unset):  Default: False.
        include_sketches (bool | Unset):  Default: False.
        include_reference_features (bool | Unset):  Default: False.
        include_assemblies (bool | Unset):  Default: False.
        include_feature_studios (bool | Unset):  Default: False.
        include_blobs (bool | Unset):  Default: False.
        allowed_blob_mime_types (str | Unset):  Default: ''.
        exclude_newer_fs_versions (bool | Unset):  Default: False.
        max_feature_script_version (int | Unset):
        include_part_studios (bool | Unset):  Default: False.
        include_features (bool | Unset):  Default: False.
        include_meshes (bool | Unset):  Default: False.
        include_wires (bool | Unset):  Default: False.
        include_flattened_bodies (bool | Unset):  Default: False.
        include_applications (bool | Unset):  Default: False.
        allowed_application_mime_types (str | Unset):  Default: ''.
        include_composite_parts (bool | Unset):  Default: False.
        include_fs_tables (bool | Unset):  Default: False.
        include_fs_computed_part_property_functions (bool | Unset):  Default: False.
        include_variables (bool | Unset):  Default: False.
        include_variable_studios (bool | Unset):  Default: False.
        allowed_blob_extensions (str | Unset):  Default: ''.
        is_obsoletion (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTInsertablesListResponse]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        element_id=element_id,
        configuration=configuration,
        link_document_id=link_document_id,
        include_parts=include_parts,
        include_surfaces=include_surfaces,
        include_sketches=include_sketches,
        include_reference_features=include_reference_features,
        include_assemblies=include_assemblies,
        include_feature_studios=include_feature_studios,
        include_blobs=include_blobs,
        allowed_blob_mime_types=allowed_blob_mime_types,
        exclude_newer_fs_versions=exclude_newer_fs_versions,
        max_feature_script_version=max_feature_script_version,
        include_part_studios=include_part_studios,
        include_features=include_features,
        include_meshes=include_meshes,
        include_wires=include_wires,
        include_flattened_bodies=include_flattened_bodies,
        include_applications=include_applications,
        allowed_application_mime_types=allowed_application_mime_types,
        include_composite_parts=include_composite_parts,
        include_fs_tables=include_fs_tables,
        include_fs_computed_part_property_functions=include_fs_computed_part_property_functions,
        include_variables=include_variables,
        include_variable_studios=include_variable_studios,
        allowed_blob_extensions=allowed_blob_extensions,
        is_obsoletion=is_obsoletion,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
    element_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    include_sketches: bool | Unset = False,
    include_reference_features: bool | Unset = False,
    include_assemblies: bool | Unset = False,
    include_feature_studios: bool | Unset = False,
    include_blobs: bool | Unset = False,
    allowed_blob_mime_types: str | Unset = "",
    exclude_newer_fs_versions: bool | Unset = False,
    max_feature_script_version: int | Unset = UNSET,
    include_part_studios: bool | Unset = False,
    include_features: bool | Unset = False,
    include_meshes: bool | Unset = False,
    include_wires: bool | Unset = False,
    include_flattened_bodies: bool | Unset = False,
    include_applications: bool | Unset = False,
    allowed_application_mime_types: str | Unset = "",
    include_composite_parts: bool | Unset = False,
    include_fs_tables: bool | Unset = False,
    include_fs_computed_part_property_functions: bool | Unset = False,
    include_variables: bool | Unset = False,
    include_variable_studios: bool | Unset = False,
    allowed_blob_extensions: str | Unset = "",
    is_obsoletion: bool | Unset = False,
) -> BTInsertablesListResponse | None:
    """Retrieve insertables by document ID and workspace or version ID.

    Args:
        did (str):
        wv (str):
        wvid (str):
        element_id (str | Unset):
        configuration (str | Unset):
        link_document_id (str | Unset):
        include_parts (bool | Unset):  Default: False.
        include_surfaces (bool | Unset):  Default: False.
        include_sketches (bool | Unset):  Default: False.
        include_reference_features (bool | Unset):  Default: False.
        include_assemblies (bool | Unset):  Default: False.
        include_feature_studios (bool | Unset):  Default: False.
        include_blobs (bool | Unset):  Default: False.
        allowed_blob_mime_types (str | Unset):  Default: ''.
        exclude_newer_fs_versions (bool | Unset):  Default: False.
        max_feature_script_version (int | Unset):
        include_part_studios (bool | Unset):  Default: False.
        include_features (bool | Unset):  Default: False.
        include_meshes (bool | Unset):  Default: False.
        include_wires (bool | Unset):  Default: False.
        include_flattened_bodies (bool | Unset):  Default: False.
        include_applications (bool | Unset):  Default: False.
        allowed_application_mime_types (str | Unset):  Default: ''.
        include_composite_parts (bool | Unset):  Default: False.
        include_fs_tables (bool | Unset):  Default: False.
        include_fs_computed_part_property_functions (bool | Unset):  Default: False.
        include_variables (bool | Unset):  Default: False.
        include_variable_studios (bool | Unset):  Default: False.
        allowed_blob_extensions (str | Unset):  Default: ''.
        is_obsoletion (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTInsertablesListResponse
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        client=client,
        element_id=element_id,
        configuration=configuration,
        link_document_id=link_document_id,
        include_parts=include_parts,
        include_surfaces=include_surfaces,
        include_sketches=include_sketches,
        include_reference_features=include_reference_features,
        include_assemblies=include_assemblies,
        include_feature_studios=include_feature_studios,
        include_blobs=include_blobs,
        allowed_blob_mime_types=allowed_blob_mime_types,
        exclude_newer_fs_versions=exclude_newer_fs_versions,
        max_feature_script_version=max_feature_script_version,
        include_part_studios=include_part_studios,
        include_features=include_features,
        include_meshes=include_meshes,
        include_wires=include_wires,
        include_flattened_bodies=include_flattened_bodies,
        include_applications=include_applications,
        allowed_application_mime_types=allowed_application_mime_types,
        include_composite_parts=include_composite_parts,
        include_fs_tables=include_fs_tables,
        include_fs_computed_part_property_functions=include_fs_computed_part_property_functions,
        include_variables=include_variables,
        include_variable_studios=include_variable_studios,
        allowed_blob_extensions=allowed_blob_extensions,
        is_obsoletion=is_obsoletion,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
    element_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    include_sketches: bool | Unset = False,
    include_reference_features: bool | Unset = False,
    include_assemblies: bool | Unset = False,
    include_feature_studios: bool | Unset = False,
    include_blobs: bool | Unset = False,
    allowed_blob_mime_types: str | Unset = "",
    exclude_newer_fs_versions: bool | Unset = False,
    max_feature_script_version: int | Unset = UNSET,
    include_part_studios: bool | Unset = False,
    include_features: bool | Unset = False,
    include_meshes: bool | Unset = False,
    include_wires: bool | Unset = False,
    include_flattened_bodies: bool | Unset = False,
    include_applications: bool | Unset = False,
    allowed_application_mime_types: str | Unset = "",
    include_composite_parts: bool | Unset = False,
    include_fs_tables: bool | Unset = False,
    include_fs_computed_part_property_functions: bool | Unset = False,
    include_variables: bool | Unset = False,
    include_variable_studios: bool | Unset = False,
    allowed_blob_extensions: str | Unset = "",
    is_obsoletion: bool | Unset = False,
) -> Response[BTInsertablesListResponse]:
    """Retrieve insertables by document ID and workspace or version ID.

    Args:
        did (str):
        wv (str):
        wvid (str):
        element_id (str | Unset):
        configuration (str | Unset):
        link_document_id (str | Unset):
        include_parts (bool | Unset):  Default: False.
        include_surfaces (bool | Unset):  Default: False.
        include_sketches (bool | Unset):  Default: False.
        include_reference_features (bool | Unset):  Default: False.
        include_assemblies (bool | Unset):  Default: False.
        include_feature_studios (bool | Unset):  Default: False.
        include_blobs (bool | Unset):  Default: False.
        allowed_blob_mime_types (str | Unset):  Default: ''.
        exclude_newer_fs_versions (bool | Unset):  Default: False.
        max_feature_script_version (int | Unset):
        include_part_studios (bool | Unset):  Default: False.
        include_features (bool | Unset):  Default: False.
        include_meshes (bool | Unset):  Default: False.
        include_wires (bool | Unset):  Default: False.
        include_flattened_bodies (bool | Unset):  Default: False.
        include_applications (bool | Unset):  Default: False.
        allowed_application_mime_types (str | Unset):  Default: ''.
        include_composite_parts (bool | Unset):  Default: False.
        include_fs_tables (bool | Unset):  Default: False.
        include_fs_computed_part_property_functions (bool | Unset):  Default: False.
        include_variables (bool | Unset):  Default: False.
        include_variable_studios (bool | Unset):  Default: False.
        allowed_blob_extensions (str | Unset):  Default: ''.
        is_obsoletion (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTInsertablesListResponse]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        element_id=element_id,
        configuration=configuration,
        link_document_id=link_document_id,
        include_parts=include_parts,
        include_surfaces=include_surfaces,
        include_sketches=include_sketches,
        include_reference_features=include_reference_features,
        include_assemblies=include_assemblies,
        include_feature_studios=include_feature_studios,
        include_blobs=include_blobs,
        allowed_blob_mime_types=allowed_blob_mime_types,
        exclude_newer_fs_versions=exclude_newer_fs_versions,
        max_feature_script_version=max_feature_script_version,
        include_part_studios=include_part_studios,
        include_features=include_features,
        include_meshes=include_meshes,
        include_wires=include_wires,
        include_flattened_bodies=include_flattened_bodies,
        include_applications=include_applications,
        allowed_application_mime_types=allowed_application_mime_types,
        include_composite_parts=include_composite_parts,
        include_fs_tables=include_fs_tables,
        include_fs_computed_part_property_functions=include_fs_computed_part_property_functions,
        include_variables=include_variables,
        include_variable_studios=include_variable_studios,
        allowed_blob_extensions=allowed_blob_extensions,
        is_obsoletion=is_obsoletion,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
    element_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    include_sketches: bool | Unset = False,
    include_reference_features: bool | Unset = False,
    include_assemblies: bool | Unset = False,
    include_feature_studios: bool | Unset = False,
    include_blobs: bool | Unset = False,
    allowed_blob_mime_types: str | Unset = "",
    exclude_newer_fs_versions: bool | Unset = False,
    max_feature_script_version: int | Unset = UNSET,
    include_part_studios: bool | Unset = False,
    include_features: bool | Unset = False,
    include_meshes: bool | Unset = False,
    include_wires: bool | Unset = False,
    include_flattened_bodies: bool | Unset = False,
    include_applications: bool | Unset = False,
    allowed_application_mime_types: str | Unset = "",
    include_composite_parts: bool | Unset = False,
    include_fs_tables: bool | Unset = False,
    include_fs_computed_part_property_functions: bool | Unset = False,
    include_variables: bool | Unset = False,
    include_variable_studios: bool | Unset = False,
    allowed_blob_extensions: str | Unset = "",
    is_obsoletion: bool | Unset = False,
) -> BTInsertablesListResponse | None:
    """Retrieve insertables by document ID and workspace or version ID.

    Args:
        did (str):
        wv (str):
        wvid (str):
        element_id (str | Unset):
        configuration (str | Unset):
        link_document_id (str | Unset):
        include_parts (bool | Unset):  Default: False.
        include_surfaces (bool | Unset):  Default: False.
        include_sketches (bool | Unset):  Default: False.
        include_reference_features (bool | Unset):  Default: False.
        include_assemblies (bool | Unset):  Default: False.
        include_feature_studios (bool | Unset):  Default: False.
        include_blobs (bool | Unset):  Default: False.
        allowed_blob_mime_types (str | Unset):  Default: ''.
        exclude_newer_fs_versions (bool | Unset):  Default: False.
        max_feature_script_version (int | Unset):
        include_part_studios (bool | Unset):  Default: False.
        include_features (bool | Unset):  Default: False.
        include_meshes (bool | Unset):  Default: False.
        include_wires (bool | Unset):  Default: False.
        include_flattened_bodies (bool | Unset):  Default: False.
        include_applications (bool | Unset):  Default: False.
        allowed_application_mime_types (str | Unset):  Default: ''.
        include_composite_parts (bool | Unset):  Default: False.
        include_fs_tables (bool | Unset):  Default: False.
        include_fs_computed_part_property_functions (bool | Unset):  Default: False.
        include_variables (bool | Unset):  Default: False.
        include_variable_studios (bool | Unset):  Default: False.
        allowed_blob_extensions (str | Unset):  Default: ''.
        is_obsoletion (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTInsertablesListResponse
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            client=client,
            element_id=element_id,
            configuration=configuration,
            link_document_id=link_document_id,
            include_parts=include_parts,
            include_surfaces=include_surfaces,
            include_sketches=include_sketches,
            include_reference_features=include_reference_features,
            include_assemblies=include_assemblies,
            include_feature_studios=include_feature_studios,
            include_blobs=include_blobs,
            allowed_blob_mime_types=allowed_blob_mime_types,
            exclude_newer_fs_versions=exclude_newer_fs_versions,
            max_feature_script_version=max_feature_script_version,
            include_part_studios=include_part_studios,
            include_features=include_features,
            include_meshes=include_meshes,
            include_wires=include_wires,
            include_flattened_bodies=include_flattened_bodies,
            include_applications=include_applications,
            allowed_application_mime_types=allowed_application_mime_types,
            include_composite_parts=include_composite_parts,
            include_fs_tables=include_fs_tables,
            include_fs_computed_part_property_functions=include_fs_computed_part_property_functions,
            include_variables=include_variables,
            include_variable_studios=include_variable_studios,
            allowed_blob_extensions=allowed_blob_extensions,
            is_obsoletion=is_obsoletion,
        )
    ).parsed
