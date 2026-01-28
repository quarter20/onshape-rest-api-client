from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_modification_request_state import BTAppModificationRequestState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAppModificationRequestInfo")


@_attrs_define
class BTAppModificationRequestInfo:
    """
    Attributes:
        document_id (str | Unset):
        element_id (str | Unset):
        failure_reason (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        output (str | Unset):
        output_status_code (int | Unset):
        parent_document_microversion_id (str | Unset):
        parent_element_microversion_id (str | Unset):
        request_state (BTAppModificationRequestState | Unset):
        result_document_microversion_id (str | Unset):
        result_element_microversion_id (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workspace_id (str | Unset):
    """

    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    failure_reason: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    output: str | Unset = UNSET
    output_status_code: int | Unset = UNSET
    parent_document_microversion_id: str | Unset = UNSET
    parent_element_microversion_id: str | Unset = UNSET
    request_state: BTAppModificationRequestState | Unset = UNSET
    result_document_microversion_id: str | Unset = UNSET
    result_element_microversion_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        element_id = self.element_id

        failure_reason = self.failure_reason

        href = self.href

        id = self.id

        name = self.name

        output = self.output

        output_status_code = self.output_status_code

        parent_document_microversion_id = self.parent_document_microversion_id

        parent_element_microversion_id = self.parent_element_microversion_id

        request_state: str | Unset = UNSET
        if not isinstance(self.request_state, Unset):
            request_state = self.request_state.value

        result_document_microversion_id = self.result_document_microversion_id

        result_element_microversion_id = self.result_element_microversion_id

        view_ref = self.view_ref

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if output is not UNSET:
            field_dict["output"] = output
        if output_status_code is not UNSET:
            field_dict["outputStatusCode"] = output_status_code
        if parent_document_microversion_id is not UNSET:
            field_dict["parentDocumentMicroversionId"] = parent_document_microversion_id
        if parent_element_microversion_id is not UNSET:
            field_dict["parentElementMicroversionId"] = parent_element_microversion_id
        if request_state is not UNSET:
            field_dict["requestState"] = request_state
        if result_document_microversion_id is not UNSET:
            field_dict["resultDocumentMicroversionId"] = result_document_microversion_id
        if result_element_microversion_id is not UNSET:
            field_dict["resultElementMicroversionId"] = result_element_microversion_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        failure_reason = d.pop("failureReason", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        output = d.pop("output", UNSET)

        output_status_code = d.pop("outputStatusCode", UNSET)

        parent_document_microversion_id = d.pop("parentDocumentMicroversionId", UNSET)

        parent_element_microversion_id = d.pop("parentElementMicroversionId", UNSET)

        _request_state = d.pop("requestState", UNSET)
        request_state: BTAppModificationRequestState | Unset
        if isinstance(_request_state, Unset):
            request_state = UNSET
        else:
            request_state = BTAppModificationRequestState(_request_state)

        result_document_microversion_id = d.pop("resultDocumentMicroversionId", UNSET)

        result_element_microversion_id = d.pop("resultElementMicroversionId", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_app_modification_request_info = cls(
            document_id=document_id,
            element_id=element_id,
            failure_reason=failure_reason,
            href=href,
            id=id,
            name=name,
            output=output,
            output_status_code=output_status_code,
            parent_document_microversion_id=parent_document_microversion_id,
            parent_element_microversion_id=parent_element_microversion_id,
            request_state=request_state,
            result_document_microversion_id=result_document_microversion_id,
            result_element_microversion_id=result_element_microversion_id,
            view_ref=view_ref,
            workspace_id=workspace_id,
        )

        bt_app_modification_request_info.additional_properties = d
        return bt_app_modification_request_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
