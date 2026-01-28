from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_configuration_info import BTConfigurationInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    cid: str,
    *,
    link_document_id: str | Unset = UNSET,
    include_display: bool | Unset = False,
    configuration_is_id: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["includeDisplay"] = include_display

    params["configurationIsId"] = configuration_is_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/elements/d/{did}/{wvm}/{wvmid}/e/{eid}/configurationencodings/{cid}".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            cid=quote(str(cid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTConfigurationInfo:
    response_default = BTConfigurationInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTConfigurationInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    cid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = UNSET,
    include_display: bool | Unset = False,
    configuration_is_id: bool | Unset = False,
) -> Response[BTConfigurationInfo]:
    """Decode a configuration string.

     Decode a configuration string into its original JSON form to obtain configuration parameter ID and
    value. See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        cid (str):
        link_document_id (str | Unset):
        include_display (bool | Unset):  Default: False.
        configuration_is_id (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTConfigurationInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        cid=cid,
        link_document_id=link_document_id,
        include_display=include_display,
        configuration_is_id=configuration_is_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    cid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = UNSET,
    include_display: bool | Unset = False,
    configuration_is_id: bool | Unset = False,
) -> BTConfigurationInfo | None:
    """Decode a configuration string.

     Decode a configuration string into its original JSON form to obtain configuration parameter ID and
    value. See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        cid (str):
        link_document_id (str | Unset):
        include_display (bool | Unset):  Default: False.
        configuration_is_id (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTConfigurationInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        cid=cid,
        client=client,
        link_document_id=link_document_id,
        include_display=include_display,
        configuration_is_id=configuration_is_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    cid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = UNSET,
    include_display: bool | Unset = False,
    configuration_is_id: bool | Unset = False,
) -> Response[BTConfigurationInfo]:
    """Decode a configuration string.

     Decode a configuration string into its original JSON form to obtain configuration parameter ID and
    value. See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        cid (str):
        link_document_id (str | Unset):
        include_display (bool | Unset):  Default: False.
        configuration_is_id (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTConfigurationInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        cid=cid,
        link_document_id=link_document_id,
        include_display=include_display,
        configuration_is_id=configuration_is_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    cid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = UNSET,
    include_display: bool | Unset = False,
    configuration_is_id: bool | Unset = False,
) -> BTConfigurationInfo | None:
    """Decode a configuration string.

     Decode a configuration string into its original JSON form to obtain configuration parameter ID and
    value. See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        cid (str):
        link_document_id (str | Unset):
        include_display (bool | Unset):  Default: False.
        configuration_is_id (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTConfigurationInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            cid=cid,
            client=client,
            link_document_id=link_document_id,
            include_display=include_display,
            configuration_is_id=configuration_is_id,
        )
    ).parsed
