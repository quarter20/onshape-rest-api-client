from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_bill_of_materials_item_source_info import BTBillOfMaterialsItemSourceInfo
    from ..models.bt_bill_of_materials_row_info_header_id_to_value import BTBillOfMaterialsRowInfoHeaderIdToValue


T = TypeVar("T", bound="BTBillOfMaterialsRowInfo")


@_attrs_define
class BTBillOfMaterialsRowInfo:
    """
    Attributes:
        header_id_to_value (BTBillOfMaterialsRowInfoHeaderIdToValue | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        indent_level (int | Unset):
        item_source (BTBillOfMaterialsItemSourceInfo | Unset):
        name (str | Unset): Name of the resource.
        related_occurrences (list[str] | Unset): Occurrence IDs in the assembly that refer to the part described by this
            BOM row.
        row_id (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    header_id_to_value: BTBillOfMaterialsRowInfoHeaderIdToValue | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    indent_level: int | Unset = UNSET
    item_source: BTBillOfMaterialsItemSourceInfo | Unset = UNSET
    name: str | Unset = UNSET
    related_occurrences: list[str] | Unset = UNSET
    row_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header_id_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header_id_to_value, Unset):
            header_id_to_value = self.header_id_to_value.to_dict()

        href = self.href

        id = self.id

        indent_level = self.indent_level

        item_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.item_source, Unset):
            item_source = self.item_source.to_dict()

        name = self.name

        related_occurrences: list[str] | Unset = UNSET
        if not isinstance(self.related_occurrences, Unset):
            related_occurrences = self.related_occurrences

        row_id = self.row_id

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header_id_to_value is not UNSET:
            field_dict["headerIdToValue"] = header_id_to_value
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if indent_level is not UNSET:
            field_dict["indentLevel"] = indent_level
        if item_source is not UNSET:
            field_dict["itemSource"] = item_source
        if name is not UNSET:
            field_dict["name"] = name
        if related_occurrences is not UNSET:
            field_dict["relatedOccurrences"] = related_occurrences
        if row_id is not UNSET:
            field_dict["rowId"] = row_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_bill_of_materials_item_source_info import BTBillOfMaterialsItemSourceInfo
        from ..models.bt_bill_of_materials_row_info_header_id_to_value import BTBillOfMaterialsRowInfoHeaderIdToValue

        d = dict(src_dict)
        _header_id_to_value = d.pop("headerIdToValue", UNSET)
        header_id_to_value: BTBillOfMaterialsRowInfoHeaderIdToValue | Unset
        if isinstance(_header_id_to_value, Unset):
            header_id_to_value = UNSET
        else:
            header_id_to_value = BTBillOfMaterialsRowInfoHeaderIdToValue.from_dict(_header_id_to_value)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        indent_level = d.pop("indentLevel", UNSET)

        _item_source = d.pop("itemSource", UNSET)
        item_source: BTBillOfMaterialsItemSourceInfo | Unset
        if isinstance(_item_source, Unset):
            item_source = UNSET
        else:
            item_source = BTBillOfMaterialsItemSourceInfo.from_dict(_item_source)

        name = d.pop("name", UNSET)

        related_occurrences = cast(list[str], d.pop("relatedOccurrences", UNSET))

        row_id = d.pop("rowId", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_bill_of_materials_row_info = cls(
            header_id_to_value=header_id_to_value,
            href=href,
            id=id,
            indent_level=indent_level,
            item_source=item_source,
            name=name,
            related_occurrences=related_occurrences,
            row_id=row_id,
            view_ref=view_ref,
        )

        bt_bill_of_materials_row_info.additional_properties = d
        return bt_bill_of_materials_row_info

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
