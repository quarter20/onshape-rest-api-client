from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtg_tol_constraint_type import GBTGTolConstraintType
from ..models.gbtg_tol_extended_constraint_type import GBTGTolExtendedConstraintType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAnnotationGTolRowDisplayData4397")


@_attrs_define
class BTAnnotationGTolRowDisplayData4397:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        constraint_type (GBTGTolConstraintType | Unset):
        extended_constraint_type (GBTGTolExtendedConstraintType | Unset):
        prefix (str | Unset):
        references (list[str] | Unset):
        suffix (str | Unset):
        tolerance (float | Unset):
        tolerance_symbol_0 (str | Unset):
        tolerance_symbol_1 (str | Unset):
    """

    bt_type: str | Unset = UNSET
    constraint_type: GBTGTolConstraintType | Unset = UNSET
    extended_constraint_type: GBTGTolExtendedConstraintType | Unset = UNSET
    prefix: str | Unset = UNSET
    references: list[str] | Unset = UNSET
    suffix: str | Unset = UNSET
    tolerance: float | Unset = UNSET
    tolerance_symbol_0: str | Unset = UNSET
    tolerance_symbol_1: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        constraint_type: str | Unset = UNSET
        if not isinstance(self.constraint_type, Unset):
            constraint_type = self.constraint_type.value

        extended_constraint_type: str | Unset = UNSET
        if not isinstance(self.extended_constraint_type, Unset):
            extended_constraint_type = self.extended_constraint_type.value

        prefix = self.prefix

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        suffix = self.suffix

        tolerance = self.tolerance

        tolerance_symbol_0 = self.tolerance_symbol_0

        tolerance_symbol_1 = self.tolerance_symbol_1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if constraint_type is not UNSET:
            field_dict["constraintType"] = constraint_type
        if extended_constraint_type is not UNSET:
            field_dict["extendedConstraintType"] = extended_constraint_type
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if references is not UNSET:
            field_dict["references"] = references
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if tolerance is not UNSET:
            field_dict["tolerance"] = tolerance
        if tolerance_symbol_0 is not UNSET:
            field_dict["toleranceSymbol0"] = tolerance_symbol_0
        if tolerance_symbol_1 is not UNSET:
            field_dict["toleranceSymbol1"] = tolerance_symbol_1

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _constraint_type = d.pop("constraintType", UNSET)
        constraint_type: GBTGTolConstraintType | Unset
        if isinstance(_constraint_type, Unset):
            constraint_type = UNSET
        else:
            constraint_type = GBTGTolConstraintType(_constraint_type)

        _extended_constraint_type = d.pop("extendedConstraintType", UNSET)
        extended_constraint_type: GBTGTolExtendedConstraintType | Unset
        if isinstance(_extended_constraint_type, Unset):
            extended_constraint_type = UNSET
        else:
            extended_constraint_type = GBTGTolExtendedConstraintType(_extended_constraint_type)

        prefix = d.pop("prefix", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        suffix = d.pop("suffix", UNSET)

        tolerance = d.pop("tolerance", UNSET)

        tolerance_symbol_0 = d.pop("toleranceSymbol0", UNSET)

        tolerance_symbol_1 = d.pop("toleranceSymbol1", UNSET)

        bt_annotation_g_tol_row_display_data_4397 = cls(
            bt_type=bt_type,
            constraint_type=constraint_type,
            extended_constraint_type=extended_constraint_type,
            prefix=prefix,
            references=references,
            suffix=suffix,
            tolerance=tolerance,
            tolerance_symbol_0=tolerance_symbol_0,
            tolerance_symbol_1=tolerance_symbol_1,
        )

        bt_annotation_g_tol_row_display_data_4397.additional_properties = d
        return bt_annotation_g_tol_row_display_data_4397

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
