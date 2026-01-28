from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_parameter_library_relation_type import GBTParameterLibraryRelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMParameterNullableQuantity807")


@_attrs_define
class BTMParameterNullableQuantity807:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        library_relation_type (GBTParameterLibraryRelationType | Unset):
        node_id (str | Unset): ID of the parameter's node.
        parameter_id (str | Unset): Unique ID of the parameter.
        parameter_name (str | Unset):
        value_string (str | Unset):
        expression (str | Unset):
        is_integer (bool | Unset):
        units (str | Unset):
        value (float | Unset):
        is_null (bool | Unset):
        null_value (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    library_relation_type: GBTParameterLibraryRelationType | Unset = UNSET
    node_id: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    parameter_name: str | Unset = UNSET
    value_string: str | Unset = UNSET
    expression: str | Unset = UNSET
    is_integer: bool | Unset = UNSET
    units: str | Unset = UNSET
    value: float | Unset = UNSET
    is_null: bool | Unset = UNSET
    null_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        library_relation_type: str | Unset = UNSET
        if not isinstance(self.library_relation_type, Unset):
            library_relation_type = self.library_relation_type.value

        node_id = self.node_id

        parameter_id = self.parameter_id

        parameter_name = self.parameter_name

        value_string = self.value_string

        expression = self.expression

        is_integer = self.is_integer

        units = self.units

        value = self.value

        is_null = self.is_null

        null_value = self.null_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if library_relation_type is not UNSET:
            field_dict["libraryRelationType"] = library_relation_type
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if value_string is not UNSET:
            field_dict["valueString"] = value_string
        if expression is not UNSET:
            field_dict["expression"] = expression
        if is_integer is not UNSET:
            field_dict["isInteger"] = is_integer
        if units is not UNSET:
            field_dict["units"] = units
        if value is not UNSET:
            field_dict["value"] = value
        if is_null is not UNSET:
            field_dict["isNull"] = is_null
        if null_value is not UNSET:
            field_dict["nullValue"] = null_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        _library_relation_type = d.pop("libraryRelationType", UNSET)
        library_relation_type: GBTParameterLibraryRelationType | Unset
        if isinstance(_library_relation_type, Unset):
            library_relation_type = UNSET
        else:
            library_relation_type = GBTParameterLibraryRelationType(_library_relation_type)

        node_id = d.pop("nodeId", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        parameter_name = d.pop("parameterName", UNSET)

        value_string = d.pop("valueString", UNSET)

        expression = d.pop("expression", UNSET)

        is_integer = d.pop("isInteger", UNSET)

        units = d.pop("units", UNSET)

        value = d.pop("value", UNSET)

        is_null = d.pop("isNull", UNSET)

        null_value = d.pop("nullValue", UNSET)

        btm_parameter_nullable_quantity_807 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            library_relation_type=library_relation_type,
            node_id=node_id,
            parameter_id=parameter_id,
            parameter_name=parameter_name,
            value_string=value_string,
            expression=expression,
            is_integer=is_integer,
            units=units,
            value=value,
            is_null=is_null,
            null_value=null_value,
        )

        btm_parameter_nullable_quantity_807.additional_properties = d
        return btm_parameter_nullable_quantity_807

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
