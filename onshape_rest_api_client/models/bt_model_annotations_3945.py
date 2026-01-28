from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_annotation_4664 import BTMAnnotation4664
    from ..models.btm_parameter_array_2025 import BTMParameterArray2025


T = TypeVar("T", bound="BTModelAnnotations3945")


@_attrs_define
class BTModelAnnotations3945:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        annotations (list[BTMAnnotation4664] | Unset):
        tolerance_schema_for_parts (BTMParameterArray2025 | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    annotations: list[BTMAnnotation4664] | Unset = UNSET
    tolerance_schema_for_parts: BTMParameterArray2025 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        tolerance_schema_for_parts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tolerance_schema_for_parts, Unset):
            tolerance_schema_for_parts = self.tolerance_schema_for_parts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if tolerance_schema_for_parts is not UNSET:
            field_dict["toleranceSchemaForParts"] = tolerance_schema_for_parts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_annotation_4664 import BTMAnnotation4664
        from ..models.btm_parameter_array_2025 import BTMParameterArray2025

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _annotations = d.pop("annotations", UNSET)
        annotations: list[BTMAnnotation4664] | Unset = UNSET
        if _annotations is not UNSET:
            annotations = []
            for annotations_item_data in _annotations:
                annotations_item = BTMAnnotation4664.from_dict(annotations_item_data)

                annotations.append(annotations_item)

        _tolerance_schema_for_parts = d.pop("toleranceSchemaForParts", UNSET)
        tolerance_schema_for_parts: BTMParameterArray2025 | Unset
        if isinstance(_tolerance_schema_for_parts, Unset):
            tolerance_schema_for_parts = UNSET
        else:
            tolerance_schema_for_parts = BTMParameterArray2025.from_dict(_tolerance_schema_for_parts)

        bt_model_annotations_3945 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            annotations=annotations,
            tolerance_schema_for_parts=tolerance_schema_for_parts,
        )

        bt_model_annotations_3945.additional_properties = d
        return bt_model_annotations_3945

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
