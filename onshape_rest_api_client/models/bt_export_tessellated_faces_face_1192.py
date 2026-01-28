from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_tessellated_faces_facet_1417 import BTExportTessellatedFacesFacet1417
    from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152


T = TypeVar("T", bound="BTExportTessellatedFacesFace1192")


@_attrs_define
class BTExportTessellatedFacesFace1192:
    """
    Attributes:
        appearance (BTGraphicsAppearance1152 | Unset):
        appearance_source_id (str | Unset):
        appearance_source_name (str | Unset):
        bt_type (str | Unset): Type of JSON object.
        error_message (str | Unset):
        facets (list[BTExportTessellatedFacesFacet1417] | Unset):
        id (str | Unset):
    """

    appearance: BTGraphicsAppearance1152 | Unset = UNSET
    appearance_source_id: str | Unset = UNSET
    appearance_source_name: str | Unset = UNSET
    bt_type: str | Unset = UNSET
    error_message: str | Unset = UNSET
    facets: list[BTExportTessellatedFacesFacet1417] | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appearance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        appearance_source_id = self.appearance_source_id

        appearance_source_name = self.appearance_source_name

        bt_type = self.bt_type

        error_message = self.error_message

        facets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.facets, Unset):
            facets = []
            for facets_item_data in self.facets:
                facets_item = facets_item_data.to_dict()
                facets.append(facets_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if appearance_source_id is not UNSET:
            field_dict["appearanceSourceId"] = appearance_source_id
        if appearance_source_name is not UNSET:
            field_dict["appearanceSourceName"] = appearance_source_name
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if facets is not UNSET:
            field_dict["facets"] = facets
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_tessellated_faces_facet_1417 import BTExportTessellatedFacesFacet1417
        from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152

        d = dict(src_dict)
        _appearance = d.pop("appearance", UNSET)
        appearance: BTGraphicsAppearance1152 | Unset
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = BTGraphicsAppearance1152.from_dict(_appearance)

        appearance_source_id = d.pop("appearanceSourceId", UNSET)

        appearance_source_name = d.pop("appearanceSourceName", UNSET)

        bt_type = d.pop("btType", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        _facets = d.pop("facets", UNSET)
        facets: list[BTExportTessellatedFacesFacet1417] | Unset = UNSET
        if _facets is not UNSET:
            facets = []
            for facets_item_data in _facets:
                facets_item = BTExportTessellatedFacesFacet1417.from_dict(facets_item_data)

                facets.append(facets_item)

        id = d.pop("id", UNSET)

        bt_export_tessellated_faces_face_1192 = cls(
            appearance=appearance,
            appearance_source_id=appearance_source_id,
            appearance_source_name=appearance_source_name,
            bt_type=bt_type,
            error_message=error_message,
            facets=facets,
            id=id,
        )

        bt_export_tessellated_faces_face_1192.additional_properties = d
        return bt_export_tessellated_faces_face_1192

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
