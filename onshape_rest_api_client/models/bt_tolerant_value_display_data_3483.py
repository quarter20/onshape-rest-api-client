from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_tolerance_precision import GBTTolerancePrecision
from ..models.gbt_tolerance_type import GBTToleranceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTolerantValueDisplayData3483")


@_attrs_define
class BTTolerantValueDisplayData3483:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        fit_class (str | Unset):
        is_angle (bool | Unset):
        is_defined (bool | Unset):
        lower_tolerance (float | Unset):
        nominal_value (float | Unset):
        precision (GBTTolerancePrecision | Unset):
        tolerance_type (GBTToleranceType | Unset):
        upper_tolerance (float | Unset):
    """

    bt_type: str | Unset = UNSET
    fit_class: str | Unset = UNSET
    is_angle: bool | Unset = UNSET
    is_defined: bool | Unset = UNSET
    lower_tolerance: float | Unset = UNSET
    nominal_value: float | Unset = UNSET
    precision: GBTTolerancePrecision | Unset = UNSET
    tolerance_type: GBTToleranceType | Unset = UNSET
    upper_tolerance: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        fit_class = self.fit_class

        is_angle = self.is_angle

        is_defined = self.is_defined

        lower_tolerance = self.lower_tolerance

        nominal_value = self.nominal_value

        precision: str | Unset = UNSET
        if not isinstance(self.precision, Unset):
            precision = self.precision.value

        tolerance_type: str | Unset = UNSET
        if not isinstance(self.tolerance_type, Unset):
            tolerance_type = self.tolerance_type.value

        upper_tolerance = self.upper_tolerance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if fit_class is not UNSET:
            field_dict["fitClass"] = fit_class
        if is_angle is not UNSET:
            field_dict["isAngle"] = is_angle
        if is_defined is not UNSET:
            field_dict["isDefined"] = is_defined
        if lower_tolerance is not UNSET:
            field_dict["lowerTolerance"] = lower_tolerance
        if nominal_value is not UNSET:
            field_dict["nominalValue"] = nominal_value
        if precision is not UNSET:
            field_dict["precision"] = precision
        if tolerance_type is not UNSET:
            field_dict["toleranceType"] = tolerance_type
        if upper_tolerance is not UNSET:
            field_dict["upperTolerance"] = upper_tolerance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        fit_class = d.pop("fitClass", UNSET)

        is_angle = d.pop("isAngle", UNSET)

        is_defined = d.pop("isDefined", UNSET)

        lower_tolerance = d.pop("lowerTolerance", UNSET)

        nominal_value = d.pop("nominalValue", UNSET)

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

        bt_tolerant_value_display_data_3483 = cls(
            bt_type=bt_type,
            fit_class=fit_class,
            is_angle=is_angle,
            is_defined=is_defined,
            lower_tolerance=lower_tolerance,
            nominal_value=nominal_value,
            precision=precision,
            tolerance_type=tolerance_type,
            upper_tolerance=upper_tolerance,
        )

        bt_tolerant_value_display_data_3483.additional_properties = d
        return bt_tolerant_value_display_data_3483

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
