from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_configuration_params import BTConfigurationParams
from ...models.bt_encoded_configuration_info import BTEncodedConfigurationInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    eid: str,
    *,
    body: BTConfigurationParams,
    version_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["versionId"] = version_id

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/elements/d/{did}/e/{eid}/configurationencodings".format(
            did=quote(str(did), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTEncodedConfigurationInfo:
    response_default = BTEncodedConfigurationInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTEncodedConfigurationInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTConfigurationParams,
    version_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTEncodedConfigurationInfo]:
    """Encode a configuration option for use in other API calls.

     Returns a configuration string in the following form:
    `configuration=parameterId%3DparameterValue`
    The configuration string can be used in other Onshape API calls to specify which configuration
    option to use. See the [Configuration API Guide](https://onshape-public.github.io/docs/api-
    adv/configs/) for additional details.

    Args:
        did (str):
        eid (str):
        version_id (str | Unset):
        link_document_id (str | Unset):
        body (BTConfigurationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTEncodedConfigurationInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        eid=eid,
        body=body,
        version_id=version_id,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTConfigurationParams,
    version_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTEncodedConfigurationInfo | None:
    """Encode a configuration option for use in other API calls.

     Returns a configuration string in the following form:
    `configuration=parameterId%3DparameterValue`
    The configuration string can be used in other Onshape API calls to specify which configuration
    option to use. See the [Configuration API Guide](https://onshape-public.github.io/docs/api-
    adv/configs/) for additional details.

    Args:
        did (str):
        eid (str):
        version_id (str | Unset):
        link_document_id (str | Unset):
        body (BTConfigurationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTEncodedConfigurationInfo
    """

    return sync_detailed(
        did=did,
        eid=eid,
        client=client,
        body=body,
        version_id=version_id,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTConfigurationParams,
    version_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTEncodedConfigurationInfo]:
    """Encode a configuration option for use in other API calls.

     Returns a configuration string in the following form:
    `configuration=parameterId%3DparameterValue`
    The configuration string can be used in other Onshape API calls to specify which configuration
    option to use. See the [Configuration API Guide](https://onshape-public.github.io/docs/api-
    adv/configs/) for additional details.

    Args:
        did (str):
        eid (str):
        version_id (str | Unset):
        link_document_id (str | Unset):
        body (BTConfigurationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTEncodedConfigurationInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        eid=eid,
        body=body,
        version_id=version_id,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTConfigurationParams,
    version_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTEncodedConfigurationInfo | None:
    """Encode a configuration option for use in other API calls.

     Returns a configuration string in the following form:
    `configuration=parameterId%3DparameterValue`
    The configuration string can be used in other Onshape API calls to specify which configuration
    option to use. See the [Configuration API Guide](https://onshape-public.github.io/docs/api-
    adv/configs/) for additional details.

    Args:
        did (str):
        eid (str):
        version_id (str | Unset):
        link_document_id (str | Unset):
        body (BTConfigurationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTEncodedConfigurationInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            eid=eid,
            client=client,
            body=body,
            version_id=version_id,
            link_document_id=link_document_id,
        )
    ).parsed
