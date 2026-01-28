from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_configuration_response_2019 import BTConfigurationResponse2019
from ...models.bt_configuration_update_call_2933 import BTConfigurationUpdateCall2933
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    body: BTConfigurationUpdateCall2933 | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/elements/d/{did}/{wvm}/{wvmid}/e/{eid}/configuration".format(
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
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTConfigurationUpdateCall2933 | Unset = UNSET,
) -> Response[BTConfigurationResponse2019]:
    """Update the configuration definition for a Part Studio, Variable Studio, or Assembly.

     See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTConfigurationUpdateCall2933 | Unset):

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
    body: BTConfigurationUpdateCall2933 | Unset = UNSET,
) -> BTConfigurationResponse2019 | None:
    """Update the configuration definition for a Part Studio, Variable Studio, or Assembly.

     See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTConfigurationUpdateCall2933 | Unset):

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
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTConfigurationUpdateCall2933 | Unset = UNSET,
) -> Response[BTConfigurationResponse2019]:
    """Update the configuration definition for a Part Studio, Variable Studio, or Assembly.

     See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTConfigurationUpdateCall2933 | Unset):

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
    body: BTConfigurationUpdateCall2933 | Unset = UNSET,
) -> BTConfigurationResponse2019 | None:
    """Update the configuration definition for a Part Studio, Variable Studio, or Assembly.

     See the [Configuration API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for
    additional details

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (BTConfigurationUpdateCall2933 | Unset):

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
            body=body,
        )
    ).parsed
