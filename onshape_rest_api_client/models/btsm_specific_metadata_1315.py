from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_entity_type import GBTEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTSMSpecificMetadata1315")


@_attrs_define
class BTSMSpecificMetadata1315:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        definition_entity_type (GBTEntityType | Unset):
        is_sm_formed_outline (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    definition_entity_type: GBTEntityType | Unset = UNSET
    is_sm_formed_outline: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        definition_entity_type: str | Unset = UNSET
        if not isinstance(self.definition_entity_type, Unset):
            definition_entity_type = self.definition_entity_type.value

        is_sm_formed_outline = self.is_sm_formed_outline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if definition_entity_type is not UNSET:
            field_dict["definitionEntityType"] = definition_entity_type
        if is_sm_formed_outline is not UNSET:
            field_dict["isSMFormedOutline"] = is_sm_formed_outline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _definition_entity_type = d.pop("definitionEntityType", UNSET)
        definition_entity_type: GBTEntityType | Unset
        if isinstance(_definition_entity_type, Unset):
            definition_entity_type = UNSET
        else:
            definition_entity_type = GBTEntityType(_definition_entity_type)

        is_sm_formed_outline = d.pop("isSMFormedOutline", UNSET)

        btsm_specific_metadata_1315 = cls(
            bt_type=bt_type,
            definition_entity_type=definition_entity_type,
            is_sm_formed_outline=is_sm_formed_outline,
        )

        btsm_specific_metadata_1315.additional_properties = d
        return btsm_specific_metadata_1315

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
