from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_element_location_params import BTElementLocationParams


T = TypeVar("T", bound="BTAppElementBulkCreateParams")


@_attrs_define
class BTAppElementBulkCreateParams:
    """
    Attributes:
        format_id (str): The data type of the application. This string allows an application to distinguish their
            elements from elements of another application.
        description (str | Unset): The label that will appear in the document's edit history for this operation. If
            blank, a value will be auto-generated.
        location (BTElementLocationParams | Unset): The location at which the new element should be inserted.
        names (list[str] | Unset): The name of the element being created. If blank, a name will be auto-generated.
    """

    format_id: str
    description: str | Unset = UNSET
    location: BTElementLocationParams | Unset = UNSET
    names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_id = self.format_id

        description = self.description

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        names: list[str] | Unset = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formatId": format_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if names is not UNSET:
            field_dict["names"] = names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_element_location_params import BTElementLocationParams

        d = dict(src_dict)
        format_id = d.pop("formatId")

        description = d.pop("description", UNSET)

        _location = d.pop("location", UNSET)
        location: BTElementLocationParams | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = BTElementLocationParams.from_dict(_location)

        names = cast(list[str], d.pop("names", UNSET))

        bt_app_element_bulk_create_params = cls(
            format_id=format_id,
            description=description,
            location=location,
            names=names,
        )

        bt_app_element_bulk_create_params.additional_properties = d
        return bt_app_element_bulk_create_params

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
