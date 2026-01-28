from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_translate_format_params_resolution import BTTranslateFormatParamsResolution
from ..models.gbt_parasolid_encoding_type import GBTParasolidEncodingType
from ..models.gbt_pre_process_parasolid_option import GBTPreProcessParasolidOption
from ..models.gbt_rhino_versions import GBTRhinoVersions
from ..models.gbt_stl_encoding_type import GBTStlEncodingType
from ..models.gbt_urdf_mesh_format import GBTUrdfMeshFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_parts_export_filter_4308 import BTPartsExportFilter4308


T = TypeVar("T", bound="BTTranslateFormatParams")


@_attrs_define
class BTTranslateFormatParams:
    """
    Attributes:
        format_name (str): The name of the file format.
        allow_faulty_parts (bool | Unset): If true, parts with faults are imported. If false, faulty parts are omitted.
            Default: False.
        angular_tolerance (float | Unset): Determines the maximum angular deviation, between the analytical surface and
            its triangulation. Lower values result in a finer geometry and higher values result in coarser geometry.
            Example: 0.001.
        blob_element_id (str | Unset):
        blob_microversion_id (str | Unset):
        cloud_object_id (str | Unset): Folder id where to store the exported model.
        cloud_storage_account_id (str | Unset): Account id to access the cloud storage.
        color_method (str | Unset):
        configuration (str | Unset): URL-encoded string of configuration values (separated by `;`). See the
            [Configurations API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for details.
        connection_id (str | Unset):
        create_composite (bool | Unset):
        current_sheet_only (bool | Unset):
        destination_name (str | Unset): The name of the exported file.
        distance_tolerance (float | Unset): Determines the maximum distance deviation, between the analytical surface
            and its triangulation. Lower values result in a finer geometry and higher values result in coarser geometry.
            Example: 0.001.
        dxf_version (str | Unset):
        element_id (str | Unset): The id of the element in which to perform the operation.
        element_ids (list[str] | Unset): An array of element ids for multi-element export.
        email_link (bool | Unset): Use `true` if a link in an email should be sent.
        email_message (str | Unset): Message to send in the email body along with the download link.
        email_subject (str | Unset): Subject to send the email with.
        email_to (list[str] | Unset): List of email addresses to send the email to.
        evaluate_export_rule (bool | Unset): Set to `true` to evaluate the export rule for the given `formatName` and to
            include an `exportRuleFileName` value in the response. Default: False.
        exclude_hidden_entities (bool | Unset): Whether or not to exclude hidden parts from export.
        exclude_off_sheet_content (bool | Unset):
        extract_assembly_hierarchy (bool | Unset):
        flat_pattern_async (bool | Unset):
        flatten (bool | Unset):
        flatten_assemblies (bool | Unset):
        foreign_id (str | Unset):
        from_user_id (str | Unset): Id of the user who does the export.
        gety_axis_is_up (bool | Unset):
        grouping (bool | Unset): Whether parts should be exported as a group or individually in a .zip file.
        hide_inspection_items (bool | Unset):
        ignore_export_rules_for_contents (bool | Unset): For multiple elements export, use `true` if export rule
            shouldn't be applied for all elements.
        image_height (int | Unset):
        image_width (int | Unset):
        import_appearances (bool | Unset):
        import_in_background (bool | Unset):
        import_material_density (bool | Unset):
        import_within_document (bool | Unset):
        include_bend_centerlines (bool | Unset):
        include_bend_lines (bool | Unset):
        include_cbore_csink (bool | Unset):
        include_export_ids (bool | Unset): Whether topology ids should be exported as parasolid attributes.
        include_formed_centermarks (bool | Unset):
        include_formed_outlines (bool | Unset):
        include_sketches (bool | Unset):
        join_adjacent_surfaces (bool | Unset):
        level (str | Unset):
        link_document_id (str | Unset): The id of the document through which the above document should be accessed; only
            applicable when accessing a version of the document. This allows a user who has access to document a to see data
            from document b, as long as document b has been linked to document a by a user who has permission to both.
        link_document_workspace_id (str | Unset): The id of the workspace through which the above document should be
            accessed; only applicable when accessing a version of the document. This allows a user who has access to
            document a to see data from document b, as long as document b has been linked to document a by a user who has
            permission to both.
        maximum_chord_length (float | Unset): Determines the maximum of a triangle edge length. Lower values result in a
            finer geometry and higher values result in coarser geometry. Example: 0.01.
        notify_user (bool | Unset): Send notification to the user client.
        occurrences_to_export (str | Unset): IDs of the occurrences to retrieve. Use comma-separated IDs for multiple
            instances (example: occurrencesToExport=JHK,JHD).
        one_part_per_doc (bool | Unset):
        original_foreign_id (str | Unset):
        parasolid_mode (GBTParasolidEncodingType | Unset): Export Parasolid in `BINARY` (.x_b) or `TEXT` (.x_t) mode.
        parent_id (str | Unset):
        part_ids (str | Unset): IDs of the parts to retrieve. Use comma-separated IDs for multiple parts (example:
            partIds=JHK,JHD).
        parts_export_filter (BTPartsExportFilter4308 | Unset): Skip mesh/curve foreign data creation in individual parts
            export
        password (str | Unset): A password to protect the email with.
        password_required (bool | Unset): Use `true` if the email should be protected with a password.
        pdf_version (str | Unset):
        processed_foreign_id (str | Unset):
        project_id (str | Unset):
        proxy_document_id (str | Unset):
        proxy_element_id (str | Unset):
        proxy_workspace_version (str | Unset):
        proxy_workspace_version_id (str | Unset):
        resolution (BTTranslateFormatParamsResolution | Unset): Determines export resolution of fine, medium, or coarse
            Example: fine.
        rhino_version (GBTRhinoVersions | Unset):
        selectable_pdf_text (bool | Unset):
        send_copy_to_me (bool | Unset): Use `true` if email copy should be sent to the user who does the export.
        sheet_indices (list[int] | Unset):
        sheet_metal_flat (bool | Unset):
        show_overridden_dimensions (bool | Unset):
        skip_bodyshop (bool | Unset):
        source_name (str | Unset):
        specify_material_data (bool | Unset):
        specify_units (bool | Unset):
        splines_as_polylines (bool | Unset):
        split_assemblies_into_multiple_documents (bool | Unset):
        step_parasolid_preprocessing_option (GBTPreProcessParasolidOption | Unset): Original geometry processing mode to
            improve results of translation to STEP.
        step_version_string (str | Unset): Export STEP in version: `AP242` | `AP203` | `AP214` Default: 'AP242'.
        stl_mode (GBTStlEncodingType | Unset): STL encoding type, `TEXT | BINARY`
        store_in_document (bool | Unset): Create a blob with exported file in the source document.
        text_as_geometry (bool | Unset):
        text_option (str | Unset):
        trigger_auto_download (bool | Unset): Automatically download a translated file.
        unit (str | Unset):
        upload_id (str | Unset):
        urdf_mesh_format (GBTUrdfMeshFormat | Unset):
        use_file_name_to_set_single_part_name (bool | Unset):
        use_gltf_compression (bool | Unset):
        use_iges_import_post_processing (bool | Unset):
        use_iges_compatibility_mode (bool | Unset):
        valid_for_days (int | Unset): Number of days to keep the link valid for.
        version_string (str | Unset): Parasolid version number as string. Use '0' for the latest. Default: '0'.
    """

    format_name: str
    allow_faulty_parts: bool | Unset = False
    angular_tolerance: float | Unset = UNSET
    blob_element_id: str | Unset = UNSET
    blob_microversion_id: str | Unset = UNSET
    cloud_object_id: str | Unset = UNSET
    cloud_storage_account_id: str | Unset = UNSET
    color_method: str | Unset = UNSET
    configuration: str | Unset = UNSET
    connection_id: str | Unset = UNSET
    create_composite: bool | Unset = UNSET
    current_sheet_only: bool | Unset = UNSET
    destination_name: str | Unset = UNSET
    distance_tolerance: float | Unset = UNSET
    dxf_version: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_ids: list[str] | Unset = UNSET
    email_link: bool | Unset = UNSET
    email_message: str | Unset = UNSET
    email_subject: str | Unset = UNSET
    email_to: list[str] | Unset = UNSET
    evaluate_export_rule: bool | Unset = False
    exclude_hidden_entities: bool | Unset = UNSET
    exclude_off_sheet_content: bool | Unset = UNSET
    extract_assembly_hierarchy: bool | Unset = UNSET
    flat_pattern_async: bool | Unset = UNSET
    flatten: bool | Unset = UNSET
    flatten_assemblies: bool | Unset = UNSET
    foreign_id: str | Unset = UNSET
    from_user_id: str | Unset = UNSET
    gety_axis_is_up: bool | Unset = UNSET
    grouping: bool | Unset = UNSET
    hide_inspection_items: bool | Unset = UNSET
    ignore_export_rules_for_contents: bool | Unset = UNSET
    image_height: int | Unset = UNSET
    image_width: int | Unset = UNSET
    import_appearances: bool | Unset = UNSET
    import_in_background: bool | Unset = UNSET
    import_material_density: bool | Unset = UNSET
    import_within_document: bool | Unset = UNSET
    include_bend_centerlines: bool | Unset = UNSET
    include_bend_lines: bool | Unset = UNSET
    include_cbore_csink: bool | Unset = UNSET
    include_export_ids: bool | Unset = UNSET
    include_formed_centermarks: bool | Unset = UNSET
    include_formed_outlines: bool | Unset = UNSET
    include_sketches: bool | Unset = UNSET
    join_adjacent_surfaces: bool | Unset = UNSET
    level: str | Unset = UNSET
    link_document_id: str | Unset = UNSET
    link_document_workspace_id: str | Unset = UNSET
    maximum_chord_length: float | Unset = UNSET
    notify_user: bool | Unset = UNSET
    occurrences_to_export: str | Unset = UNSET
    one_part_per_doc: bool | Unset = UNSET
    original_foreign_id: str | Unset = UNSET
    parasolid_mode: GBTParasolidEncodingType | Unset = UNSET
    parent_id: str | Unset = UNSET
    part_ids: str | Unset = UNSET
    parts_export_filter: BTPartsExportFilter4308 | Unset = UNSET
    password: str | Unset = UNSET
    password_required: bool | Unset = UNSET
    pdf_version: str | Unset = UNSET
    processed_foreign_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    proxy_document_id: str | Unset = UNSET
    proxy_element_id: str | Unset = UNSET
    proxy_workspace_version: str | Unset = UNSET
    proxy_workspace_version_id: str | Unset = UNSET
    resolution: BTTranslateFormatParamsResolution | Unset = UNSET
    rhino_version: GBTRhinoVersions | Unset = UNSET
    selectable_pdf_text: bool | Unset = UNSET
    send_copy_to_me: bool | Unset = UNSET
    sheet_indices: list[int] | Unset = UNSET
    sheet_metal_flat: bool | Unset = UNSET
    show_overridden_dimensions: bool | Unset = UNSET
    skip_bodyshop: bool | Unset = UNSET
    source_name: str | Unset = UNSET
    specify_material_data: bool | Unset = UNSET
    specify_units: bool | Unset = UNSET
    splines_as_polylines: bool | Unset = UNSET
    split_assemblies_into_multiple_documents: bool | Unset = UNSET
    step_parasolid_preprocessing_option: GBTPreProcessParasolidOption | Unset = UNSET
    step_version_string: str | Unset = "AP242"
    stl_mode: GBTStlEncodingType | Unset = UNSET
    store_in_document: bool | Unset = UNSET
    text_as_geometry: bool | Unset = UNSET
    text_option: str | Unset = UNSET
    trigger_auto_download: bool | Unset = UNSET
    unit: str | Unset = UNSET
    upload_id: str | Unset = UNSET
    urdf_mesh_format: GBTUrdfMeshFormat | Unset = UNSET
    use_file_name_to_set_single_part_name: bool | Unset = UNSET
    use_gltf_compression: bool | Unset = UNSET
    use_iges_import_post_processing: bool | Unset = UNSET
    use_iges_compatibility_mode: bool | Unset = UNSET
    valid_for_days: int | Unset = UNSET
    version_string: str | Unset = "0"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_name = self.format_name

        allow_faulty_parts = self.allow_faulty_parts

        angular_tolerance = self.angular_tolerance

        blob_element_id = self.blob_element_id

        blob_microversion_id = self.blob_microversion_id

        cloud_object_id = self.cloud_object_id

        cloud_storage_account_id = self.cloud_storage_account_id

        color_method = self.color_method

        configuration = self.configuration

        connection_id = self.connection_id

        create_composite = self.create_composite

        current_sheet_only = self.current_sheet_only

        destination_name = self.destination_name

        distance_tolerance = self.distance_tolerance

        dxf_version = self.dxf_version

        element_id = self.element_id

        element_ids: list[str] | Unset = UNSET
        if not isinstance(self.element_ids, Unset):
            element_ids = self.element_ids

        email_link = self.email_link

        email_message = self.email_message

        email_subject = self.email_subject

        email_to: list[str] | Unset = UNSET
        if not isinstance(self.email_to, Unset):
            email_to = self.email_to

        evaluate_export_rule = self.evaluate_export_rule

        exclude_hidden_entities = self.exclude_hidden_entities

        exclude_off_sheet_content = self.exclude_off_sheet_content

        extract_assembly_hierarchy = self.extract_assembly_hierarchy

        flat_pattern_async = self.flat_pattern_async

        flatten = self.flatten

        flatten_assemblies = self.flatten_assemblies

        foreign_id = self.foreign_id

        from_user_id = self.from_user_id

        gety_axis_is_up = self.gety_axis_is_up

        grouping = self.grouping

        hide_inspection_items = self.hide_inspection_items

        ignore_export_rules_for_contents = self.ignore_export_rules_for_contents

        image_height = self.image_height

        image_width = self.image_width

        import_appearances = self.import_appearances

        import_in_background = self.import_in_background

        import_material_density = self.import_material_density

        import_within_document = self.import_within_document

        include_bend_centerlines = self.include_bend_centerlines

        include_bend_lines = self.include_bend_lines

        include_cbore_csink = self.include_cbore_csink

        include_export_ids = self.include_export_ids

        include_formed_centermarks = self.include_formed_centermarks

        include_formed_outlines = self.include_formed_outlines

        include_sketches = self.include_sketches

        join_adjacent_surfaces = self.join_adjacent_surfaces

        level = self.level

        link_document_id = self.link_document_id

        link_document_workspace_id = self.link_document_workspace_id

        maximum_chord_length = self.maximum_chord_length

        notify_user = self.notify_user

        occurrences_to_export = self.occurrences_to_export

        one_part_per_doc = self.one_part_per_doc

        original_foreign_id = self.original_foreign_id

        parasolid_mode: str | Unset = UNSET
        if not isinstance(self.parasolid_mode, Unset):
            parasolid_mode = self.parasolid_mode.value

        parent_id = self.parent_id

        part_ids = self.part_ids

        parts_export_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parts_export_filter, Unset):
            parts_export_filter = self.parts_export_filter.to_dict()

        password = self.password

        password_required = self.password_required

        pdf_version = self.pdf_version

        processed_foreign_id = self.processed_foreign_id

        project_id = self.project_id

        proxy_document_id = self.proxy_document_id

        proxy_element_id = self.proxy_element_id

        proxy_workspace_version = self.proxy_workspace_version

        proxy_workspace_version_id = self.proxy_workspace_version_id

        resolution: str | Unset = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value

        rhino_version: str | Unset = UNSET
        if not isinstance(self.rhino_version, Unset):
            rhino_version = self.rhino_version.value

        selectable_pdf_text = self.selectable_pdf_text

        send_copy_to_me = self.send_copy_to_me

        sheet_indices: list[int] | Unset = UNSET
        if not isinstance(self.sheet_indices, Unset):
            sheet_indices = self.sheet_indices

        sheet_metal_flat = self.sheet_metal_flat

        show_overridden_dimensions = self.show_overridden_dimensions

        skip_bodyshop = self.skip_bodyshop

        source_name = self.source_name

        specify_material_data = self.specify_material_data

        specify_units = self.specify_units

        splines_as_polylines = self.splines_as_polylines

        split_assemblies_into_multiple_documents = self.split_assemblies_into_multiple_documents

        step_parasolid_preprocessing_option: str | Unset = UNSET
        if not isinstance(self.step_parasolid_preprocessing_option, Unset):
            step_parasolid_preprocessing_option = self.step_parasolid_preprocessing_option.value

        step_version_string = self.step_version_string

        stl_mode: str | Unset = UNSET
        if not isinstance(self.stl_mode, Unset):
            stl_mode = self.stl_mode.value

        store_in_document = self.store_in_document

        text_as_geometry = self.text_as_geometry

        text_option = self.text_option

        trigger_auto_download = self.trigger_auto_download

        unit = self.unit

        upload_id = self.upload_id

        urdf_mesh_format: str | Unset = UNSET
        if not isinstance(self.urdf_mesh_format, Unset):
            urdf_mesh_format = self.urdf_mesh_format.value

        use_file_name_to_set_single_part_name = self.use_file_name_to_set_single_part_name

        use_gltf_compression = self.use_gltf_compression

        use_iges_import_post_processing = self.use_iges_import_post_processing

        use_iges_compatibility_mode = self.use_iges_compatibility_mode

        valid_for_days = self.valid_for_days

        version_string = self.version_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formatName": format_name,
            }
        )
        if allow_faulty_parts is not UNSET:
            field_dict["allowFaultyParts"] = allow_faulty_parts
        if angular_tolerance is not UNSET:
            field_dict["angularTolerance"] = angular_tolerance
        if blob_element_id is not UNSET:
            field_dict["blobElementId"] = blob_element_id
        if blob_microversion_id is not UNSET:
            field_dict["blobMicroversionId"] = blob_microversion_id
        if cloud_object_id is not UNSET:
            field_dict["cloudObjectId"] = cloud_object_id
        if cloud_storage_account_id is not UNSET:
            field_dict["cloudStorageAccountId"] = cloud_storage_account_id
        if color_method is not UNSET:
            field_dict["colorMethod"] = color_method
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if create_composite is not UNSET:
            field_dict["createComposite"] = create_composite
        if current_sheet_only is not UNSET:
            field_dict["currentSheetOnly"] = current_sheet_only
        if destination_name is not UNSET:
            field_dict["destinationName"] = destination_name
        if distance_tolerance is not UNSET:
            field_dict["distanceTolerance"] = distance_tolerance
        if dxf_version is not UNSET:
            field_dict["dxfVersion"] = dxf_version
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_ids is not UNSET:
            field_dict["elementIds"] = element_ids
        if email_link is not UNSET:
            field_dict["emailLink"] = email_link
        if email_message is not UNSET:
            field_dict["emailMessage"] = email_message
        if email_subject is not UNSET:
            field_dict["emailSubject"] = email_subject
        if email_to is not UNSET:
            field_dict["emailTo"] = email_to
        if evaluate_export_rule is not UNSET:
            field_dict["evaluateExportRule"] = evaluate_export_rule
        if exclude_hidden_entities is not UNSET:
            field_dict["excludeHiddenEntities"] = exclude_hidden_entities
        if exclude_off_sheet_content is not UNSET:
            field_dict["excludeOffSheetContent"] = exclude_off_sheet_content
        if extract_assembly_hierarchy is not UNSET:
            field_dict["extractAssemblyHierarchy"] = extract_assembly_hierarchy
        if flat_pattern_async is not UNSET:
            field_dict["flatPatternAsync"] = flat_pattern_async
        if flatten is not UNSET:
            field_dict["flatten"] = flatten
        if flatten_assemblies is not UNSET:
            field_dict["flattenAssemblies"] = flatten_assemblies
        if foreign_id is not UNSET:
            field_dict["foreignId"] = foreign_id
        if from_user_id is not UNSET:
            field_dict["fromUserId"] = from_user_id
        if gety_axis_is_up is not UNSET:
            field_dict["getyAxisIsUp"] = gety_axis_is_up
        if grouping is not UNSET:
            field_dict["grouping"] = grouping
        if hide_inspection_items is not UNSET:
            field_dict["hideInspectionItems"] = hide_inspection_items
        if ignore_export_rules_for_contents is not UNSET:
            field_dict["ignoreExportRulesForContents"] = ignore_export_rules_for_contents
        if image_height is not UNSET:
            field_dict["imageHeight"] = image_height
        if image_width is not UNSET:
            field_dict["imageWidth"] = image_width
        if import_appearances is not UNSET:
            field_dict["importAppearances"] = import_appearances
        if import_in_background is not UNSET:
            field_dict["importInBackground"] = import_in_background
        if import_material_density is not UNSET:
            field_dict["importMaterialDensity"] = import_material_density
        if import_within_document is not UNSET:
            field_dict["importWithinDocument"] = import_within_document
        if include_bend_centerlines is not UNSET:
            field_dict["includeBendCenterlines"] = include_bend_centerlines
        if include_bend_lines is not UNSET:
            field_dict["includeBendLines"] = include_bend_lines
        if include_cbore_csink is not UNSET:
            field_dict["includeCboreCsink"] = include_cbore_csink
        if include_export_ids is not UNSET:
            field_dict["includeExportIds"] = include_export_ids
        if include_formed_centermarks is not UNSET:
            field_dict["includeFormedCentermarks"] = include_formed_centermarks
        if include_formed_outlines is not UNSET:
            field_dict["includeFormedOutlines"] = include_formed_outlines
        if include_sketches is not UNSET:
            field_dict["includeSketches"] = include_sketches
        if join_adjacent_surfaces is not UNSET:
            field_dict["joinAdjacentSurfaces"] = join_adjacent_surfaces
        if level is not UNSET:
            field_dict["level"] = level
        if link_document_id is not UNSET:
            field_dict["linkDocumentId"] = link_document_id
        if link_document_workspace_id is not UNSET:
            field_dict["linkDocumentWorkspaceId"] = link_document_workspace_id
        if maximum_chord_length is not UNSET:
            field_dict["maximumChordLength"] = maximum_chord_length
        if notify_user is not UNSET:
            field_dict["notifyUser"] = notify_user
        if occurrences_to_export is not UNSET:
            field_dict["occurrencesToExport"] = occurrences_to_export
        if one_part_per_doc is not UNSET:
            field_dict["onePartPerDoc"] = one_part_per_doc
        if original_foreign_id is not UNSET:
            field_dict["originalForeignId"] = original_foreign_id
        if parasolid_mode is not UNSET:
            field_dict["parasolidMode"] = parasolid_mode
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if part_ids is not UNSET:
            field_dict["partIds"] = part_ids
        if parts_export_filter is not UNSET:
            field_dict["partsExportFilter"] = parts_export_filter
        if password is not UNSET:
            field_dict["password"] = password
        if password_required is not UNSET:
            field_dict["passwordRequired"] = password_required
        if pdf_version is not UNSET:
            field_dict["pdfVersion"] = pdf_version
        if processed_foreign_id is not UNSET:
            field_dict["processedForeignId"] = processed_foreign_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if proxy_document_id is not UNSET:
            field_dict["proxyDocumentId"] = proxy_document_id
        if proxy_element_id is not UNSET:
            field_dict["proxyElementId"] = proxy_element_id
        if proxy_workspace_version is not UNSET:
            field_dict["proxyWorkspaceVersion"] = proxy_workspace_version
        if proxy_workspace_version_id is not UNSET:
            field_dict["proxyWorkspaceVersionId"] = proxy_workspace_version_id
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if rhino_version is not UNSET:
            field_dict["rhinoVersion"] = rhino_version
        if selectable_pdf_text is not UNSET:
            field_dict["selectablePdfText"] = selectable_pdf_text
        if send_copy_to_me is not UNSET:
            field_dict["sendCopyToMe"] = send_copy_to_me
        if sheet_indices is not UNSET:
            field_dict["sheetIndices"] = sheet_indices
        if sheet_metal_flat is not UNSET:
            field_dict["sheetMetalFlat"] = sheet_metal_flat
        if show_overridden_dimensions is not UNSET:
            field_dict["showOverriddenDimensions"] = show_overridden_dimensions
        if skip_bodyshop is not UNSET:
            field_dict["skipBodyshop"] = skip_bodyshop
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if specify_material_data is not UNSET:
            field_dict["specifyMaterialData"] = specify_material_data
        if specify_units is not UNSET:
            field_dict["specifyUnits"] = specify_units
        if splines_as_polylines is not UNSET:
            field_dict["splinesAsPolylines"] = splines_as_polylines
        if split_assemblies_into_multiple_documents is not UNSET:
            field_dict["splitAssembliesIntoMultipleDocuments"] = split_assemblies_into_multiple_documents
        if step_parasolid_preprocessing_option is not UNSET:
            field_dict["stepParasolidPreprocessingOption"] = step_parasolid_preprocessing_option
        if step_version_string is not UNSET:
            field_dict["stepVersionString"] = step_version_string
        if stl_mode is not UNSET:
            field_dict["stlMode"] = stl_mode
        if store_in_document is not UNSET:
            field_dict["storeInDocument"] = store_in_document
        if text_as_geometry is not UNSET:
            field_dict["textAsGeometry"] = text_as_geometry
        if text_option is not UNSET:
            field_dict["textOption"] = text_option
        if trigger_auto_download is not UNSET:
            field_dict["triggerAutoDownload"] = trigger_auto_download
        if unit is not UNSET:
            field_dict["unit"] = unit
        if upload_id is not UNSET:
            field_dict["uploadId"] = upload_id
        if urdf_mesh_format is not UNSET:
            field_dict["urdfMeshFormat"] = urdf_mesh_format
        if use_file_name_to_set_single_part_name is not UNSET:
            field_dict["useFileNameToSetSinglePartName"] = use_file_name_to_set_single_part_name
        if use_gltf_compression is not UNSET:
            field_dict["useGltfCompression"] = use_gltf_compression
        if use_iges_import_post_processing is not UNSET:
            field_dict["useIGESImportPostProcessing"] = use_iges_import_post_processing
        if use_iges_compatibility_mode is not UNSET:
            field_dict["useIgesCompatibilityMode"] = use_iges_compatibility_mode
        if valid_for_days is not UNSET:
            field_dict["validForDays"] = valid_for_days
        if version_string is not UNSET:
            field_dict["versionString"] = version_string

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parts_export_filter_4308 import BTPartsExportFilter4308

        d = dict(src_dict)
        format_name = d.pop("formatName")

        allow_faulty_parts = d.pop("allowFaultyParts", UNSET)

        angular_tolerance = d.pop("angularTolerance", UNSET)

        blob_element_id = d.pop("blobElementId", UNSET)

        blob_microversion_id = d.pop("blobMicroversionId", UNSET)

        cloud_object_id = d.pop("cloudObjectId", UNSET)

        cloud_storage_account_id = d.pop("cloudStorageAccountId", UNSET)

        color_method = d.pop("colorMethod", UNSET)

        configuration = d.pop("configuration", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        create_composite = d.pop("createComposite", UNSET)

        current_sheet_only = d.pop("currentSheetOnly", UNSET)

        destination_name = d.pop("destinationName", UNSET)

        distance_tolerance = d.pop("distanceTolerance", UNSET)

        dxf_version = d.pop("dxfVersion", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_ids = cast(list[str], d.pop("elementIds", UNSET))

        email_link = d.pop("emailLink", UNSET)

        email_message = d.pop("emailMessage", UNSET)

        email_subject = d.pop("emailSubject", UNSET)

        email_to = cast(list[str], d.pop("emailTo", UNSET))

        evaluate_export_rule = d.pop("evaluateExportRule", UNSET)

        exclude_hidden_entities = d.pop("excludeHiddenEntities", UNSET)

        exclude_off_sheet_content = d.pop("excludeOffSheetContent", UNSET)

        extract_assembly_hierarchy = d.pop("extractAssemblyHierarchy", UNSET)

        flat_pattern_async = d.pop("flatPatternAsync", UNSET)

        flatten = d.pop("flatten", UNSET)

        flatten_assemblies = d.pop("flattenAssemblies", UNSET)

        foreign_id = d.pop("foreignId", UNSET)

        from_user_id = d.pop("fromUserId", UNSET)

        gety_axis_is_up = d.pop("getyAxisIsUp", UNSET)

        grouping = d.pop("grouping", UNSET)

        hide_inspection_items = d.pop("hideInspectionItems", UNSET)

        ignore_export_rules_for_contents = d.pop("ignoreExportRulesForContents", UNSET)

        image_height = d.pop("imageHeight", UNSET)

        image_width = d.pop("imageWidth", UNSET)

        import_appearances = d.pop("importAppearances", UNSET)

        import_in_background = d.pop("importInBackground", UNSET)

        import_material_density = d.pop("importMaterialDensity", UNSET)

        import_within_document = d.pop("importWithinDocument", UNSET)

        include_bend_centerlines = d.pop("includeBendCenterlines", UNSET)

        include_bend_lines = d.pop("includeBendLines", UNSET)

        include_cbore_csink = d.pop("includeCboreCsink", UNSET)

        include_export_ids = d.pop("includeExportIds", UNSET)

        include_formed_centermarks = d.pop("includeFormedCentermarks", UNSET)

        include_formed_outlines = d.pop("includeFormedOutlines", UNSET)

        include_sketches = d.pop("includeSketches", UNSET)

        join_adjacent_surfaces = d.pop("joinAdjacentSurfaces", UNSET)

        level = d.pop("level", UNSET)

        link_document_id = d.pop("linkDocumentId", UNSET)

        link_document_workspace_id = d.pop("linkDocumentWorkspaceId", UNSET)

        maximum_chord_length = d.pop("maximumChordLength", UNSET)

        notify_user = d.pop("notifyUser", UNSET)

        occurrences_to_export = d.pop("occurrencesToExport", UNSET)

        one_part_per_doc = d.pop("onePartPerDoc", UNSET)

        original_foreign_id = d.pop("originalForeignId", UNSET)

        _parasolid_mode = d.pop("parasolidMode", UNSET)
        parasolid_mode: GBTParasolidEncodingType | Unset
        if isinstance(_parasolid_mode, Unset):
            parasolid_mode = UNSET
        else:
            parasolid_mode = GBTParasolidEncodingType(_parasolid_mode)

        parent_id = d.pop("parentId", UNSET)

        part_ids = d.pop("partIds", UNSET)

        _parts_export_filter = d.pop("partsExportFilter", UNSET)
        parts_export_filter: BTPartsExportFilter4308 | Unset
        if isinstance(_parts_export_filter, Unset):
            parts_export_filter = UNSET
        else:
            parts_export_filter = BTPartsExportFilter4308.from_dict(_parts_export_filter)

        password = d.pop("password", UNSET)

        password_required = d.pop("passwordRequired", UNSET)

        pdf_version = d.pop("pdfVersion", UNSET)

        processed_foreign_id = d.pop("processedForeignId", UNSET)

        project_id = d.pop("projectId", UNSET)

        proxy_document_id = d.pop("proxyDocumentId", UNSET)

        proxy_element_id = d.pop("proxyElementId", UNSET)

        proxy_workspace_version = d.pop("proxyWorkspaceVersion", UNSET)

        proxy_workspace_version_id = d.pop("proxyWorkspaceVersionId", UNSET)

        _resolution = d.pop("resolution", UNSET)
        resolution: BTTranslateFormatParamsResolution | Unset
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = BTTranslateFormatParamsResolution(_resolution)

        _rhino_version = d.pop("rhinoVersion", UNSET)
        rhino_version: GBTRhinoVersions | Unset
        if isinstance(_rhino_version, Unset):
            rhino_version = UNSET
        else:
            rhino_version = GBTRhinoVersions(_rhino_version)

        selectable_pdf_text = d.pop("selectablePdfText", UNSET)

        send_copy_to_me = d.pop("sendCopyToMe", UNSET)

        sheet_indices = cast(list[int], d.pop("sheetIndices", UNSET))

        sheet_metal_flat = d.pop("sheetMetalFlat", UNSET)

        show_overridden_dimensions = d.pop("showOverriddenDimensions", UNSET)

        skip_bodyshop = d.pop("skipBodyshop", UNSET)

        source_name = d.pop("sourceName", UNSET)

        specify_material_data = d.pop("specifyMaterialData", UNSET)

        specify_units = d.pop("specifyUnits", UNSET)

        splines_as_polylines = d.pop("splinesAsPolylines", UNSET)

        split_assemblies_into_multiple_documents = d.pop("splitAssembliesIntoMultipleDocuments", UNSET)

        _step_parasolid_preprocessing_option = d.pop("stepParasolidPreprocessingOption", UNSET)
        step_parasolid_preprocessing_option: GBTPreProcessParasolidOption | Unset
        if isinstance(_step_parasolid_preprocessing_option, Unset):
            step_parasolid_preprocessing_option = UNSET
        else:
            step_parasolid_preprocessing_option = GBTPreProcessParasolidOption(_step_parasolid_preprocessing_option)

        step_version_string = d.pop("stepVersionString", UNSET)

        _stl_mode = d.pop("stlMode", UNSET)
        stl_mode: GBTStlEncodingType | Unset
        if isinstance(_stl_mode, Unset):
            stl_mode = UNSET
        else:
            stl_mode = GBTStlEncodingType(_stl_mode)

        store_in_document = d.pop("storeInDocument", UNSET)

        text_as_geometry = d.pop("textAsGeometry", UNSET)

        text_option = d.pop("textOption", UNSET)

        trigger_auto_download = d.pop("triggerAutoDownload", UNSET)

        unit = d.pop("unit", UNSET)

        upload_id = d.pop("uploadId", UNSET)

        _urdf_mesh_format = d.pop("urdfMeshFormat", UNSET)
        urdf_mesh_format: GBTUrdfMeshFormat | Unset
        if isinstance(_urdf_mesh_format, Unset):
            urdf_mesh_format = UNSET
        else:
            urdf_mesh_format = GBTUrdfMeshFormat(_urdf_mesh_format)

        use_file_name_to_set_single_part_name = d.pop("useFileNameToSetSinglePartName", UNSET)

        use_gltf_compression = d.pop("useGltfCompression", UNSET)

        use_iges_import_post_processing = d.pop("useIGESImportPostProcessing", UNSET)

        use_iges_compatibility_mode = d.pop("useIgesCompatibilityMode", UNSET)

        valid_for_days = d.pop("validForDays", UNSET)

        version_string = d.pop("versionString", UNSET)

        bt_translate_format_params = cls(
            format_name=format_name,
            allow_faulty_parts=allow_faulty_parts,
            angular_tolerance=angular_tolerance,
            blob_element_id=blob_element_id,
            blob_microversion_id=blob_microversion_id,
            cloud_object_id=cloud_object_id,
            cloud_storage_account_id=cloud_storage_account_id,
            color_method=color_method,
            configuration=configuration,
            connection_id=connection_id,
            create_composite=create_composite,
            current_sheet_only=current_sheet_only,
            destination_name=destination_name,
            distance_tolerance=distance_tolerance,
            dxf_version=dxf_version,
            element_id=element_id,
            element_ids=element_ids,
            email_link=email_link,
            email_message=email_message,
            email_subject=email_subject,
            email_to=email_to,
            evaluate_export_rule=evaluate_export_rule,
            exclude_hidden_entities=exclude_hidden_entities,
            exclude_off_sheet_content=exclude_off_sheet_content,
            extract_assembly_hierarchy=extract_assembly_hierarchy,
            flat_pattern_async=flat_pattern_async,
            flatten=flatten,
            flatten_assemblies=flatten_assemblies,
            foreign_id=foreign_id,
            from_user_id=from_user_id,
            gety_axis_is_up=gety_axis_is_up,
            grouping=grouping,
            hide_inspection_items=hide_inspection_items,
            ignore_export_rules_for_contents=ignore_export_rules_for_contents,
            image_height=image_height,
            image_width=image_width,
            import_appearances=import_appearances,
            import_in_background=import_in_background,
            import_material_density=import_material_density,
            import_within_document=import_within_document,
            include_bend_centerlines=include_bend_centerlines,
            include_bend_lines=include_bend_lines,
            include_cbore_csink=include_cbore_csink,
            include_export_ids=include_export_ids,
            include_formed_centermarks=include_formed_centermarks,
            include_formed_outlines=include_formed_outlines,
            include_sketches=include_sketches,
            join_adjacent_surfaces=join_adjacent_surfaces,
            level=level,
            link_document_id=link_document_id,
            link_document_workspace_id=link_document_workspace_id,
            maximum_chord_length=maximum_chord_length,
            notify_user=notify_user,
            occurrences_to_export=occurrences_to_export,
            one_part_per_doc=one_part_per_doc,
            original_foreign_id=original_foreign_id,
            parasolid_mode=parasolid_mode,
            parent_id=parent_id,
            part_ids=part_ids,
            parts_export_filter=parts_export_filter,
            password=password,
            password_required=password_required,
            pdf_version=pdf_version,
            processed_foreign_id=processed_foreign_id,
            project_id=project_id,
            proxy_document_id=proxy_document_id,
            proxy_element_id=proxy_element_id,
            proxy_workspace_version=proxy_workspace_version,
            proxy_workspace_version_id=proxy_workspace_version_id,
            resolution=resolution,
            rhino_version=rhino_version,
            selectable_pdf_text=selectable_pdf_text,
            send_copy_to_me=send_copy_to_me,
            sheet_indices=sheet_indices,
            sheet_metal_flat=sheet_metal_flat,
            show_overridden_dimensions=show_overridden_dimensions,
            skip_bodyshop=skip_bodyshop,
            source_name=source_name,
            specify_material_data=specify_material_data,
            specify_units=specify_units,
            splines_as_polylines=splines_as_polylines,
            split_assemblies_into_multiple_documents=split_assemblies_into_multiple_documents,
            step_parasolid_preprocessing_option=step_parasolid_preprocessing_option,
            step_version_string=step_version_string,
            stl_mode=stl_mode,
            store_in_document=store_in_document,
            text_as_geometry=text_as_geometry,
            text_option=text_option,
            trigger_auto_download=trigger_auto_download,
            unit=unit,
            upload_id=upload_id,
            urdf_mesh_format=urdf_mesh_format,
            use_file_name_to_set_single_part_name=use_file_name_to_set_single_part_name,
            use_gltf_compression=use_gltf_compression,
            use_iges_import_post_processing=use_iges_import_post_processing,
            use_iges_compatibility_mode=use_iges_compatibility_mode,
            valid_for_days=valid_for_days,
            version_string=version_string,
        )

        bt_translate_format_params.additional_properties = d
        return bt_translate_format_params

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
