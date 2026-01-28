from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_body_type import GBTBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_tessellated_faces_face_1192 import BTExportTessellatedFacesFace1192
    from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTExportTessellatedFacesBody1321")


@_attrs_define
class BTExportTessellatedFacesBody1321:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        constituents (list[str] | Unset):
        id (str | Unset):
        name (str | Unset):
        appearance (BTGraphicsAppearance1152 | Unset):
        body_type (GBTBodyType | Unset):
        faces (list[BTExportTessellatedFacesFace1192] | Unset):
        facet_points (list[BTVector3D389] | Unset):
    """

    bt_type: str | Unset = UNSET
    constituents: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    appearance: BTGraphicsAppearance1152 | Unset = UNSET
    body_type: GBTBodyType | Unset = UNSET
    faces: list[BTExportTessellatedFacesFace1192] | Unset = UNSET
    facet_points: list[BTVector3D389] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        constituents: list[str] | Unset = UNSET
        if not isinstance(self.constituents, Unset):
            constituents = self.constituents

        id = self.id

        name = self.name

        appearance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        body_type: str | Unset = UNSET
        if not isinstance(self.body_type, Unset):
            body_type = self.body_type.value

        faces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.faces, Unset):
            faces = []
            for faces_item_data in self.faces:
                faces_item = faces_item_data.to_dict()
                faces.append(faces_item)

        facet_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.facet_points, Unset):
            facet_points = []
            for facet_points_item_data in self.facet_points:
                facet_points_item = facet_points_item_data.to_dict()
                facet_points.append(facet_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if constituents is not UNSET:
            field_dict["constituents"] = constituents
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type
        if faces is not UNSET:
            field_dict["faces"] = faces
        if facet_points is not UNSET:
            field_dict["facetPoints"] = facet_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_tessellated_faces_face_1192 import BTExportTessellatedFacesFace1192
        from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        constituents = cast(list[str], d.pop("constituents", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _appearance = d.pop("appearance", UNSET)
        appearance: BTGraphicsAppearance1152 | Unset
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = BTGraphicsAppearance1152.from_dict(_appearance)

        _body_type = d.pop("bodyType", UNSET)
        body_type: GBTBodyType | Unset
        if isinstance(_body_type, Unset):
            body_type = UNSET
        else:
            body_type = GBTBodyType(_body_type)

        _faces = d.pop("faces", UNSET)
        faces: list[BTExportTessellatedFacesFace1192] | Unset = UNSET
        if _faces is not UNSET:
            faces = []
            for faces_item_data in _faces:
                faces_item = BTExportTessellatedFacesFace1192.from_dict(faces_item_data)

                faces.append(faces_item)

        _facet_points = d.pop("facetPoints", UNSET)
        facet_points: list[BTVector3D389] | Unset = UNSET
        if _facet_points is not UNSET:
            facet_points = []
            for facet_points_item_data in _facet_points:
                facet_points_item = BTVector3D389.from_dict(facet_points_item_data)

                facet_points.append(facet_points_item)

        bt_export_tessellated_faces_body_1321 = cls(
            bt_type=bt_type,
            constituents=constituents,
            id=id,
            name=name,
            appearance=appearance,
            body_type=body_type,
            faces=faces,
            facet_points=facet_points,
        )

        bt_export_tessellated_faces_body_1321.additional_properties = d
        return bt_export_tessellated_faces_body_1321

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
