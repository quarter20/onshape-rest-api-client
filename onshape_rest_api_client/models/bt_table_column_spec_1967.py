from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_table_column_width_units import GBTTableColumnWidthUnits
from ..models.gbt_table_text_alignment import GBTTableTextAlignment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_parameter_spec_6 import BTParameterSpec6


T = TypeVar("T", bound="BTTableColumnSpec1967")


@_attrs_define
class BTTableColumnSpec1967:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        default_cell_spec (BTParameterSpec6 | Unset):
        default_column_width_units (GBTTableColumnWidthUnits | Unset):
        default_column_width_value (int | Unset):
        default_header_name (str | Unset):
        default_text_alignment (GBTTableTextAlignment | Unset):
        is_expandable (bool | Unset):
        is_renamable (bool | Unset):
        read_only (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    default_cell_spec: BTParameterSpec6 | Unset = UNSET
    default_column_width_units: GBTTableColumnWidthUnits | Unset = UNSET
    default_column_width_value: int | Unset = UNSET
    default_header_name: str | Unset = UNSET
    default_text_alignment: GBTTableTextAlignment | Unset = UNSET
    is_expandable: bool | Unset = UNSET
    is_renamable: bool | Unset = UNSET
    read_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        default_cell_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_cell_spec, Unset):
            default_cell_spec = self.default_cell_spec.to_dict()

        default_column_width_units: str | Unset = UNSET
        if not isinstance(self.default_column_width_units, Unset):
            default_column_width_units = self.default_column_width_units.value

        default_column_width_value = self.default_column_width_value

        default_header_name = self.default_header_name

        default_text_alignment: str | Unset = UNSET
        if not isinstance(self.default_text_alignment, Unset):
            default_text_alignment = self.default_text_alignment.value

        is_expandable = self.is_expandable

        is_renamable = self.is_renamable

        read_only = self.read_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if default_cell_spec is not UNSET:
            field_dict["defaultCellSpec"] = default_cell_spec
        if default_column_width_units is not UNSET:
            field_dict["defaultColumnWidthUnits"] = default_column_width_units
        if default_column_width_value is not UNSET:
            field_dict["defaultColumnWidthValue"] = default_column_width_value
        if default_header_name is not UNSET:
            field_dict["defaultHeaderName"] = default_header_name
        if default_text_alignment is not UNSET:
            field_dict["defaultTextAlignment"] = default_text_alignment
        if is_expandable is not UNSET:
            field_dict["isExpandable"] = is_expandable
        if is_renamable is not UNSET:
            field_dict["isRenamable"] = is_renamable
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parameter_spec_6 import BTParameterSpec6

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _default_cell_spec = d.pop("defaultCellSpec", UNSET)
        default_cell_spec: BTParameterSpec6 | Unset
        if isinstance(_default_cell_spec, Unset):
            default_cell_spec = UNSET
        else:
            default_cell_spec = BTParameterSpec6.from_dict(_default_cell_spec)

        _default_column_width_units = d.pop("defaultColumnWidthUnits", UNSET)
        default_column_width_units: GBTTableColumnWidthUnits | Unset
        if isinstance(_default_column_width_units, Unset):
            default_column_width_units = UNSET
        else:
            default_column_width_units = GBTTableColumnWidthUnits(_default_column_width_units)

        default_column_width_value = d.pop("defaultColumnWidthValue", UNSET)

        default_header_name = d.pop("defaultHeaderName", UNSET)

        _default_text_alignment = d.pop("defaultTextAlignment", UNSET)
        default_text_alignment: GBTTableTextAlignment | Unset
        if isinstance(_default_text_alignment, Unset):
            default_text_alignment = UNSET
        else:
            default_text_alignment = GBTTableTextAlignment(_default_text_alignment)

        is_expandable = d.pop("isExpandable", UNSET)

        is_renamable = d.pop("isRenamable", UNSET)

        read_only = d.pop("readOnly", UNSET)

        bt_table_column_spec_1967 = cls(
            bt_type=bt_type,
            default_cell_spec=default_cell_spec,
            default_column_width_units=default_column_width_units,
            default_column_width_value=default_column_width_value,
            default_header_name=default_header_name,
            default_text_alignment=default_text_alignment,
            is_expandable=is_expandable,
            is_renamable=is_renamable,
            read_only=read_only,
        )

        bt_table_column_spec_1967.additional_properties = d
        return bt_table_column_spec_1967

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
