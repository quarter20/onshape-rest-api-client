from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_revert_unchanged_element_params import BTRevertUnchangedElementParams


T = TypeVar("T", bound="BTRevertUnchangedParams")


@_attrs_define
class BTRevertUnchangedParams:
    """
    Attributes:
        company_id (str | Unset):
        connection_id (str | Unset):
        do_update (bool | Unset):
        elements (list[BTRevertUnchangedElementParams] | Unset):
    """

    company_id: str | Unset = UNSET
    connection_id: str | Unset = UNSET
    do_update: bool | Unset = UNSET
    elements: list[BTRevertUnchangedElementParams] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        connection_id = self.connection_id

        do_update = self.do_update

        elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if do_update is not UNSET:
            field_dict["doUpdate"] = do_update
        if elements is not UNSET:
            field_dict["elements"] = elements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_revert_unchanged_element_params import BTRevertUnchangedElementParams

        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        do_update = d.pop("doUpdate", UNSET)

        _elements = d.pop("elements", UNSET)
        elements: list[BTRevertUnchangedElementParams] | Unset = UNSET
        if _elements is not UNSET:
            elements = []
            for elements_item_data in _elements:
                elements_item = BTRevertUnchangedElementParams.from_dict(elements_item_data)

                elements.append(elements_item)

        bt_revert_unchanged_params = cls(
            company_id=company_id,
            connection_id=connection_id,
            do_update=do_update,
            elements=elements,
        )

        bt_revert_unchanged_params.additional_properties = d
        return bt_revert_unchanged_params

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
