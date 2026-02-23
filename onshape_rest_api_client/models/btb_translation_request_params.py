from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BTBTranslationRequestParams")


@_attrs_define
class BTBTranslationRequestParams:
    """
    Attributes:
        allow_faulty_parts (bool | Unset):
        create_composite (bool | Unset):
        create_drawing_if_possible (bool | Unset):
        encoded_filename (str | Unset):
        extract_assembly_hierarchy (bool | Unset):
        file (File | Unset): The file to upload.
        flatten_assemblies (bool | Unset):
        format_name (str | Unset):
        import_appearances (bool | Unset):
        import_material_density (bool | Unset):
        import_within_document (bool | Unset):
        join_adjacent_surfaces (bool | Unset):
        location_element_id (str | Unset):
        location_group_id (str | Unset):
        location_position (int | Unset):
        make_public (bool | Unset):
        notify_user (bool | Unset):
        one_part_per_doc (bool | Unset):
        owner_id (str | Unset):
        parent_id (str | Unset):
        project_id (str | Unset):
        repoint_app_element_version_refs (bool | Unset):
        split_assemblies_into_multiple_documents (bool | Unset):
        store_in_document (bool | Unset):
        translate (bool | Unset):
        unit (str | Unset):
        upload_id (str | Unset):
        use_iges_import_post_processing (bool | Unset):
        version_string (str | Unset):
        y_axis_is_up (bool | Unset):
    """

    allow_faulty_parts: bool | Unset = UNSET
    create_composite: bool | Unset = UNSET
    create_drawing_if_possible: bool | Unset = UNSET
    encoded_filename: str | Unset = UNSET
    extract_assembly_hierarchy: bool | Unset = UNSET
    file: File | Unset = UNSET
    flatten_assemblies: bool | Unset = UNSET
    format_name: str | Unset = UNSET
    import_appearances: bool | Unset = UNSET
    import_material_density: bool | Unset = UNSET
    import_within_document: bool | Unset = UNSET
    join_adjacent_surfaces: bool | Unset = UNSET
    location_element_id: str | Unset = UNSET
    location_group_id: str | Unset = UNSET
    location_position: int | Unset = UNSET
    make_public: bool | Unset = UNSET
    notify_user: bool | Unset = UNSET
    one_part_per_doc: bool | Unset = UNSET
    owner_id: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    repoint_app_element_version_refs: bool | Unset = UNSET
    split_assemblies_into_multiple_documents: bool | Unset = UNSET
    store_in_document: bool | Unset = UNSET
    translate: bool | Unset = UNSET
    unit: str | Unset = UNSET
    upload_id: str | Unset = UNSET
    use_iges_import_post_processing: bool | Unset = UNSET
    version_string: str | Unset = UNSET
    y_axis_is_up: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_faulty_parts = self.allow_faulty_parts

        create_composite = self.create_composite

        create_drawing_if_possible = self.create_drawing_if_possible

        encoded_filename = self.encoded_filename

        extract_assembly_hierarchy = self.extract_assembly_hierarchy

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        flatten_assemblies = self.flatten_assemblies

        format_name = self.format_name

        import_appearances = self.import_appearances

        import_material_density = self.import_material_density

        import_within_document = self.import_within_document

        join_adjacent_surfaces = self.join_adjacent_surfaces

        location_element_id = self.location_element_id

        location_group_id = self.location_group_id

        location_position = self.location_position

        make_public = self.make_public

        notify_user = self.notify_user

        one_part_per_doc = self.one_part_per_doc

        owner_id = self.owner_id

        parent_id = self.parent_id

        project_id = self.project_id

        repoint_app_element_version_refs = self.repoint_app_element_version_refs

        split_assemblies_into_multiple_documents = self.split_assemblies_into_multiple_documents

        store_in_document = self.store_in_document

        translate = self.translate

        unit = self.unit

        upload_id = self.upload_id

        use_iges_import_post_processing = self.use_iges_import_post_processing

        version_string = self.version_string

        y_axis_is_up = self.y_axis_is_up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if file is not UNSET:
            field_dict["file"] = file
        if flatten_assemblies is not UNSET:
            field_dict["flattenAssemblies"] = flatten_assemblies
        if format_name is not UNSET:
            field_dict["formatName"] = format_name
        if import_appearances is not UNSET:
            field_dict["importAppearances"] = import_appearances
        if import_material_density is not UNSET:
            field_dict["importMaterialDensity"] = import_material_density
        if import_within_document is not UNSET:
            field_dict["importWithinDocument"] = import_within_document
        if join_adjacent_surfaces is not UNSET:
            field_dict["joinAdjacentSurfaces"] = join_adjacent_surfaces
        if location_element_id is not UNSET:
            field_dict["locationElementId"] = location_element_id
        if location_group_id is not UNSET:
            field_dict["locationGroupId"] = location_group_id
        if location_position is not UNSET:
            field_dict["locationPosition"] = location_position
        if make_public is not UNSET:
            field_dict["makePublic"] = make_public
        if notify_user is not UNSET:
            field_dict["notifyUser"] = notify_user
        if one_part_per_doc is not UNSET:
            field_dict["onePartPerDoc"] = one_part_per_doc
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if repoint_app_element_version_refs is not UNSET:
            field_dict["repointAppElementVersionRefs"] = repoint_app_element_version_refs
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
        if use_iges_import_post_processing is not UNSET:
            field_dict["useIGESImportPostProcessing"] = use_iges_import_post_processing
        if version_string is not UNSET:
            field_dict["versionString"] = version_string
        if y_axis_is_up is not UNSET:
            field_dict["yAxisIsUp"] = y_axis_is_up

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

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

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        if not isinstance(self.flatten_assemblies, Unset):
            files.append(("flattenAssemblies", (None, str(self.flatten_assemblies).encode(), "text/plain")))

        if not isinstance(self.format_name, Unset):
            files.append(("formatName", (None, str(self.format_name).encode(), "text/plain")))

        if not isinstance(self.import_appearances, Unset):
            files.append(("importAppearances", (None, str(self.import_appearances).encode(), "text/plain")))

        if not isinstance(self.import_material_density, Unset):
            files.append(("importMaterialDensity", (None, str(self.import_material_density).encode(), "text/plain")))

        if not isinstance(self.import_within_document, Unset):
            files.append(("importWithinDocument", (None, str(self.import_within_document).encode(), "text/plain")))

        if not isinstance(self.join_adjacent_surfaces, Unset):
            files.append(("joinAdjacentSurfaces", (None, str(self.join_adjacent_surfaces).encode(), "text/plain")))

        if not isinstance(self.location_element_id, Unset):
            files.append(("locationElementId", (None, str(self.location_element_id).encode(), "text/plain")))

        if not isinstance(self.location_group_id, Unset):
            files.append(("locationGroupId", (None, str(self.location_group_id).encode(), "text/plain")))

        if not isinstance(self.location_position, Unset):
            files.append(("locationPosition", (None, str(self.location_position).encode(), "text/plain")))

        if not isinstance(self.make_public, Unset):
            files.append(("makePublic", (None, str(self.make_public).encode(), "text/plain")))

        if not isinstance(self.notify_user, Unset):
            files.append(("notifyUser", (None, str(self.notify_user).encode(), "text/plain")))

        if not isinstance(self.one_part_per_doc, Unset):
            files.append(("onePartPerDoc", (None, str(self.one_part_per_doc).encode(), "text/plain")))

        if not isinstance(self.owner_id, Unset):
            files.append(("ownerId", (None, str(self.owner_id).encode(), "text/plain")))

        if not isinstance(self.parent_id, Unset):
            files.append(("parentId", (None, str(self.parent_id).encode(), "text/plain")))

        if not isinstance(self.project_id, Unset):
            files.append(("projectId", (None, str(self.project_id).encode(), "text/plain")))

        if not isinstance(self.repoint_app_element_version_refs, Unset):
            files.append(
                (
                    "repointAppElementVersionRefs",
                    (None, str(self.repoint_app_element_version_refs).encode(), "text/plain"),
                )
            )

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

        if not isinstance(self.use_iges_import_post_processing, Unset):
            files.append(
                (
                    "useIGESImportPostProcessing",
                    (None, str(self.use_iges_import_post_processing).encode(), "text/plain"),
                )
            )

        if not isinstance(self.version_string, Unset):
            files.append(("versionString", (None, str(self.version_string).encode(), "text/plain")))

        if not isinstance(self.y_axis_is_up, Unset):
            files.append(("yAxisIsUp", (None, str(self.y_axis_is_up).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_faulty_parts = d.pop("allowFaultyParts", UNSET)

        create_composite = d.pop("createComposite", UNSET)

        create_drawing_if_possible = d.pop("createDrawingIfPossible", UNSET)

        encoded_filename = d.pop("encodedFilename", UNSET)

        extract_assembly_hierarchy = d.pop("extractAssemblyHierarchy", UNSET)

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        flatten_assemblies = d.pop("flattenAssemblies", UNSET)

        format_name = d.pop("formatName", UNSET)

        import_appearances = d.pop("importAppearances", UNSET)

        import_material_density = d.pop("importMaterialDensity", UNSET)

        import_within_document = d.pop("importWithinDocument", UNSET)

        join_adjacent_surfaces = d.pop("joinAdjacentSurfaces", UNSET)

        location_element_id = d.pop("locationElementId", UNSET)

        location_group_id = d.pop("locationGroupId", UNSET)

        location_position = d.pop("locationPosition", UNSET)

        make_public = d.pop("makePublic", UNSET)

        notify_user = d.pop("notifyUser", UNSET)

        one_part_per_doc = d.pop("onePartPerDoc", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        repoint_app_element_version_refs = d.pop("repointAppElementVersionRefs", UNSET)

        split_assemblies_into_multiple_documents = d.pop("splitAssembliesIntoMultipleDocuments", UNSET)

        store_in_document = d.pop("storeInDocument", UNSET)

        translate = d.pop("translate", UNSET)

        unit = d.pop("unit", UNSET)

        upload_id = d.pop("uploadId", UNSET)

        use_iges_import_post_processing = d.pop("useIGESImportPostProcessing", UNSET)

        version_string = d.pop("versionString", UNSET)

        y_axis_is_up = d.pop("yAxisIsUp", UNSET)

        btb_translation_request_params = cls(
            allow_faulty_parts=allow_faulty_parts,
            create_composite=create_composite,
            create_drawing_if_possible=create_drawing_if_possible,
            encoded_filename=encoded_filename,
            extract_assembly_hierarchy=extract_assembly_hierarchy,
            file=file,
            flatten_assemblies=flatten_assemblies,
            format_name=format_name,
            import_appearances=import_appearances,
            import_material_density=import_material_density,
            import_within_document=import_within_document,
            join_adjacent_surfaces=join_adjacent_surfaces,
            location_element_id=location_element_id,
            location_group_id=location_group_id,
            location_position=location_position,
            make_public=make_public,
            notify_user=notify_user,
            one_part_per_doc=one_part_per_doc,
            owner_id=owner_id,
            parent_id=parent_id,
            project_id=project_id,
            repoint_app_element_version_refs=repoint_app_element_version_refs,
            split_assemblies_into_multiple_documents=split_assemblies_into_multiple_documents,
            store_in_document=store_in_document,
            translate=translate,
            unit=unit,
            upload_id=upload_id,
            use_iges_import_post_processing=use_iges_import_post_processing,
            version_string=version_string,
            y_axis_is_up=y_axis_is_up,
        )

        btb_translation_request_params.additional_properties = d
        return btb_translation_request_params

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
