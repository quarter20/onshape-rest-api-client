from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_standard_content_set_custom_parameters_batch_request import (
    BTStandardContentSetCustomParametersBatchRequest,
)
from ...models.bt_standard_content_set_custom_parameters_batch_response import (
    BTStandardContentSetCustomParametersBatchResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    *,
    body: BTStandardContentSetCustomParametersBatchRequest | Unset = UNSET,
    company_id: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["companyId"] = company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/standardcontent/d/{did}/customparameters".format(
            did=quote(str(did), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTStandardContentSetCustomParametersBatchResponse:
    response_default = BTStandardContentSetCustomParametersBatchResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTStandardContentSetCustomParametersBatchResponse]:
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
    body: BTStandardContentSetCustomParametersBatchRequest | Unset = UNSET,
    company_id: str | Unset = "",
) -> Response[BTStandardContentSetCustomParametersBatchResponse]:
    """Sets the part number and description for a standard content component.

    Args:
        did (str):
        company_id (str | Unset):  Default: ''.
        body (BTStandardContentSetCustomParametersBatchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTStandardContentSetCustomParametersBatchResponse]
    """

    kwargs = _get_kwargs(
        did=did,
        body=body,
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTStandardContentSetCustomParametersBatchRequest | Unset = UNSET,
    company_id: str | Unset = "",
) -> BTStandardContentSetCustomParametersBatchResponse | None:
    """Sets the part number and description for a standard content component.

    Args:
        did (str):
        company_id (str | Unset):  Default: ''.
        body (BTStandardContentSetCustomParametersBatchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTStandardContentSetCustomParametersBatchResponse
    """

    return sync_detailed(
        did=did,
        client=client,
        body=body,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTStandardContentSetCustomParametersBatchRequest | Unset = UNSET,
    company_id: str | Unset = "",
) -> Response[BTStandardContentSetCustomParametersBatchResponse]:
    """Sets the part number and description for a standard content component.

    Args:
        did (str):
        company_id (str | Unset):  Default: ''.
        body (BTStandardContentSetCustomParametersBatchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTStandardContentSetCustomParametersBatchResponse]
    """

    kwargs = _get_kwargs(
        did=did,
        body=body,
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTStandardContentSetCustomParametersBatchRequest | Unset = UNSET,
    company_id: str | Unset = "",
) -> BTStandardContentSetCustomParametersBatchResponse | None:
    """Sets the part number and description for a standard content component.

    Args:
        did (str):
        company_id (str | Unset):  Default: ''.
        body (BTStandardContentSetCustomParametersBatchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTStandardContentSetCustomParametersBatchResponse
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
            body=body,
            company_id=company_id,
        )
    ).parsed
