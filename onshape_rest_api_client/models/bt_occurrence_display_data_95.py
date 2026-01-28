from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_occurrence_data_75 import BTOccurrenceData75


T = TypeVar("T", bound="BTOccurrenceDisplayData95")


@_attrs_define
class BTOccurrenceDisplayData95:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        element_id (str | Unset):
        force_highest_quality_tessellation (bool | Unset):
        full_element_id (BTFullElementId756 | Unset):
        is_hidden (bool | Unset):
        is_pattern_descendant (bool | Unset):
        occurrence_data (BTOccurrenceData75 | Unset):
        part_ids (list[str] | Unset):
        sketch_feature_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    element_id: str | Unset = UNSET
    force_highest_quality_tessellation: bool | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    is_pattern_descendant: bool | Unset = UNSET
    occurrence_data: BTOccurrenceData75 | Unset = UNSET
    part_ids: list[str] | Unset = UNSET
    sketch_feature_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        element_id = self.element_id

        force_highest_quality_tessellation = self.force_highest_quality_tessellation

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        is_hidden = self.is_hidden

        is_pattern_descendant = self.is_pattern_descendant

        occurrence_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence_data, Unset):
            occurrence_data = self.occurrence_data.to_dict()

        part_ids: list[str] | Unset = UNSET
        if not isinstance(self.part_ids, Unset):
            part_ids = self.part_ids

        sketch_feature_id = self.sketch_feature_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if force_highest_quality_tessellation is not UNSET:
            field_dict["forceHighestQualityTessellation"] = force_highest_quality_tessellation
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if is_pattern_descendant is not UNSET:
            field_dict["isPatternDescendant"] = is_pattern_descendant
        if occurrence_data is not UNSET:
            field_dict["occurrenceData"] = occurrence_data
        if part_ids is not UNSET:
            field_dict["partIds"] = part_ids
        if sketch_feature_id is not UNSET:
            field_dict["sketchFeatureId"] = sketch_feature_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_occurrence_data_75 import BTOccurrenceData75

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        element_id = d.pop("elementId", UNSET)

        force_highest_quality_tessellation = d.pop("forceHighestQualityTessellation", UNSET)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        is_hidden = d.pop("isHidden", UNSET)

        is_pattern_descendant = d.pop("isPatternDescendant", UNSET)

        _occurrence_data = d.pop("occurrenceData", UNSET)
        occurrence_data: BTOccurrenceData75 | Unset
        if isinstance(_occurrence_data, Unset):
            occurrence_data = UNSET
        else:
            occurrence_data = BTOccurrenceData75.from_dict(_occurrence_data)

        part_ids = cast(list[str], d.pop("partIds", UNSET))

        sketch_feature_id = d.pop("sketchFeatureId", UNSET)

        bt_occurrence_display_data_95 = cls(
            bt_type=bt_type,
            element_id=element_id,
            force_highest_quality_tessellation=force_highest_quality_tessellation,
            full_element_id=full_element_id,
            is_hidden=is_hidden,
            is_pattern_descendant=is_pattern_descendant,
            occurrence_data=occurrence_data,
            part_ids=part_ids,
            sketch_feature_id=sketch_feature_id,
        )

        bt_occurrence_display_data_95.additional_properties = d
        return bt_occurrence_display_data_95

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
