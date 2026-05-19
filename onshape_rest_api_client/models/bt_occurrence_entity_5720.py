from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_occurrence_74 import BTOccurrence74


T = TypeVar("T", bound="BTOccurrenceEntity5720")


@_attrs_define
class BTOccurrenceEntity5720:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        deterministic_id (str | Unset):
        occurrence (BTOccurrence74 | Unset):
    """

    bt_type: str | Unset = UNSET
    deterministic_id: str | Unset = UNSET
    occurrence: BTOccurrence74 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        deterministic_id = self.deterministic_id

        occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if deterministic_id is not UNSET:
            field_dict["deterministicId"] = deterministic_id
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_occurrence_74 import BTOccurrence74

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        deterministic_id = d.pop("deterministicId", UNSET)

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: BTOccurrence74 | Unset
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = BTOccurrence74.from_dict(_occurrence)

        bt_occurrence_entity_5720 = cls(
            bt_type=bt_type,
            deterministic_id=deterministic_id,
            occurrence=occurrence,
        )

        bt_occurrence_entity_5720.additional_properties = d
        return bt_occurrence_entity_5720

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
