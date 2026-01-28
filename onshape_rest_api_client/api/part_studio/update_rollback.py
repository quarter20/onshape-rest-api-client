from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_set_feature_rollback_response_1042 import BTSetFeatureRollbackResponse1042
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/partstudios/d/{did}/w/{wid}/e/{eid}/features/rollback".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTSetFeatureRollbackResponse1042:
    response_default = BTSetFeatureRollbackResponse1042.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTSetFeatureRollbackResponse1042]:
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
    body: str,
) -> Response[BTSetFeatureRollbackResponse1042]:
    r"""Move the Feature List rollback bar in the Part Studio.

     Replace `\"string\"` in the request body with an object that specifies the new location for the
    rollback bar:
     `{ \"rollbackIndex\": integer }`

    For example: `{ \"rollbackIndex\": 2 }`

    Set to `-1` to move the rollback bar to the end of the list.

    See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTSetFeatureRollbackResponse1042]
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
    body: str,
) -> BTSetFeatureRollbackResponse1042 | None:
    r"""Move the Feature List rollback bar in the Part Studio.

     Replace `\"string\"` in the request body with an object that specifies the new location for the
    rollback bar:
     `{ \"rollbackIndex\": integer }`

    For example: `{ \"rollbackIndex\": 2 }`

    Set to `-1` to move the rollback bar to the end of the list.

    See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTSetFeatureRollbackResponse1042
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
    body: str,
) -> Response[BTSetFeatureRollbackResponse1042]:
    r"""Move the Feature List rollback bar in the Part Studio.

     Replace `\"string\"` in the request body with an object that specifies the new location for the
    rollback bar:
     `{ \"rollbackIndex\": integer }`

    For example: `{ \"rollbackIndex\": 2 }`

    Set to `-1` to move the rollback bar to the end of the list.

    See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTSetFeatureRollbackResponse1042]
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
    body: str,
) -> BTSetFeatureRollbackResponse1042 | None:
    r"""Move the Feature List rollback bar in the Part Studio.

     Replace `\"string\"` in the request body with an object that specifies the new location for the
    rollback bar:
     `{ \"rollbackIndex\": integer }`

    For example: `{ \"rollbackIndex\": 2 }`

    Set to `-1` to move the rollback bar to the end of the list.

    See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTSetFeatureRollbackResponse1042
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
