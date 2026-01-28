from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_translation_request_state import BTTranslationRequestState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTranslationRequestInfo")


@_attrs_define
class BTTranslationRequestInfo:
    """
    Attributes:
        document_id (str | Unset):
        export_rule_file_name (str | Unset): The file name after evaluating a rule for the given `formatName`. `NULL` if
            `evaluateExportRule=false` or if the export rule is not found.
        failure_reason (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        request_element_id (str | Unset):
        request_state (BTTranslationRequestState | Unset):
        result_document_id (str | Unset):
        result_element_ids (list[str] | Unset):
        result_external_data_ids (list[str] | Unset):
        result_workspace_id (str | Unset):
        version_id (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workspace_id (str | Unset):
    """

    document_id: str | Unset = UNSET
    export_rule_file_name: str | Unset = UNSET
    failure_reason: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    request_element_id: str | Unset = UNSET
    request_state: BTTranslationRequestState | Unset = UNSET
    result_document_id: str | Unset = UNSET
    result_element_ids: list[str] | Unset = UNSET
    result_external_data_ids: list[str] | Unset = UNSET
    result_workspace_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        export_rule_file_name = self.export_rule_file_name

        failure_reason = self.failure_reason

        href = self.href

        id = self.id

        name = self.name

        request_element_id = self.request_element_id

        request_state: str | Unset = UNSET
        if not isinstance(self.request_state, Unset):
            request_state = self.request_state.value

        result_document_id = self.result_document_id

        result_element_ids: list[str] | Unset = UNSET
        if not isinstance(self.result_element_ids, Unset):
            result_element_ids = self.result_element_ids

        result_external_data_ids: list[str] | Unset = UNSET
        if not isinstance(self.result_external_data_ids, Unset):
            result_external_data_ids = self.result_external_data_ids

        result_workspace_id = self.result_workspace_id

        version_id = self.version_id

        view_ref = self.view_ref

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if export_rule_file_name is not UNSET:
            field_dict["exportRuleFileName"] = export_rule_file_name
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if request_element_id is not UNSET:
            field_dict["requestElementId"] = request_element_id
        if request_state is not UNSET:
            field_dict["requestState"] = request_state
        if result_document_id is not UNSET:
            field_dict["resultDocumentId"] = result_document_id
        if result_element_ids is not UNSET:
            field_dict["resultElementIds"] = result_element_ids
        if result_external_data_ids is not UNSET:
            field_dict["resultExternalDataIds"] = result_external_data_ids
        if result_workspace_id is not UNSET:
            field_dict["resultWorkspaceId"] = result_workspace_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId", UNSET)

        export_rule_file_name = d.pop("exportRuleFileName", UNSET)

        failure_reason = d.pop("failureReason", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        request_element_id = d.pop("requestElementId", UNSET)

        _request_state = d.pop("requestState", UNSET)
        request_state: BTTranslationRequestState | Unset
        if isinstance(_request_state, Unset):
            request_state = UNSET
        else:
            request_state = BTTranslationRequestState(_request_state)

        result_document_id = d.pop("resultDocumentId", UNSET)

        result_element_ids = cast(list[str], d.pop("resultElementIds", UNSET))

        result_external_data_ids = cast(list[str], d.pop("resultExternalDataIds", UNSET))

        result_workspace_id = d.pop("resultWorkspaceId", UNSET)

        version_id = d.pop("versionId", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_translation_request_info = cls(
            document_id=document_id,
            export_rule_file_name=export_rule_file_name,
            failure_reason=failure_reason,
            href=href,
            id=id,
            name=name,
            request_element_id=request_element_id,
            request_state=request_state,
            result_document_id=result_document_id,
            result_element_ids=result_element_ids,
            result_external_data_ids=result_external_data_ids,
            result_workspace_id=result_workspace_id,
            version_id=version_id,
            view_ref=view_ref,
            workspace_id=workspace_id,
        )

        bt_translation_request_info.additional_properties = d
        return bt_translation_request_info

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
