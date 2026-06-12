from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bt_where_used_item_info_list import BTWhereUsedItemInfoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    document_id: str | Unset = UNSET,
    element_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    part_number: str | Unset = UNSET,
    include_properties: bool | Unset = False,
    filter_: int | Unset = UNSET,
    include_version_info: bool | Unset = UNSET,
    use_latest_version: bool | Unset = False,
    limit_to_types: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["documentId"] = document_id

    params["elementId"] = element_id

    params["versionId"] = version_id

    params["configuration"] = configuration

    params["partId"] = part_id

    params["partNumber"] = part_number

    params["includeProperties"] = include_properties

    params["filter"] = filter_

    params["includeVersionInfo"] = include_version_info

    params["useLatestVersion"] = use_latest_version

    params["limitToTypes"] = limit_to_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/productstructure/whereused",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTWhereUsedItemInfoList | None:
    if response.status_code == 200:
        response_200 = BTWhereUsedItemInfoList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTWhereUsedItemInfoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    document_id: str | Unset = UNSET,
    element_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    part_number: str | Unset = UNSET,
    include_properties: bool | Unset = False,
    filter_: int | Unset = UNSET,
    include_version_info: bool | Unset = UNSET,
    use_latest_version: bool | Unset = False,
    limit_to_types: str | Unset = "",
) -> Response[BTWhereUsedItemInfoList]:
    """Find where a part or assembly is used.

     Only supported for Enterprise and Professional plans. See [Dev Docs: Where Used](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#where-used) for a tutorial on using this endpoint.

    Args:
        document_id (str | Unset):
        element_id (str | Unset):
        version_id (str | Unset):
        configuration (str | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        include_properties (bool | Unset):  Default: False.
        filter_ (int | Unset):
        include_version_info (bool | Unset):
        use_latest_version (bool | Unset):  Default: False.
        limit_to_types (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTWhereUsedItemInfoList]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        element_id=element_id,
        version_id=version_id,
        configuration=configuration,
        part_id=part_id,
        part_number=part_number,
        include_properties=include_properties,
        filter_=filter_,
        include_version_info=include_version_info,
        use_latest_version=use_latest_version,
        limit_to_types=limit_to_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    document_id: str | Unset = UNSET,
    element_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    part_number: str | Unset = UNSET,
    include_properties: bool | Unset = False,
    filter_: int | Unset = UNSET,
    include_version_info: bool | Unset = UNSET,
    use_latest_version: bool | Unset = False,
    limit_to_types: str | Unset = "",
) -> BTWhereUsedItemInfoList | None:
    """Find where a part or assembly is used.

     Only supported for Enterprise and Professional plans. See [Dev Docs: Where Used](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#where-used) for a tutorial on using this endpoint.

    Args:
        document_id (str | Unset):
        element_id (str | Unset):
        version_id (str | Unset):
        configuration (str | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        include_properties (bool | Unset):  Default: False.
        filter_ (int | Unset):
        include_version_info (bool | Unset):
        use_latest_version (bool | Unset):  Default: False.
        limit_to_types (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTWhereUsedItemInfoList
    """

    return sync_detailed(
        client=client,
        document_id=document_id,
        element_id=element_id,
        version_id=version_id,
        configuration=configuration,
        part_id=part_id,
        part_number=part_number,
        include_properties=include_properties,
        filter_=filter_,
        include_version_info=include_version_info,
        use_latest_version=use_latest_version,
        limit_to_types=limit_to_types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    document_id: str | Unset = UNSET,
    element_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    part_number: str | Unset = UNSET,
    include_properties: bool | Unset = False,
    filter_: int | Unset = UNSET,
    include_version_info: bool | Unset = UNSET,
    use_latest_version: bool | Unset = False,
    limit_to_types: str | Unset = "",
) -> Response[BTWhereUsedItemInfoList]:
    """Find where a part or assembly is used.

     Only supported for Enterprise and Professional plans. See [Dev Docs: Where Used](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#where-used) for a tutorial on using this endpoint.

    Args:
        document_id (str | Unset):
        element_id (str | Unset):
        version_id (str | Unset):
        configuration (str | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        include_properties (bool | Unset):  Default: False.
        filter_ (int | Unset):
        include_version_info (bool | Unset):
        use_latest_version (bool | Unset):  Default: False.
        limit_to_types (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTWhereUsedItemInfoList]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        element_id=element_id,
        version_id=version_id,
        configuration=configuration,
        part_id=part_id,
        part_number=part_number,
        include_properties=include_properties,
        filter_=filter_,
        include_version_info=include_version_info,
        use_latest_version=use_latest_version,
        limit_to_types=limit_to_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    document_id: str | Unset = UNSET,
    element_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    configuration: str | Unset = UNSET,
    part_id: str | Unset = UNSET,
    part_number: str | Unset = UNSET,
    include_properties: bool | Unset = False,
    filter_: int | Unset = UNSET,
    include_version_info: bool | Unset = UNSET,
    use_latest_version: bool | Unset = False,
    limit_to_types: str | Unset = "",
) -> BTWhereUsedItemInfoList | None:
    """Find where a part or assembly is used.

     Only supported for Enterprise and Professional plans. See [Dev Docs: Where Used](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#where-used) for a tutorial on using this endpoint.

    Args:
        document_id (str | Unset):
        element_id (str | Unset):
        version_id (str | Unset):
        configuration (str | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        include_properties (bool | Unset):  Default: False.
        filter_ (int | Unset):
        include_version_info (bool | Unset):
        use_latest_version (bool | Unset):  Default: False.
        limit_to_types (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTWhereUsedItemInfoList
    """

    return (
        await asyncio_detailed(
            client=client,
            document_id=document_id,
            element_id=element_id,
            version_id=version_id,
            configuration=configuration,
            part_id=part_id,
            part_number=part_number,
            include_properties=include_properties,
            filter_=filter_,
            include_version_info=include_version_info,
            use_latest_version=use_latest_version,
            limit_to_types=limit_to_types,
        )
    ).parsed
