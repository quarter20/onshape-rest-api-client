from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAssemblyItemMetadataRequestInfo")


@_attrs_define
class BTAssemblyItemMetadataRequestInfo:
    """
    Attributes:
        api_config (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        item_id (str | Unset):
        linked_document_id (str | Unset):
        part_id (str | Unset):
        wvm_id (str | Unset):
        wvm_type (str | Unset):
    """

    api_config: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    item_id: str | Unset = UNSET
    linked_document_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    wvm_id: str | Unset = UNSET
    wvm_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_config = self.api_config

        document_id = self.document_id

        element_id = self.element_id

        item_id = self.item_id

        linked_document_id = self.linked_document_id

        part_id = self.part_id

        wvm_id = self.wvm_id

        wvm_type = self.wvm_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_config is not UNSET:
            field_dict["apiConfig"] = api_config
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if linked_document_id is not UNSET:
            field_dict["linkedDocumentId"] = linked_document_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if wvm_id is not UNSET:
            field_dict["wvmId"] = wvm_id
        if wvm_type is not UNSET:
            field_dict["wvmType"] = wvm_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_config = d.pop("apiConfig", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        item_id = d.pop("itemId", UNSET)

        linked_document_id = d.pop("linkedDocumentId", UNSET)

        part_id = d.pop("partId", UNSET)

        wvm_id = d.pop("wvmId", UNSET)

        wvm_type = d.pop("wvmType", UNSET)

        bt_assembly_item_metadata_request_info = cls(
            api_config=api_config,
            document_id=document_id,
            element_id=element_id,
            item_id=item_id,
            linked_document_id=linked_document_id,
            part_id=part_id,
            wvm_id=wvm_id,
            wvm_type=wvm_type,
        )

        bt_assembly_item_metadata_request_info.additional_properties = d
        return bt_assembly_item_metadata_request_info

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
