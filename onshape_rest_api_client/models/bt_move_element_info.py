from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_move_element_info_element_original_to_new_map import BTMoveElementInfoElementOriginalToNewMap


T = TypeVar("T", bound="BTMoveElementInfo")


@_attrs_define
class BTMoveElementInfo:
    """
    Attributes:
        element_original_to_new_map (BTMoveElementInfoElementOriginalToNewMap | Unset):
        error_message (str | Unset):
        is_new_document (bool | Unset):
        new_document_id (str | Unset):
        new_document_name (str | Unset):
        new_document_version_id (str | Unset):
        new_workspace_id (str | Unset):
    """

    element_original_to_new_map: BTMoveElementInfoElementOriginalToNewMap | Unset = UNSET
    error_message: str | Unset = UNSET
    is_new_document: bool | Unset = UNSET
    new_document_id: str | Unset = UNSET
    new_document_name: str | Unset = UNSET
    new_document_version_id: str | Unset = UNSET
    new_workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_original_to_new_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_original_to_new_map, Unset):
            element_original_to_new_map = self.element_original_to_new_map.to_dict()

        error_message = self.error_message

        is_new_document = self.is_new_document

        new_document_id = self.new_document_id

        new_document_name = self.new_document_name

        new_document_version_id = self.new_document_version_id

        new_workspace_id = self.new_workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_original_to_new_map is not UNSET:
            field_dict["elementOriginalToNewMap"] = element_original_to_new_map
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if is_new_document is not UNSET:
            field_dict["isNewDocument"] = is_new_document
        if new_document_id is not UNSET:
            field_dict["newDocumentId"] = new_document_id
        if new_document_name is not UNSET:
            field_dict["newDocumentName"] = new_document_name
        if new_document_version_id is not UNSET:
            field_dict["newDocumentVersionId"] = new_document_version_id
        if new_workspace_id is not UNSET:
            field_dict["newWorkspaceId"] = new_workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_move_element_info_element_original_to_new_map import BTMoveElementInfoElementOriginalToNewMap

        d = dict(src_dict)
        _element_original_to_new_map = d.pop("elementOriginalToNewMap", UNSET)
        element_original_to_new_map: BTMoveElementInfoElementOriginalToNewMap | Unset
        if isinstance(_element_original_to_new_map, Unset):
            element_original_to_new_map = UNSET
        else:
            element_original_to_new_map = BTMoveElementInfoElementOriginalToNewMap.from_dict(
                _element_original_to_new_map
            )

        error_message = d.pop("errorMessage", UNSET)

        is_new_document = d.pop("isNewDocument", UNSET)

        new_document_id = d.pop("newDocumentId", UNSET)

        new_document_name = d.pop("newDocumentName", UNSET)

        new_document_version_id = d.pop("newDocumentVersionId", UNSET)

        new_workspace_id = d.pop("newWorkspaceId", UNSET)

        bt_move_element_info = cls(
            element_original_to_new_map=element_original_to_new_map,
            error_message=error_message,
            is_new_document=is_new_document,
            new_document_id=new_document_id,
            new_document_name=new_document_name,
            new_document_version_id=new_document_version_id,
            new_workspace_id=new_workspace_id,
        )

        bt_move_element_info.additional_properties = d
        return bt_move_element_info

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
