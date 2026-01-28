from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_assembly_feature_display_status import GBTAssemblyFeatureDisplayStatus
from ..models.gbt_load_type import GBTLoadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_occurrence_74 import BTOccurrence74
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTLoadDisplayData837")


@_attrs_define
class BTLoadDisplayData837:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        hidden (bool | Unset):
        is_derived_feature (bool | Unset):
        node_id (str | Unset):
        owner_occurrence (BTOccurrence74 | Unset):
        status (GBTAssemblyFeatureDisplayStatus | Unset):
        component_values (BTVector3D389 | Unset):
        direction_mate_connector_id (str | Unset):
        face_load_deterministic_ids (list[str] | Unset):
        is_direction_flipped (bool | Unset):
        load_type (GBTLoadType | Unset):
        occurrence (BTOccurrence74 | Unset):
    """

    bt_type: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    is_derived_feature: bool | Unset = UNSET
    node_id: str | Unset = UNSET
    owner_occurrence: BTOccurrence74 | Unset = UNSET
    status: GBTAssemblyFeatureDisplayStatus | Unset = UNSET
    component_values: BTVector3D389 | Unset = UNSET
    direction_mate_connector_id: str | Unset = UNSET
    face_load_deterministic_ids: list[str] | Unset = UNSET
    is_direction_flipped: bool | Unset = UNSET
    load_type: GBTLoadType | Unset = UNSET
    occurrence: BTOccurrence74 | Unset = UNSET
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

        component_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component_values, Unset):
            component_values = self.component_values.to_dict()

        direction_mate_connector_id = self.direction_mate_connector_id

        face_load_deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.face_load_deterministic_ids, Unset):
            face_load_deterministic_ids = self.face_load_deterministic_ids

        is_direction_flipped = self.is_direction_flipped

        load_type: str | Unset = UNSET
        if not isinstance(self.load_type, Unset):
            load_type = self.load_type.value

        occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

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
        if component_values is not UNSET:
            field_dict["componentValues"] = component_values
        if direction_mate_connector_id is not UNSET:
            field_dict["directionMateConnectorId"] = direction_mate_connector_id
        if face_load_deterministic_ids is not UNSET:
            field_dict["faceLoadDeterministicIds"] = face_load_deterministic_ids
        if is_direction_flipped is not UNSET:
            field_dict["isDirectionFlipped"] = is_direction_flipped
        if load_type is not UNSET:
            field_dict["loadType"] = load_type
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_occurrence_74 import BTOccurrence74
        from ..models.bt_vector_3d389 import BTVector3D389

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

        _component_values = d.pop("componentValues", UNSET)
        component_values: BTVector3D389 | Unset
        if isinstance(_component_values, Unset):
            component_values = UNSET
        else:
            component_values = BTVector3D389.from_dict(_component_values)

        direction_mate_connector_id = d.pop("directionMateConnectorId", UNSET)

        face_load_deterministic_ids = cast(list[str], d.pop("faceLoadDeterministicIds", UNSET))

        is_direction_flipped = d.pop("isDirectionFlipped", UNSET)

        _load_type = d.pop("loadType", UNSET)
        load_type: GBTLoadType | Unset
        if isinstance(_load_type, Unset):
            load_type = UNSET
        else:
            load_type = GBTLoadType(_load_type)

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: BTOccurrence74 | Unset
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = BTOccurrence74.from_dict(_occurrence)

        bt_load_display_data_837 = cls(
            bt_type=bt_type,
            hidden=hidden,
            is_derived_feature=is_derived_feature,
            node_id=node_id,
            owner_occurrence=owner_occurrence,
            status=status,
            component_values=component_values,
            direction_mate_connector_id=direction_mate_connector_id,
            face_load_deterministic_ids=face_load_deterministic_ids,
            is_direction_flipped=is_direction_flipped,
            load_type=load_type,
            occurrence=occurrence,
        )

        bt_load_display_data_837.additional_properties = d
        return bt_load_display_data_837

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
