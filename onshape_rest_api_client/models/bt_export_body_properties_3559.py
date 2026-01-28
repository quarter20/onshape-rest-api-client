from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_part_visibility import GBTPartVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
    from ..models.bt_part_material_1445 import BTPartMaterial1445


T = TypeVar("T", bound="BTExportBodyProperties3559")


@_attrs_define
class BTExportBodyProperties3559:
    """
    Attributes:
        appearance (BTGraphicsAppearance1152 | Unset):
        bt_type (str | Unset): Type of JSON object.
        name (str | Unset):
        material (BTPartMaterial1445 | Unset):
        visibility (GBTPartVisibility | Unset):
    """

    appearance: BTGraphicsAppearance1152 | Unset = UNSET
    bt_type: str | Unset = UNSET
    name: str | Unset = UNSET
    material: BTPartMaterial1445 | Unset = UNSET
    visibility: GBTPartVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appearance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        bt_type = self.bt_type

        name = self.name

        material: dict[str, Any] | Unset = UNSET
        if not isinstance(self.material, Unset):
            material = self.material.to_dict()

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if name is not UNSET:
            field_dict["name"] = name
        if material is not UNSET:
            field_dict["material"] = material
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
        from ..models.bt_part_material_1445 import BTPartMaterial1445

        d = dict(src_dict)
        _appearance = d.pop("appearance", UNSET)
        appearance: BTGraphicsAppearance1152 | Unset
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = BTGraphicsAppearance1152.from_dict(_appearance)

        bt_type = d.pop("btType", UNSET)

        name = d.pop("name", UNSET)

        _material = d.pop("material", UNSET)
        material: BTPartMaterial1445 | Unset
        if isinstance(_material, Unset):
            material = UNSET
        else:
            material = BTPartMaterial1445.from_dict(_material)

        _visibility = d.pop("visibility", UNSET)
        visibility: GBTPartVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = GBTPartVisibility(_visibility)

        bt_export_body_properties_3559 = cls(
            appearance=appearance,
            bt_type=bt_type,
            name=name,
            material=material,
            visibility=visibility,
        )

        bt_export_body_properties_3559.additional_properties = d
        return bt_export_body_properties_3559

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
