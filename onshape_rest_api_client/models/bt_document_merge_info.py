from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_element_info import BTDocumentElementInfo


T = TypeVar("T", bound="BTDocumentMergeInfo")


@_attrs_define
class BTDocumentMergeInfo:
    """
    Attributes:
        library_version_mismatch (bool | Unset):
        overwritten_elements (list[BTDocumentElementInfo] | Unset):
        parent_document_microversion_id (str | Unset):
        result_document_microversion_id (str | Unset):
        source_document_microversion_id (str | Unset):
    """

    library_version_mismatch: bool | Unset = UNSET
    overwritten_elements: list[BTDocumentElementInfo] | Unset = UNSET
    parent_document_microversion_id: str | Unset = UNSET
    result_document_microversion_id: str | Unset = UNSET
    source_document_microversion_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        library_version_mismatch = self.library_version_mismatch

        overwritten_elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.overwritten_elements, Unset):
            overwritten_elements = []
            for overwritten_elements_item_data in self.overwritten_elements:
                overwritten_elements_item = overwritten_elements_item_data.to_dict()
                overwritten_elements.append(overwritten_elements_item)

        parent_document_microversion_id = self.parent_document_microversion_id

        result_document_microversion_id = self.result_document_microversion_id

        source_document_microversion_id = self.source_document_microversion_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if library_version_mismatch is not UNSET:
            field_dict["libraryVersionMismatch"] = library_version_mismatch
        if overwritten_elements is not UNSET:
            field_dict["overwrittenElements"] = overwritten_elements
        if parent_document_microversion_id is not UNSET:
            field_dict["parentDocumentMicroversionId"] = parent_document_microversion_id
        if result_document_microversion_id is not UNSET:
            field_dict["resultDocumentMicroversionId"] = result_document_microversion_id
        if source_document_microversion_id is not UNSET:
            field_dict["sourceDocumentMicroversionId"] = source_document_microversion_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_element_info import BTDocumentElementInfo

        d = dict(src_dict)
        library_version_mismatch = d.pop("libraryVersionMismatch", UNSET)

        _overwritten_elements = d.pop("overwrittenElements", UNSET)
        overwritten_elements: list[BTDocumentElementInfo] | Unset = UNSET
        if _overwritten_elements is not UNSET:
            overwritten_elements = []
            for overwritten_elements_item_data in _overwritten_elements:
                overwritten_elements_item = BTDocumentElementInfo.from_dict(overwritten_elements_item_data)

                overwritten_elements.append(overwritten_elements_item)

        parent_document_microversion_id = d.pop("parentDocumentMicroversionId", UNSET)

        result_document_microversion_id = d.pop("resultDocumentMicroversionId", UNSET)

        source_document_microversion_id = d.pop("sourceDocumentMicroversionId", UNSET)

        bt_document_merge_info = cls(
            library_version_mismatch=library_version_mismatch,
            overwritten_elements=overwritten_elements,
            parent_document_microversion_id=parent_document_microversion_id,
            result_document_microversion_id=result_document_microversion_id,
            source_document_microversion_id=source_document_microversion_id,
        )

        bt_document_merge_info.additional_properties = d
        return bt_document_merge_info

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
