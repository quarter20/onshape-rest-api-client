from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_bill_of_materials_header_info import BTBillOfMaterialsHeaderInfo
    from ..models.bt_bill_of_materials_row_info import BTBillOfMaterialsRowInfo
    from ..models.bt_bill_of_materials_source_info import BTBillOfMaterialsSourceInfo


T = TypeVar("T", bound="BTBillOfMaterialsInfo")


@_attrs_define
class BTBillOfMaterialsInfo:
    """
    Attributes:
        bom_source (BTBillOfMaterialsSourceInfo | Unset):
        created_at (str | Unset):
        format_version (str | Unset):
        headers (list[BTBillOfMaterialsHeaderInfo] | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        rows (list[BTBillOfMaterialsRowInfo] | Unset):
        template_id (str | Unset):
        top_level_assembly_row (BTBillOfMaterialsRowInfo | Unset):
        type_ (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    bom_source: BTBillOfMaterialsSourceInfo | Unset = UNSET
    created_at: str | Unset = UNSET
    format_version: str | Unset = UNSET
    headers: list[BTBillOfMaterialsHeaderInfo] | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    rows: list[BTBillOfMaterialsRowInfo] | Unset = UNSET
    template_id: str | Unset = UNSET
    top_level_assembly_row: BTBillOfMaterialsRowInfo | Unset = UNSET
    type_: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bom_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bom_source, Unset):
            bom_source = self.bom_source.to_dict()

        created_at = self.created_at

        format_version = self.format_version

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        href = self.href

        id = self.id

        name = self.name

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        template_id = self.template_id

        top_level_assembly_row: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_level_assembly_row, Unset):
            top_level_assembly_row = self.top_level_assembly_row.to_dict()

        type_ = self.type_

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bom_source is not UNSET:
            field_dict["bomSource"] = bom_source
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if format_version is not UNSET:
            field_dict["formatVersion"] = format_version
        if headers is not UNSET:
            field_dict["headers"] = headers
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rows is not UNSET:
            field_dict["rows"] = rows
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if top_level_assembly_row is not UNSET:
            field_dict["topLevelAssemblyRow"] = top_level_assembly_row
        if type_ is not UNSET:
            field_dict["type"] = type_
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_bill_of_materials_header_info import BTBillOfMaterialsHeaderInfo
        from ..models.bt_bill_of_materials_row_info import BTBillOfMaterialsRowInfo
        from ..models.bt_bill_of_materials_source_info import BTBillOfMaterialsSourceInfo

        d = dict(src_dict)
        _bom_source = d.pop("bomSource", UNSET)
        bom_source: BTBillOfMaterialsSourceInfo | Unset
        if isinstance(_bom_source, Unset):
            bom_source = UNSET
        else:
            bom_source = BTBillOfMaterialsSourceInfo.from_dict(_bom_source)

        created_at = d.pop("createdAt", UNSET)

        format_version = d.pop("formatVersion", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: list[BTBillOfMaterialsHeaderInfo] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = BTBillOfMaterialsHeaderInfo.from_dict(headers_item_data)

                headers.append(headers_item)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[BTBillOfMaterialsRowInfo] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = BTBillOfMaterialsRowInfo.from_dict(rows_item_data)

                rows.append(rows_item)

        template_id = d.pop("templateId", UNSET)

        _top_level_assembly_row = d.pop("topLevelAssemblyRow", UNSET)
        top_level_assembly_row: BTBillOfMaterialsRowInfo | Unset
        if isinstance(_top_level_assembly_row, Unset):
            top_level_assembly_row = UNSET
        else:
            top_level_assembly_row = BTBillOfMaterialsRowInfo.from_dict(_top_level_assembly_row)

        type_ = d.pop("type", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_bill_of_materials_info = cls(
            bom_source=bom_source,
            created_at=created_at,
            format_version=format_version,
            headers=headers,
            href=href,
            id=id,
            name=name,
            rows=rows,
            template_id=template_id,
            top_level_assembly_row=top_level_assembly_row,
            type_=type_,
            view_ref=view_ref,
        )

        bt_bill_of_materials_info.additional_properties = d
        return bt_bill_of_materials_info

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
