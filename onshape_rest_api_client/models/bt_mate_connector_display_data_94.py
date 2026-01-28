from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
    from ..models.bt_occurrence_74 import BTOccurrence74


T = TypeVar("T", bound="BTMateConnectorDisplayData94")


@_attrs_define
class BTMateConnectorDisplayData94:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        element_id (str | Unset):
        entity_ids (list[str] | Unset):
        hidden (bool | Unset):
        implicit (bool | Unset):
        is_derived_feature (bool | Unset):
        location (BTCoordinateSystem387 | Unset):
        node_id (str | Unset):
        occurrence (BTOccurrence74 | Unset):
        owner_occurrence (BTOccurrence74 | Unset):
        part_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    element_id: str | Unset = UNSET
    entity_ids: list[str] | Unset = UNSET
    hidden: bool | Unset = UNSET
    implicit: bool | Unset = UNSET
    is_derived_feature: bool | Unset = UNSET
    location: BTCoordinateSystem387 | Unset = UNSET
    node_id: str | Unset = UNSET
    occurrence: BTOccurrence74 | Unset = UNSET
    owner_occurrence: BTOccurrence74 | Unset = UNSET
    part_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        element_id = self.element_id

        entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids

        hidden = self.hidden

        implicit = self.implicit

        is_derived_feature = self.is_derived_feature

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        node_id = self.node_id

        occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

        owner_occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner_occurrence, Unset):
            owner_occurrence = self.owner_occurrence.to_dict()

        part_id = self.part_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if entity_ids is not UNSET:
            field_dict["entityIds"] = entity_ids
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if is_derived_feature is not UNSET:
            field_dict["isDerivedFeature"] = is_derived_feature
        if location is not UNSET:
            field_dict["location"] = location
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence
        if owner_occurrence is not UNSET:
            field_dict["ownerOccurrence"] = owner_occurrence
        if part_id is not UNSET:
            field_dict["partId"] = part_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
        from ..models.bt_occurrence_74 import BTOccurrence74

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        element_id = d.pop("elementId", UNSET)

        entity_ids = cast(list[str], d.pop("entityIds", UNSET))

        hidden = d.pop("hidden", UNSET)

        implicit = d.pop("implicit", UNSET)

        is_derived_feature = d.pop("isDerivedFeature", UNSET)

        _location = d.pop("location", UNSET)
        location: BTCoordinateSystem387 | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = BTCoordinateSystem387.from_dict(_location)

        node_id = d.pop("nodeId", UNSET)

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: BTOccurrence74 | Unset
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = BTOccurrence74.from_dict(_occurrence)

        _owner_occurrence = d.pop("ownerOccurrence", UNSET)
        owner_occurrence: BTOccurrence74 | Unset
        if isinstance(_owner_occurrence, Unset):
            owner_occurrence = UNSET
        else:
            owner_occurrence = BTOccurrence74.from_dict(_owner_occurrence)

        part_id = d.pop("partId", UNSET)

        bt_mate_connector_display_data_94 = cls(
            bt_type=bt_type,
            element_id=element_id,
            entity_ids=entity_ids,
            hidden=hidden,
            implicit=implicit,
            is_derived_feature=is_derived_feature,
            location=location,
            node_id=node_id,
            occurrence=occurrence,
            owner_occurrence=owner_occurrence,
            part_id=part_id,
        )

        bt_mate_connector_display_data_94.additional_properties = d
        return bt_mate_connector_display_data_94

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
