from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_drawing_hidden_line_option import BTDrawingHiddenLineOption
from ..models.gbt_app_element_reference_type import GBTAppElementReferenceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_element_location_params import BTElementLocationParams


T = TypeVar("T", bound="BTDrawingParams")


@_attrs_define
class BTDrawingParams:
    """JSON schema for creating or updating a drawing.

    Attributes:
        border (bool | Unset): Set to `true` to include a border in the drawing. Default: False.
        compute_intersection (bool | Unset): Set to `true` to compute and display virtual edges (curves drawn where
            parts intersect). Leave as `false` to improve performance. Default: False.
        decimal_separator (str | Unset): `PERIOD` | `COMMA` Default: 'PERIOD'.
        display_state_id (str | Unset): Apply this display state's properties to the drawing.
        document_id (str | Unset): The document in which to create the drawing. If used, this value must match the
            document ID (`did`) value provided in the URL.
        document_microversion_id (str | Unset): Create a drawing of a part or assembly from this microversion.
        drawing_name (str | Unset): Provide a name for the drawing.
        element_configuration (str | Unset): Apply this configuration from the source element to the drawing.
        element_id (str | Unset): The id of the element in which to perform the operation.
        element_microversion_id (str | Unset): The id of the element microversion in which to perform the operation.
        explosion_id (str | Unset): Apply this exploded view to the drawing.
        external_document_id (str | Unset): Create a drawing of an element from this external document.
        external_document_version_id (str | Unset): Create a drawing of an element from this external document version.
        hidden_lines (BTDrawingHiddenLineOption | Unset):
        include_surfaces (bool | Unset): Set to `true` to include surfaces in the drawing. Default: False.
        include_wires (bool | Unset): Set to `true` to include wires in the drawing. Default: False.
        is_flattened_part (bool | Unset): Set to `true` if creating a drawing from a flattened part. Default: False.
        is_sketch_only (bool | Unset): Set to `true` if creating a drawing of a sketch. Default: False.
        is_surface (bool | Unset): Set to `true` if creating a drawing from a surface. Default: False.
        language (str | Unset): Set the language for the drawing. Accepts any ISO 639-1 standard language code. Default:
            'en-us'.
        location (BTElementLocationParams | Unset): The location at which the new element should be inserted.
        model_type (str | Unset): The type of model to include in the drawing: `partstudio` | `assembly`
        named_position_id (str | Unset): Apply this named view to the drawing.
        number_horizontal_zones (int | Unset): The number of horizontal zones to include in the drawing's graphics area.
            Default: 0. Example: 2.
        number_vertical_zones (int | Unset): The number of vertical zones to include in the drawing's graphics area.
            Default: 0. Example: 2.
        part_id (str | Unset): Include this part in the drawing.
        part_number (str | Unset): Include this part in the drawing.
        part_query (str | Unset): Include all parts found by the query in the drawing.
        projection (str | Unset): Apply this projection to the drawing.
        pure_sketch (bool | Unset): Set to `true` if creating the drawing of an empty sketch. Default: False.
        quality_option (str | Unset): `BEST_PERFORMANCE` | `BEST_QUALITY` | `BALANCED` | `ADAPTIVE`
        reference_type (int | Unset): Specify the type of element to create the drawing from. `0: UNKNOWN` | `1:
            PARTSTUDIO` | `2: ASSEMBLY` | `3: PART` | `4: FLATTENED_PART` | `5: COMPOSITE_PART` | `6: MESH_PART` | `7:
            SURFACE` | `8: SKETCH` | `9: CURVE`
        reference_type_enum (GBTAppElementReferenceType | Unset):
        revision (str | Unset): Create the drawing from this specific revision.
        show_cut_geom_only (bool | Unset): Set to `true` to show only cut geometry in the drawing. Default: False.
        simplification_option (str | Unset): `NONE` | `ABSOLUTE` | `RATIO_TO_MODEL` | `RATIO_TO_BODY` | `AUTOMATIC`
        simplification_threshold (float | Unset): `NONE` | `UNKNOWN` | `SMOOTH` | `DRAFTING`
        size (str | Unset): Provide a size for the drawing.
        sketch_ids (list[str] | Unset): Include these sketches in the drawing.
        standard (str | Unset): Provide the Standard to use in the drawing. Example: ANSI.
        start_zones (str | Unset): The zone in which to start the drawing. Example: A1.
        template_args (list[str] | Unset): Provide any additional arguments for the template being used for this
            drawing.
        template_document_id (str | Unset): Apply the template from this document to the drawing.
        template_element_id (str | Unset): Apply the template from this element to the drawing.
        template_name (str | Unset): Apply this template to the drawing.
        template_version_id (str | Unset): Apply the template from this version to the drawing.
        template_workspace_id (str | Unset): Apply the template from this workspace to the drawing.
        titleblock (bool | Unset): Set to `true` to include a title block in the drawing. Default: False.
        units (str | Unset): Units for the element: `METER` | `CENTIMETER` | `MILLIMETER` | `INCH` | `FOOT` | `YARD`
        views (str | Unset): Add these views to the drawing.
        workspace_id (str | Unset): Create a drawing of a part or assembly from this workspace.
    """

    border: bool | Unset = False
    compute_intersection: bool | Unset = False
    decimal_separator: str | Unset = "PERIOD"
    display_state_id: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_microversion_id: str | Unset = UNSET
    drawing_name: str | Unset = UNSET
    element_configuration: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_microversion_id: str | Unset = UNSET
    explosion_id: str | Unset = UNSET
    external_document_id: str | Unset = UNSET
    external_document_version_id: str | Unset = UNSET
    hidden_lines: BTDrawingHiddenLineOption | Unset = UNSET
    include_surfaces: bool | Unset = False
    include_wires: bool | Unset = False
    is_flattened_part: bool | Unset = False
    is_sketch_only: bool | Unset = False
    is_surface: bool | Unset = False
    language: str | Unset = "en-us"
    location: BTElementLocationParams | Unset = UNSET
    model_type: str | Unset = UNSET
    named_position_id: str | Unset = UNSET
    number_horizontal_zones: int | Unset = 0
    number_vertical_zones: int | Unset = 0
    part_id: str | Unset = UNSET
    part_number: str | Unset = UNSET
    part_query: str | Unset = UNSET
    projection: str | Unset = UNSET
    pure_sketch: bool | Unset = False
    quality_option: str | Unset = UNSET
    reference_type: int | Unset = UNSET
    reference_type_enum: GBTAppElementReferenceType | Unset = UNSET
    revision: str | Unset = UNSET
    show_cut_geom_only: bool | Unset = False
    simplification_option: str | Unset = UNSET
    simplification_threshold: float | Unset = UNSET
    size: str | Unset = UNSET
    sketch_ids: list[str] | Unset = UNSET
    standard: str | Unset = UNSET
    start_zones: str | Unset = UNSET
    template_args: list[str] | Unset = UNSET
    template_document_id: str | Unset = UNSET
    template_element_id: str | Unset = UNSET
    template_name: str | Unset = UNSET
    template_version_id: str | Unset = UNSET
    template_workspace_id: str | Unset = UNSET
    titleblock: bool | Unset = False
    units: str | Unset = UNSET
    views: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        border = self.border

        compute_intersection = self.compute_intersection

        decimal_separator = self.decimal_separator

        display_state_id = self.display_state_id

        document_id = self.document_id

        document_microversion_id = self.document_microversion_id

        drawing_name = self.drawing_name

        element_configuration = self.element_configuration

        element_id = self.element_id

        element_microversion_id = self.element_microversion_id

        explosion_id = self.explosion_id

        external_document_id = self.external_document_id

        external_document_version_id = self.external_document_version_id

        hidden_lines: str | Unset = UNSET
        if not isinstance(self.hidden_lines, Unset):
            hidden_lines = self.hidden_lines.value

        include_surfaces = self.include_surfaces

        include_wires = self.include_wires

        is_flattened_part = self.is_flattened_part

        is_sketch_only = self.is_sketch_only

        is_surface = self.is_surface

        language = self.language

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        model_type = self.model_type

        named_position_id = self.named_position_id

        number_horizontal_zones = self.number_horizontal_zones

        number_vertical_zones = self.number_vertical_zones

        part_id = self.part_id

        part_number = self.part_number

        part_query = self.part_query

        projection = self.projection

        pure_sketch = self.pure_sketch

        quality_option = self.quality_option

        reference_type = self.reference_type

        reference_type_enum: str | Unset = UNSET
        if not isinstance(self.reference_type_enum, Unset):
            reference_type_enum = self.reference_type_enum.value

        revision = self.revision

        show_cut_geom_only = self.show_cut_geom_only

        simplification_option = self.simplification_option

        simplification_threshold = self.simplification_threshold

        size = self.size

        sketch_ids: list[str] | Unset = UNSET
        if not isinstance(self.sketch_ids, Unset):
            sketch_ids = self.sketch_ids

        standard = self.standard

        start_zones = self.start_zones

        template_args: list[str] | Unset = UNSET
        if not isinstance(self.template_args, Unset):
            template_args = self.template_args

        template_document_id = self.template_document_id

        template_element_id = self.template_element_id

        template_name = self.template_name

        template_version_id = self.template_version_id

        template_workspace_id = self.template_workspace_id

        titleblock = self.titleblock

        units = self.units

        views = self.views

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if border is not UNSET:
            field_dict["border"] = border
        if compute_intersection is not UNSET:
            field_dict["computeIntersection"] = compute_intersection
        if decimal_separator is not UNSET:
            field_dict["decimalSeparator"] = decimal_separator
        if display_state_id is not UNSET:
            field_dict["displayStateId"] = display_state_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_microversion_id is not UNSET:
            field_dict["documentMicroversionId"] = document_microversion_id
        if drawing_name is not UNSET:
            field_dict["drawingName"] = drawing_name
        if element_configuration is not UNSET:
            field_dict["elementConfiguration"] = element_configuration
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_microversion_id is not UNSET:
            field_dict["elementMicroversionId"] = element_microversion_id
        if explosion_id is not UNSET:
            field_dict["explosionId"] = explosion_id
        if external_document_id is not UNSET:
            field_dict["externalDocumentId"] = external_document_id
        if external_document_version_id is not UNSET:
            field_dict["externalDocumentVersionId"] = external_document_version_id
        if hidden_lines is not UNSET:
            field_dict["hiddenLines"] = hidden_lines
        if include_surfaces is not UNSET:
            field_dict["includeSurfaces"] = include_surfaces
        if include_wires is not UNSET:
            field_dict["includeWires"] = include_wires
        if is_flattened_part is not UNSET:
            field_dict["isFlattenedPart"] = is_flattened_part
        if is_sketch_only is not UNSET:
            field_dict["isSketchOnly"] = is_sketch_only
        if is_surface is not UNSET:
            field_dict["isSurface"] = is_surface
        if language is not UNSET:
            field_dict["language"] = language
        if location is not UNSET:
            field_dict["location"] = location
        if model_type is not UNSET:
            field_dict["modelType"] = model_type
        if named_position_id is not UNSET:
            field_dict["namedPositionId"] = named_position_id
        if number_horizontal_zones is not UNSET:
            field_dict["numberHorizontalZones"] = number_horizontal_zones
        if number_vertical_zones is not UNSET:
            field_dict["numberVerticalZones"] = number_vertical_zones
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if part_query is not UNSET:
            field_dict["partQuery"] = part_query
        if projection is not UNSET:
            field_dict["projection"] = projection
        if pure_sketch is not UNSET:
            field_dict["pureSketch"] = pure_sketch
        if quality_option is not UNSET:
            field_dict["qualityOption"] = quality_option
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_type_enum is not UNSET:
            field_dict["referenceTypeEnum"] = reference_type_enum
        if revision is not UNSET:
            field_dict["revision"] = revision
        if show_cut_geom_only is not UNSET:
            field_dict["showCutGeomOnly"] = show_cut_geom_only
        if simplification_option is not UNSET:
            field_dict["simplificationOption"] = simplification_option
        if simplification_threshold is not UNSET:
            field_dict["simplificationThreshold"] = simplification_threshold
        if size is not UNSET:
            field_dict["size"] = size
        if sketch_ids is not UNSET:
            field_dict["sketchIds"] = sketch_ids
        if standard is not UNSET:
            field_dict["standard"] = standard
        if start_zones is not UNSET:
            field_dict["startZones"] = start_zones
        if template_args is not UNSET:
            field_dict["templateArgs"] = template_args
        if template_document_id is not UNSET:
            field_dict["templateDocumentId"] = template_document_id
        if template_element_id is not UNSET:
            field_dict["templateElementId"] = template_element_id
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if template_version_id is not UNSET:
            field_dict["templateVersionId"] = template_version_id
        if template_workspace_id is not UNSET:
            field_dict["templateWorkspaceId"] = template_workspace_id
        if titleblock is not UNSET:
            field_dict["titleblock"] = titleblock
        if units is not UNSET:
            field_dict["units"] = units
        if views is not UNSET:
            field_dict["views"] = views
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_element_location_params import BTElementLocationParams

        d = dict(src_dict)
        border = d.pop("border", UNSET)

        compute_intersection = d.pop("computeIntersection", UNSET)

        decimal_separator = d.pop("decimalSeparator", UNSET)

        display_state_id = d.pop("displayStateId", UNSET)

        document_id = d.pop("documentId", UNSET)

        document_microversion_id = d.pop("documentMicroversionId", UNSET)

        drawing_name = d.pop("drawingName", UNSET)

        element_configuration = d.pop("elementConfiguration", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_microversion_id = d.pop("elementMicroversionId", UNSET)

        explosion_id = d.pop("explosionId", UNSET)

        external_document_id = d.pop("externalDocumentId", UNSET)

        external_document_version_id = d.pop("externalDocumentVersionId", UNSET)

        _hidden_lines = d.pop("hiddenLines", UNSET)
        hidden_lines: BTDrawingHiddenLineOption | Unset
        if isinstance(_hidden_lines, Unset):
            hidden_lines = UNSET
        else:
            hidden_lines = BTDrawingHiddenLineOption(_hidden_lines)

        include_surfaces = d.pop("includeSurfaces", UNSET)

        include_wires = d.pop("includeWires", UNSET)

        is_flattened_part = d.pop("isFlattenedPart", UNSET)

        is_sketch_only = d.pop("isSketchOnly", UNSET)

        is_surface = d.pop("isSurface", UNSET)

        language = d.pop("language", UNSET)

        _location = d.pop("location", UNSET)
        location: BTElementLocationParams | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = BTElementLocationParams.from_dict(_location)

        model_type = d.pop("modelType", UNSET)

        named_position_id = d.pop("namedPositionId", UNSET)

        number_horizontal_zones = d.pop("numberHorizontalZones", UNSET)

        number_vertical_zones = d.pop("numberVerticalZones", UNSET)

        part_id = d.pop("partId", UNSET)

        part_number = d.pop("partNumber", UNSET)

        part_query = d.pop("partQuery", UNSET)

        projection = d.pop("projection", UNSET)

        pure_sketch = d.pop("pureSketch", UNSET)

        quality_option = d.pop("qualityOption", UNSET)

        reference_type = d.pop("referenceType", UNSET)

        _reference_type_enum = d.pop("referenceTypeEnum", UNSET)
        reference_type_enum: GBTAppElementReferenceType | Unset
        if isinstance(_reference_type_enum, Unset):
            reference_type_enum = UNSET
        else:
            reference_type_enum = GBTAppElementReferenceType(_reference_type_enum)

        revision = d.pop("revision", UNSET)

        show_cut_geom_only = d.pop("showCutGeomOnly", UNSET)

        simplification_option = d.pop("simplificationOption", UNSET)

        simplification_threshold = d.pop("simplificationThreshold", UNSET)

        size = d.pop("size", UNSET)

        sketch_ids = cast(list[str], d.pop("sketchIds", UNSET))

        standard = d.pop("standard", UNSET)

        start_zones = d.pop("startZones", UNSET)

        template_args = cast(list[str], d.pop("templateArgs", UNSET))

        template_document_id = d.pop("templateDocumentId", UNSET)

        template_element_id = d.pop("templateElementId", UNSET)

        template_name = d.pop("templateName", UNSET)

        template_version_id = d.pop("templateVersionId", UNSET)

        template_workspace_id = d.pop("templateWorkspaceId", UNSET)

        titleblock = d.pop("titleblock", UNSET)

        units = d.pop("units", UNSET)

        views = d.pop("views", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_drawing_params = cls(
            border=border,
            compute_intersection=compute_intersection,
            decimal_separator=decimal_separator,
            display_state_id=display_state_id,
            document_id=document_id,
            document_microversion_id=document_microversion_id,
            drawing_name=drawing_name,
            element_configuration=element_configuration,
            element_id=element_id,
            element_microversion_id=element_microversion_id,
            explosion_id=explosion_id,
            external_document_id=external_document_id,
            external_document_version_id=external_document_version_id,
            hidden_lines=hidden_lines,
            include_surfaces=include_surfaces,
            include_wires=include_wires,
            is_flattened_part=is_flattened_part,
            is_sketch_only=is_sketch_only,
            is_surface=is_surface,
            language=language,
            location=location,
            model_type=model_type,
            named_position_id=named_position_id,
            number_horizontal_zones=number_horizontal_zones,
            number_vertical_zones=number_vertical_zones,
            part_id=part_id,
            part_number=part_number,
            part_query=part_query,
            projection=projection,
            pure_sketch=pure_sketch,
            quality_option=quality_option,
            reference_type=reference_type,
            reference_type_enum=reference_type_enum,
            revision=revision,
            show_cut_geom_only=show_cut_geom_only,
            simplification_option=simplification_option,
            simplification_threshold=simplification_threshold,
            size=size,
            sketch_ids=sketch_ids,
            standard=standard,
            start_zones=start_zones,
            template_args=template_args,
            template_document_id=template_document_id,
            template_element_id=template_element_id,
            template_name=template_name,
            template_version_id=template_version_id,
            template_workspace_id=template_workspace_id,
            titleblock=titleblock,
            units=units,
            views=views,
            workspace_id=workspace_id,
        )

        bt_drawing_params.additional_properties = d
        return bt_drawing_params

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
