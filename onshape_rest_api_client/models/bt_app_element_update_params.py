from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_update_params_return_json_difference_format import (
    BTAppElementUpdateParamsReturnJsonDifferenceFormat,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_property_update_params import BTMetadataPropertyUpdateParams
    from ..models.btj_edit_3734 import BTJEdit3734


T = TypeVar("T", bound="BTAppElementUpdateParams")


@_attrs_define
class BTAppElementUpdateParams:
    """
    Attributes:
        description (str | Unset): The label that will appear in the document's edit history for this operation. If
            blank, a value will be auto-generated.
        json_patch (str | Unset): A json patch that will be applied to the application element's json data. The JSON
            patch format is as specified in RFC 6902 from the IETF.
        json_tree_edit (BTJEdit3734 | Unset): An edit that will be applied to the application element's json data.
        parent_change_id (str | Unset): The id of the last change made to this application element. This can be
            retrieved from the response for any app element modification endpoint.
        property_updates (list[BTMetadataPropertyUpdateParams] | Unset): Edits to be applied to the element's metadata.
        return_error (bool | Unset): If true, errors in request processing will be returned in a 200 response with a
            meaningful description. Otherwise, errors will result in a relevant HTTP error response.
        return_json_difference_format (BTAppElementUpdateParamsReturnJsonDifferenceFormat | Unset): If specified, and
            jsonTreeEdit is non-empty, the json difference will be returned in this format, otherwise no json difference
            will be returned.
        transaction_id (str | Unset): The id of the transaction in which this operation should take place. Transaction
            ids can be generated through the AppElement startTransaction API.
    """

    description: str | Unset = UNSET
    json_patch: str | Unset = UNSET
    json_tree_edit: BTJEdit3734 | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    property_updates: list[BTMetadataPropertyUpdateParams] | Unset = UNSET
    return_error: bool | Unset = UNSET
    return_json_difference_format: BTAppElementUpdateParamsReturnJsonDifferenceFormat | Unset = UNSET
    transaction_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        json_patch = self.json_patch

        json_tree_edit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.json_tree_edit, Unset):
            json_tree_edit = self.json_tree_edit.to_dict()

        parent_change_id = self.parent_change_id

        property_updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_updates, Unset):
            property_updates = []
            for property_updates_item_data in self.property_updates:
                property_updates_item = property_updates_item_data.to_dict()
                property_updates.append(property_updates_item)

        return_error = self.return_error

        return_json_difference_format: str | Unset = UNSET
        if not isinstance(self.return_json_difference_format, Unset):
            return_json_difference_format = self.return_json_difference_format.value

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if json_patch is not UNSET:
            field_dict["jsonPatch"] = json_patch
        if json_tree_edit is not UNSET:
            field_dict["jsonTreeEdit"] = json_tree_edit
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id
        if property_updates is not UNSET:
            field_dict["propertyUpdates"] = property_updates
        if return_error is not UNSET:
            field_dict["returnError"] = return_error
        if return_json_difference_format is not UNSET:
            field_dict["returnJsonDifferenceFormat"] = return_json_difference_format
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_metadata_property_update_params import BTMetadataPropertyUpdateParams
        from ..models.btj_edit_3734 import BTJEdit3734

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        json_patch = d.pop("jsonPatch", UNSET)

        _json_tree_edit = d.pop("jsonTreeEdit", UNSET)
        json_tree_edit: BTJEdit3734 | Unset
        if isinstance(_json_tree_edit, Unset):
            json_tree_edit = UNSET
        else:
            json_tree_edit = BTJEdit3734.from_dict(_json_tree_edit)

        parent_change_id = d.pop("parentChangeId", UNSET)

        _property_updates = d.pop("propertyUpdates", UNSET)
        property_updates: list[BTMetadataPropertyUpdateParams] | Unset = UNSET
        if _property_updates is not UNSET:
            property_updates = []
            for property_updates_item_data in _property_updates:
                property_updates_item = BTMetadataPropertyUpdateParams.from_dict(property_updates_item_data)

                property_updates.append(property_updates_item)

        return_error = d.pop("returnError", UNSET)

        _return_json_difference_format = d.pop("returnJsonDifferenceFormat", UNSET)
        return_json_difference_format: BTAppElementUpdateParamsReturnJsonDifferenceFormat | Unset
        if isinstance(_return_json_difference_format, Unset):
            return_json_difference_format = UNSET
        else:
            return_json_difference_format = BTAppElementUpdateParamsReturnJsonDifferenceFormat(
                _return_json_difference_format
            )

        transaction_id = d.pop("transactionId", UNSET)

        bt_app_element_update_params = cls(
            description=description,
            json_patch=json_patch,
            json_tree_edit=json_tree_edit,
            parent_change_id=parent_change_id,
            property_updates=property_updates,
            return_error=return_error,
            return_json_difference_format=return_json_difference_format,
            transaction_id=transaction_id,
        )

        bt_app_element_update_params.additional_properties = d
        return bt_app_element_update_params

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
