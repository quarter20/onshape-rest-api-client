from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_rest_user_role import BTRestUserRole
from ...models.open_api import OpenAPI
from ...models.status import Status
from ...models.version_alias import VersionAlias
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    force_reload: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    version_alias: VersionAlias | Unset = UNSET,
    no_filter: bool | Unset = False,
    included_tags: list[str] | Unset = UNSET,
    excluded_tags: list[str] | Unset = UNSET,
    include_deprecated: bool | Unset = False,
    only_deprecated: bool | Unset = False,
    documentation_statuses: list[Status] | Unset = UNSET,
    rest_user_role: BTRestUserRole | Unset = UNSET,
    operation_ids: list[str] | Unset = UNSET,
    excluded_operation_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["forceReload"] = force_reload

    params["version"] = version

    json_version_alias: str | Unset = UNSET
    if not isinstance(version_alias, Unset):
        json_version_alias = version_alias.value

    params["versionAlias"] = json_version_alias

    params["noFilter"] = no_filter

    json_included_tags: list[str] | Unset = UNSET
    if not isinstance(included_tags, Unset):
        json_included_tags = included_tags

    params["includedTags"] = json_included_tags

    json_excluded_tags: list[str] | Unset = UNSET
    if not isinstance(excluded_tags, Unset):
        json_excluded_tags = excluded_tags

    params["excludedTags"] = json_excluded_tags

    params["includeDeprecated"] = include_deprecated

    params["onlyDeprecated"] = only_deprecated

    json_documentation_statuses: list[str] | Unset = UNSET
    if not isinstance(documentation_statuses, Unset):
        json_documentation_statuses = []
        for documentation_statuses_item_data in documentation_statuses:
            documentation_statuses_item = documentation_statuses_item_data.value
            json_documentation_statuses.append(documentation_statuses_item)

    params["documentationStatuses"] = json_documentation_statuses

    json_rest_user_role: str | Unset = UNSET
    if not isinstance(rest_user_role, Unset):
        json_rest_user_role = rest_user_role.value

    params["restUserRole"] = json_rest_user_role

    json_operation_ids: list[str] | Unset = UNSET
    if not isinstance(operation_ids, Unset):
        json_operation_ids = operation_ids

    params["operationIds"] = json_operation_ids

    json_excluded_operation_ids: list[str] | Unset = UNSET
    if not isinstance(excluded_operation_ids, Unset):
        json_excluded_operation_ids = excluded_operation_ids

    params["excludedOperationIds"] = json_excluded_operation_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OpenAPI:
    response_default = OpenAPI.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OpenAPI]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    force_reload: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    version_alias: VersionAlias | Unset = UNSET,
    no_filter: bool | Unset = False,
    included_tags: list[str] | Unset = UNSET,
    excluded_tags: list[str] | Unset = UNSET,
    include_deprecated: bool | Unset = False,
    only_deprecated: bool | Unset = False,
    documentation_statuses: list[Status] | Unset = UNSET,
    rest_user_role: BTRestUserRole | Unset = UNSET,
    operation_ids: list[str] | Unset = UNSET,
    excluded_operation_ids: list[str] | Unset = UNSET,
) -> Response[OpenAPI]:
    """Get the OpenAPI specification for the Onshape REST API.

     The Onshape API OpenAPI specification is returned in the JSON format.

    Args:
        force_reload (bool | Unset):
        version (str | Unset):
        version_alias (VersionAlias | Unset):
        no_filter (bool | Unset):  Default: False.
        included_tags (list[str] | Unset):
        excluded_tags (list[str] | Unset):
        include_deprecated (bool | Unset):  Default: False.
        only_deprecated (bool | Unset):  Default: False.
        documentation_statuses (list[Status] | Unset):
        rest_user_role (BTRestUserRole | Unset):
        operation_ids (list[str] | Unset):
        excluded_operation_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenAPI]
    """

    kwargs = _get_kwargs(
        force_reload=force_reload,
        version=version,
        version_alias=version_alias,
        no_filter=no_filter,
        included_tags=included_tags,
        excluded_tags=excluded_tags,
        include_deprecated=include_deprecated,
        only_deprecated=only_deprecated,
        documentation_statuses=documentation_statuses,
        rest_user_role=rest_user_role,
        operation_ids=operation_ids,
        excluded_operation_ids=excluded_operation_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    force_reload: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    version_alias: VersionAlias | Unset = UNSET,
    no_filter: bool | Unset = False,
    included_tags: list[str] | Unset = UNSET,
    excluded_tags: list[str] | Unset = UNSET,
    include_deprecated: bool | Unset = False,
    only_deprecated: bool | Unset = False,
    documentation_statuses: list[Status] | Unset = UNSET,
    rest_user_role: BTRestUserRole | Unset = UNSET,
    operation_ids: list[str] | Unset = UNSET,
    excluded_operation_ids: list[str] | Unset = UNSET,
) -> OpenAPI | None:
    """Get the OpenAPI specification for the Onshape REST API.

     The Onshape API OpenAPI specification is returned in the JSON format.

    Args:
        force_reload (bool | Unset):
        version (str | Unset):
        version_alias (VersionAlias | Unset):
        no_filter (bool | Unset):  Default: False.
        included_tags (list[str] | Unset):
        excluded_tags (list[str] | Unset):
        include_deprecated (bool | Unset):  Default: False.
        only_deprecated (bool | Unset):  Default: False.
        documentation_statuses (list[Status] | Unset):
        rest_user_role (BTRestUserRole | Unset):
        operation_ids (list[str] | Unset):
        excluded_operation_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenAPI
    """

    return sync_detailed(
        client=client,
        force_reload=force_reload,
        version=version,
        version_alias=version_alias,
        no_filter=no_filter,
        included_tags=included_tags,
        excluded_tags=excluded_tags,
        include_deprecated=include_deprecated,
        only_deprecated=only_deprecated,
        documentation_statuses=documentation_statuses,
        rest_user_role=rest_user_role,
        operation_ids=operation_ids,
        excluded_operation_ids=excluded_operation_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    force_reload: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    version_alias: VersionAlias | Unset = UNSET,
    no_filter: bool | Unset = False,
    included_tags: list[str] | Unset = UNSET,
    excluded_tags: list[str] | Unset = UNSET,
    include_deprecated: bool | Unset = False,
    only_deprecated: bool | Unset = False,
    documentation_statuses: list[Status] | Unset = UNSET,
    rest_user_role: BTRestUserRole | Unset = UNSET,
    operation_ids: list[str] | Unset = UNSET,
    excluded_operation_ids: list[str] | Unset = UNSET,
) -> Response[OpenAPI]:
    """Get the OpenAPI specification for the Onshape REST API.

     The Onshape API OpenAPI specification is returned in the JSON format.

    Args:
        force_reload (bool | Unset):
        version (str | Unset):
        version_alias (VersionAlias | Unset):
        no_filter (bool | Unset):  Default: False.
        included_tags (list[str] | Unset):
        excluded_tags (list[str] | Unset):
        include_deprecated (bool | Unset):  Default: False.
        only_deprecated (bool | Unset):  Default: False.
        documentation_statuses (list[Status] | Unset):
        rest_user_role (BTRestUserRole | Unset):
        operation_ids (list[str] | Unset):
        excluded_operation_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenAPI]
    """

    kwargs = _get_kwargs(
        force_reload=force_reload,
        version=version,
        version_alias=version_alias,
        no_filter=no_filter,
        included_tags=included_tags,
        excluded_tags=excluded_tags,
        include_deprecated=include_deprecated,
        only_deprecated=only_deprecated,
        documentation_statuses=documentation_statuses,
        rest_user_role=rest_user_role,
        operation_ids=operation_ids,
        excluded_operation_ids=excluded_operation_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    force_reload: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    version_alias: VersionAlias | Unset = UNSET,
    no_filter: bool | Unset = False,
    included_tags: list[str] | Unset = UNSET,
    excluded_tags: list[str] | Unset = UNSET,
    include_deprecated: bool | Unset = False,
    only_deprecated: bool | Unset = False,
    documentation_statuses: list[Status] | Unset = UNSET,
    rest_user_role: BTRestUserRole | Unset = UNSET,
    operation_ids: list[str] | Unset = UNSET,
    excluded_operation_ids: list[str] | Unset = UNSET,
) -> OpenAPI | None:
    """Get the OpenAPI specification for the Onshape REST API.

     The Onshape API OpenAPI specification is returned in the JSON format.

    Args:
        force_reload (bool | Unset):
        version (str | Unset):
        version_alias (VersionAlias | Unset):
        no_filter (bool | Unset):  Default: False.
        included_tags (list[str] | Unset):
        excluded_tags (list[str] | Unset):
        include_deprecated (bool | Unset):  Default: False.
        only_deprecated (bool | Unset):  Default: False.
        documentation_statuses (list[Status] | Unset):
        rest_user_role (BTRestUserRole | Unset):
        operation_ids (list[str] | Unset):
        excluded_operation_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenAPI
    """

    return (
        await asyncio_detailed(
            client=client,
            force_reload=force_reload,
            version=version,
            version_alias=version_alias,
            no_filter=no_filter,
            included_tags=included_tags,
            excluded_tags=excluded_tags,
            include_deprecated=include_deprecated,
            only_deprecated=only_deprecated,
            documentation_statuses=documentation_statuses,
            rest_user_role=rest_user_role,
            operation_ids=operation_ids,
            excluded_operation_ids=excluded_operation_ids,
        )
    ).parsed
