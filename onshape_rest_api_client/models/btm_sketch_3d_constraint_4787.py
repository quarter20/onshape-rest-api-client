from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_constraint_type import GBTConstraintType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTMSketch3DConstraint4787")


@_attrs_define
class BTMSketch3DConstraint4787:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        entity_id (str | Unset):
        parameters (list[BTMParameter1] | Unset):
        constraint_type (GBTConstraintType | Unset):
        help_parameters (list[float] | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    entity_id: str | Unset = UNSET
    parameters: list[BTMParameter1] | Unset = UNSET
    constraint_type: GBTConstraintType | Unset = UNSET
    help_parameters: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        entity_id = self.entity_id

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        constraint_type: str | Unset = UNSET
        if not isinstance(self.constraint_type, Unset):
            constraint_type = self.constraint_type.value

        help_parameters: list[float] | Unset = UNSET
        if not isinstance(self.help_parameters, Unset):
            help_parameters = self.help_parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if constraint_type is not UNSET:
            field_dict["constraintType"] = constraint_type
        if help_parameters is not UNSET:
            field_dict["helpParameters"] = help_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_parameter_1 import BTMParameter1  # noqa: PLC0415

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        entity_id = d.pop("entityId", UNSET)

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

        help_parameters = cast(list[float], d.pop("helpParameters", UNSET))

        btm_sketch_3d_constraint_4787 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            entity_id=entity_id,
            parameters=parameters,
            constraint_type=constraint_type,
            help_parameters=help_parameters,
        )

        btm_sketch_3d_constraint_4787.additional_properties = d
        return btm_sketch_3d_constraint_4787

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
