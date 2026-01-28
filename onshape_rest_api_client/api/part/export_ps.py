from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    version: str | Unset = "0",
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["version"] = version

    params["configuration"] = configuration

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/parts/d/{did}/{wvm}/{wvmid}/e/{eid}/partid/{partid}/parasolid".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            partid=quote(str(partid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> File | None:
    if response.status_code == 307:
        response_307 = File(payload=BytesIO(response.content))

        return response_307

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[File]:
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
    partid: str,
    *,
    client: AuthenticatedClient,
    version: str | Unset = "0",
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[File]:
    """Synchronously export a part to a Parasolid file.

     Creates a synchronous export of the part (with limited tessellation settings) to a Parasolid file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        version (str | Unset):  Default: '0'.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        version=version,
        configuration=configuration,
        link_document_id=link_document_id,
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
    partid: str,
    *,
    client: AuthenticatedClient,
    version: str | Unset = "0",
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> File | None:
    """Synchronously export a part to a Parasolid file.

     Creates a synchronous export of the part (with limited tessellation settings) to a Parasolid file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        version (str | Unset):  Default: '0'.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        client=client,
        version=version,
        configuration=configuration,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    version: str | Unset = "0",
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[File]:
    """Synchronously export a part to a Parasolid file.

     Creates a synchronous export of the part (with limited tessellation settings) to a Parasolid file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        version (str | Unset):  Default: '0'.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        version=version,
        configuration=configuration,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    version: str | Unset = "0",
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> File | None:
    """Synchronously export a part to a Parasolid file.

     Creates a synchronous export of the part (with limited tessellation settings) to a Parasolid file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        version (str | Unset):  Default: '0'.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            partid=partid,
            client=client,
            version=version,
            configuration=configuration,
            link_document_id=link_document_id,
        )
    ).parsed
