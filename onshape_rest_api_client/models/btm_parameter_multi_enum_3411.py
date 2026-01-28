from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_parameter_library_relation_type import GBTParameterLibraryRelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMParameterMultiEnum3411")


@_attrs_define
class BTMParameterMultiEnum3411:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        library_relation_type (GBTParameterLibraryRelationType | Unset):
        node_id (str | Unset): ID of the parameter's node.
        parameter_id (str | Unset): Unique ID of the parameter.
        parameter_name (str | Unset):
        value_string (str | Unset):
        enum_name (str | Unset):
        namespace (str | Unset):
        values (list[str] | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    library_relation_type: GBTParameterLibraryRelationType | Unset = UNSET
    node_id: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    parameter_name: str | Unset = UNSET
    value_string: str | Unset = UNSET
    enum_name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    values: list[str] | Unset = UNSET
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

        enum_name = self.enum_name

        namespace = self.namespace

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

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
        if enum_name is not UNSET:
            field_dict["enumName"] = enum_name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if values is not UNSET:
            field_dict["values"] = values

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

        enum_name = d.pop("enumName", UNSET)

        namespace = d.pop("namespace", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        btm_parameter_multi_enum_3411 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            library_relation_type=library_relation_type,
            node_id=node_id,
            parameter_id=parameter_id,
            parameter_name=parameter_name,
            value_string=value_string,
            enum_name=enum_name,
            namespace=namespace,
            values=values,
        )

        btm_parameter_multi_enum_3411.additional_properties = d
        return btm_parameter_multi_enum_3411

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
