from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_configuration_response_2019 import BTConfigurationResponse2019
from ...models.get_configuration_wvm import GetConfigurationWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetConfigurationWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/elements/d/{did}/{wvm}/{wvmid}/e/{eid}/configuration".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTConfigurationResponse2019:
    response_default = BTConfigurationResponse2019.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTConfigurationResponse2019]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetConfigurationWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> Response[BTConfigurationResponse2019]:
    """Get the configuration definition for a Part Studio, Variable Studio, or Assembly.

     Use Configurations to create variations of elements. You can configure feature and parameter values,
    part properties, custom part properties, face and part appearances, and sketch text. Each Part
    Studio can have only one Configuration, but it can contain multiple Configuration inputs.
    See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details.

    Args:
        did (str):
        wvm (GetConfigurationWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTConfigurationResponse2019]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetConfigurationWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> BTConfigurationResponse2019 | None:
    """Get the configuration definition for a Part Studio, Variable Studio, or Assembly.

     Use Configurations to create variations of elements. You can configure feature and parameter values,
    part properties, custom part properties, face and part appearances, and sketch text. Each Part
    Studio can have only one Configuration, but it can contain multiple Configuration inputs.
    See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details.

    Args:
        did (str):
        wvm (GetConfigurationWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTConfigurationResponse2019
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetConfigurationWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> Response[BTConfigurationResponse2019]:
    """Get the configuration definition for a Part Studio, Variable Studio, or Assembly.

     Use Configurations to create variations of elements. You can configure feature and parameter values,
    part properties, custom part properties, face and part appearances, and sketch text. Each Part
    Studio can have only one Configuration, but it can contain multiple Configuration inputs.
    See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details.

    Args:
        did (str):
        wvm (GetConfigurationWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTConfigurationResponse2019]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetConfigurationWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> BTConfigurationResponse2019 | None:
    """Get the configuration definition for a Part Studio, Variable Studio, or Assembly.

     Use Configurations to create variations of elements. You can configure feature and parameter values,
    part properties, custom part properties, face and part appearances, and sketch text. Each Part
    Studio can have only one Configuration, but it can contain multiple Configuration inputs.
    See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details.

    Args:
        did (str):
        wvm (GetConfigurationWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTConfigurationResponse2019
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
        )
    ).parsed
