from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
    from ..models.bt_part_metadata_source_2895 import BTPartMetadataSource2895


T = TypeVar("T", bound="BTBaseEntityAppearanceEntry3607")


@_attrs_define
class BTBaseEntityAppearanceEntry3607:
    """
    Attributes:
        affected_deterministic_ids (list[str] | Unset):
        appearance (BTGraphicsAppearance1152 | Unset):
        bt_type (str | Unset): Type of JSON object.
        source (BTPartMetadataSource2895 | Unset):
    """

    affected_deterministic_ids: list[str] | Unset = UNSET
    appearance: BTGraphicsAppearance1152 | Unset = UNSET
    bt_type: str | Unset = UNSET
    source: BTPartMetadataSource2895 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.affected_deterministic_ids, Unset):
            affected_deterministic_ids = self.affected_deterministic_ids

        appearance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        bt_type = self.bt_type

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_deterministic_ids is not UNSET:
            field_dict["affectedDeterministicIds"] = affected_deterministic_ids
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
        from ..models.bt_part_metadata_source_2895 import BTPartMetadataSource2895

        d = dict(src_dict)
        affected_deterministic_ids = cast(list[str], d.pop("affectedDeterministicIds", UNSET))

        _appearance = d.pop("appearance", UNSET)
        appearance: BTGraphicsAppearance1152 | Unset
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = BTGraphicsAppearance1152.from_dict(_appearance)

        bt_type = d.pop("btType", UNSET)

        _source = d.pop("source", UNSET)
        source: BTPartMetadataSource2895 | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = BTPartMetadataSource2895.from_dict(_source)

        bt_base_entity_appearance_entry_3607 = cls(
            affected_deterministic_ids=affected_deterministic_ids,
            appearance=appearance,
            bt_type=bt_type,
            source=source,
        )

        bt_base_entity_appearance_entry_3607.additional_properties = d
        return bt_base_entity_appearance_entry_3607

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
