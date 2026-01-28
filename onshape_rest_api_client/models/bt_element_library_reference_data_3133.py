from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_object_id import BTObjectId


T = TypeVar("T", bound="BTElementLibraryReferenceData3133")


@_attrs_define
class BTElementLibraryReferenceData3133:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        element_library_id (str | Unset):
        element_library_id_raw (BTObjectId | Unset):
        element_library_selection_path (list[BTObjectId] | Unset):
        element_library_version (str | Unset):
        element_library_version_raw (BTObjectId | Unset):
    """

    bt_type: str | Unset = UNSET
    element_library_id: str | Unset = UNSET
    element_library_id_raw: BTObjectId | Unset = UNSET
    element_library_selection_path: list[BTObjectId] | Unset = UNSET
    element_library_version: str | Unset = UNSET
    element_library_version_raw: BTObjectId | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        element_library_id = self.element_library_id

        element_library_id_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_library_id_raw, Unset):
            element_library_id_raw = self.element_library_id_raw.to_dict()

        element_library_selection_path: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.element_library_selection_path, Unset):
            element_library_selection_path = []
            for element_library_selection_path_item_data in self.element_library_selection_path:
                element_library_selection_path_item = element_library_selection_path_item_data.to_dict()
                element_library_selection_path.append(element_library_selection_path_item)

        element_library_version = self.element_library_version

        element_library_version_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_library_version_raw, Unset):
            element_library_version_raw = self.element_library_version_raw.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if element_library_id is not UNSET:
            field_dict["elementLibraryId"] = element_library_id
        if element_library_id_raw is not UNSET:
            field_dict["elementLibraryIdRaw"] = element_library_id_raw
        if element_library_selection_path is not UNSET:
            field_dict["elementLibrarySelectionPath"] = element_library_selection_path
        if element_library_version is not UNSET:
            field_dict["elementLibraryVersion"] = element_library_version
        if element_library_version_raw is not UNSET:
            field_dict["elementLibraryVersionRaw"] = element_library_version_raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_object_id import BTObjectId

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        element_library_id = d.pop("elementLibraryId", UNSET)

        _element_library_id_raw = d.pop("elementLibraryIdRaw", UNSET)
        element_library_id_raw: BTObjectId | Unset
        if isinstance(_element_library_id_raw, Unset):
            element_library_id_raw = UNSET
        else:
            element_library_id_raw = BTObjectId.from_dict(_element_library_id_raw)

        _element_library_selection_path = d.pop("elementLibrarySelectionPath", UNSET)
        element_library_selection_path: list[BTObjectId] | Unset = UNSET
        if _element_library_selection_path is not UNSET:
            element_library_selection_path = []
            for element_library_selection_path_item_data in _element_library_selection_path:
                element_library_selection_path_item = BTObjectId.from_dict(element_library_selection_path_item_data)

                element_library_selection_path.append(element_library_selection_path_item)

        element_library_version = d.pop("elementLibraryVersion", UNSET)

        _element_library_version_raw = d.pop("elementLibraryVersionRaw", UNSET)
        element_library_version_raw: BTObjectId | Unset
        if isinstance(_element_library_version_raw, Unset):
            element_library_version_raw = UNSET
        else:
            element_library_version_raw = BTObjectId.from_dict(_element_library_version_raw)

        bt_element_library_reference_data_3133 = cls(
            bt_type=bt_type,
            element_library_id=element_library_id,
            element_library_id_raw=element_library_id_raw,
            element_library_selection_path=element_library_selection_path,
            element_library_version=element_library_version,
            element_library_version_raw=element_library_version_raw,
        )

        bt_element_library_reference_data_3133.additional_properties = d
        return bt_element_library_reference_data_3133

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
