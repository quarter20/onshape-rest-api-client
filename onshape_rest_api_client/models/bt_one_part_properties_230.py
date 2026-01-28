from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_part_visibility import GBTPartVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
    from ..models.bt_part_custom_properties_1338 import BTPartCustomProperties1338
    from ..models.bt_part_material_1445 import BTPartMaterial1445
    from ..models.btm_parameter_query_list_148 import BTMParameterQueryList148
    from ..models.btp_function_declaration_246 import BTPFunctionDeclaration246


T = TypeVar("T", bound="BTOnePartProperties230")


@_attrs_define
class BTOnePartProperties230:
    """
    Attributes:
        appearance (BTGraphicsAppearance1152 | Unset):
        appearance_for_new_cell (BTGraphicsAppearance1152 | Unset):
        bt_type (str | Unset): Type of JSON object.
        changed_properties_set (list[str] | Unset):
        custom_properties (BTPartCustomProperties1338 | Unset):
        material (BTPartMaterial1445 | Unset):
        material_for_new_cell (BTPartMaterial1445 | Unset):
        name (str | Unset):
        name_for_new_cell (str | Unset):
        name_if_not_null (BTOnePartProperties230 | Unset):
        node_id (str | Unset):
        parsed_query (BTPFunctionDeclaration246 | Unset):
        query (str | Unset):
        query_list_parameter (BTMParameterQueryList148 | Unset):
        sheet_metal_bend_order (list[str] | Unset):
        sheet_metal_bend_order_if_not_null (BTOnePartProperties230 | Unset):
        visibility (GBTPartVisibility | Unset):
    """

    appearance: BTGraphicsAppearance1152 | Unset = UNSET
    appearance_for_new_cell: BTGraphicsAppearance1152 | Unset = UNSET
    bt_type: str | Unset = UNSET
    changed_properties_set: list[str] | Unset = UNSET
    custom_properties: BTPartCustomProperties1338 | Unset = UNSET
    material: BTPartMaterial1445 | Unset = UNSET
    material_for_new_cell: BTPartMaterial1445 | Unset = UNSET
    name: str | Unset = UNSET
    name_for_new_cell: str | Unset = UNSET
    name_if_not_null: BTOnePartProperties230 | Unset = UNSET
    node_id: str | Unset = UNSET
    parsed_query: BTPFunctionDeclaration246 | Unset = UNSET
    query: str | Unset = UNSET
    query_list_parameter: BTMParameterQueryList148 | Unset = UNSET
    sheet_metal_bend_order: list[str] | Unset = UNSET
    sheet_metal_bend_order_if_not_null: BTOnePartProperties230 | Unset = UNSET
    visibility: GBTPartVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appearance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        appearance_for_new_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance_for_new_cell, Unset):
            appearance_for_new_cell = self.appearance_for_new_cell.to_dict()

        bt_type = self.bt_type

        changed_properties_set: list[str] | Unset = UNSET
        if not isinstance(self.changed_properties_set, Unset):
            changed_properties_set = self.changed_properties_set

        custom_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_properties, Unset):
            custom_properties = self.custom_properties.to_dict()

        material: dict[str, Any] | Unset = UNSET
        if not isinstance(self.material, Unset):
            material = self.material.to_dict()

        material_for_new_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.material_for_new_cell, Unset):
            material_for_new_cell = self.material_for_new_cell.to_dict()

        name = self.name

        name_for_new_cell = self.name_for_new_cell

        name_if_not_null: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_if_not_null, Unset):
            name_if_not_null = self.name_if_not_null.to_dict()

        node_id = self.node_id

        parsed_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parsed_query, Unset):
            parsed_query = self.parsed_query.to_dict()

        query = self.query

        query_list_parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_list_parameter, Unset):
            query_list_parameter = self.query_list_parameter.to_dict()

        sheet_metal_bend_order: list[str] | Unset = UNSET
        if not isinstance(self.sheet_metal_bend_order, Unset):
            sheet_metal_bend_order = self.sheet_metal_bend_order

        sheet_metal_bend_order_if_not_null: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sheet_metal_bend_order_if_not_null, Unset):
            sheet_metal_bend_order_if_not_null = self.sheet_metal_bend_order_if_not_null.to_dict()

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if appearance_for_new_cell is not UNSET:
            field_dict["appearanceForNewCell"] = appearance_for_new_cell
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if changed_properties_set is not UNSET:
            field_dict["changedPropertiesSet"] = changed_properties_set
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if material is not UNSET:
            field_dict["material"] = material
        if material_for_new_cell is not UNSET:
            field_dict["materialForNewCell"] = material_for_new_cell
        if name is not UNSET:
            field_dict["name"] = name
        if name_for_new_cell is not UNSET:
            field_dict["nameForNewCell"] = name_for_new_cell
        if name_if_not_null is not UNSET:
            field_dict["nameIfNotNull"] = name_if_not_null
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parsed_query is not UNSET:
            field_dict["parsedQuery"] = parsed_query
        if query is not UNSET:
            field_dict["query"] = query
        if query_list_parameter is not UNSET:
            field_dict["queryListParameter"] = query_list_parameter
        if sheet_metal_bend_order is not UNSET:
            field_dict["sheetMetalBendOrder"] = sheet_metal_bend_order
        if sheet_metal_bend_order_if_not_null is not UNSET:
            field_dict["sheetMetalBendOrderIfNotNull"] = sheet_metal_bend_order_if_not_null
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
        from ..models.bt_part_custom_properties_1338 import BTPartCustomProperties1338
        from ..models.bt_part_material_1445 import BTPartMaterial1445
        from ..models.btm_parameter_query_list_148 import BTMParameterQueryList148
        from ..models.btp_function_declaration_246 import BTPFunctionDeclaration246

        d = dict(src_dict)
        _appearance = d.pop("appearance", UNSET)
        appearance: BTGraphicsAppearance1152 | Unset
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = BTGraphicsAppearance1152.from_dict(_appearance)

        _appearance_for_new_cell = d.pop("appearanceForNewCell", UNSET)
        appearance_for_new_cell: BTGraphicsAppearance1152 | Unset
        if isinstance(_appearance_for_new_cell, Unset):
            appearance_for_new_cell = UNSET
        else:
            appearance_for_new_cell = BTGraphicsAppearance1152.from_dict(_appearance_for_new_cell)

        bt_type = d.pop("btType", UNSET)

        changed_properties_set = cast(list[str], d.pop("changedPropertiesSet", UNSET))

        _custom_properties = d.pop("customProperties", UNSET)
        custom_properties: BTPartCustomProperties1338 | Unset
        if isinstance(_custom_properties, Unset):
            custom_properties = UNSET
        else:
            custom_properties = BTPartCustomProperties1338.from_dict(_custom_properties)

        _material = d.pop("material", UNSET)
        material: BTPartMaterial1445 | Unset
        if isinstance(_material, Unset):
            material = UNSET
        else:
            material = BTPartMaterial1445.from_dict(_material)

        _material_for_new_cell = d.pop("materialForNewCell", UNSET)
        material_for_new_cell: BTPartMaterial1445 | Unset
        if isinstance(_material_for_new_cell, Unset):
            material_for_new_cell = UNSET
        else:
            material_for_new_cell = BTPartMaterial1445.from_dict(_material_for_new_cell)

        name = d.pop("name", UNSET)

        name_for_new_cell = d.pop("nameForNewCell", UNSET)

        _name_if_not_null = d.pop("nameIfNotNull", UNSET)
        name_if_not_null: BTOnePartProperties230 | Unset
        if isinstance(_name_if_not_null, Unset):
            name_if_not_null = UNSET
        else:
            name_if_not_null = BTOnePartProperties230.from_dict(_name_if_not_null)

        node_id = d.pop("nodeId", UNSET)

        _parsed_query = d.pop("parsedQuery", UNSET)
        parsed_query: BTPFunctionDeclaration246 | Unset
        if isinstance(_parsed_query, Unset):
            parsed_query = UNSET
        else:
            parsed_query = BTPFunctionDeclaration246.from_dict(_parsed_query)

        query = d.pop("query", UNSET)

        _query_list_parameter = d.pop("queryListParameter", UNSET)
        query_list_parameter: BTMParameterQueryList148 | Unset
        if isinstance(_query_list_parameter, Unset):
            query_list_parameter = UNSET
        else:
            query_list_parameter = BTMParameterQueryList148.from_dict(_query_list_parameter)

        sheet_metal_bend_order = cast(list[str], d.pop("sheetMetalBendOrder", UNSET))

        _sheet_metal_bend_order_if_not_null = d.pop("sheetMetalBendOrderIfNotNull", UNSET)
        sheet_metal_bend_order_if_not_null: BTOnePartProperties230 | Unset
        if isinstance(_sheet_metal_bend_order_if_not_null, Unset):
            sheet_metal_bend_order_if_not_null = UNSET
        else:
            sheet_metal_bend_order_if_not_null = BTOnePartProperties230.from_dict(_sheet_metal_bend_order_if_not_null)

        _visibility = d.pop("visibility", UNSET)
        visibility: GBTPartVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = GBTPartVisibility(_visibility)

        bt_one_part_properties_230 = cls(
            appearance=appearance,
            appearance_for_new_cell=appearance_for_new_cell,
            bt_type=bt_type,
            changed_properties_set=changed_properties_set,
            custom_properties=custom_properties,
            material=material,
            material_for_new_cell=material_for_new_cell,
            name=name,
            name_for_new_cell=name_for_new_cell,
            name_if_not_null=name_if_not_null,
            node_id=node_id,
            parsed_query=parsed_query,
            query=query,
            query_list_parameter=query_list_parameter,
            sheet_metal_bend_order=sheet_metal_bend_order,
            sheet_metal_bend_order_if_not_null=sheet_metal_bend_order_if_not_null,
            visibility=visibility,
        )

        bt_one_part_properties_230.additional_properties = d
        return bt_one_part_properties_230

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
