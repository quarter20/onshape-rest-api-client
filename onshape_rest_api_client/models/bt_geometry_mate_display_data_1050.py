from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_assembly_feature_display_status import GBTAssemblyFeatureDisplayStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
    from ..models.bt_occurrence_74 import BTOccurrence74


T = TypeVar("T", bound="BTGeometryMateDisplayData1050")


@_attrs_define
class BTGeometryMateDisplayData1050:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        hidden (bool | Unset):
        is_derived_feature (bool | Unset):
        node_id (str | Unset):
        owner_occurrence (BTOccurrence74 | Unset):
        status (GBTAssemblyFeatureDisplayStatus | Unset):
        first_deterministic_id (str | Unset):
        first_occurrence (BTOccurrence74 | Unset):
        location (BTCoordinateSystem387 | Unset):
        second_deterministic_id (str | Unset):
        second_occurrence (BTOccurrence74 | Unset):
    """

    bt_type: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    is_derived_feature: bool | Unset = UNSET
    node_id: str | Unset = UNSET
    owner_occurrence: BTOccurrence74 | Unset = UNSET
    status: GBTAssemblyFeatureDisplayStatus | Unset = UNSET
    first_deterministic_id: str | Unset = UNSET
    first_occurrence: BTOccurrence74 | Unset = UNSET
    location: BTCoordinateSystem387 | Unset = UNSET
    second_deterministic_id: str | Unset = UNSET
    second_occurrence: BTOccurrence74 | Unset = UNSET
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

        first_deterministic_id = self.first_deterministic_id

        first_occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_occurrence, Unset):
            first_occurrence = self.first_occurrence.to_dict()

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        second_deterministic_id = self.second_deterministic_id

        second_occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.second_occurrence, Unset):
            second_occurrence = self.second_occurrence.to_dict()

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
        if first_deterministic_id is not UNSET:
            field_dict["firstDeterministicId"] = first_deterministic_id
        if first_occurrence is not UNSET:
            field_dict["firstOccurrence"] = first_occurrence
        if location is not UNSET:
            field_dict["location"] = location
        if second_deterministic_id is not UNSET:
            field_dict["secondDeterministicId"] = second_deterministic_id
        if second_occurrence is not UNSET:
            field_dict["secondOccurrence"] = second_occurrence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
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

        first_deterministic_id = d.pop("firstDeterministicId", UNSET)

        _first_occurrence = d.pop("firstOccurrence", UNSET)
        first_occurrence: BTOccurrence74 | Unset
        if isinstance(_first_occurrence, Unset):
            first_occurrence = UNSET
        else:
            first_occurrence = BTOccurrence74.from_dict(_first_occurrence)

        _location = d.pop("location", UNSET)
        location: BTCoordinateSystem387 | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = BTCoordinateSystem387.from_dict(_location)

        second_deterministic_id = d.pop("secondDeterministicId", UNSET)

        _second_occurrence = d.pop("secondOccurrence", UNSET)
        second_occurrence: BTOccurrence74 | Unset
        if isinstance(_second_occurrence, Unset):
            second_occurrence = UNSET
        else:
            second_occurrence = BTOccurrence74.from_dict(_second_occurrence)

        bt_geometry_mate_display_data_1050 = cls(
            bt_type=bt_type,
            hidden=hidden,
            is_derived_feature=is_derived_feature,
            node_id=node_id,
            owner_occurrence=owner_occurrence,
            status=status,
            first_deterministic_id=first_deterministic_id,
            first_occurrence=first_occurrence,
            location=location,
            second_deterministic_id=second_deterministic_id,
            second_occurrence=second_occurrence,
        )

        bt_geometry_mate_display_data_1050.additional_properties = d
        return bt_geometry_mate_display_data_1050

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
