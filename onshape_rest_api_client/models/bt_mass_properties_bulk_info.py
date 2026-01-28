from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_mass_properties_bulk_info_bodies import BTMassPropertiesBulkInfoBodies


T = TypeVar("T", bound="BTMassPropertiesBulkInfo")


@_attrs_define
class BTMassPropertiesBulkInfo:
    """
    Attributes:
        bodies (BTMassPropertiesBulkInfoBodies | Unset):
        microversion_id (str | Unset):
    """

    bodies: BTMassPropertiesBulkInfoBodies | Unset = UNSET
    microversion_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bodies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bodies, Unset):
            bodies = self.bodies.to_dict()

        microversion_id = self.microversion_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bodies is not UNSET:
            field_dict["bodies"] = bodies
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_mass_properties_bulk_info_bodies import BTMassPropertiesBulkInfoBodies

        d = dict(src_dict)
        _bodies = d.pop("bodies", UNSET)
        bodies: BTMassPropertiesBulkInfoBodies | Unset
        if isinstance(_bodies, Unset):
            bodies = UNSET
        else:
            bodies = BTMassPropertiesBulkInfoBodies.from_dict(_bodies)

        microversion_id = d.pop("microversionId", UNSET)

        bt_mass_properties_bulk_info = cls(
            bodies=bodies,
            microversion_id=microversion_id,
        )

        bt_mass_properties_bulk_info.additional_properties = d
        return bt_mass_properties_bulk_info

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
