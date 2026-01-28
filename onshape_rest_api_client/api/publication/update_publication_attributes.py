from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_publication_params import BTPublicationParams
from ...models.update_publication_attributes_response_default import UpdatePublicationAttributesResponseDefault
from ...types import Response


def _get_kwargs(
    pid: str,
    *,
    body: BTPublicationParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/publications/{pid}".format(
            pid=quote(str(pid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdatePublicationAttributesResponseDefault:
    response_default = UpdatePublicationAttributesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdatePublicationAttributesResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: BTPublicationParams,
) -> Response[UpdatePublicationAttributesResponseDefault]:
    """Update publication's attributes name, description, and notes.

    Args:
        pid (str):
        body (BTPublicationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePublicationAttributesResponseDefault]
    """

    kwargs = _get_kwargs(
        pid=pid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: BTPublicationParams,
) -> UpdatePublicationAttributesResponseDefault | None:
    """Update publication's attributes name, description, and notes.

    Args:
        pid (str):
        body (BTPublicationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePublicationAttributesResponseDefault
    """

    return sync_detailed(
        pid=pid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: BTPublicationParams,
) -> Response[UpdatePublicationAttributesResponseDefault]:
    """Update publication's attributes name, description, and notes.

    Args:
        pid (str):
        body (BTPublicationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePublicationAttributesResponseDefault]
    """

    kwargs = _get_kwargs(
        pid=pid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: BTPublicationParams,
) -> UpdatePublicationAttributesResponseDefault | None:
    """Update publication's attributes name, description, and notes.

    Args:
        pid (str):
        body (BTPublicationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePublicationAttributesResponseDefault
    """

    return (
        await asyncio_detailed(
            pid=pid,
            client=client,
            body=body,
        )
    ).parsed
