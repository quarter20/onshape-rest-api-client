from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_category_property_info import BTListResponseBTCategoryPropertyInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owner_id: str | Unset = UNSET,
    owner_type: int | Unset = 1,
    document_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    object_type: int | Unset = UNSET,
    strict: bool | Unset = True,
    include_object_type_defaults: bool | Unset = False,
    include_computed_properties: bool | Unset = True,
    include_part_properties_table_only_properties: bool | Unset = True,
    only_active: bool | Unset = False,
    only_object_type_defaults: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ownerId"] = owner_id

    params["ownerType"] = owner_type

    params["documentId"] = document_id

    json_category_ids: list[str] | Unset = UNSET
    if not isinstance(category_ids, Unset):
        json_category_ids = category_ids

    params["categoryIds"] = json_category_ids

    params["objectType"] = object_type

    params["strict"] = strict

    params["includeObjectTypeDefaults"] = include_object_type_defaults

    params["includeComputedProperties"] = include_computed_properties

    params["includePartPropertiesTableOnlyProperties"] = include_part_properties_table_only_properties

    params["onlyActive"] = only_active

    params["onlyObjectTypeDefaults"] = only_object_type_defaults

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metadatacategory/categoryproperties",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTListResponseBTCategoryPropertyInfo:
    response_default = BTListResponseBTCategoryPropertyInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTCategoryPropertyInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: int | Unset = 1,
    document_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    object_type: int | Unset = UNSET,
    strict: bool | Unset = True,
    include_object_type_defaults: bool | Unset = False,
    include_computed_properties: bool | Unset = True,
    include_part_properties_table_only_properties: bool | Unset = True,
    only_active: bool | Unset = False,
    only_object_type_defaults: bool | Unset = False,
) -> Response[BTListResponseBTCategoryPropertyInfo]:
    """Get properties associated with the specified metadata categories.

     An object's category specifies its type: Part, Assembly, Drawing, etc. Available properties depend
    on the object's category.

    Args:
        owner_id (str | Unset):
        owner_type (int | Unset):  Default: 1.
        document_id (str | Unset):
        category_ids (list[str] | Unset):
        object_type (int | Unset):
        strict (bool | Unset):  Default: True.
        include_object_type_defaults (bool | Unset):  Default: False.
        include_computed_properties (bool | Unset):  Default: True.
        include_part_properties_table_only_properties (bool | Unset):  Default: True.
        only_active (bool | Unset):  Default: False.
        only_object_type_defaults (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTCategoryPropertyInfo]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        owner_type=owner_type,
        document_id=document_id,
        category_ids=category_ids,
        object_type=object_type,
        strict=strict,
        include_object_type_defaults=include_object_type_defaults,
        include_computed_properties=include_computed_properties,
        include_part_properties_table_only_properties=include_part_properties_table_only_properties,
        only_active=only_active,
        only_object_type_defaults=only_object_type_defaults,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: int | Unset = 1,
    document_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    object_type: int | Unset = UNSET,
    strict: bool | Unset = True,
    include_object_type_defaults: bool | Unset = False,
    include_computed_properties: bool | Unset = True,
    include_part_properties_table_only_properties: bool | Unset = True,
    only_active: bool | Unset = False,
    only_object_type_defaults: bool | Unset = False,
) -> BTListResponseBTCategoryPropertyInfo | None:
    """Get properties associated with the specified metadata categories.

     An object's category specifies its type: Part, Assembly, Drawing, etc. Available properties depend
    on the object's category.

    Args:
        owner_id (str | Unset):
        owner_type (int | Unset):  Default: 1.
        document_id (str | Unset):
        category_ids (list[str] | Unset):
        object_type (int | Unset):
        strict (bool | Unset):  Default: True.
        include_object_type_defaults (bool | Unset):  Default: False.
        include_computed_properties (bool | Unset):  Default: True.
        include_part_properties_table_only_properties (bool | Unset):  Default: True.
        only_active (bool | Unset):  Default: False.
        only_object_type_defaults (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTCategoryPropertyInfo
    """

    return sync_detailed(
        client=client,
        owner_id=owner_id,
        owner_type=owner_type,
        document_id=document_id,
        category_ids=category_ids,
        object_type=object_type,
        strict=strict,
        include_object_type_defaults=include_object_type_defaults,
        include_computed_properties=include_computed_properties,
        include_part_properties_table_only_properties=include_part_properties_table_only_properties,
        only_active=only_active,
        only_object_type_defaults=only_object_type_defaults,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: int | Unset = 1,
    document_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    object_type: int | Unset = UNSET,
    strict: bool | Unset = True,
    include_object_type_defaults: bool | Unset = False,
    include_computed_properties: bool | Unset = True,
    include_part_properties_table_only_properties: bool | Unset = True,
    only_active: bool | Unset = False,
    only_object_type_defaults: bool | Unset = False,
) -> Response[BTListResponseBTCategoryPropertyInfo]:
    """Get properties associated with the specified metadata categories.

     An object's category specifies its type: Part, Assembly, Drawing, etc. Available properties depend
    on the object's category.

    Args:
        owner_id (str | Unset):
        owner_type (int | Unset):  Default: 1.
        document_id (str | Unset):
        category_ids (list[str] | Unset):
        object_type (int | Unset):
        strict (bool | Unset):  Default: True.
        include_object_type_defaults (bool | Unset):  Default: False.
        include_computed_properties (bool | Unset):  Default: True.
        include_part_properties_table_only_properties (bool | Unset):  Default: True.
        only_active (bool | Unset):  Default: False.
        only_object_type_defaults (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTCategoryPropertyInfo]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        owner_type=owner_type,
        document_id=document_id,
        category_ids=category_ids,
        object_type=object_type,
        strict=strict,
        include_object_type_defaults=include_object_type_defaults,
        include_computed_properties=include_computed_properties,
        include_part_properties_table_only_properties=include_part_properties_table_only_properties,
        only_active=only_active,
        only_object_type_defaults=only_object_type_defaults,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: int | Unset = 1,
    document_id: str | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    object_type: int | Unset = UNSET,
    strict: bool | Unset = True,
    include_object_type_defaults: bool | Unset = False,
    include_computed_properties: bool | Unset = True,
    include_part_properties_table_only_properties: bool | Unset = True,
    only_active: bool | Unset = False,
    only_object_type_defaults: bool | Unset = False,
) -> BTListResponseBTCategoryPropertyInfo | None:
    """Get properties associated with the specified metadata categories.

     An object's category specifies its type: Part, Assembly, Drawing, etc. Available properties depend
    on the object's category.

    Args:
        owner_id (str | Unset):
        owner_type (int | Unset):  Default: 1.
        document_id (str | Unset):
        category_ids (list[str] | Unset):
        object_type (int | Unset):
        strict (bool | Unset):  Default: True.
        include_object_type_defaults (bool | Unset):  Default: False.
        include_computed_properties (bool | Unset):  Default: True.
        include_part_properties_table_only_properties (bool | Unset):  Default: True.
        only_active (bool | Unset):  Default: False.
        only_object_type_defaults (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTCategoryPropertyInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_id=owner_id,
            owner_type=owner_type,
            document_id=document_id,
            category_ids=category_ids,
            object_type=object_type,
            strict=strict,
            include_object_type_defaults=include_object_type_defaults,
            include_computed_properties=include_computed_properties,
            include_part_properties_table_only_properties=include_part_properties_table_only_properties,
            only_active=only_active,
            only_object_type_defaults=only_object_type_defaults,
        )
    ).parsed
