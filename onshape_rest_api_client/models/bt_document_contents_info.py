from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_element_info import BTDocumentElementInfo
    from ..models.bt_element_group_1458 import BTElementGroup1458


T = TypeVar("T", bound="BTDocumentContentsInfo")


@_attrs_define
class BTDocumentContentsInfo:
    """
    Attributes:
        elements (list[BTDocumentElementInfo] | Unset): The elements (tabs) in the document. This does not include
            folders.
        folders (BTElementGroup1458 | Unset):
    """

    elements: list[BTDocumentElementInfo] | Unset = UNSET
    folders: BTElementGroup1458 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        folders: dict[str, Any] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = self.folders.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elements is not UNSET:
            field_dict["elements"] = elements
        if folders is not UNSET:
            field_dict["folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_element_info import BTDocumentElementInfo
        from ..models.bt_element_group_1458 import BTElementGroup1458

        d = dict(src_dict)
        _elements = d.pop("elements", UNSET)
        elements: list[BTDocumentElementInfo] | Unset = UNSET
        if _elements is not UNSET:
            elements = []
            for elements_item_data in _elements:
                elements_item = BTDocumentElementInfo.from_dict(elements_item_data)

                elements.append(elements_item)

        _folders = d.pop("folders", UNSET)
        folders: BTElementGroup1458 | Unset
        if isinstance(_folders, Unset):
            folders = UNSET
        else:
            folders = BTElementGroup1458.from_dict(_folders)

        bt_document_contents_info = cls(
            elements=elements,
            folders=folders,
        )

        bt_document_contents_info.additional_properties = d
        return bt_document_contents_info

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
