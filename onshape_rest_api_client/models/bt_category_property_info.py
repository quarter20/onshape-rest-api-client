from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_category_property_config_info import BTCategoryPropertyConfigInfo
    from ..models.bt_metadata_category_summary_info import BTMetadataCategorySummaryInfo


T = TypeVar("T", bound="BTCategoryPropertyInfo")


@_attrs_define
class BTCategoryPropertyInfo:
    """
    Attributes:
        array (bool | Unset):
        assignable (bool | Unset):
        blob_mime_type (str | Unset):
        category_property_config_info (BTCategoryPropertyConfigInfo | Unset):
        category_summary_info_list (list[BTMetadataCategorySummaryInfo] | Unset):
        description (str | Unset):
        editable_in_microversion (bool | Unset):
        editable_in_version (bool | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        object_def_name (str | Unset):
        owner_id (str | Unset):
        owner_type (int | Unset):
        ui_readonly_in_microversion (bool | Unset):
        ui_readonly_in_version (bool | Unset):
        value_type (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    array: bool | Unset = UNSET
    assignable: bool | Unset = UNSET
    blob_mime_type: str | Unset = UNSET
    category_property_config_info: BTCategoryPropertyConfigInfo | Unset = UNSET
    category_summary_info_list: list[BTMetadataCategorySummaryInfo] | Unset = UNSET
    description: str | Unset = UNSET
    editable_in_microversion: bool | Unset = UNSET
    editable_in_version: bool | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    object_def_name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: int | Unset = UNSET
    ui_readonly_in_microversion: bool | Unset = UNSET
    ui_readonly_in_version: bool | Unset = UNSET
    value_type: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array = self.array

        assignable = self.assignable

        blob_mime_type = self.blob_mime_type

        category_property_config_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category_property_config_info, Unset):
            category_property_config_info = self.category_property_config_info.to_dict()

        category_summary_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category_summary_info_list, Unset):
            category_summary_info_list = []
            for category_summary_info_list_item_data in self.category_summary_info_list:
                category_summary_info_list_item = category_summary_info_list_item_data.to_dict()
                category_summary_info_list.append(category_summary_info_list_item)

        description = self.description

        editable_in_microversion = self.editable_in_microversion

        editable_in_version = self.editable_in_version

        href = self.href

        id = self.id

        name = self.name

        object_def_name = self.object_def_name

        owner_id = self.owner_id

        owner_type = self.owner_type

        ui_readonly_in_microversion = self.ui_readonly_in_microversion

        ui_readonly_in_version = self.ui_readonly_in_version

        value_type = self.value_type

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if array is not UNSET:
            field_dict["array"] = array
        if assignable is not UNSET:
            field_dict["assignable"] = assignable
        if blob_mime_type is not UNSET:
            field_dict["blobMimeType"] = blob_mime_type
        if category_property_config_info is not UNSET:
            field_dict["categoryPropertyConfigInfo"] = category_property_config_info
        if category_summary_info_list is not UNSET:
            field_dict["categorySummaryInfoList"] = category_summary_info_list
        if description is not UNSET:
            field_dict["description"] = description
        if editable_in_microversion is not UNSET:
            field_dict["editableInMicroversion"] = editable_in_microversion
        if editable_in_version is not UNSET:
            field_dict["editableInVersion"] = editable_in_version
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if object_def_name is not UNSET:
            field_dict["objectDefName"] = object_def_name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if ui_readonly_in_microversion is not UNSET:
            field_dict["uiReadonlyInMicroversion"] = ui_readonly_in_microversion
        if ui_readonly_in_version is not UNSET:
            field_dict["uiReadonlyInVersion"] = ui_readonly_in_version
        if value_type is not UNSET:
            field_dict["valueType"] = value_type
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_category_property_config_info import BTCategoryPropertyConfigInfo
        from ..models.bt_metadata_category_summary_info import BTMetadataCategorySummaryInfo

        d = dict(src_dict)
        array = d.pop("array", UNSET)

        assignable = d.pop("assignable", UNSET)

        blob_mime_type = d.pop("blobMimeType", UNSET)

        _category_property_config_info = d.pop("categoryPropertyConfigInfo", UNSET)
        category_property_config_info: BTCategoryPropertyConfigInfo | Unset
        if isinstance(_category_property_config_info, Unset):
            category_property_config_info = UNSET
        else:
            category_property_config_info = BTCategoryPropertyConfigInfo.from_dict(_category_property_config_info)

        _category_summary_info_list = d.pop("categorySummaryInfoList", UNSET)
        category_summary_info_list: list[BTMetadataCategorySummaryInfo] | Unset = UNSET
        if _category_summary_info_list is not UNSET:
            category_summary_info_list = []
            for category_summary_info_list_item_data in _category_summary_info_list:
                category_summary_info_list_item = BTMetadataCategorySummaryInfo.from_dict(
                    category_summary_info_list_item_data
                )

                category_summary_info_list.append(category_summary_info_list_item)

        description = d.pop("description", UNSET)

        editable_in_microversion = d.pop("editableInMicroversion", UNSET)

        editable_in_version = d.pop("editableInVersion", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        object_def_name = d.pop("objectDefName", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_type = d.pop("ownerType", UNSET)

        ui_readonly_in_microversion = d.pop("uiReadonlyInMicroversion", UNSET)

        ui_readonly_in_version = d.pop("uiReadonlyInVersion", UNSET)

        value_type = d.pop("valueType", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_category_property_info = cls(
            array=array,
            assignable=assignable,
            blob_mime_type=blob_mime_type,
            category_property_config_info=category_property_config_info,
            category_summary_info_list=category_summary_info_list,
            description=description,
            editable_in_microversion=editable_in_microversion,
            editable_in_version=editable_in_version,
            href=href,
            id=id,
            name=name,
            object_def_name=object_def_name,
            owner_id=owner_id,
            owner_type=owner_type,
            ui_readonly_in_microversion=ui_readonly_in_microversion,
            ui_readonly_in_version=ui_readonly_in_version,
            value_type=value_type,
            view_ref=view_ref,
        )

        bt_category_property_info.additional_properties = d
        return bt_category_property_info

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
