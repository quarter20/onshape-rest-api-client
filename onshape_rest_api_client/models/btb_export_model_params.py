from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTBExportModelParams")


@_attrs_define
class BTBExportModelParams:
    """Onshape document export schema

    Attributes:
        document_id (str):
        format_ (str):
        angle_tolerance (float | Unset):
        batch_all_flat_patterns (bool | Unset):
        batch_flat_patterns (bool | Unset):
        chord_tolerance (float | Unset):
        cloud_object_id (str | Unset):
        cloud_storage_account_id (str | Unset):
        configuration (str | Unset):
        destination_name (str | Unset):
        document_version_id (str | Unset):
        element_id (str | Unset):
        element_ids (str | Unset):
        email_link (bool | Unset):
        email_message (str | Unset):
        email_subject (str | Unset):
        email_to (str | Unset): Base64-encoded email address. When sending an email, the `fromUserId` parameter is also
            required.
        exclude_hidden_entities (bool | Unset): If `true`, the exported file won't have any parts and assemblies marked
            as hidden
        feature_ids (str | Unset):
        flat_pattern_async (bool | Unset): If `true`, flat pattern export being called via async
        flatten (bool | Unset):
        from_user_id (str | Unset): Your user ID. Required when providing the `emailTo` parameter.
        grouping (str | Unset):
        ignore_export_rules_for_contents (bool | Unset):
        include_bend_centerlines (bool | Unset):
        include_bend_lines (bool | Unset):
        include_cbore_csink (bool | Unset):
        include_export_ids (bool | Unset):
        include_formed_centermarks (bool | Unset):
        include_formed_outlines (bool | Unset):
        include_sketches (bool | Unset):
        is_parting_out (bool | Unset):
        link_document_id (str | Unset):
        link_document_workspace_id (str | Unset):
        max_facet_width (float | Unset):
        microversion (str | Unset):
        min_facet_width (float | Unset):
        mode (str | Unset):
        occurrences_to_export (str | Unset):
        part_ids (str | Unset):
        part_query (str | Unset):
        password (str | Unset):
        password_required (bool | Unset):
        resolution (str | Unset):
        scale (float | Unset):
        send_copy_to_me (bool | Unset):
        sheet_metal_flat (bool | Unset):
        splines_as_polylines (bool | Unset):
        store_in_document (bool | Unset):
        trigger_auto_download (bool | Unset):
        units (str | Unset):
        use_y_axis_as_up (bool | Unset): If `true`, the exported file will have all the parts and assemblies reoriented
            such that the Z-axis within Onshape becomes the Y-axis in the exported file.
        user_id (str | Unset):
        valid_for_days (int | Unset):
        version (str | Unset):
        view (str | Unset):
        workspace_id (str | Unset):
        zip_single_file_output (bool | Unset):
    """

    document_id: str
    format_: str
    angle_tolerance: float | Unset = UNSET
    batch_all_flat_patterns: bool | Unset = UNSET
    batch_flat_patterns: bool | Unset = UNSET
    chord_tolerance: float | Unset = UNSET
    cloud_object_id: str | Unset = UNSET
    cloud_storage_account_id: str | Unset = UNSET
    configuration: str | Unset = UNSET
    destination_name: str | Unset = UNSET
    document_version_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_ids: str | Unset = UNSET
    email_link: bool | Unset = UNSET
    email_message: str | Unset = UNSET
    email_subject: str | Unset = UNSET
    email_to: str | Unset = UNSET
    exclude_hidden_entities: bool | Unset = UNSET
    feature_ids: str | Unset = UNSET
    flat_pattern_async: bool | Unset = UNSET
    flatten: bool | Unset = UNSET
    from_user_id: str | Unset = UNSET
    grouping: str | Unset = UNSET
    ignore_export_rules_for_contents: bool | Unset = UNSET
    include_bend_centerlines: bool | Unset = UNSET
    include_bend_lines: bool | Unset = UNSET
    include_cbore_csink: bool | Unset = UNSET
    include_export_ids: bool | Unset = UNSET
    include_formed_centermarks: bool | Unset = UNSET
    include_formed_outlines: bool | Unset = UNSET
    include_sketches: bool | Unset = UNSET
    is_parting_out: bool | Unset = UNSET
    link_document_id: str | Unset = UNSET
    link_document_workspace_id: str | Unset = UNSET
    max_facet_width: float | Unset = UNSET
    microversion: str | Unset = UNSET
    min_facet_width: float | Unset = UNSET
    mode: str | Unset = UNSET
    occurrences_to_export: str | Unset = UNSET
    part_ids: str | Unset = UNSET
    part_query: str | Unset = UNSET
    password: str | Unset = UNSET
    password_required: bool | Unset = UNSET
    resolution: str | Unset = UNSET
    scale: float | Unset = UNSET
    send_copy_to_me: bool | Unset = UNSET
    sheet_metal_flat: bool | Unset = UNSET
    splines_as_polylines: bool | Unset = UNSET
    store_in_document: bool | Unset = UNSET
    trigger_auto_download: bool | Unset = UNSET
    units: str | Unset = UNSET
    use_y_axis_as_up: bool | Unset = UNSET
    user_id: str | Unset = UNSET
    valid_for_days: int | Unset = UNSET
    version: str | Unset = UNSET
    view: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    zip_single_file_output: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        format_ = self.format_

        angle_tolerance = self.angle_tolerance

        batch_all_flat_patterns = self.batch_all_flat_patterns

        batch_flat_patterns = self.batch_flat_patterns

        chord_tolerance = self.chord_tolerance

        cloud_object_id = self.cloud_object_id

        cloud_storage_account_id = self.cloud_storage_account_id

        configuration = self.configuration

        destination_name = self.destination_name

        document_version_id = self.document_version_id

        element_id = self.element_id

        element_ids = self.element_ids

        email_link = self.email_link

        email_message = self.email_message

        email_subject = self.email_subject

        email_to = self.email_to

        exclude_hidden_entities = self.exclude_hidden_entities

        feature_ids = self.feature_ids

        flat_pattern_async = self.flat_pattern_async

        flatten = self.flatten

        from_user_id = self.from_user_id

        grouping = self.grouping

        ignore_export_rules_for_contents = self.ignore_export_rules_for_contents

        include_bend_centerlines = self.include_bend_centerlines

        include_bend_lines = self.include_bend_lines

        include_cbore_csink = self.include_cbore_csink

        include_export_ids = self.include_export_ids

        include_formed_centermarks = self.include_formed_centermarks

        include_formed_outlines = self.include_formed_outlines

        include_sketches = self.include_sketches

        is_parting_out = self.is_parting_out

        link_document_id = self.link_document_id

        link_document_workspace_id = self.link_document_workspace_id

        max_facet_width = self.max_facet_width

        microversion = self.microversion

        min_facet_width = self.min_facet_width

        mode = self.mode

        occurrences_to_export = self.occurrences_to_export

        part_ids = self.part_ids

        part_query = self.part_query

        password = self.password

        password_required = self.password_required

        resolution = self.resolution

        scale = self.scale

        send_copy_to_me = self.send_copy_to_me

        sheet_metal_flat = self.sheet_metal_flat

        splines_as_polylines = self.splines_as_polylines

        store_in_document = self.store_in_document

        trigger_auto_download = self.trigger_auto_download

        units = self.units

        use_y_axis_as_up = self.use_y_axis_as_up

        user_id = self.user_id

        valid_for_days = self.valid_for_days

        version = self.version

        view = self.view

        workspace_id = self.workspace_id

        zip_single_file_output = self.zip_single_file_output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "format": format_,
            }
        )
        if angle_tolerance is not UNSET:
            field_dict["angleTolerance"] = angle_tolerance
        if batch_all_flat_patterns is not UNSET:
            field_dict["batchAllFlatPatterns"] = batch_all_flat_patterns
        if batch_flat_patterns is not UNSET:
            field_dict["batchFlatPatterns"] = batch_flat_patterns
        if chord_tolerance is not UNSET:
            field_dict["chordTolerance"] = chord_tolerance
        if cloud_object_id is not UNSET:
            field_dict["cloudObjectId"] = cloud_object_id
        if cloud_storage_account_id is not UNSET:
            field_dict["cloudStorageAccountId"] = cloud_storage_account_id
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if destination_name is not UNSET:
            field_dict["destinationName"] = destination_name
        if document_version_id is not UNSET:
            field_dict["documentVersionId"] = document_version_id
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
        if exclude_hidden_entities is not UNSET:
            field_dict["excludeHiddenEntities"] = exclude_hidden_entities
        if feature_ids is not UNSET:
            field_dict["featureIds"] = feature_ids
        if flat_pattern_async is not UNSET:
            field_dict["flatPatternAsync"] = flat_pattern_async
        if flatten is not UNSET:
            field_dict["flatten"] = flatten
        if from_user_id is not UNSET:
            field_dict["fromUserId"] = from_user_id
        if grouping is not UNSET:
            field_dict["grouping"] = grouping
        if ignore_export_rules_for_contents is not UNSET:
            field_dict["ignoreExportRulesForContents"] = ignore_export_rules_for_contents
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
        if is_parting_out is not UNSET:
            field_dict["isPartingOut"] = is_parting_out
        if link_document_id is not UNSET:
            field_dict["linkDocumentId"] = link_document_id
        if link_document_workspace_id is not UNSET:
            field_dict["linkDocumentWorkspaceId"] = link_document_workspace_id
        if max_facet_width is not UNSET:
            field_dict["maxFacetWidth"] = max_facet_width
        if microversion is not UNSET:
            field_dict["microversion"] = microversion
        if min_facet_width is not UNSET:
            field_dict["minFacetWidth"] = min_facet_width
        if mode is not UNSET:
            field_dict["mode"] = mode
        if occurrences_to_export is not UNSET:
            field_dict["occurrencesToExport"] = occurrences_to_export
        if part_ids is not UNSET:
            field_dict["partIds"] = part_ids
        if part_query is not UNSET:
            field_dict["partQuery"] = part_query
        if password is not UNSET:
            field_dict["password"] = password
        if password_required is not UNSET:
            field_dict["passwordRequired"] = password_required
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if scale is not UNSET:
            field_dict["scale"] = scale
        if send_copy_to_me is not UNSET:
            field_dict["sendCopyToMe"] = send_copy_to_me
        if sheet_metal_flat is not UNSET:
            field_dict["sheetMetalFlat"] = sheet_metal_flat
        if splines_as_polylines is not UNSET:
            field_dict["splinesAsPolylines"] = splines_as_polylines
        if store_in_document is not UNSET:
            field_dict["storeInDocument"] = store_in_document
        if trigger_auto_download is not UNSET:
            field_dict["triggerAutoDownload"] = trigger_auto_download
        if units is not UNSET:
            field_dict["units"] = units
        if use_y_axis_as_up is not UNSET:
            field_dict["useYAxisAsUp"] = use_y_axis_as_up
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if valid_for_days is not UNSET:
            field_dict["validForDays"] = valid_for_days
        if version is not UNSET:
            field_dict["version"] = version
        if view is not UNSET:
            field_dict["view"] = view
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if zip_single_file_output is not UNSET:
            field_dict["zipSingleFileOutput"] = zip_single_file_output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId")

        format_ = d.pop("format")

        angle_tolerance = d.pop("angleTolerance", UNSET)

        batch_all_flat_patterns = d.pop("batchAllFlatPatterns", UNSET)

        batch_flat_patterns = d.pop("batchFlatPatterns", UNSET)

        chord_tolerance = d.pop("chordTolerance", UNSET)

        cloud_object_id = d.pop("cloudObjectId", UNSET)

        cloud_storage_account_id = d.pop("cloudStorageAccountId", UNSET)

        configuration = d.pop("configuration", UNSET)

        destination_name = d.pop("destinationName", UNSET)

        document_version_id = d.pop("documentVersionId", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_ids = d.pop("elementIds", UNSET)

        email_link = d.pop("emailLink", UNSET)

        email_message = d.pop("emailMessage", UNSET)

        email_subject = d.pop("emailSubject", UNSET)

        email_to = d.pop("emailTo", UNSET)

        exclude_hidden_entities = d.pop("excludeHiddenEntities", UNSET)

        feature_ids = d.pop("featureIds", UNSET)

        flat_pattern_async = d.pop("flatPatternAsync", UNSET)

        flatten = d.pop("flatten", UNSET)

        from_user_id = d.pop("fromUserId", UNSET)

        grouping = d.pop("grouping", UNSET)

        ignore_export_rules_for_contents = d.pop("ignoreExportRulesForContents", UNSET)

        include_bend_centerlines = d.pop("includeBendCenterlines", UNSET)

        include_bend_lines = d.pop("includeBendLines", UNSET)

        include_cbore_csink = d.pop("includeCboreCsink", UNSET)

        include_export_ids = d.pop("includeExportIds", UNSET)

        include_formed_centermarks = d.pop("includeFormedCentermarks", UNSET)

        include_formed_outlines = d.pop("includeFormedOutlines", UNSET)

        include_sketches = d.pop("includeSketches", UNSET)

        is_parting_out = d.pop("isPartingOut", UNSET)

        link_document_id = d.pop("linkDocumentId", UNSET)

        link_document_workspace_id = d.pop("linkDocumentWorkspaceId", UNSET)

        max_facet_width = d.pop("maxFacetWidth", UNSET)

        microversion = d.pop("microversion", UNSET)

        min_facet_width = d.pop("minFacetWidth", UNSET)

        mode = d.pop("mode", UNSET)

        occurrences_to_export = d.pop("occurrencesToExport", UNSET)

        part_ids = d.pop("partIds", UNSET)

        part_query = d.pop("partQuery", UNSET)

        password = d.pop("password", UNSET)

        password_required = d.pop("passwordRequired", UNSET)

        resolution = d.pop("resolution", UNSET)

        scale = d.pop("scale", UNSET)

        send_copy_to_me = d.pop("sendCopyToMe", UNSET)

        sheet_metal_flat = d.pop("sheetMetalFlat", UNSET)

        splines_as_polylines = d.pop("splinesAsPolylines", UNSET)

        store_in_document = d.pop("storeInDocument", UNSET)

        trigger_auto_download = d.pop("triggerAutoDownload", UNSET)

        units = d.pop("units", UNSET)

        use_y_axis_as_up = d.pop("useYAxisAsUp", UNSET)

        user_id = d.pop("userId", UNSET)

        valid_for_days = d.pop("validForDays", UNSET)

        version = d.pop("version", UNSET)

        view = d.pop("view", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        zip_single_file_output = d.pop("zipSingleFileOutput", UNSET)

        btb_export_model_params = cls(
            document_id=document_id,
            format_=format_,
            angle_tolerance=angle_tolerance,
            batch_all_flat_patterns=batch_all_flat_patterns,
            batch_flat_patterns=batch_flat_patterns,
            chord_tolerance=chord_tolerance,
            cloud_object_id=cloud_object_id,
            cloud_storage_account_id=cloud_storage_account_id,
            configuration=configuration,
            destination_name=destination_name,
            document_version_id=document_version_id,
            element_id=element_id,
            element_ids=element_ids,
            email_link=email_link,
            email_message=email_message,
            email_subject=email_subject,
            email_to=email_to,
            exclude_hidden_entities=exclude_hidden_entities,
            feature_ids=feature_ids,
            flat_pattern_async=flat_pattern_async,
            flatten=flatten,
            from_user_id=from_user_id,
            grouping=grouping,
            ignore_export_rules_for_contents=ignore_export_rules_for_contents,
            include_bend_centerlines=include_bend_centerlines,
            include_bend_lines=include_bend_lines,
            include_cbore_csink=include_cbore_csink,
            include_export_ids=include_export_ids,
            include_formed_centermarks=include_formed_centermarks,
            include_formed_outlines=include_formed_outlines,
            include_sketches=include_sketches,
            is_parting_out=is_parting_out,
            link_document_id=link_document_id,
            link_document_workspace_id=link_document_workspace_id,
            max_facet_width=max_facet_width,
            microversion=microversion,
            min_facet_width=min_facet_width,
            mode=mode,
            occurrences_to_export=occurrences_to_export,
            part_ids=part_ids,
            part_query=part_query,
            password=password,
            password_required=password_required,
            resolution=resolution,
            scale=scale,
            send_copy_to_me=send_copy_to_me,
            sheet_metal_flat=sheet_metal_flat,
            splines_as_polylines=splines_as_polylines,
            store_in_document=store_in_document,
            trigger_auto_download=trigger_auto_download,
            units=units,
            use_y_axis_as_up=use_y_axis_as_up,
            user_id=user_id,
            valid_for_days=valid_for_days,
            version=version,
            view=view,
            workspace_id=workspace_id,
            zip_single_file_output=zip_single_file_output,
        )

        btb_export_model_params.additional_properties = d
        return btb_export_model_params

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
