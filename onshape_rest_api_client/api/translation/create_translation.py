from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_translation_request_import_info import BTTranslationRequestImportInfo
from ...models.create_translation_body import CreateTranslationBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    *,
    body: CreateTranslationBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/translations/d/{did}/w/{wid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTTranslationRequestImportInfo:
    response_default = BTTranslationRequestImportInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTTranslationRequestImportInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: CreateTranslationBody | Unset = UNSET,
) -> Response[BTTranslationRequestImportInfo]:
    """Import or upload a CAD file into Onshape, and translate the data into parts or assemblies.

     The API call may complete before the translation is finished. If `requestState = ACTIVE`, the
    translation can be polled until the state is either `DONE` or `FAILED`. Alternatively, a webhook
    callback can be registered for notification of translation completion (requires `Write` scope if
    `storeInDocument` is `true`).

    See [API Guide: Import & Export](https://onshape-public.github.io/docs/api-adv/translation/) for
    examples.

    Args:
        did (str):
        wid (str):
        body (CreateTranslationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTranslationRequestImportInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: CreateTranslationBody | Unset = UNSET,
) -> BTTranslationRequestImportInfo | None:
    """Import or upload a CAD file into Onshape, and translate the data into parts or assemblies.

     The API call may complete before the translation is finished. If `requestState = ACTIVE`, the
    translation can be polled until the state is either `DONE` or `FAILED`. Alternatively, a webhook
    callback can be registered for notification of translation completion (requires `Write` scope if
    `storeInDocument` is `true`).

    See [API Guide: Import & Export](https://onshape-public.github.io/docs/api-adv/translation/) for
    examples.

    Args:
        did (str):
        wid (str):
        body (CreateTranslationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTranslationRequestImportInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: CreateTranslationBody | Unset = UNSET,
) -> Response[BTTranslationRequestImportInfo]:
    """Import or upload a CAD file into Onshape, and translate the data into parts or assemblies.

     The API call may complete before the translation is finished. If `requestState = ACTIVE`, the
    translation can be polled until the state is either `DONE` or `FAILED`. Alternatively, a webhook
    callback can be registered for notification of translation completion (requires `Write` scope if
    `storeInDocument` is `true`).

    See [API Guide: Import & Export](https://onshape-public.github.io/docs/api-adv/translation/) for
    examples.

    Args:
        did (str):
        wid (str):
        body (CreateTranslationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTranslationRequestImportInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: CreateTranslationBody | Unset = UNSET,
) -> BTTranslationRequestImportInfo | None:
    """Import or upload a CAD file into Onshape, and translate the data into parts or assemblies.

     The API call may complete before the translation is finished. If `requestState = ACTIVE`, the
    translation can be polled until the state is either `DONE` or `FAILED`. Alternatively, a webhook
    callback can be registered for notification of translation completion (requires `Write` scope if
    `storeInDocument` is `true`).

    See [API Guide: Import & Export](https://onshape-public.github.io/docs/api-adv/translation/) for
    examples.

    Args:
        did (str):
        wid (str):
        body (CreateTranslationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTranslationRequestImportInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
            body=body,
        )
    ).parsed
