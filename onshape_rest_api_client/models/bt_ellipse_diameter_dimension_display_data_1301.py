from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_tolerance_precision import GBTTolerancePrecision
from ..models.gbt_tolerance_type import GBTToleranceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_curve_display_data_4722 import BTCurveDisplayData4722
    from ..models.bt_matrix_3x3340 import BTMatrix3X3340
    from ..models.btbs_matrix_386 import BTBSMatrix386


T = TypeVar("T", bound="BTEllipseDiameterDimensionDisplayData1301")


@_attrs_define
class BTEllipseDiameterDimensionDisplayData1301:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        characteristic_id (str | Unset):
        coordinate_system (BTMatrix3X3340 | Unset):
        feature_id (str | Unset):
        fit_class (str | Unset):
        has_maximum_limit (bool | Unset):
        has_minimum_limit (bool | Unset):
        id (str | Unset):
        is_annotation_dimension (bool | Unset):
        is_associated_with_flat (bool | Unset):
        is_driven (bool | Unset):
        is_over_defined (bool | Unset):
        lower_tolerance (float | Unset):
        maximum_limit (float | Unset):
        minimum_limit (float | Unset):
        parameter_id (str | Unset):
        part_id (str | Unset):
        plane_matrix (BTBSMatrix386 | Unset):
        precision (GBTTolerancePrecision | Unset):
        tolerance_type (GBTToleranceType | Unset):
        upper_tolerance (float | Unset):
        value (float | Unset):
        has_extension (bool | Unset):
        position_x (float | Unset):
        position_y (float | Unset):
        witness_end_point_0x (float | Unset):
        witness_end_point_0y (float | Unset):
        witness_end_point_1x (float | Unset):
        witness_end_point_1y (float | Unset):
        witness_extension_0z (float | Unset):
        witness_extension_1z (float | Unset):
        witness_extension_curve (BTCurveDisplayData4722 | Unset):
    """

    bt_type: str | Unset = UNSET
    characteristic_id: str | Unset = UNSET
    coordinate_system: BTMatrix3X3340 | Unset = UNSET
    feature_id: str | Unset = UNSET
    fit_class: str | Unset = UNSET
    has_maximum_limit: bool | Unset = UNSET
    has_minimum_limit: bool | Unset = UNSET
    id: str | Unset = UNSET
    is_annotation_dimension: bool | Unset = UNSET
    is_associated_with_flat: bool | Unset = UNSET
    is_driven: bool | Unset = UNSET
    is_over_defined: bool | Unset = UNSET
    lower_tolerance: float | Unset = UNSET
    maximum_limit: float | Unset = UNSET
    minimum_limit: float | Unset = UNSET
    parameter_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    plane_matrix: BTBSMatrix386 | Unset = UNSET
    precision: GBTTolerancePrecision | Unset = UNSET
    tolerance_type: GBTToleranceType | Unset = UNSET
    upper_tolerance: float | Unset = UNSET
    value: float | Unset = UNSET
    has_extension: bool | Unset = UNSET
    position_x: float | Unset = UNSET
    position_y: float | Unset = UNSET
    witness_end_point_0x: float | Unset = UNSET
    witness_end_point_0y: float | Unset = UNSET
    witness_end_point_1x: float | Unset = UNSET
    witness_end_point_1y: float | Unset = UNSET
    witness_extension_0z: float | Unset = UNSET
    witness_extension_1z: float | Unset = UNSET
    witness_extension_curve: BTCurveDisplayData4722 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        characteristic_id = self.characteristic_id

        coordinate_system: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coordinate_system, Unset):
            coordinate_system = self.coordinate_system.to_dict()

        feature_id = self.feature_id

        fit_class = self.fit_class

        has_maximum_limit = self.has_maximum_limit

        has_minimum_limit = self.has_minimum_limit

        id = self.id

        is_annotation_dimension = self.is_annotation_dimension

        is_associated_with_flat = self.is_associated_with_flat

        is_driven = self.is_driven

        is_over_defined = self.is_over_defined

        lower_tolerance = self.lower_tolerance

        maximum_limit = self.maximum_limit

        minimum_limit = self.minimum_limit

        parameter_id = self.parameter_id

        part_id = self.part_id

        plane_matrix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plane_matrix, Unset):
            plane_matrix = self.plane_matrix.to_dict()

        precision: str | Unset = UNSET
        if not isinstance(self.precision, Unset):
            precision = self.precision.value

        tolerance_type: str | Unset = UNSET
        if not isinstance(self.tolerance_type, Unset):
            tolerance_type = self.tolerance_type.value

        upper_tolerance = self.upper_tolerance

        value = self.value

        has_extension = self.has_extension

        position_x = self.position_x

        position_y = self.position_y

        witness_end_point_0x = self.witness_end_point_0x

        witness_end_point_0y = self.witness_end_point_0y

        witness_end_point_1x = self.witness_end_point_1x

        witness_end_point_1y = self.witness_end_point_1y

        witness_extension_0z = self.witness_extension_0z

        witness_extension_1z = self.witness_extension_1z

        witness_extension_curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.witness_extension_curve, Unset):
            witness_extension_curve = self.witness_extension_curve.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if characteristic_id is not UNSET:
            field_dict["characteristicId"] = characteristic_id
        if coordinate_system is not UNSET:
            field_dict["coordinateSystem"] = coordinate_system
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if fit_class is not UNSET:
            field_dict["fitClass"] = fit_class
        if has_maximum_limit is not UNSET:
            field_dict["hasMaximumLimit"] = has_maximum_limit
        if has_minimum_limit is not UNSET:
            field_dict["hasMinimumLimit"] = has_minimum_limit
        if id is not UNSET:
            field_dict["id"] = id
        if is_annotation_dimension is not UNSET:
            field_dict["isAnnotationDimension"] = is_annotation_dimension
        if is_associated_with_flat is not UNSET:
            field_dict["isAssociatedWithFlat"] = is_associated_with_flat
        if is_driven is not UNSET:
            field_dict["isDriven"] = is_driven
        if is_over_defined is not UNSET:
            field_dict["isOverDefined"] = is_over_defined
        if lower_tolerance is not UNSET:
            field_dict["lowerTolerance"] = lower_tolerance
        if maximum_limit is not UNSET:
            field_dict["maximumLimit"] = maximum_limit
        if minimum_limit is not UNSET:
            field_dict["minimumLimit"] = minimum_limit
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if plane_matrix is not UNSET:
            field_dict["planeMatrix"] = plane_matrix
        if precision is not UNSET:
            field_dict["precision"] = precision
        if tolerance_type is not UNSET:
            field_dict["toleranceType"] = tolerance_type
        if upper_tolerance is not UNSET:
            field_dict["upperTolerance"] = upper_tolerance
        if value is not UNSET:
            field_dict["value"] = value
        if has_extension is not UNSET:
            field_dict["hasExtension"] = has_extension
        if position_x is not UNSET:
            field_dict["positionX"] = position_x
        if position_y is not UNSET:
            field_dict["positionY"] = position_y
        if witness_end_point_0x is not UNSET:
            field_dict["witnessEndPoint0X"] = witness_end_point_0x
        if witness_end_point_0y is not UNSET:
            field_dict["witnessEndPoint0Y"] = witness_end_point_0y
        if witness_end_point_1x is not UNSET:
            field_dict["witnessEndPoint1X"] = witness_end_point_1x
        if witness_end_point_1y is not UNSET:
            field_dict["witnessEndPoint1Y"] = witness_end_point_1y
        if witness_extension_0z is not UNSET:
            field_dict["witnessExtension0Z"] = witness_extension_0z
        if witness_extension_1z is not UNSET:
            field_dict["witnessExtension1Z"] = witness_extension_1z
        if witness_extension_curve is not UNSET:
            field_dict["witnessExtensionCurve"] = witness_extension_curve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_curve_display_data_4722 import BTCurveDisplayData4722
        from ..models.bt_matrix_3x3340 import BTMatrix3X3340
        from ..models.btbs_matrix_386 import BTBSMatrix386

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        characteristic_id = d.pop("characteristicId", UNSET)

        _coordinate_system = d.pop("coordinateSystem", UNSET)
        coordinate_system: BTMatrix3X3340 | Unset
        if isinstance(_coordinate_system, Unset):
            coordinate_system = UNSET
        else:
            coordinate_system = BTMatrix3X3340.from_dict(_coordinate_system)

        feature_id = d.pop("featureId", UNSET)

        fit_class = d.pop("fitClass", UNSET)

        has_maximum_limit = d.pop("hasMaximumLimit", UNSET)

        has_minimum_limit = d.pop("hasMinimumLimit", UNSET)

        id = d.pop("id", UNSET)

        is_annotation_dimension = d.pop("isAnnotationDimension", UNSET)

        is_associated_with_flat = d.pop("isAssociatedWithFlat", UNSET)

        is_driven = d.pop("isDriven", UNSET)

        is_over_defined = d.pop("isOverDefined", UNSET)

        lower_tolerance = d.pop("lowerTolerance", UNSET)

        maximum_limit = d.pop("maximumLimit", UNSET)

        minimum_limit = d.pop("minimumLimit", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        part_id = d.pop("partId", UNSET)

        _plane_matrix = d.pop("planeMatrix", UNSET)
        plane_matrix: BTBSMatrix386 | Unset
        if isinstance(_plane_matrix, Unset):
            plane_matrix = UNSET
        else:
            plane_matrix = BTBSMatrix386.from_dict(_plane_matrix)

        _precision = d.pop("precision", UNSET)
        precision: GBTTolerancePrecision | Unset
        if isinstance(_precision, Unset):
            precision = UNSET
        else:
            precision = GBTTolerancePrecision(_precision)

        _tolerance_type = d.pop("toleranceType", UNSET)
        tolerance_type: GBTToleranceType | Unset
        if isinstance(_tolerance_type, Unset):
            tolerance_type = UNSET
        else:
            tolerance_type = GBTToleranceType(_tolerance_type)

        upper_tolerance = d.pop("upperTolerance", UNSET)

        value = d.pop("value", UNSET)

        has_extension = d.pop("hasExtension", UNSET)

        position_x = d.pop("positionX", UNSET)

        position_y = d.pop("positionY", UNSET)

        witness_end_point_0x = d.pop("witnessEndPoint0X", UNSET)

        witness_end_point_0y = d.pop("witnessEndPoint0Y", UNSET)

        witness_end_point_1x = d.pop("witnessEndPoint1X", UNSET)

        witness_end_point_1y = d.pop("witnessEndPoint1Y", UNSET)

        witness_extension_0z = d.pop("witnessExtension0Z", UNSET)

        witness_extension_1z = d.pop("witnessExtension1Z", UNSET)

        _witness_extension_curve = d.pop("witnessExtensionCurve", UNSET)
        witness_extension_curve: BTCurveDisplayData4722 | Unset
        if isinstance(_witness_extension_curve, Unset):
            witness_extension_curve = UNSET
        else:
            witness_extension_curve = BTCurveDisplayData4722.from_dict(_witness_extension_curve)

        bt_ellipse_diameter_dimension_display_data_1301 = cls(
            bt_type=bt_type,
            characteristic_id=characteristic_id,
            coordinate_system=coordinate_system,
            feature_id=feature_id,
            fit_class=fit_class,
            has_maximum_limit=has_maximum_limit,
            has_minimum_limit=has_minimum_limit,
            id=id,
            is_annotation_dimension=is_annotation_dimension,
            is_associated_with_flat=is_associated_with_flat,
            is_driven=is_driven,
            is_over_defined=is_over_defined,
            lower_tolerance=lower_tolerance,
            maximum_limit=maximum_limit,
            minimum_limit=minimum_limit,
            parameter_id=parameter_id,
            part_id=part_id,
            plane_matrix=plane_matrix,
            precision=precision,
            tolerance_type=tolerance_type,
            upper_tolerance=upper_tolerance,
            value=value,
            has_extension=has_extension,
            position_x=position_x,
            position_y=position_y,
            witness_end_point_0x=witness_end_point_0x,
            witness_end_point_0y=witness_end_point_0y,
            witness_end_point_1x=witness_end_point_1x,
            witness_end_point_1y=witness_end_point_1y,
            witness_extension_0z=witness_extension_0z,
            witness_extension_1z=witness_extension_1z,
            witness_extension_curve=witness_extension_curve,
        )

        bt_ellipse_diameter_dimension_display_data_1301.additional_properties = d
        return bt_ellipse_diameter_dimension_display_data_1301

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
