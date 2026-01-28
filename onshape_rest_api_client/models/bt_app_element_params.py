from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_app_element_change_params import BTAppElementChangeParams
    from ..models.bt_app_element_params_json_tree import BTAppElementParamsJsonTree
    from ..models.bt_element_location_params import BTElementLocationParams


T = TypeVar("T", bound="BTAppElementParams")


@_attrs_define
class BTAppElementParams:
    """
    Attributes:
        format_id (str): The data type of the application. This string allows an application to distinguish their
            elements from elements of another application.
        description (str | Unset): The label that will appear in the document's edit history for this operation. If
            blank, a value will be auto-generated.
        json_tree (BTAppElementParamsJsonTree | Unset): Initialization data for the new element's json tree. Example: {
            'stringKey': 'bar', 'arrayKey': [ 1, 2, 3 ], 'objectKey': { 'subKey': false } }.
        location (BTElementLocationParams | Unset): The location at which the new element should be inserted.
        name (str | Unset): The name of the element being created. If blank, a name will be auto-generated.
        subelements (list[BTAppElementChangeParams] | Unset): Initialization data for the new element's subelements.
    """

    format_id: str
    description: str | Unset = UNSET
    json_tree: BTAppElementParamsJsonTree | Unset = UNSET
    location: BTElementLocationParams | Unset = UNSET
    name: str | Unset = UNSET
    subelements: list[BTAppElementChangeParams] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_id = self.format_id

        description = self.description

        json_tree: dict[str, Any] | Unset = UNSET
        if not isinstance(self.json_tree, Unset):
            json_tree = self.json_tree.to_dict()

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        name = self.name

        subelements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subelements, Unset):
            subelements = []
            for subelements_item_data in self.subelements:
                subelements_item = subelements_item_data.to_dict()
                subelements.append(subelements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formatId": format_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if json_tree is not UNSET:
            field_dict["jsonTree"] = json_tree
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if subelements is not UNSET:
            field_dict["subelements"] = subelements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_app_element_change_params import BTAppElementChangeParams
        from ..models.bt_app_element_params_json_tree import BTAppElementParamsJsonTree
        from ..models.bt_element_location_params import BTElementLocationParams

        d = dict(src_dict)
        format_id = d.pop("formatId")

        description = d.pop("description", UNSET)

        _json_tree = d.pop("jsonTree", UNSET)
        json_tree: BTAppElementParamsJsonTree | Unset
        if isinstance(_json_tree, Unset):
            json_tree = UNSET
        else:
            json_tree = BTAppElementParamsJsonTree.from_dict(_json_tree)

        _location = d.pop("location", UNSET)
        location: BTElementLocationParams | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = BTElementLocationParams.from_dict(_location)

        name = d.pop("name", UNSET)

        _subelements = d.pop("subelements", UNSET)
        subelements: list[BTAppElementChangeParams] | Unset = UNSET
        if _subelements is not UNSET:
            subelements = []
            for subelements_item_data in _subelements:
                subelements_item = BTAppElementChangeParams.from_dict(subelements_item_data)

                subelements.append(subelements_item)

        bt_app_element_params = cls(
            format_id=format_id,
            description=description,
            json_tree=json_tree,
            location=location,
            name=name,
            subelements=subelements,
        )

        bt_app_element_params.additional_properties = d
        return bt_app_element_params

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
