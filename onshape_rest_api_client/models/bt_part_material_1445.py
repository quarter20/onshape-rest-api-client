from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_element_reference_725 import BTElementReference725
    from ..models.bt_part_material_1445_properties import BTPartMaterial1445Properties


T = TypeVar("T", bound="BTPartMaterial1445")


@_attrs_define
class BTPartMaterial1445:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        id (str | Unset):
        library_name (str | Unset):
        library_reference (BTElementReference725 | Unset):
        name (str | Unset):
        properties (BTPartMaterial1445Properties | Unset):
        version (int | Unset):
    """

    bt_type: str | Unset = UNSET
    id: str | Unset = UNSET
    library_name: str | Unset = UNSET
    library_reference: BTElementReference725 | Unset = UNSET
    name: str | Unset = UNSET
    properties: BTPartMaterial1445Properties | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        id = self.id

        library_name = self.library_name

        library_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.library_reference, Unset):
            library_reference = self.library_reference.to_dict()

        name = self.name

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if id is not UNSET:
            field_dict["id"] = id
        if library_name is not UNSET:
            field_dict["libraryName"] = library_name
        if library_reference is not UNSET:
            field_dict["libraryReference"] = library_reference
        if name is not UNSET:
            field_dict["name"] = name
        if properties is not UNSET:
            field_dict["properties"] = properties
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_element_reference_725 import BTElementReference725
        from ..models.bt_part_material_1445_properties import BTPartMaterial1445Properties

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        id = d.pop("id", UNSET)

        library_name = d.pop("libraryName", UNSET)

        _library_reference = d.pop("libraryReference", UNSET)
        library_reference: BTElementReference725 | Unset
        if isinstance(_library_reference, Unset):
            library_reference = UNSET
        else:
            library_reference = BTElementReference725.from_dict(_library_reference)

        name = d.pop("name", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: BTPartMaterial1445Properties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = BTPartMaterial1445Properties.from_dict(_properties)

        version = d.pop("version", UNSET)

        bt_part_material_1445 = cls(
            bt_type=bt_type,
            id=id,
            library_name=library_name,
            library_reference=library_reference,
            name=name,
            properties=properties,
            version=version,
        )

        bt_part_material_1445.additional_properties = d
        return bt_part_material_1445

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
