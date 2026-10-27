from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_std_version_replace_info import BTStdVersionReplaceInfo
from ...models.bt_std_version_replace_params import BTStdVersionReplaceParams
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    *,
    body: BTStdVersionReplaceParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/featurestudios/d/{did}/w/{wid}/stdversionreplace".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTStdVersionReplaceInfo:
    response_default = BTStdVersionReplaceInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTStdVersionReplaceInfo]:
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
    body: BTStdVersionReplaceParams,
) -> Response[BTStdVersionReplaceInfo]:
    """Replace the standard library version of the imports in the Feature Studios of a workspace.

     Rewrites the version of every `onshape/std` import selected by the `includeVersions` and
    `excludeVersions` filters, using the same filter syntax as the standard library version search. By
    default the modified Feature Studios are committed to the workspace; pass `commit` as false to leave
    them as uncommitted edits for a user to review and commit in the Onshape UI.
    `replaceWith` is checked for the right form but is not checked against the released standard library
    versions, so a version that does not exist will leave the rewritten imports unresolved.

    Args:
        did (str):
        wid (str):
        body (BTStdVersionReplaceParams): Parameters for replacing the standard library version of
            `onshape/std` imports in the Feature Studios of a workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTStdVersionReplaceInfo]
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
    body: BTStdVersionReplaceParams,
) -> BTStdVersionReplaceInfo | None:
    """Replace the standard library version of the imports in the Feature Studios of a workspace.

     Rewrites the version of every `onshape/std` import selected by the `includeVersions` and
    `excludeVersions` filters, using the same filter syntax as the standard library version search. By
    default the modified Feature Studios are committed to the workspace; pass `commit` as false to leave
    them as uncommitted edits for a user to review and commit in the Onshape UI.
    `replaceWith` is checked for the right form but is not checked against the released standard library
    versions, so a version that does not exist will leave the rewritten imports unresolved.

    Args:
        did (str):
        wid (str):
        body (BTStdVersionReplaceParams): Parameters for replacing the standard library version of
            `onshape/std` imports in the Feature Studios of a workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTStdVersionReplaceInfo
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
    body: BTStdVersionReplaceParams,
) -> Response[BTStdVersionReplaceInfo]:
    """Replace the standard library version of the imports in the Feature Studios of a workspace.

     Rewrites the version of every `onshape/std` import selected by the `includeVersions` and
    `excludeVersions` filters, using the same filter syntax as the standard library version search. By
    default the modified Feature Studios are committed to the workspace; pass `commit` as false to leave
    them as uncommitted edits for a user to review and commit in the Onshape UI.
    `replaceWith` is checked for the right form but is not checked against the released standard library
    versions, so a version that does not exist will leave the rewritten imports unresolved.

    Args:
        did (str):
        wid (str):
        body (BTStdVersionReplaceParams): Parameters for replacing the standard library version of
            `onshape/std` imports in the Feature Studios of a workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTStdVersionReplaceInfo]
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
    body: BTStdVersionReplaceParams,
) -> BTStdVersionReplaceInfo | None:
    """Replace the standard library version of the imports in the Feature Studios of a workspace.

     Rewrites the version of every `onshape/std` import selected by the `includeVersions` and
    `excludeVersions` filters, using the same filter syntax as the standard library version search. By
    default the modified Feature Studios are committed to the workspace; pass `commit` as false to leave
    them as uncommitted edits for a user to review and commit in the Onshape UI.
    `replaceWith` is checked for the right form but is not checked against the released standard library
    versions, so a version that does not exist will leave the rewritten imports unresolved.

    Args:
        did (str):
        wid (str):
        body (BTStdVersionReplaceParams): Parameters for replacing the standard library version of
            `onshape/std` imports in the Feature Studios of a workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTStdVersionReplaceInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
            body=body,
        )
    ).parsed
