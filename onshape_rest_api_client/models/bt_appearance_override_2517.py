from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152


T = TypeVar("T", bound="BTAppearanceOverride2517")


@_attrs_define
class BTAppearanceOverride2517:
    """
    Attributes:
        appearance (BTGraphicsAppearance1152 | Unset):
        appearance_reset (bool | Unset):
        bt_type (str | Unset): Type of JSON object.
        copy_without_entities (BTAppearanceOverride2517 | Unset):
        entity_deterministic_ids (list[str] | Unset):
        is_deletion (bool | Unset):
    """

    appearance: BTGraphicsAppearance1152 | Unset = UNSET
    appearance_reset: bool | Unset = UNSET
    bt_type: str | Unset = UNSET
    copy_without_entities: BTAppearanceOverride2517 | Unset = UNSET
    entity_deterministic_ids: list[str] | Unset = UNSET
    is_deletion: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appearance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        appearance_reset = self.appearance_reset

        bt_type = self.bt_type

        copy_without_entities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy_without_entities, Unset):
            copy_without_entities = self.copy_without_entities.to_dict()

        entity_deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.entity_deterministic_ids, Unset):
            entity_deterministic_ids = self.entity_deterministic_ids

        is_deletion = self.is_deletion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if appearance_reset is not UNSET:
            field_dict["appearanceReset"] = appearance_reset
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if copy_without_entities is not UNSET:
            field_dict["copyWithoutEntities"] = copy_without_entities
        if entity_deterministic_ids is not UNSET:
            field_dict["entityDeterministicIds"] = entity_deterministic_ids
        if is_deletion is not UNSET:
            field_dict["isDeletion"] = is_deletion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152

        d = dict(src_dict)
        _appearance = d.pop("appearance", UNSET)
        appearance: BTGraphicsAppearance1152 | Unset
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = BTGraphicsAppearance1152.from_dict(_appearance)

        appearance_reset = d.pop("appearanceReset", UNSET)

        bt_type = d.pop("btType", UNSET)

        _copy_without_entities = d.pop("copyWithoutEntities", UNSET)
        copy_without_entities: BTAppearanceOverride2517 | Unset
        if isinstance(_copy_without_entities, Unset):
            copy_without_entities = UNSET
        else:
            copy_without_entities = BTAppearanceOverride2517.from_dict(_copy_without_entities)

        entity_deterministic_ids = cast(list[str], d.pop("entityDeterministicIds", UNSET))

        is_deletion = d.pop("isDeletion", UNSET)

        bt_appearance_override_2517 = cls(
            appearance=appearance,
            appearance_reset=appearance_reset,
            bt_type=bt_type,
            copy_without_entities=copy_without_entities,
            entity_deterministic_ids=entity_deterministic_ids,
            is_deletion=is_deletion,
        )

        bt_appearance_override_2517.additional_properties = d
        return bt_appearance_override_2517

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
