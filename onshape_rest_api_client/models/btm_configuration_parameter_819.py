from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_configuration_parameter_type import GBTConfigurationParameterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_parameter_visibility_condition_177 import BTParameterVisibilityCondition177
    from ..models.bt_tree_node_20 import BTTreeNode20


T = TypeVar("T", bound="BTMConfigurationParameter819")


@_attrs_define
class BTMConfigurationParameter819:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        enum_option_ids (list[str] | Unset):
        generated_parameter_id (BTTreeNode20 | Unset):
        is_cosmetic (bool | Unset):
        parameter_id (str | Unset):
        parameter_name (str | Unset):
        parameter_type (GBTConfigurationParameterType | Unset):
        valid (bool | Unset):
        visibility_condition (BTParameterVisibilityCondition177 | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    enum_option_ids: list[str] | Unset = UNSET
    generated_parameter_id: BTTreeNode20 | Unset = UNSET
    is_cosmetic: bool | Unset = UNSET
    parameter_id: str | Unset = UNSET
    parameter_name: str | Unset = UNSET
    parameter_type: GBTConfigurationParameterType | Unset = UNSET
    valid: bool | Unset = UNSET
    visibility_condition: BTParameterVisibilityCondition177 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        enum_option_ids: list[str] | Unset = UNSET
        if not isinstance(self.enum_option_ids, Unset):
            enum_option_ids = self.enum_option_ids

        generated_parameter_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.generated_parameter_id, Unset):
            generated_parameter_id = self.generated_parameter_id.to_dict()

        is_cosmetic = self.is_cosmetic

        parameter_id = self.parameter_id

        parameter_name = self.parameter_name

        parameter_type: str | Unset = UNSET
        if not isinstance(self.parameter_type, Unset):
            parameter_type = self.parameter_type.value

        valid = self.valid

        visibility_condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_condition, Unset):
            visibility_condition = self.visibility_condition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if enum_option_ids is not UNSET:
            field_dict["enumOptionIds"] = enum_option_ids
        if generated_parameter_id is not UNSET:
            field_dict["generatedParameterId"] = generated_parameter_id
        if is_cosmetic is not UNSET:
            field_dict["isCosmetic"] = is_cosmetic
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if parameter_type is not UNSET:
            field_dict["parameterType"] = parameter_type
        if valid is not UNSET:
            field_dict["valid"] = valid
        if visibility_condition is not UNSET:
            field_dict["visibilityCondition"] = visibility_condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parameter_visibility_condition_177 import BTParameterVisibilityCondition177
        from ..models.bt_tree_node_20 import BTTreeNode20

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        enum_option_ids = cast(list[str], d.pop("enumOptionIds", UNSET))

        _generated_parameter_id = d.pop("generatedParameterId", UNSET)
        generated_parameter_id: BTTreeNode20 | Unset
        if isinstance(_generated_parameter_id, Unset):
            generated_parameter_id = UNSET
        else:
            generated_parameter_id = BTTreeNode20.from_dict(_generated_parameter_id)

        is_cosmetic = d.pop("isCosmetic", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        parameter_name = d.pop("parameterName", UNSET)

        _parameter_type = d.pop("parameterType", UNSET)
        parameter_type: GBTConfigurationParameterType | Unset
        if isinstance(_parameter_type, Unset):
            parameter_type = UNSET
        else:
            parameter_type = GBTConfigurationParameterType(_parameter_type)

        valid = d.pop("valid", UNSET)

        _visibility_condition = d.pop("visibilityCondition", UNSET)
        visibility_condition: BTParameterVisibilityCondition177 | Unset
        if isinstance(_visibility_condition, Unset):
            visibility_condition = UNSET
        else:
            visibility_condition = BTParameterVisibilityCondition177.from_dict(_visibility_condition)

        btm_configuration_parameter_819 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            enum_option_ids=enum_option_ids,
            generated_parameter_id=generated_parameter_id,
            is_cosmetic=is_cosmetic,
            parameter_id=parameter_id,
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            valid=valid,
            visibility_condition=visibility_condition,
        )

        btm_configuration_parameter_819.additional_properties = d
        return btm_configuration_parameter_819

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
