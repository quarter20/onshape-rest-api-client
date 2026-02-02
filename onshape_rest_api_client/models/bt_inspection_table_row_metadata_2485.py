from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_annotation_type import GBTAnnotationType
from ..models.gbt_tolerance_precision import GBTTolerancePrecision
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_base_cross_highlight_data_2609 import BTTableBaseCrossHighlightData2609
    from ..models.bt_table_cross_highlight_data_1753 import BTTableCrossHighlightData1753


T = TypeVar("T", bound="BTInspectionTableRowMetadata2485")


@_attrs_define
class BTInspectionTableRowMetadata2485:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        cross_highlight_data_if_any (BTTableBaseCrossHighlightData2609 | Unset):
        annotation_id (str | Unset):
        annotation_type (GBTAnnotationType | Unset):
        chamfer_callout_id (str | Unset):
        constraint_id (str | Unset):
        cross_highlight_data (BTTableCrossHighlightData1753 | Unset):
        feature_id (str | Unset):
        has_default_tolerances (bool | Unset):
        hole_callout_id (str | Unset):
        is_derived (bool | Unset):
        parameter_id (str | Unset):
        part_id (str | Unset):
        precision (GBTTolerancePrecision | Unset):
    """

    bt_type: str | Unset = UNSET
    cross_highlight_data_if_any: BTTableBaseCrossHighlightData2609 | Unset = UNSET
    annotation_id: str | Unset = UNSET
    annotation_type: GBTAnnotationType | Unset = UNSET
    chamfer_callout_id: str | Unset = UNSET
    constraint_id: str | Unset = UNSET
    cross_highlight_data: BTTableCrossHighlightData1753 | Unset = UNSET
    feature_id: str | Unset = UNSET
    has_default_tolerances: bool | Unset = UNSET
    hole_callout_id: str | Unset = UNSET
    is_derived: bool | Unset = UNSET
    parameter_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    precision: GBTTolerancePrecision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        cross_highlight_data_if_any: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data_if_any, Unset):
            cross_highlight_data_if_any = self.cross_highlight_data_if_any.to_dict()

        annotation_id = self.annotation_id

        annotation_type: str | Unset = UNSET
        if not isinstance(self.annotation_type, Unset):
            annotation_type = self.annotation_type.value

        chamfer_callout_id = self.chamfer_callout_id

        constraint_id = self.constraint_id

        cross_highlight_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data, Unset):
            cross_highlight_data = self.cross_highlight_data.to_dict()

        feature_id = self.feature_id

        has_default_tolerances = self.has_default_tolerances

        hole_callout_id = self.hole_callout_id

        is_derived = self.is_derived

        parameter_id = self.parameter_id

        part_id = self.part_id

        precision: str | Unset = UNSET
        if not isinstance(self.precision, Unset):
            precision = self.precision.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cross_highlight_data_if_any is not UNSET:
            field_dict["crossHighlightDataIfAny"] = cross_highlight_data_if_any
        if annotation_id is not UNSET:
            field_dict["annotationId"] = annotation_id
        if annotation_type is not UNSET:
            field_dict["annotationType"] = annotation_type
        if chamfer_callout_id is not UNSET:
            field_dict["chamferCalloutId"] = chamfer_callout_id
        if constraint_id is not UNSET:
            field_dict["constraintId"] = constraint_id
        if cross_highlight_data is not UNSET:
            field_dict["crossHighlightData"] = cross_highlight_data
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if has_default_tolerances is not UNSET:
            field_dict["hasDefaultTolerances"] = has_default_tolerances
        if hole_callout_id is not UNSET:
            field_dict["holeCalloutId"] = hole_callout_id
        if is_derived is not UNSET:
            field_dict["isDerived"] = is_derived
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if precision is not UNSET:
            field_dict["precision"] = precision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_base_cross_highlight_data_2609 import BTTableBaseCrossHighlightData2609
        from ..models.bt_table_cross_highlight_data_1753 import BTTableCrossHighlightData1753

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _cross_highlight_data_if_any = d.pop("crossHighlightDataIfAny", UNSET)
        cross_highlight_data_if_any: BTTableBaseCrossHighlightData2609 | Unset
        if isinstance(_cross_highlight_data_if_any, Unset):
            cross_highlight_data_if_any = UNSET
        else:
            cross_highlight_data_if_any = BTTableBaseCrossHighlightData2609.from_dict(_cross_highlight_data_if_any)

        annotation_id = d.pop("annotationId", UNSET)

        _annotation_type = d.pop("annotationType", UNSET)
        annotation_type: GBTAnnotationType | Unset
        if isinstance(_annotation_type, Unset):
            annotation_type = UNSET
        else:
            annotation_type = GBTAnnotationType(_annotation_type)

        chamfer_callout_id = d.pop("chamferCalloutId", UNSET)

        constraint_id = d.pop("constraintId", UNSET)

        _cross_highlight_data = d.pop("crossHighlightData", UNSET)
        cross_highlight_data: BTTableCrossHighlightData1753 | Unset
        if isinstance(_cross_highlight_data, Unset):
            cross_highlight_data = UNSET
        else:
            cross_highlight_data = BTTableCrossHighlightData1753.from_dict(_cross_highlight_data)

        feature_id = d.pop("featureId", UNSET)

        has_default_tolerances = d.pop("hasDefaultTolerances", UNSET)

        hole_callout_id = d.pop("holeCalloutId", UNSET)

        is_derived = d.pop("isDerived", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        part_id = d.pop("partId", UNSET)

        _precision = d.pop("precision", UNSET)
        precision: GBTTolerancePrecision | Unset
        if isinstance(_precision, Unset):
            precision = UNSET
        else:
            precision = GBTTolerancePrecision(_precision)

        bt_inspection_table_row_metadata_2485 = cls(
            bt_type=bt_type,
            cross_highlight_data_if_any=cross_highlight_data_if_any,
            annotation_id=annotation_id,
            annotation_type=annotation_type,
            chamfer_callout_id=chamfer_callout_id,
            constraint_id=constraint_id,
            cross_highlight_data=cross_highlight_data,
            feature_id=feature_id,
            has_default_tolerances=has_default_tolerances,
            hole_callout_id=hole_callout_id,
            is_derived=is_derived,
            parameter_id=parameter_id,
            part_id=part_id,
            precision=precision,
        )

        bt_inspection_table_row_metadata_2485.additional_properties = d
        return bt_inspection_table_row_metadata_2485

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
