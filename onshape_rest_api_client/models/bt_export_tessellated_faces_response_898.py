from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_error_string_enum import GBTErrorStringEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_model_bodies_response_734 import BTExportModelBodiesResponse734
    from ..models.bt_export_tessellated_body_3398 import BTExportTessellatedBody3398
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_part_studio_display_data_346 import BTPartStudioDisplayData346
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTExportTessellatedFacesResponse898")


@_attrs_define
class BTExportTessellatedFacesResponse898:
    """
    Attributes:
        bodies (list[BTExportTessellatedBody3398] | Unset):
        bodies_info (BTExportModelBodiesResponse734 | Unset):
        bt_type (str | Unset): Type of JSON object.
        combine_composite_part_constituents (bool | Unset):
        display_data (BTPartStudioDisplayData346 | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        error_enum (GBTErrorStringEnum | Unset):
        facet_points (list[BTVector3D389] | Unset):
        full_element_id (BTFullElementId756 | Unset):
        output_face_appearances (bool | Unset):
        output_separate_face_nodes (bool | Unset):
    """

    bodies: list[BTExportTessellatedBody3398] | Unset = UNSET
    bodies_info: BTExportModelBodiesResponse734 | Unset = UNSET
    bt_type: str | Unset = UNSET
    combine_composite_part_constituents: bool | Unset = UNSET
    display_data: BTPartStudioDisplayData346 | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    error_enum: GBTErrorStringEnum | Unset = UNSET
    facet_points: list[BTVector3D389] | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    output_face_appearances: bool | Unset = UNSET
    output_separate_face_nodes: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bodies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bodies, Unset):
            bodies = []
            for bodies_item_data in self.bodies:
                bodies_item = bodies_item_data.to_dict()
                bodies.append(bodies_item)

        bodies_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bodies_info, Unset):
            bodies_info = self.bodies_info.to_dict()

        bt_type = self.bt_type

        combine_composite_part_constituents = self.combine_composite_part_constituents

        display_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display_data, Unset):
            display_data = self.display_data.to_dict()

        document_id = self.document_id

        element_id = self.element_id

        error_enum: str | Unset = UNSET
        if not isinstance(self.error_enum, Unset):
            error_enum = self.error_enum.value

        facet_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.facet_points, Unset):
            facet_points = []
            for facet_points_item_data in self.facet_points:
                facet_points_item = facet_points_item_data.to_dict()
                facet_points.append(facet_points_item)

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        output_face_appearances = self.output_face_appearances

        output_separate_face_nodes = self.output_separate_face_nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bodies is not UNSET:
            field_dict["bodies"] = bodies
        if bodies_info is not UNSET:
            field_dict["bodiesInfo"] = bodies_info
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if combine_composite_part_constituents is not UNSET:
            field_dict["combineCompositePartConstituents"] = combine_composite_part_constituents
        if display_data is not UNSET:
            field_dict["displayData"] = display_data
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if error_enum is not UNSET:
            field_dict["errorEnum"] = error_enum
        if facet_points is not UNSET:
            field_dict["facetPoints"] = facet_points
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if output_face_appearances is not UNSET:
            field_dict["outputFaceAppearances"] = output_face_appearances
        if output_separate_face_nodes is not UNSET:
            field_dict["outputSeparateFaceNodes"] = output_separate_face_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_model_bodies_response_734 import BTExportModelBodiesResponse734
        from ..models.bt_export_tessellated_body_3398 import BTExportTessellatedBody3398
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_part_studio_display_data_346 import BTPartStudioDisplayData346
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        _bodies = d.pop("bodies", UNSET)
        bodies: list[BTExportTessellatedBody3398] | Unset = UNSET
        if _bodies is not UNSET:
            bodies = []
            for bodies_item_data in _bodies:
                bodies_item = BTExportTessellatedBody3398.from_dict(bodies_item_data)

                bodies.append(bodies_item)

        _bodies_info = d.pop("bodiesInfo", UNSET)
        bodies_info: BTExportModelBodiesResponse734 | Unset
        if isinstance(_bodies_info, Unset):
            bodies_info = UNSET
        else:
            bodies_info = BTExportModelBodiesResponse734.from_dict(_bodies_info)

        bt_type = d.pop("btType", UNSET)

        combine_composite_part_constituents = d.pop("combineCompositePartConstituents", UNSET)

        _display_data = d.pop("displayData", UNSET)
        display_data: BTPartStudioDisplayData346 | Unset
        if isinstance(_display_data, Unset):
            display_data = UNSET
        else:
            display_data = BTPartStudioDisplayData346.from_dict(_display_data)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _error_enum = d.pop("errorEnum", UNSET)
        error_enum: GBTErrorStringEnum | Unset
        if isinstance(_error_enum, Unset):
            error_enum = UNSET
        else:
            error_enum = GBTErrorStringEnum(_error_enum)

        _facet_points = d.pop("facetPoints", UNSET)
        facet_points: list[BTVector3D389] | Unset = UNSET
        if _facet_points is not UNSET:
            facet_points = []
            for facet_points_item_data in _facet_points:
                facet_points_item = BTVector3D389.from_dict(facet_points_item_data)

                facet_points.append(facet_points_item)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        output_face_appearances = d.pop("outputFaceAppearances", UNSET)

        output_separate_face_nodes = d.pop("outputSeparateFaceNodes", UNSET)

        bt_export_tessellated_faces_response_898 = cls(
            bodies=bodies,
            bodies_info=bodies_info,
            bt_type=bt_type,
            combine_composite_part_constituents=combine_composite_part_constituents,
            display_data=display_data,
            document_id=document_id,
            element_id=element_id,
            error_enum=error_enum,
            facet_points=facet_points,
            full_element_id=full_element_id,
            output_face_appearances=output_face_appearances,
            output_separate_face_nodes=output_separate_face_nodes,
        )

        bt_export_tessellated_faces_response_898.additional_properties = d
        return bt_export_tessellated_faces_response_898

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
