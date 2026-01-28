from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btb_cloud_storage_options import BTBCloudStorageOptions
    from ..models.btb_email_export_options import BTBEmailExportOptions
    from ..models.btb_export_advanced_params import BTBExportAdvancedParams
    from ..models.btb_export_mesh_params import BTBExportMeshParams


T = TypeVar("T", bound="BTBGltfExportParams")


@_attrs_define
class BTBGltfExportParams:
    """Options for exporting elements to GLTF.

    Attributes:
        advanced_params (BTBExportAdvancedParams | Unset): Advanced element export options.
        cloud_storage_options (BTBCloudStorageOptions | Unset): Options for exporting elements to cloud storage.
        destination_name (str | Unset): The name of the exported file. Default: 'Untitled'.
        email_export_options (BTBEmailExportOptions | Unset): Options for exporting elements as a link in an email.
        exclude_hidden_entities (bool | Unset): Whether or not to exclude hidden parts from export. Default: False.
        grouping (bool | Unset): Whether parts should be exported as a group or individually in a .zip file. Default:
            True.
        include_export_ids (bool | Unset): Whether topology ids should be exported as parasolid attributes. Default:
            False.
        is_y_axis_up (bool | Unset): Rotate model from Z-axis-up orientation to Y-axis-up. Default: False.
        mesh_params (BTBExportMeshParams | Unset): Options for an element export to mesh format.
        notify_user (bool | Unset): Send notification to the user client. Default: True.
        store_in_document (bool | Unset): Create a blob with exported file in the source document. Default: True.
        trigger_auto_download (bool | Unset): Automatically download a translated file. Default: False.
    """

    advanced_params: BTBExportAdvancedParams | Unset = UNSET
    cloud_storage_options: BTBCloudStorageOptions | Unset = UNSET
    destination_name: str | Unset = "Untitled"
    email_export_options: BTBEmailExportOptions | Unset = UNSET
    exclude_hidden_entities: bool | Unset = False
    grouping: bool | Unset = True
    include_export_ids: bool | Unset = False
    is_y_axis_up: bool | Unset = False
    mesh_params: BTBExportMeshParams | Unset = UNSET
    notify_user: bool | Unset = True
    store_in_document: bool | Unset = True
    trigger_auto_download: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advanced_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_params, Unset):
            advanced_params = self.advanced_params.to_dict()

        cloud_storage_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_storage_options, Unset):
            cloud_storage_options = self.cloud_storage_options.to_dict()

        destination_name = self.destination_name

        email_export_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email_export_options, Unset):
            email_export_options = self.email_export_options.to_dict()

        exclude_hidden_entities = self.exclude_hidden_entities

        grouping = self.grouping

        include_export_ids = self.include_export_ids

        is_y_axis_up = self.is_y_axis_up

        mesh_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mesh_params, Unset):
            mesh_params = self.mesh_params.to_dict()

        notify_user = self.notify_user

        store_in_document = self.store_in_document

        trigger_auto_download = self.trigger_auto_download

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advanced_params is not UNSET:
            field_dict["advancedParams"] = advanced_params
        if cloud_storage_options is not UNSET:
            field_dict["cloudStorageOptions"] = cloud_storage_options
        if destination_name is not UNSET:
            field_dict["destinationName"] = destination_name
        if email_export_options is not UNSET:
            field_dict["emailExportOptions"] = email_export_options
        if exclude_hidden_entities is not UNSET:
            field_dict["excludeHiddenEntities"] = exclude_hidden_entities
        if grouping is not UNSET:
            field_dict["grouping"] = grouping
        if include_export_ids is not UNSET:
            field_dict["includeExportIds"] = include_export_ids
        if is_y_axis_up is not UNSET:
            field_dict["isYAxisUp"] = is_y_axis_up
        if mesh_params is not UNSET:
            field_dict["meshParams"] = mesh_params
        if notify_user is not UNSET:
            field_dict["notifyUser"] = notify_user
        if store_in_document is not UNSET:
            field_dict["storeInDocument"] = store_in_document
        if trigger_auto_download is not UNSET:
            field_dict["triggerAutoDownload"] = trigger_auto_download

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btb_cloud_storage_options import BTBCloudStorageOptions
        from ..models.btb_email_export_options import BTBEmailExportOptions
        from ..models.btb_export_advanced_params import BTBExportAdvancedParams
        from ..models.btb_export_mesh_params import BTBExportMeshParams

        d = dict(src_dict)
        _advanced_params = d.pop("advancedParams", UNSET)
        advanced_params: BTBExportAdvancedParams | Unset
        if isinstance(_advanced_params, Unset):
            advanced_params = UNSET
        else:
            advanced_params = BTBExportAdvancedParams.from_dict(_advanced_params)

        _cloud_storage_options = d.pop("cloudStorageOptions", UNSET)
        cloud_storage_options: BTBCloudStorageOptions | Unset
        if isinstance(_cloud_storage_options, Unset):
            cloud_storage_options = UNSET
        else:
            cloud_storage_options = BTBCloudStorageOptions.from_dict(_cloud_storage_options)

        destination_name = d.pop("destinationName", UNSET)

        _email_export_options = d.pop("emailExportOptions", UNSET)
        email_export_options: BTBEmailExportOptions | Unset
        if isinstance(_email_export_options, Unset):
            email_export_options = UNSET
        else:
            email_export_options = BTBEmailExportOptions.from_dict(_email_export_options)

        exclude_hidden_entities = d.pop("excludeHiddenEntities", UNSET)

        grouping = d.pop("grouping", UNSET)

        include_export_ids = d.pop("includeExportIds", UNSET)

        is_y_axis_up = d.pop("isYAxisUp", UNSET)

        _mesh_params = d.pop("meshParams", UNSET)
        mesh_params: BTBExportMeshParams | Unset
        if isinstance(_mesh_params, Unset):
            mesh_params = UNSET
        else:
            mesh_params = BTBExportMeshParams.from_dict(_mesh_params)

        notify_user = d.pop("notifyUser", UNSET)

        store_in_document = d.pop("storeInDocument", UNSET)

        trigger_auto_download = d.pop("triggerAutoDownload", UNSET)

        btb_gltf_export_params = cls(
            advanced_params=advanced_params,
            cloud_storage_options=cloud_storage_options,
            destination_name=destination_name,
            email_export_options=email_export_options,
            exclude_hidden_entities=exclude_hidden_entities,
            grouping=grouping,
            include_export_ids=include_export_ids,
            is_y_axis_up=is_y_axis_up,
            mesh_params=mesh_params,
            notify_user=notify_user,
            store_in_document=store_in_document,
            trigger_auto_download=trigger_auto_download,
        )

        btb_gltf_export_params.additional_properties = d
        return btb_gltf_export_params

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
