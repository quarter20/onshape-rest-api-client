from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_revision_list_response import BTRevisionListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    pnum: str,
    *,
    element_type: str,
    fill_approvers: bool | Unset = False,
    fill_export_permission: bool | Unset = False,
    support_change_type: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["elementType"] = element_type

    params["fillApprovers"] = fill_approvers

    params["fillExportPermission"] = fill_export_permission

    params["supportChangeType"] = support_change_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/revisions/companies/{cid}/partnumber/{pnum}".format(
            cid=quote(str(cid), safe=""),
            pnum=quote(str(pnum), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTRevisionListResponse:
    response_default = BTRevisionListResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTRevisionListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    element_type: str,
    fill_approvers: bool | Unset = False,
    fill_export_permission: bool | Unset = False,
    support_change_type: bool | Unset = False,
) -> Response[BTRevisionListResponse]:
    """Get all revisions for a part number.

     You can also request `elementType` in addition to `partNumber` since companies may or may not allow
    drawings to share part numbers with their parts/assemblies. To perform search without `elementType`,
    use `elementType = -1` (UNKNOWN).  See [API Guide: Release Management](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#get-all-revisions) for more details.

    Args:
        cid (str):
        pnum (str):
        element_type (str):
        fill_approvers (bool | Unset):  Default: False.
        fill_export_permission (bool | Unset):  Default: False.
        support_change_type (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRevisionListResponse]
    """

    kwargs = _get_kwargs(
        cid=cid,
        pnum=pnum,
        element_type=element_type,
        fill_approvers=fill_approvers,
        fill_export_permission=fill_export_permission,
        support_change_type=support_change_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    element_type: str,
    fill_approvers: bool | Unset = False,
    fill_export_permission: bool | Unset = False,
    support_change_type: bool | Unset = False,
) -> BTRevisionListResponse | None:
    """Get all revisions for a part number.

     You can also request `elementType` in addition to `partNumber` since companies may or may not allow
    drawings to share part numbers with their parts/assemblies. To perform search without `elementType`,
    use `elementType = -1` (UNKNOWN).  See [API Guide: Release Management](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#get-all-revisions) for more details.

    Args:
        cid (str):
        pnum (str):
        element_type (str):
        fill_approvers (bool | Unset):  Default: False.
        fill_export_permission (bool | Unset):  Default: False.
        support_change_type (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRevisionListResponse
    """

    return sync_detailed(
        cid=cid,
        pnum=pnum,
        client=client,
        element_type=element_type,
        fill_approvers=fill_approvers,
        fill_export_permission=fill_export_permission,
        support_change_type=support_change_type,
    ).parsed


async def asyncio_detailed(
    cid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    element_type: str,
    fill_approvers: bool | Unset = False,
    fill_export_permission: bool | Unset = False,
    support_change_type: bool | Unset = False,
) -> Response[BTRevisionListResponse]:
    """Get all revisions for a part number.

     You can also request `elementType` in addition to `partNumber` since companies may or may not allow
    drawings to share part numbers with their parts/assemblies. To perform search without `elementType`,
    use `elementType = -1` (UNKNOWN).  See [API Guide: Release Management](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#get-all-revisions) for more details.

    Args:
        cid (str):
        pnum (str):
        element_type (str):
        fill_approvers (bool | Unset):  Default: False.
        fill_export_permission (bool | Unset):  Default: False.
        support_change_type (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRevisionListResponse]
    """

    kwargs = _get_kwargs(
        cid=cid,
        pnum=pnum,
        element_type=element_type,
        fill_approvers=fill_approvers,
        fill_export_permission=fill_export_permission,
        support_change_type=support_change_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    pnum: str,
    *,
    client: AuthenticatedClient,
    element_type: str,
    fill_approvers: bool | Unset = False,
    fill_export_permission: bool | Unset = False,
    support_change_type: bool | Unset = False,
) -> BTRevisionListResponse | None:
    """Get all revisions for a part number.

     You can also request `elementType` in addition to `partNumber` since companies may or may not allow
    drawings to share part numbers with their parts/assemblies. To perform search without `elementType`,
    use `elementType = -1` (UNKNOWN).  See [API Guide: Release Management](https://onshape-
    public.github.io/docs/api-adv/relmgmt/#get-all-revisions) for more details.

    Args:
        cid (str):
        pnum (str):
        element_type (str):
        fill_approvers (bool | Unset):  Default: False.
        fill_export_permission (bool | Unset):  Default: False.
        support_change_type (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRevisionListResponse
    """

    return (
        await asyncio_detailed(
            cid=cid,
            pnum=pnum,
            client=client,
            element_type=element_type,
            fill_approvers=fill_approvers,
            fill_export_permission=fill_export_permission,
            support_change_type=support_change_type,
        )
    ).parsed
