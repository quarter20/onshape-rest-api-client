from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_assembly_feature_display_status import GBTAssemblyFeatureDisplayStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_occurrence_74 import BTOccurrence74


T = TypeVar("T", bound="BTRigidFeatureDisplayData1595")


@_attrs_define
class BTRigidFeatureDisplayData1595:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        hidden (bool | Unset):
        is_derived_feature (bool | Unset):
        node_id (str | Unset):
        owner_occurrence (BTOccurrence74 | Unset):
        status (GBTAssemblyFeatureDisplayStatus | Unset):
        occurrences (list[BTOccurrence74] | Unset):
    """

    bt_type: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    is_derived_feature: bool | Unset = UNSET
    node_id: str | Unset = UNSET
    owner_occurrence: BTOccurrence74 | Unset = UNSET
    status: GBTAssemblyFeatureDisplayStatus | Unset = UNSET
    occurrences: list[BTOccurrence74] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        hidden = self.hidden

        is_derived_feature = self.is_derived_feature

        node_id = self.node_id

        owner_occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner_occurrence, Unset):
            owner_occurrence = self.owner_occurrence.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        occurrences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occurrences, Unset):
            occurrences = []
            for occurrences_item_data in self.occurrences:
                occurrences_item = occurrences_item_data.to_dict()
                occurrences.append(occurrences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if is_derived_feature is not UNSET:
            field_dict["isDerivedFeature"] = is_derived_feature
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if owner_occurrence is not UNSET:
            field_dict["ownerOccurrence"] = owner_occurrence
        if status is not UNSET:
            field_dict["status"] = status
        if occurrences is not UNSET:
            field_dict["occurrences"] = occurrences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_occurrence_74 import BTOccurrence74

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        hidden = d.pop("hidden", UNSET)

        is_derived_feature = d.pop("isDerivedFeature", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _owner_occurrence = d.pop("ownerOccurrence", UNSET)
        owner_occurrence: BTOccurrence74 | Unset
        if isinstance(_owner_occurrence, Unset):
            owner_occurrence = UNSET
        else:
            owner_occurrence = BTOccurrence74.from_dict(_owner_occurrence)

        _status = d.pop("status", UNSET)
        status: GBTAssemblyFeatureDisplayStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GBTAssemblyFeatureDisplayStatus(_status)

        _occurrences = d.pop("occurrences", UNSET)
        occurrences: list[BTOccurrence74] | Unset = UNSET
        if _occurrences is not UNSET:
            occurrences = []
            for occurrences_item_data in _occurrences:
                occurrences_item = BTOccurrence74.from_dict(occurrences_item_data)

                occurrences.append(occurrences_item)

        bt_rigid_feature_display_data_1595 = cls(
            bt_type=bt_type,
            hidden=hidden,
            is_derived_feature=is_derived_feature,
            node_id=node_id,
            owner_occurrence=owner_occurrence,
            status=status,
            occurrences=occurrences,
        )

        bt_rigid_feature_display_data_1595.additional_properties = d
        return bt_rigid_feature_display_data_1595

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
