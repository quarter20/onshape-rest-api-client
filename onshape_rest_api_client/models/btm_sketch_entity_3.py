from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.combined_sketch_entity_type import CombinedSketchEntityType


T = TypeVar("T", bound="BTMSketchEntity3")


@_attrs_define
class BTMSketchEntity3:
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

        btm_sketch_entity_3 = cls(
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
        )

        btm_sketch_entity_3.additional_properties = d
        return btm_sketch_entity_3

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
