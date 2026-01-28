from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTMConfiguredValueByEnum1923")


@_attrs_define
class BTMConfiguredValueByEnum1923:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Element microversion that is being imported.
        node_id (str | Unset):
        configuration_value_string (str | Unset):
        value (BTMParameter1 | Unset): A list of parameter values for instantiation of the feature spec. Parameters are
            present for all defined parameters, even if not used in a specific instantiation.
        enum_name (str | Unset):
        enum_value (str | Unset):
        namespace (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    configuration_value_string: str | Unset = UNSET
    value: BTMParameter1 | Unset = UNSET
    enum_name: str | Unset = UNSET
    enum_value: str | Unset = UNSET
    namespace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        configuration_value_string = self.configuration_value_string

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        enum_name = self.enum_name

        enum_value = self.enum_value

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if configuration_value_string is not UNSET:
            field_dict["configurationValueString"] = configuration_value_string
        if value is not UNSET:
            field_dict["value"] = value
        if enum_name is not UNSET:
            field_dict["enumName"] = enum_name
        if enum_value is not UNSET:
            field_dict["enumValue"] = enum_value
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_parameter_1 import BTMParameter1

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        configuration_value_string = d.pop("configurationValueString", UNSET)

        _value = d.pop("value", UNSET)
        value: BTMParameter1 | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTMParameter1.from_dict(_value)

        enum_name = d.pop("enumName", UNSET)

        enum_value = d.pop("enumValue", UNSET)

        namespace = d.pop("namespace", UNSET)

        btm_configured_value_by_enum_1923 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            configuration_value_string=configuration_value_string,
            value=value,
            enum_name=enum_name,
            enum_value=enum_value,
            namespace=namespace,
        )

        btm_configured_value_by_enum_1923.additional_properties = d
        return btm_configured_value_by_enum_1923

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
