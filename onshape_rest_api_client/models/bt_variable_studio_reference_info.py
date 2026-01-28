from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_variable_studio_reference_info_configuration_id_to_value import (
        BTVariableStudioReferenceInfoConfigurationIdToValue,
    )


T = TypeVar("T", bound="BTVariableStudioReferenceInfo")


@_attrs_define
class BTVariableStudioReferenceInfo:
    """List of variable studio references

    Attributes:
        reference_element_id (str): ElementId of referenced variable studio
        configuration_id_to_value (BTVariableStudioReferenceInfoConfigurationIdToValue | Unset): Optional map of
            configuration parameter id to value
        entire_variable_studio (bool | Unset): Whether all variables in the referenced variable studio are included
        reference_document_id (str | Unset): DocumentId of referenced variable studio, blank for intra-workspace
            references
        reference_version_id (str | Unset): VersionId of referenced variable studio, blank for intra-workspace
            references
        variable_names (list[str] | Unset): Optional list of selected variables
    """

    reference_element_id: str
    configuration_id_to_value: BTVariableStudioReferenceInfoConfigurationIdToValue | Unset = UNSET
    entire_variable_studio: bool | Unset = UNSET
    reference_document_id: str | Unset = UNSET
    reference_version_id: str | Unset = UNSET
    variable_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_element_id = self.reference_element_id

        configuration_id_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration_id_to_value, Unset):
            configuration_id_to_value = self.configuration_id_to_value.to_dict()

        entire_variable_studio = self.entire_variable_studio

        reference_document_id = self.reference_document_id

        reference_version_id = self.reference_version_id

        variable_names: list[str] | Unset = UNSET
        if not isinstance(self.variable_names, Unset):
            variable_names = self.variable_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "referenceElementId": reference_element_id,
            }
        )
        if configuration_id_to_value is not UNSET:
            field_dict["configurationIdToValue"] = configuration_id_to_value
        if entire_variable_studio is not UNSET:
            field_dict["entireVariableStudio"] = entire_variable_studio
        if reference_document_id is not UNSET:
            field_dict["referenceDocumentId"] = reference_document_id
        if reference_version_id is not UNSET:
            field_dict["referenceVersionId"] = reference_version_id
        if variable_names is not UNSET:
            field_dict["variableNames"] = variable_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_variable_studio_reference_info_configuration_id_to_value import (
            BTVariableStudioReferenceInfoConfigurationIdToValue,
        )

        d = dict(src_dict)
        reference_element_id = d.pop("referenceElementId")

        _configuration_id_to_value = d.pop("configurationIdToValue", UNSET)
        configuration_id_to_value: BTVariableStudioReferenceInfoConfigurationIdToValue | Unset
        if isinstance(_configuration_id_to_value, Unset):
            configuration_id_to_value = UNSET
        else:
            configuration_id_to_value = BTVariableStudioReferenceInfoConfigurationIdToValue.from_dict(
                _configuration_id_to_value
            )

        entire_variable_studio = d.pop("entireVariableStudio", UNSET)

        reference_document_id = d.pop("referenceDocumentId", UNSET)

        reference_version_id = d.pop("referenceVersionId", UNSET)

        variable_names = cast(list[str], d.pop("variableNames", UNSET))

        bt_variable_studio_reference_info = cls(
            reference_element_id=reference_element_id,
            configuration_id_to_value=configuration_id_to_value,
            entire_variable_studio=entire_variable_studio,
            reference_document_id=reference_document_id,
            reference_version_id=reference_version_id,
            variable_names=variable_names,
        )

        bt_variable_studio_reference_info.additional_properties = d
        return bt_variable_studio_reference_info

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
