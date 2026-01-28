from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_bounding_box_1052 import BTBoundingBox1052
    from ..models.bt_cosmetic_thread_metadata_3248 import BTCosmeticThreadMetadata3248
    from ..models.bt_export_model_face_1363_decal_id_to_decal import BTExportModelFace1363DecalIdToDecal
    from ..models.bt_export_model_loop_1182 import BTExportModelLoop1182
    from ..models.bt_export_model_properties_3216 import BTExportModelProperties3216
    from ..models.bt_surface_description_1564 import BTSurfaceDescription1564


T = TypeVar("T", bound="BTExportModelFace1363")


@_attrs_define
class BTExportModelFace1363:
    """
    Attributes:
        appearance_property_node_id (str | Unset): Identifies the application of the appearance. Faces that share a
            value were assigned an appearance together.
        area (float | Unset):
        box (BTBoundingBox1052 | Unset): An axis-aligned bounding box indicated by two opposite corners.
        bt_type (str | Unset): Type of JSON object.
        cosmetic_thread_metadata (BTCosmeticThreadMetadata3248 | Unset):
        decal_id_to_decal (BTExportModelFace1363DecalIdToDecal | Unset):
        face_properties (BTExportModelProperties3216 | Unset):
        id (str | Unset):
        loops (list[BTExportModelLoop1182] | Unset):
        orientation (bool | Unset):
        surface (BTSurfaceDescription1564 | Unset):
    """

    appearance_property_node_id: str | Unset = UNSET
    area: float | Unset = UNSET
    box: BTBoundingBox1052 | Unset = UNSET
    bt_type: str | Unset = UNSET
    cosmetic_thread_metadata: BTCosmeticThreadMetadata3248 | Unset = UNSET
    decal_id_to_decal: BTExportModelFace1363DecalIdToDecal | Unset = UNSET
    face_properties: BTExportModelProperties3216 | Unset = UNSET
    id: str | Unset = UNSET
    loops: list[BTExportModelLoop1182] | Unset = UNSET
    orientation: bool | Unset = UNSET
    surface: BTSurfaceDescription1564 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appearance_property_node_id = self.appearance_property_node_id

        area = self.area

        box: dict[str, Any] | Unset = UNSET
        if not isinstance(self.box, Unset):
            box = self.box.to_dict()

        bt_type = self.bt_type

        cosmetic_thread_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cosmetic_thread_metadata, Unset):
            cosmetic_thread_metadata = self.cosmetic_thread_metadata.to_dict()

        decal_id_to_decal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decal_id_to_decal, Unset):
            decal_id_to_decal = self.decal_id_to_decal.to_dict()

        face_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.face_properties, Unset):
            face_properties = self.face_properties.to_dict()

        id = self.id

        loops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.loops, Unset):
            loops = []
            for loops_item_data in self.loops:
                loops_item = loops_item_data.to_dict()
                loops.append(loops_item)

        orientation = self.orientation

        surface: dict[str, Any] | Unset = UNSET
        if not isinstance(self.surface, Unset):
            surface = self.surface.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appearance_property_node_id is not UNSET:
            field_dict["appearancePropertyNodeId"] = appearance_property_node_id
        if area is not UNSET:
            field_dict["area"] = area
        if box is not UNSET:
            field_dict["box"] = box
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cosmetic_thread_metadata is not UNSET:
            field_dict["cosmeticThreadMetadata"] = cosmetic_thread_metadata
        if decal_id_to_decal is not UNSET:
            field_dict["decalIdToDecal"] = decal_id_to_decal
        if face_properties is not UNSET:
            field_dict["faceProperties"] = face_properties
        if id is not UNSET:
            field_dict["id"] = id
        if loops is not UNSET:
            field_dict["loops"] = loops
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if surface is not UNSET:
            field_dict["surface"] = surface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_bounding_box_1052 import BTBoundingBox1052
        from ..models.bt_cosmetic_thread_metadata_3248 import BTCosmeticThreadMetadata3248
        from ..models.bt_export_model_face_1363_decal_id_to_decal import BTExportModelFace1363DecalIdToDecal
        from ..models.bt_export_model_loop_1182 import BTExportModelLoop1182
        from ..models.bt_export_model_properties_3216 import BTExportModelProperties3216
        from ..models.bt_surface_description_1564 import BTSurfaceDescription1564

        d = dict(src_dict)
        appearance_property_node_id = d.pop("appearancePropertyNodeId", UNSET)

        area = d.pop("area", UNSET)

        _box = d.pop("box", UNSET)
        box: BTBoundingBox1052 | Unset
        if isinstance(_box, Unset):
            box = UNSET
        else:
            box = BTBoundingBox1052.from_dict(_box)

        bt_type = d.pop("btType", UNSET)

        _cosmetic_thread_metadata = d.pop("cosmeticThreadMetadata", UNSET)
        cosmetic_thread_metadata: BTCosmeticThreadMetadata3248 | Unset
        if isinstance(_cosmetic_thread_metadata, Unset):
            cosmetic_thread_metadata = UNSET
        else:
            cosmetic_thread_metadata = BTCosmeticThreadMetadata3248.from_dict(_cosmetic_thread_metadata)

        _decal_id_to_decal = d.pop("decalIdToDecal", UNSET)
        decal_id_to_decal: BTExportModelFace1363DecalIdToDecal | Unset
        if isinstance(_decal_id_to_decal, Unset):
            decal_id_to_decal = UNSET
        else:
            decal_id_to_decal = BTExportModelFace1363DecalIdToDecal.from_dict(_decal_id_to_decal)

        _face_properties = d.pop("faceProperties", UNSET)
        face_properties: BTExportModelProperties3216 | Unset
        if isinstance(_face_properties, Unset):
            face_properties = UNSET
        else:
            face_properties = BTExportModelProperties3216.from_dict(_face_properties)

        id = d.pop("id", UNSET)

        _loops = d.pop("loops", UNSET)
        loops: list[BTExportModelLoop1182] | Unset = UNSET
        if _loops is not UNSET:
            loops = []
            for loops_item_data in _loops:
                loops_item = BTExportModelLoop1182.from_dict(loops_item_data)

                loops.append(loops_item)

        orientation = d.pop("orientation", UNSET)

        _surface = d.pop("surface", UNSET)
        surface: BTSurfaceDescription1564 | Unset
        if isinstance(_surface, Unset):
            surface = UNSET
        else:
            surface = BTSurfaceDescription1564.from_dict(_surface)

        bt_export_model_face_1363 = cls(
            appearance_property_node_id=appearance_property_node_id,
            area=area,
            box=box,
            bt_type=bt_type,
            cosmetic_thread_metadata=cosmetic_thread_metadata,
            decal_id_to_decal=decal_id_to_decal,
            face_properties=face_properties,
            id=id,
            loops=loops,
            orientation=orientation,
            surface=surface,
        )

        bt_export_model_face_1363.additional_properties = d
        return bt_export_model_face_1363

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
