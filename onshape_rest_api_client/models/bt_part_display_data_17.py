from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_mesh_state import GBTMeshState
from ..models.gbt_part_visibility import GBTPartVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
    from ..models.bt_object_id import BTObjectId
    from ..models.bt_part_custom_properties_1338 import BTPartCustomProperties1338
    from ..models.bt_part_display_data_17_property_id_to_source import BTPartDisplayData17PropertyIdToSource
    from ..models.bt_part_material_1445 import BTPartMaterial1445
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTPartDisplayData17")


@_attrs_define
class BTPartDisplayData17:
    """
    Attributes:
        appearance (BTGraphicsAppearance1152 | Unset):
        appearance_for_new_cell (BTGraphicsAppearance1152 | Unset):
        bt_type (str | Unset): Type of JSON object.
        custom_properties (BTPartCustomProperties1338 | Unset):
        default_color_hash (str | Unset):
        has_faults (bool | Unset):
        hidden (bool | Unset):
        high_box_corner (BTVector3D389 | Unset):
        id (str | Unset):
        is_active_sheet_metal (bool | Unset):
        is_mesh (bool | Unset):
        is_modifiable (bool | Unset):
        is_sheet (bool | Unset):
        is_solid (bool | Unset):
        is_wire (bool | Unset):
        low_box_corner (BTVector3D389 | Unset):
        material (BTPartMaterial1445 | Unset):
        material_for_new_cell (BTPartMaterial1445 | Unset):
        mesh_state (GBTMeshState | Unset):
        name (str | Unset):
        name_for_new_cell (str | Unset):
        ordinal (int | Unset):
        part_id (str | Unset):
        property_id_to_source (BTPartDisplayData17PropertyIdToSource | Unset):
        referencing_configured_part_node_ids (list[BTObjectId] | Unset):
        visibility (GBTPartVisibility | Unset):
    """

    appearance: BTGraphicsAppearance1152 | Unset = UNSET
    appearance_for_new_cell: BTGraphicsAppearance1152 | Unset = UNSET
    bt_type: str | Unset = UNSET
    custom_properties: BTPartCustomProperties1338 | Unset = UNSET
    default_color_hash: str | Unset = UNSET
    has_faults: bool | Unset = UNSET
    hidden: bool | Unset = UNSET
    high_box_corner: BTVector3D389 | Unset = UNSET
    id: str | Unset = UNSET
    is_active_sheet_metal: bool | Unset = UNSET
    is_mesh: bool | Unset = UNSET
    is_modifiable: bool | Unset = UNSET
    is_sheet: bool | Unset = UNSET
    is_solid: bool | Unset = UNSET
    is_wire: bool | Unset = UNSET
    low_box_corner: BTVector3D389 | Unset = UNSET
    material: BTPartMaterial1445 | Unset = UNSET
    material_for_new_cell: BTPartMaterial1445 | Unset = UNSET
    mesh_state: GBTMeshState | Unset = UNSET
    name: str | Unset = UNSET
    name_for_new_cell: str | Unset = UNSET
    ordinal: int | Unset = UNSET
    part_id: str | Unset = UNSET
    property_id_to_source: BTPartDisplayData17PropertyIdToSource | Unset = UNSET
    referencing_configured_part_node_ids: list[BTObjectId] | Unset = UNSET
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

        custom_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_properties, Unset):
            custom_properties = self.custom_properties.to_dict()

        default_color_hash = self.default_color_hash

        has_faults = self.has_faults

        hidden = self.hidden

        high_box_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.high_box_corner, Unset):
            high_box_corner = self.high_box_corner.to_dict()

        id = self.id

        is_active_sheet_metal = self.is_active_sheet_metal

        is_mesh = self.is_mesh

        is_modifiable = self.is_modifiable

        is_sheet = self.is_sheet

        is_solid = self.is_solid

        is_wire = self.is_wire

        low_box_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.low_box_corner, Unset):
            low_box_corner = self.low_box_corner.to_dict()

        material: dict[str, Any] | Unset = UNSET
        if not isinstance(self.material, Unset):
            material = self.material.to_dict()

        material_for_new_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.material_for_new_cell, Unset):
            material_for_new_cell = self.material_for_new_cell.to_dict()

        mesh_state: str | Unset = UNSET
        if not isinstance(self.mesh_state, Unset):
            mesh_state = self.mesh_state.value

        name = self.name

        name_for_new_cell = self.name_for_new_cell

        ordinal = self.ordinal

        part_id = self.part_id

        property_id_to_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_id_to_source, Unset):
            property_id_to_source = self.property_id_to_source.to_dict()

        referencing_configured_part_node_ids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.referencing_configured_part_node_ids, Unset):
            referencing_configured_part_node_ids = []
            for referencing_configured_part_node_ids_item_data in self.referencing_configured_part_node_ids:
                referencing_configured_part_node_ids_item = referencing_configured_part_node_ids_item_data.to_dict()
                referencing_configured_part_node_ids.append(referencing_configured_part_node_ids_item)

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
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if default_color_hash is not UNSET:
            field_dict["defaultColorHash"] = default_color_hash
        if has_faults is not UNSET:
            field_dict["hasFaults"] = has_faults
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if high_box_corner is not UNSET:
            field_dict["highBoxCorner"] = high_box_corner
        if id is not UNSET:
            field_dict["id"] = id
        if is_active_sheet_metal is not UNSET:
            field_dict["isActiveSheetMetal"] = is_active_sheet_metal
        if is_mesh is not UNSET:
            field_dict["isMesh"] = is_mesh
        if is_modifiable is not UNSET:
            field_dict["isModifiable"] = is_modifiable
        if is_sheet is not UNSET:
            field_dict["isSheet"] = is_sheet
        if is_solid is not UNSET:
            field_dict["isSolid"] = is_solid
        if is_wire is not UNSET:
            field_dict["isWire"] = is_wire
        if low_box_corner is not UNSET:
            field_dict["lowBoxCorner"] = low_box_corner
        if material is not UNSET:
            field_dict["material"] = material
        if material_for_new_cell is not UNSET:
            field_dict["materialForNewCell"] = material_for_new_cell
        if mesh_state is not UNSET:
            field_dict["meshState"] = mesh_state
        if name is not UNSET:
            field_dict["name"] = name
        if name_for_new_cell is not UNSET:
            field_dict["nameForNewCell"] = name_for_new_cell
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if property_id_to_source is not UNSET:
            field_dict["propertyIdToSource"] = property_id_to_source
        if referencing_configured_part_node_ids is not UNSET:
            field_dict["referencingConfiguredPartNodeIds"] = referencing_configured_part_node_ids
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
        from ..models.bt_object_id import BTObjectId
        from ..models.bt_part_custom_properties_1338 import BTPartCustomProperties1338
        from ..models.bt_part_display_data_17_property_id_to_source import BTPartDisplayData17PropertyIdToSource
        from ..models.bt_part_material_1445 import BTPartMaterial1445
        from ..models.bt_vector_3d389 import BTVector3D389

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

        _custom_properties = d.pop("customProperties", UNSET)
        custom_properties: BTPartCustomProperties1338 | Unset
        if isinstance(_custom_properties, Unset):
            custom_properties = UNSET
        else:
            custom_properties = BTPartCustomProperties1338.from_dict(_custom_properties)

        default_color_hash = d.pop("defaultColorHash", UNSET)

        has_faults = d.pop("hasFaults", UNSET)

        hidden = d.pop("hidden", UNSET)

        _high_box_corner = d.pop("highBoxCorner", UNSET)
        high_box_corner: BTVector3D389 | Unset
        if isinstance(_high_box_corner, Unset):
            high_box_corner = UNSET
        else:
            high_box_corner = BTVector3D389.from_dict(_high_box_corner)

        id = d.pop("id", UNSET)

        is_active_sheet_metal = d.pop("isActiveSheetMetal", UNSET)

        is_mesh = d.pop("isMesh", UNSET)

        is_modifiable = d.pop("isModifiable", UNSET)

        is_sheet = d.pop("isSheet", UNSET)

        is_solid = d.pop("isSolid", UNSET)

        is_wire = d.pop("isWire", UNSET)

        _low_box_corner = d.pop("lowBoxCorner", UNSET)
        low_box_corner: BTVector3D389 | Unset
        if isinstance(_low_box_corner, Unset):
            low_box_corner = UNSET
        else:
            low_box_corner = BTVector3D389.from_dict(_low_box_corner)

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

        _mesh_state = d.pop("meshState", UNSET)
        mesh_state: GBTMeshState | Unset
        if isinstance(_mesh_state, Unset):
            mesh_state = UNSET
        else:
            mesh_state = GBTMeshState(_mesh_state)

        name = d.pop("name", UNSET)

        name_for_new_cell = d.pop("nameForNewCell", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        part_id = d.pop("partId", UNSET)

        _property_id_to_source = d.pop("propertyIdToSource", UNSET)
        property_id_to_source: BTPartDisplayData17PropertyIdToSource | Unset
        if isinstance(_property_id_to_source, Unset):
            property_id_to_source = UNSET
        else:
            property_id_to_source = BTPartDisplayData17PropertyIdToSource.from_dict(_property_id_to_source)

        _referencing_configured_part_node_ids = d.pop("referencingConfiguredPartNodeIds", UNSET)
        referencing_configured_part_node_ids: list[BTObjectId] | Unset = UNSET
        if _referencing_configured_part_node_ids is not UNSET:
            referencing_configured_part_node_ids = []
            for referencing_configured_part_node_ids_item_data in _referencing_configured_part_node_ids:
                referencing_configured_part_node_ids_item = BTObjectId.from_dict(
                    referencing_configured_part_node_ids_item_data
                )

                referencing_configured_part_node_ids.append(referencing_configured_part_node_ids_item)

        _visibility = d.pop("visibility", UNSET)
        visibility: GBTPartVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = GBTPartVisibility(_visibility)

        bt_part_display_data_17 = cls(
            appearance=appearance,
            appearance_for_new_cell=appearance_for_new_cell,
            bt_type=bt_type,
            custom_properties=custom_properties,
            default_color_hash=default_color_hash,
            has_faults=has_faults,
            hidden=hidden,
            high_box_corner=high_box_corner,
            id=id,
            is_active_sheet_metal=is_active_sheet_metal,
            is_mesh=is_mesh,
            is_modifiable=is_modifiable,
            is_sheet=is_sheet,
            is_solid=is_solid,
            is_wire=is_wire,
            low_box_corner=low_box_corner,
            material=material,
            material_for_new_cell=material_for_new_cell,
            mesh_state=mesh_state,
            name=name,
            name_for_new_cell=name_for_new_cell,
            ordinal=ordinal,
            part_id=part_id,
            property_id_to_source=property_id_to_source,
            referencing_configured_part_node_ids=referencing_configured_part_node_ids,
            visibility=visibility,
        )

        bt_part_display_data_17.additional_properties = d
        return bt_part_display_data_17

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
