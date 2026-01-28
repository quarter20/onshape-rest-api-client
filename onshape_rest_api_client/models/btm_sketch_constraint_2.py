from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_constraint_type import GBTConstraintType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.combined_sketch_entity_type import CombinedSketchEntityType


T = TypeVar("T", bound="BTMSketchConstraint2")


@_attrs_define
class BTMSketchConstraint2:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Element microversion that is being imported.
        node_id (str | Unset):
        combined_sketch_entity_type (CombinedSketchEntityType | Unset):
        entity_id (str | Unset):
        entity_id_and_replace_in_dependent_fields (str | Unset):
        index (int | Unset):
        name (str | Unset):
        namespace (str | Unset):
        parameters (list[BTMParameter1] | Unset):
        constraint_type (GBTConstraintType | Unset):
        driven_dimension (bool | Unset):
        has_offset_data_1 (bool | Unset):
        has_offset_data_2 (bool | Unset):
        has_pierce_parameter (bool | Unset):
        help_parameters (list[float] | Unset):
        offset_distance_1 (float | Unset):
        offset_distance_2 (float | Unset):
        offset_orientation_1 (bool | Unset):
        offset_orientation_2 (bool | Unset):
        pierce_parameter (float | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    combined_sketch_entity_type: CombinedSketchEntityType | Unset = UNSET
    entity_id: str | Unset = UNSET
    entity_id_and_replace_in_dependent_fields: str | Unset = UNSET
    index: int | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    parameters: list[BTMParameter1] | Unset = UNSET
    constraint_type: GBTConstraintType | Unset = UNSET
    driven_dimension: bool | Unset = UNSET
    has_offset_data_1: bool | Unset = UNSET
    has_offset_data_2: bool | Unset = UNSET
    has_pierce_parameter: bool | Unset = UNSET
    help_parameters: list[float] | Unset = UNSET
    offset_distance_1: float | Unset = UNSET
    offset_distance_2: float | Unset = UNSET
    offset_orientation_1: bool | Unset = UNSET
    offset_orientation_2: bool | Unset = UNSET
    pierce_parameter: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        combined_sketch_entity_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.combined_sketch_entity_type, Unset):
            combined_sketch_entity_type = self.combined_sketch_entity_type.to_dict()

        entity_id = self.entity_id

        entity_id_and_replace_in_dependent_fields = self.entity_id_and_replace_in_dependent_fields

        index = self.index

        name = self.name

        namespace = self.namespace

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        constraint_type: str | Unset = UNSET
        if not isinstance(self.constraint_type, Unset):
            constraint_type = self.constraint_type.value

        driven_dimension = self.driven_dimension

        has_offset_data_1 = self.has_offset_data_1

        has_offset_data_2 = self.has_offset_data_2

        has_pierce_parameter = self.has_pierce_parameter

        help_parameters: list[float] | Unset = UNSET
        if not isinstance(self.help_parameters, Unset):
            help_parameters = self.help_parameters

        offset_distance_1 = self.offset_distance_1

        offset_distance_2 = self.offset_distance_2

        offset_orientation_1 = self.offset_orientation_1

        offset_orientation_2 = self.offset_orientation_2

        pierce_parameter = self.pierce_parameter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if combined_sketch_entity_type is not UNSET:
            field_dict["combinedSketchEntityType"] = combined_sketch_entity_type
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_id_and_replace_in_dependent_fields is not UNSET:
            field_dict["entityIdAndReplaceInDependentFields"] = entity_id_and_replace_in_dependent_fields
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if constraint_type is not UNSET:
            field_dict["constraintType"] = constraint_type
        if driven_dimension is not UNSET:
            field_dict["drivenDimension"] = driven_dimension
        if has_offset_data_1 is not UNSET:
            field_dict["hasOffsetData1"] = has_offset_data_1
        if has_offset_data_2 is not UNSET:
            field_dict["hasOffsetData2"] = has_offset_data_2
        if has_pierce_parameter is not UNSET:
            field_dict["hasPierceParameter"] = has_pierce_parameter
        if help_parameters is not UNSET:
            field_dict["helpParameters"] = help_parameters
        if offset_distance_1 is not UNSET:
            field_dict["offsetDistance1"] = offset_distance_1
        if offset_distance_2 is not UNSET:
            field_dict["offsetDistance2"] = offset_distance_2
        if offset_orientation_1 is not UNSET:
            field_dict["offsetOrientation1"] = offset_orientation_1
        if offset_orientation_2 is not UNSET:
            field_dict["offsetOrientation2"] = offset_orientation_2
        if pierce_parameter is not UNSET:
            field_dict["pierceParameter"] = pierce_parameter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_parameter_1 import BTMParameter1
        from ..models.combined_sketch_entity_type import CombinedSketchEntityType

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _combined_sketch_entity_type = d.pop("combinedSketchEntityType", UNSET)
        combined_sketch_entity_type: CombinedSketchEntityType | Unset
        if isinstance(_combined_sketch_entity_type, Unset):
            combined_sketch_entity_type = UNSET
        else:
            combined_sketch_entity_type = CombinedSketchEntityType.from_dict(_combined_sketch_entity_type)

        entity_id = d.pop("entityId", UNSET)

        entity_id_and_replace_in_dependent_fields = d.pop("entityIdAndReplaceInDependentFields", UNSET)

        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[BTMParameter1] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = BTMParameter1.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        _constraint_type = d.pop("constraintType", UNSET)
        constraint_type: GBTConstraintType | Unset
        if isinstance(_constraint_type, Unset):
            constraint_type = UNSET
        else:
            constraint_type = GBTConstraintType(_constraint_type)

        driven_dimension = d.pop("drivenDimension", UNSET)

        has_offset_data_1 = d.pop("hasOffsetData1", UNSET)

        has_offset_data_2 = d.pop("hasOffsetData2", UNSET)

        has_pierce_parameter = d.pop("hasPierceParameter", UNSET)

        help_parameters = cast(list[float], d.pop("helpParameters", UNSET))

        offset_distance_1 = d.pop("offsetDistance1", UNSET)

        offset_distance_2 = d.pop("offsetDistance2", UNSET)

        offset_orientation_1 = d.pop("offsetOrientation1", UNSET)

        offset_orientation_2 = d.pop("offsetOrientation2", UNSET)

        pierce_parameter = d.pop("pierceParameter", UNSET)

        btm_sketch_constraint_2 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            combined_sketch_entity_type=combined_sketch_entity_type,
            entity_id=entity_id,
            entity_id_and_replace_in_dependent_fields=entity_id_and_replace_in_dependent_fields,
            index=index,
            name=name,
            namespace=namespace,
            parameters=parameters,
            constraint_type=constraint_type,
            driven_dimension=driven_dimension,
            has_offset_data_1=has_offset_data_1,
            has_offset_data_2=has_offset_data_2,
            has_pierce_parameter=has_pierce_parameter,
            help_parameters=help_parameters,
            offset_distance_1=offset_distance_1,
            offset_distance_2=offset_distance_2,
            offset_orientation_1=offset_orientation_1,
            offset_orientation_2=offset_orientation_2,
            pierce_parameter=pierce_parameter,
        )

        btm_sketch_constraint_2.additional_properties = d
        return btm_sketch_constraint_2

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
