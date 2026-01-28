from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_acl_params import BTAclParams
from ...models.update_public_access_response_default import UpdatePublicAccessResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    *,
    body: BTAclParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/{did}/acl/public".format(
            did=quote(str(did), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdatePublicAccessResponseDefault:
    response_default = UpdatePublicAccessResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdatePublicAccessResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTAclParams | Unset = UNSET,
) -> Response[UpdatePublicAccessResponseDefault]:
    """Make a document public or private.

      * Set `public=true` in the request body to make the document public. Set to `false` to make it
    private. Free users cannot make documents private.
     * The `documentId` provided in the URL must match the one provided in the request body exactly.

    Args:
        did (str):
        body (BTAclParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePublicAccessResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTAclParams | Unset = UNSET,
) -> UpdatePublicAccessResponseDefault | None:
    """Make a document public or private.

      * Set `public=true` in the request body to make the document public. Set to `false` to make it
    private. Free users cannot make documents private.
     * The `documentId` provided in the URL must match the one provided in the request body exactly.

    Args:
        did (str):
        body (BTAclParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePublicAccessResponseDefault
    """

    return sync_detailed(
        did=did,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTAclParams | Unset = UNSET,
) -> Response[UpdatePublicAccessResponseDefault]:
    """Make a document public or private.

      * Set `public=true` in the request body to make the document public. Set to `false` to make it
    private. Free users cannot make documents private.
     * The `documentId` provided in the URL must match the one provided in the request body exactly.

    Args:
        did (str):
        body (BTAclParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePublicAccessResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTAclParams | Unset = UNSET,
) -> UpdatePublicAccessResponseDefault | None:
    """Make a document public or private.

      * Set `public=true` in the request body to make the document public. Set to `false` to make it
    private. Free users cannot make documents private.
     * The `documentId` provided in the URL must match the one provided in the request body exactly.

    Args:
        did (str):
        body (BTAclParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePublicAccessResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
            body=body,
        )
    ).parsed
