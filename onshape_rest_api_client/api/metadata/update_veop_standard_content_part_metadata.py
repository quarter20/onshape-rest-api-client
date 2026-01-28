from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.update_veop_standard_content_part_metadata_response_default import (
    UpdateVEOPStandardContentPartMetadataResponseDefault,
)
from ...types import UNSET, Response


def _get_kwargs(
    did: str,
    *,
    body: str,
    link_document_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/metadata/standardcontent/d/{did}".format(
            did=quote(str(did), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateVEOPStandardContentPartMetadataResponseDefault:
    response_default = UpdateVEOPStandardContentPartMetadataResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateVEOPStandardContentPartMetadataResponseDefault]:
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
    body: str,
    link_document_id: str,
) -> Response[UpdateVEOPStandardContentPartMetadataResponseDefault]:
    """Update the metadata for a standard content part.

     Specify the property metadata to update in the Request body. See [API Guide:
    Metadata](https://onshape-public.github.io/docs/api-adv/metadata/#update-standard-content-part-
    metadata) for an example.

    Args:
        did (str):
        link_document_id (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateVEOPStandardContentPartMetadataResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        body=body,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient,
    body: str,
    link_document_id: str,
) -> UpdateVEOPStandardContentPartMetadataResponseDefault | None:
    """Update the metadata for a standard content part.

     Specify the property metadata to update in the Request body. See [API Guide:
    Metadata](https://onshape-public.github.io/docs/api-adv/metadata/#update-standard-content-part-
    metadata) for an example.

    Args:
        did (str):
        link_document_id (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateVEOPStandardContentPartMetadataResponseDefault
    """

    return sync_detailed(
        did=did,
        client=client,
        body=body,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    body: str,
    link_document_id: str,
) -> Response[UpdateVEOPStandardContentPartMetadataResponseDefault]:
    """Update the metadata for a standard content part.

     Specify the property metadata to update in the Request body. See [API Guide:
    Metadata](https://onshape-public.github.io/docs/api-adv/metadata/#update-standard-content-part-
    metadata) for an example.

    Args:
        did (str):
        link_document_id (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateVEOPStandardContentPartMetadataResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        body=body,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient,
    body: str,
    link_document_id: str,
) -> UpdateVEOPStandardContentPartMetadataResponseDefault | None:
    """Update the metadata for a standard content part.

     Specify the property metadata to update in the Request body. See [API Guide:
    Metadata](https://onshape-public.github.io/docs/api-adv/metadata/#update-standard-content-part-
    metadata) for an example.

    Args:
        did (str):
        link_document_id (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateVEOPStandardContentPartMetadataResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
            body=body,
            link_document_id=link_document_id,
        )
    ).parsed
