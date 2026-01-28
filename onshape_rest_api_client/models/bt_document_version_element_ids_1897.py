from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTDocumentVersionElementIds1897")


@_attrs_define
class BTDocumentVersionElementIds1897:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        document_id (str | Unset):
        element_id (str | Unset):
        version_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        document_id = self.document_id

        element_id = self.element_id

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        version_id = d.pop("versionId", UNSET)

        bt_document_version_element_ids_1897 = cls(
            bt_type=bt_type,
            document_id=document_id,
            element_id=element_id,
            version_id=version_id,
        )

        bt_document_version_element_ids_1897.additional_properties = d
        return bt_document_version_element_ids_1897

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
