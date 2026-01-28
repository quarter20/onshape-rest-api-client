from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_feature_definition_call_1406 import BTFeatureDefinitionCall1406
from ...models.bt_feature_definition_response_1617 import BTFeatureDefinitionResponse1617
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    body: BTFeatureDefinitionCall1406 | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTFeatureDefinitionResponse1617:
    response_default = BTFeatureDefinitionResponse1617.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTFeatureDefinitionResponse1617]:
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
    *,
    client: AuthenticatedClient,
    body: BTFeatureDefinitionCall1406 | Unset = UNSET,
) -> Response[BTFeatureDefinitionResponse1617]:
    """Add a feature to the Part Studio's Feature List.

     The feature is added immediately before the rollback bar. Any geometry IDs specified in the feature
    must be valid at that point in the feature tree.

    See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTFeatureDefinitionCall1406 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureDefinitionResponse1617]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
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
    *,
    client: AuthenticatedClient,
    body: BTFeatureDefinitionCall1406 | Unset = UNSET,
) -> BTFeatureDefinitionResponse1617 | None:
    """Add a feature to the Part Studio's Feature List.

     The feature is added immediately before the rollback bar. Any geometry IDs specified in the feature
    must be valid at that point in the feature tree.

    See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTFeatureDefinitionCall1406 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureDefinitionResponse1617
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTFeatureDefinitionCall1406 | Unset = UNSET,
) -> Response[BTFeatureDefinitionResponse1617]:
    """Add a feature to the Part Studio's Feature List.

     The feature is added immediately before the rollback bar. Any geometry IDs specified in the feature
    must be valid at that point in the feature tree.

    See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTFeatureDefinitionCall1406 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureDefinitionResponse1617]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTFeatureDefinitionCall1406 | Unset = UNSET,
) -> BTFeatureDefinitionResponse1617 | None:
    """Add a feature to the Part Studio's Feature List.

     The feature is added immediately before the rollback bar. Any geometry IDs specified in the feature
    must be valid at that point in the feature tree.

    See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTFeatureDefinitionCall1406 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureDefinitionResponse1617
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            body=body,
        )
    ).parsed
