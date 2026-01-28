from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_file_update_element_body_file import UploadFileUpdateElementBodyFile


T = TypeVar("T", bound="UploadFileUpdateElementBody")


@_attrs_define
class UploadFileUpdateElementBody:
    """
    Attributes:
        file (UploadFileUpdateElementBodyFile | Unset): The file to upload.
        allow_faulty_parts (bool | Unset): If true, and a part doesn't pass Onshape validation, it will be imported with
            faults.
        create_composite (bool | Unset): Not supported for importing into a single part studio.
        create_drawing_if_possible (bool | Unset):
        encoded_filename (str | Unset): If the filename contains non-ASCII characters. Use this field to store the
            filename.
        extract_assembly_hierarchy (bool | Unset):
        flatten_assemblies (bool | Unset): If the file is an assembly, or contains an assembly, setting this to True
            will import it as a Part Studio. In this case the assembly will be flattened to a set of parts in a Part Studio.
            There will be duplicate parts created whenever a part is instanced more than once. If False, it will be imported
            as an Assembly.
        format_name (str | Unset):
        join_adjacent_surfaces (bool | Unset):
        location_element_id (str | Unset):
        location_group_id (str | Unset):
        location_position (int | Unset):  Default: -1.
        notify_user (bool | Unset):  Default: True.
        owner_id (str | Unset):
        parent_id (str | Unset):
        project_id (str | Unset):
        public (bool | Unset):
        one_part_per_doc (bool | Unset):  Default: False.
        split_assemblies_into_multiple_documents (bool | Unset):  Default: False.
        store_in_document (bool | Unset):  Default: True.
        translate (bool | Unset):  Default: True.
        unit (str | Unset):  Default: ''.
        upload_id (str | Unset):
        version_string (str | Unset):
        import_appearances (bool | Unset): Face appearances defined on models will be imported. Default: True.
        import_material_density (bool | Unset): Material density defined on models will be imported. Default: False.
        y_axis_is_up (bool | Unset): If the file was created in a system that orients with Y Axis Up, the models would
            by default be brought into Onshape (a Z Axis Up system) with a flipped coordinate system. Toggle this value to
            reorient the axis system to match Onshape and display the model with the coordinates you expect.
        import_within_document (bool | Unset):
        use_iges_import_post_processing (bool | Unset): Try getting optimized topology from IGES model. Default: False.
        upgrade_feature_script_version (bool | Unset):  Default: False.
        preserve_source_ids (bool | Unset):  Default: False.
        document_id (str | Unset):
        version_id (str | Unset):
        version_name (str | Unset):
        version_description (str | Unset):
        repoint_app_element_version_refs (bool | Unset): Re-point the version references in APP elements to initial
            version in the new document Default: False.
    """

    file: UploadFileUpdateElementBodyFile | Unset = UNSET
    allow_faulty_parts: bool | Unset = UNSET
    create_composite: bool | Unset = UNSET
    create_drawing_if_possible: bool | Unset = UNSET
    encoded_filename: str | Unset = UNSET
    extract_assembly_hierarchy: bool | Unset = UNSET
    flatten_assemblies: bool | Unset = UNSET
    format_name: str | Unset = UNSET
    join_adjacent_surfaces: bool | Unset = UNSET
    location_element_id: str | Unset = UNSET
    location_group_id: str | Unset = UNSET
    location_position: int | Unset = -1
    notify_user: bool | Unset = True
    owner_id: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    public: bool | Unset = UNSET
    one_part_per_doc: bool | Unset = False
    split_assemblies_into_multiple_documents: bool | Unset = False
    store_in_document: bool | Unset = True
    translate: bool | Unset = True
    unit: str | Unset = ""
    upload_id: str | Unset = UNSET
    version_string: str | Unset = UNSET
    import_appearances: bool | Unset = True
    import_material_density: bool | Unset = False
    y_axis_is_up: bool | Unset = UNSET
    import_within_document: bool | Unset = UNSET
    use_iges_import_post_processing: bool | Unset = False
    upgrade_feature_script_version: bool | Unset = False
    preserve_source_ids: bool | Unset = False
    document_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    version_name: str | Unset = UNSET
    version_description: str | Unset = UNSET
    repoint_app_element_version_refs: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        allow_faulty_parts = self.allow_faulty_parts

        create_composite = self.create_composite

        create_drawing_if_possible = self.create_drawing_if_possible

        encoded_filename = self.encoded_filename

        extract_assembly_hierarchy = self.extract_assembly_hierarchy

        flatten_assemblies = self.flatten_assemblies

        format_name = self.format_name

        join_adjacent_surfaces = self.join_adjacent_surfaces

        location_element_id = self.location_element_id

        location_group_id = self.location_group_id

        location_position = self.location_position

        notify_user = self.notify_user

        owner_id = self.owner_id

        parent_id = self.parent_id

        project_id = self.project_id

        public = self.public

        one_part_per_doc = self.one_part_per_doc

        split_assemblies_into_multiple_documents = self.split_assemblies_into_multiple_documents

        store_in_document = self.store_in_document

        translate = self.translate

        unit = self.unit

        upload_id = self.upload_id

        version_string = self.version_string

        import_appearances = self.import_appearances

        import_material_density = self.import_material_density

        y_axis_is_up = self.y_axis_is_up

        import_within_document = self.import_within_document

        use_iges_import_post_processing = self.use_iges_import_post_processing

        upgrade_feature_script_version = self.upgrade_feature_script_version

        preserve_source_ids = self.preserve_source_ids

        document_id = self.document_id

        version_id = self.version_id

        version_name = self.version_name

        version_description = self.version_description

        repoint_app_element_version_refs = self.repoint_app_element_version_refs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if allow_faulty_parts is not UNSET:
            field_dict["allowFaultyParts"] = allow_faulty_parts
        if create_composite is not UNSET:
            field_dict["createComposite"] = create_composite
        if create_drawing_if_possible is not UNSET:
            field_dict["createDrawingIfPossible"] = create_drawing_if_possible
        if encoded_filename is not UNSET:
            field_dict["encodedFilename"] = encoded_filename
        if extract_assembly_hierarchy is not UNSET:
            field_dict["extractAssemblyHierarchy"] = extract_assembly_hierarchy
        if flatten_assemblies is not UNSET:
            field_dict["flattenAssemblies"] = flatten_assemblies
        if format_name is not UNSET:
            field_dict["formatName"] = format_name
        if join_adjacent_surfaces is not UNSET:
            field_dict["joinAdjacentSurfaces"] = join_adjacent_surfaces
        if location_element_id is not UNSET:
            field_dict["locationElementId"] = location_element_id
        if location_group_id is not UNSET:
            field_dict["locationGroupId"] = location_group_id
        if location_position is not UNSET:
            field_dict["locationPosition"] = location_position
        if notify_user is not UNSET:
            field_dict["notifyUser"] = notify_user
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if public is not UNSET:
            field_dict["public"] = public
        if one_part_per_doc is not UNSET:
            field_dict["onePartPerDoc"] = one_part_per_doc
        if split_assemblies_into_multiple_documents is not UNSET:
            field_dict["splitAssembliesIntoMultipleDocuments"] = split_assemblies_into_multiple_documents
        if store_in_document is not UNSET:
            field_dict["storeInDocument"] = store_in_document
        if translate is not UNSET:
            field_dict["translate"] = translate
        if unit is not UNSET:
            field_dict["unit"] = unit
        if upload_id is not UNSET:
            field_dict["uploadId"] = upload_id
        if version_string is not UNSET:
            field_dict["versionString"] = version_string
        if import_appearances is not UNSET:
            field_dict["importAppearances"] = import_appearances
        if import_material_density is not UNSET:
            field_dict["importMaterialDensity"] = import_material_density
        if y_axis_is_up is not UNSET:
            field_dict["yAxisIsUp"] = y_axis_is_up
        if import_within_document is not UNSET:
            field_dict["importWithinDocument"] = import_within_document
        if use_iges_import_post_processing is not UNSET:
            field_dict["useIGESImportPostProcessing"] = use_iges_import_post_processing
        if upgrade_feature_script_version is not UNSET:
            field_dict["upgradeFeatureScriptVersion"] = upgrade_feature_script_version
        if preserve_source_ids is not UNSET:
            field_dict["preserveSourceIds"] = preserve_source_ids
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if version_description is not UNSET:
            field_dict["versionDescription"] = version_description
        if repoint_app_element_version_refs is not UNSET:
            field_dict["repointAppElementVersionRefs"] = repoint_app_element_version_refs

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.file, Unset):
            files.append(("file", (None, json.dumps(self.file.to_dict()).encode(), "application/json")))

        if not isinstance(self.allow_faulty_parts, Unset):
            files.append(("allowFaultyParts", (None, str(self.allow_faulty_parts).encode(), "text/plain")))

        if not isinstance(self.create_composite, Unset):
            files.append(("createComposite", (None, str(self.create_composite).encode(), "text/plain")))

        if not isinstance(self.create_drawing_if_possible, Unset):
            files.append(
                ("createDrawingIfPossible", (None, str(self.create_drawing_if_possible).encode(), "text/plain"))
            )

        if not isinstance(self.encoded_filename, Unset):
            files.append(("encodedFilename", (None, str(self.encoded_filename).encode(), "text/plain")))

        if not isinstance(self.extract_assembly_hierarchy, Unset):
            files.append(
                ("extractAssemblyHierarchy", (None, str(self.extract_assembly_hierarchy).encode(), "text/plain"))
            )

        if not isinstance(self.flatten_assemblies, Unset):
            files.append(("flattenAssemblies", (None, str(self.flatten_assemblies).encode(), "text/plain")))

        if not isinstance(self.format_name, Unset):
            files.append(("formatName", (None, str(self.format_name).encode(), "text/plain")))

        if not isinstance(self.join_adjacent_surfaces, Unset):
            files.append(("joinAdjacentSurfaces", (None, str(self.join_adjacent_surfaces).encode(), "text/plain")))

        if not isinstance(self.location_element_id, Unset):
            files.append(("locationElementId", (None, str(self.location_element_id).encode(), "text/plain")))

        if not isinstance(self.location_group_id, Unset):
            files.append(("locationGroupId", (None, str(self.location_group_id).encode(), "text/plain")))

        if not isinstance(self.location_position, Unset):
            files.append(("locationPosition", (None, str(self.location_position).encode(), "text/plain")))

        if not isinstance(self.notify_user, Unset):
            files.append(("notifyUser", (None, str(self.notify_user).encode(), "text/plain")))

        if not isinstance(self.owner_id, Unset):
            files.append(("ownerId", (None, str(self.owner_id).encode(), "text/plain")))

        if not isinstance(self.parent_id, Unset):
            files.append(("parentId", (None, str(self.parent_id).encode(), "text/plain")))

        if not isinstance(self.project_id, Unset):
            files.append(("projectId", (None, str(self.project_id).encode(), "text/plain")))

        if not isinstance(self.public, Unset):
            files.append(("public", (None, str(self.public).encode(), "text/plain")))

        if not isinstance(self.one_part_per_doc, Unset):
            files.append(("onePartPerDoc", (None, str(self.one_part_per_doc).encode(), "text/plain")))

        if not isinstance(self.split_assemblies_into_multiple_documents, Unset):
            files.append(
                (
                    "splitAssembliesIntoMultipleDocuments",
                    (None, str(self.split_assemblies_into_multiple_documents).encode(), "text/plain"),
                )
            )

        if not isinstance(self.store_in_document, Unset):
            files.append(("storeInDocument", (None, str(self.store_in_document).encode(), "text/plain")))

        if not isinstance(self.translate, Unset):
            files.append(("translate", (None, str(self.translate).encode(), "text/plain")))

        if not isinstance(self.unit, Unset):
            files.append(("unit", (None, str(self.unit).encode(), "text/plain")))

        if not isinstance(self.upload_id, Unset):
            files.append(("uploadId", (None, str(self.upload_id).encode(), "text/plain")))

        if not isinstance(self.version_string, Unset):
            files.append(("versionString", (None, str(self.version_string).encode(), "text/plain")))

        if not isinstance(self.import_appearances, Unset):
            files.append(("importAppearances", (None, str(self.import_appearances).encode(), "text/plain")))

        if not isinstance(self.import_material_density, Unset):
            files.append(("importMaterialDensity", (None, str(self.import_material_density).encode(), "text/plain")))

        if not isinstance(self.y_axis_is_up, Unset):
            files.append(("yAxisIsUp", (None, str(self.y_axis_is_up).encode(), "text/plain")))

        if not isinstance(self.import_within_document, Unset):
            files.append(("importWithinDocument", (None, str(self.import_within_document).encode(), "text/plain")))

        if not isinstance(self.use_iges_import_post_processing, Unset):
            files.append(
                (
                    "useIGESImportPostProcessing",
                    (None, str(self.use_iges_import_post_processing).encode(), "text/plain"),
                )
            )

        if not isinstance(self.upgrade_feature_script_version, Unset):
            files.append(
                ("upgradeFeatureScriptVersion", (None, str(self.upgrade_feature_script_version).encode(), "text/plain"))
            )

        if not isinstance(self.preserve_source_ids, Unset):
            files.append(("preserveSourceIds", (None, str(self.preserve_source_ids).encode(), "text/plain")))

        if not isinstance(self.document_id, Unset):
            files.append(("documentId", (None, str(self.document_id).encode(), "text/plain")))

        if not isinstance(self.version_id, Unset):
            files.append(("versionId", (None, str(self.version_id).encode(), "text/plain")))

        if not isinstance(self.version_name, Unset):
            files.append(("versionName", (None, str(self.version_name).encode(), "text/plain")))

        if not isinstance(self.version_description, Unset):
            files.append(("versionDescription", (None, str(self.version_description).encode(), "text/plain")))

        if not isinstance(self.repoint_app_element_version_refs, Unset):
            files.append(
                (
                    "repointAppElementVersionRefs",
                    (None, str(self.repoint_app_element_version_refs).encode(), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_file_update_element_body_file import UploadFileUpdateElementBodyFile

        d = dict(src_dict)
        _file = d.pop("file", UNSET)
        file: UploadFileUpdateElementBodyFile | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = UploadFileUpdateElementBodyFile.from_dict(_file)

        allow_faulty_parts = d.pop("allowFaultyParts", UNSET)

        create_composite = d.pop("createComposite", UNSET)

        create_drawing_if_possible = d.pop("createDrawingIfPossible", UNSET)

        encoded_filename = d.pop("encodedFilename", UNSET)

        extract_assembly_hierarchy = d.pop("extractAssemblyHierarchy", UNSET)

        flatten_assemblies = d.pop("flattenAssemblies", UNSET)

        format_name = d.pop("formatName", UNSET)

        join_adjacent_surfaces = d.pop("joinAdjacentSurfaces", UNSET)

        location_element_id = d.pop("locationElementId", UNSET)

        location_group_id = d.pop("locationGroupId", UNSET)

        location_position = d.pop("locationPosition", UNSET)

        notify_user = d.pop("notifyUser", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        public = d.pop("public", UNSET)

        one_part_per_doc = d.pop("onePartPerDoc", UNSET)

        split_assemblies_into_multiple_documents = d.pop("splitAssembliesIntoMultipleDocuments", UNSET)

        store_in_document = d.pop("storeInDocument", UNSET)

        translate = d.pop("translate", UNSET)

        unit = d.pop("unit", UNSET)

        upload_id = d.pop("uploadId", UNSET)

        version_string = d.pop("versionString", UNSET)

        import_appearances = d.pop("importAppearances", UNSET)

        import_material_density = d.pop("importMaterialDensity", UNSET)

        y_axis_is_up = d.pop("yAxisIsUp", UNSET)

        import_within_document = d.pop("importWithinDocument", UNSET)

        use_iges_import_post_processing = d.pop("useIGESImportPostProcessing", UNSET)

        upgrade_feature_script_version = d.pop("upgradeFeatureScriptVersion", UNSET)

        preserve_source_ids = d.pop("preserveSourceIds", UNSET)

        document_id = d.pop("documentId", UNSET)

        version_id = d.pop("versionId", UNSET)

        version_name = d.pop("versionName", UNSET)

        version_description = d.pop("versionDescription", UNSET)

        repoint_app_element_version_refs = d.pop("repointAppElementVersionRefs", UNSET)

        upload_file_update_element_body = cls(
            file=file,
            allow_faulty_parts=allow_faulty_parts,
            create_composite=create_composite,
            create_drawing_if_possible=create_drawing_if_possible,
            encoded_filename=encoded_filename,
            extract_assembly_hierarchy=extract_assembly_hierarchy,
            flatten_assemblies=flatten_assemblies,
            format_name=format_name,
            join_adjacent_surfaces=join_adjacent_surfaces,
            location_element_id=location_element_id,
            location_group_id=location_group_id,
            location_position=location_position,
            notify_user=notify_user,
            owner_id=owner_id,
            parent_id=parent_id,
            project_id=project_id,
            public=public,
            one_part_per_doc=one_part_per_doc,
            split_assemblies_into_multiple_documents=split_assemblies_into_multiple_documents,
            store_in_document=store_in_document,
            translate=translate,
            unit=unit,
            upload_id=upload_id,
            version_string=version_string,
            import_appearances=import_appearances,
            import_material_density=import_material_density,
            y_axis_is_up=y_axis_is_up,
            import_within_document=import_within_document,
            use_iges_import_post_processing=use_iges_import_post_processing,
            upgrade_feature_script_version=upgrade_feature_script_version,
            preserve_source_ids=preserve_source_ids,
            document_id=document_id,
            version_id=version_id,
            version_name=version_name,
            version_description=version_description,
            repoint_app_element_version_refs=repoint_app_element_version_refs,
        )

        upload_file_update_element_body.additional_properties = d
        return upload_file_update_element_body

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
