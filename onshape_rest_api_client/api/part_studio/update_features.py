from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_update_features_call_1748 import BTUpdateFeaturesCall1748
from ...models.bt_update_features_response_1333 import BTUpdateFeaturesResponse1333
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTUpdateFeaturesCall1748 | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/partstudios/d/{did}/w/{wid}/e/{eid}/features/updates".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTUpdateFeaturesResponse1333:
    response_default = BTUpdateFeaturesResponse1333.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTUpdateFeaturesResponse1333]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateFeaturesCall1748 | Unset = UNSET,
) -> Response[BTUpdateFeaturesResponse1333]:
    """Update multiple features in a Part Studio

     This API accepts a list of features (that must already exist in the Part Studio) to update. This
    call does not fully redefine the features; it updates only the parameters supplied in the top-level
    feature structure, and optionally can update feature suppression attributes.
    See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTUpdateFeaturesCall1748 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTUpdateFeaturesResponse1333]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateFeaturesCall1748 | Unset = UNSET,
) -> BTUpdateFeaturesResponse1333 | None:
    """Update multiple features in a Part Studio

     This API accepts a list of features (that must already exist in the Part Studio) to update. This
    call does not fully redefine the features; it updates only the parameters supplied in the top-level
    feature structure, and optionally can update feature suppression attributes.
    See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTUpdateFeaturesCall1748 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTUpdateFeaturesResponse1333
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateFeaturesCall1748 | Unset = UNSET,
) -> Response[BTUpdateFeaturesResponse1333]:
    """Update multiple features in a Part Studio

     This API accepts a list of features (that must already exist in the Part Studio) to update. This
    call does not fully redefine the features; it updates only the parameters supplied in the top-level
    feature structure, and optionally can update feature suppression attributes.
    See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTUpdateFeaturesCall1748 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTUpdateFeaturesResponse1333]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateFeaturesCall1748 | Unset = UNSET,
) -> BTUpdateFeaturesResponse1333 | None:
    """Update multiple features in a Part Studio

     This API accepts a list of features (that must already exist in the Part Studio) to update. This
    call does not fully redefine the features; it updates only the parameters supplied in the top-level
    feature structure, and optionally can update feature suppression attributes.
    See the [Features API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/) for
    additional information.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTUpdateFeaturesCall1748 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTUpdateFeaturesResponse1333
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            client=client,
            body=body,
        )
    ).parsed
