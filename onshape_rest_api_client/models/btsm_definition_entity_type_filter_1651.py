from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_entity_type import GBTEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTSMDefinitionEntityTypeFilter1651")


@_attrs_define
class BTSMDefinitionEntityTypeFilter1651:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        sm_definition_entity_type (GBTEntityType | Unset):
    """

    bt_type: str | Unset = UNSET
    sm_definition_entity_type: GBTEntityType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        sm_definition_entity_type: str | Unset = UNSET
        if not isinstance(self.sm_definition_entity_type, Unset):
            sm_definition_entity_type = self.sm_definition_entity_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if sm_definition_entity_type is not UNSET:
            field_dict["smDefinitionEntityType"] = sm_definition_entity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _sm_definition_entity_type = d.pop("smDefinitionEntityType", UNSET)
        sm_definition_entity_type: GBTEntityType | Unset
        if isinstance(_sm_definition_entity_type, Unset):
            sm_definition_entity_type = UNSET
        else:
            sm_definition_entity_type = GBTEntityType(_sm_definition_entity_type)

        btsm_definition_entity_type_filter_1651 = cls(
            bt_type=bt_type,
            sm_definition_entity_type=sm_definition_entity_type,
        )

        btsm_definition_entity_type_filter_1651.additional_properties = d
        return btsm_definition_entity_type_filter_1651

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
