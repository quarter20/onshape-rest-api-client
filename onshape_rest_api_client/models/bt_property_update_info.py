from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_property_update_info_new_value import BTPropertyUpdateInfoNewValue
    from ..models.bt_property_update_info_old_value import BTPropertyUpdateInfoOldValue


T = TypeVar("T", bound="BTPropertyUpdateInfo")


@_attrs_define
class BTPropertyUpdateInfo:
    """
    Attributes:
        error_message (str | Unset):
        item_href (str | Unset):
        new_value (BTPropertyUpdateInfoNewValue | Unset):
        old_value (BTPropertyUpdateInfoOldValue | Unset):
        property_id (str | Unset):
    """

    error_message: str | Unset = UNSET
    item_href: str | Unset = UNSET
    new_value: BTPropertyUpdateInfoNewValue | Unset = UNSET
    old_value: BTPropertyUpdateInfoOldValue | Unset = UNSET
    property_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        item_href = self.item_href

        new_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_value, Unset):
            new_value = self.new_value.to_dict()

        old_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.old_value, Unset):
            old_value = self.old_value.to_dict()

        property_id = self.property_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if item_href is not UNSET:
            field_dict["itemHref"] = item_href
        if new_value is not UNSET:
            field_dict["newValue"] = new_value
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_property_update_info_new_value import BTPropertyUpdateInfoNewValue
        from ..models.bt_property_update_info_old_value import BTPropertyUpdateInfoOldValue

        d = dict(src_dict)
        error_message = d.pop("errorMessage", UNSET)

        item_href = d.pop("itemHref", UNSET)

        _new_value = d.pop("newValue", UNSET)
        new_value: BTPropertyUpdateInfoNewValue | Unset
        if isinstance(_new_value, Unset):
            new_value = UNSET
        else:
            new_value = BTPropertyUpdateInfoNewValue.from_dict(_new_value)

        _old_value = d.pop("oldValue", UNSET)
        old_value: BTPropertyUpdateInfoOldValue | Unset
        if isinstance(_old_value, Unset):
            old_value = UNSET
        else:
            old_value = BTPropertyUpdateInfoOldValue.from_dict(_old_value)

        property_id = d.pop("propertyId", UNSET)

        bt_property_update_info = cls(
            error_message=error_message,
            item_href=item_href,
            new_value=new_value,
            old_value=old_value,
            property_id=property_id,
        )

        bt_property_update_info.additional_properties = d
        return bt_property_update_info

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
