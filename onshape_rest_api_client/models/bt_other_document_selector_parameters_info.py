from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_folder_state_info import BTFolderStateInfo


T = TypeVar("T", bound="BTOtherDocumentSelectorParametersInfo")


@_attrs_define
class BTOtherDocumentSelectorParametersInfo:
    """
    Attributes:
        json_type (str):
        folder_state_path (list[BTFolderStateInfo] | Unset):
        selected_document_id (str | Unset):
        selected_version_id (str | Unset):
    """

    json_type: str
    folder_state_path: list[BTFolderStateInfo] | Unset = UNSET
    selected_document_id: str | Unset = UNSET
    selected_version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        folder_state_path: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.folder_state_path, Unset):
            folder_state_path = []
            for folder_state_path_item_data in self.folder_state_path:
                folder_state_path_item = folder_state_path_item_data.to_dict()
                folder_state_path.append(folder_state_path_item)

        selected_document_id = self.selected_document_id

        selected_version_id = self.selected_version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if folder_state_path is not UNSET:
            field_dict["folderStatePath"] = folder_state_path
        if selected_document_id is not UNSET:
            field_dict["selectedDocumentId"] = selected_document_id
        if selected_version_id is not UNSET:
            field_dict["selectedVersionId"] = selected_version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_folder_state_info import BTFolderStateInfo

        d = dict(src_dict)
        json_type = d.pop("jsonType")

        _folder_state_path = d.pop("folderStatePath", UNSET)
        folder_state_path: list[BTFolderStateInfo] | Unset = UNSET
        if _folder_state_path is not UNSET:
            folder_state_path = []
            for folder_state_path_item_data in _folder_state_path:
                folder_state_path_item = BTFolderStateInfo.from_dict(folder_state_path_item_data)

                folder_state_path.append(folder_state_path_item)

        selected_document_id = d.pop("selectedDocumentId", UNSET)

        selected_version_id = d.pop("selectedVersionId", UNSET)

        bt_other_document_selector_parameters_info = cls(
            json_type=json_type,
            folder_state_path=folder_state_path,
            selected_document_id=selected_document_id,
            selected_version_id=selected_version_id,
        )

        bt_other_document_selector_parameters_info.additional_properties = d
        return bt_other_document_selector_parameters_info

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
