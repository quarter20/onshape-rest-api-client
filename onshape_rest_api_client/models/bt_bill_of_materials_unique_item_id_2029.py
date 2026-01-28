from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_metadata_object_type import BTMetadataObjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_element_reference_725 import BTElementReference725
    from ..models.btpso_identity_2741 import BTPSOIdentity2741


T = TypeVar("T", bound="BTBillOfMaterialsUniqueItemId2029")


@_attrs_define
class BTBillOfMaterialsUniqueItemId2029:
    """
    Attributes:
        api_configuration (str | Unset):
        bt_type (str | Unset): Type of JSON object.
        is_standard_content (bool | Unset):
        item_definition_id (str | Unset):
        metadata_object_type (BTMetadataObjectType | Unset):
        part_id (str | Unset):
        part_identity (BTPSOIdentity2741 | Unset):
        source_element (BTElementReference725 | Unset):
        version_metadata_workspace_id (str | Unset):
        version_metadata_workspace_microversion_id (str | Unset):
    """

    api_configuration: str | Unset = UNSET
    bt_type: str | Unset = UNSET
    is_standard_content: bool | Unset = UNSET
    item_definition_id: str | Unset = UNSET
    metadata_object_type: BTMetadataObjectType | Unset = UNSET
    part_id: str | Unset = UNSET
    part_identity: BTPSOIdentity2741 | Unset = UNSET
    source_element: BTElementReference725 | Unset = UNSET
    version_metadata_workspace_id: str | Unset = UNSET
    version_metadata_workspace_microversion_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_configuration = self.api_configuration

        bt_type = self.bt_type

        is_standard_content = self.is_standard_content

        item_definition_id = self.item_definition_id

        metadata_object_type: str | Unset = UNSET
        if not isinstance(self.metadata_object_type, Unset):
            metadata_object_type = self.metadata_object_type.value

        part_id = self.part_id

        part_identity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_identity, Unset):
            part_identity = self.part_identity.to_dict()

        source_element: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_element, Unset):
            source_element = self.source_element.to_dict()

        version_metadata_workspace_id = self.version_metadata_workspace_id

        version_metadata_workspace_microversion_id = self.version_metadata_workspace_microversion_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_configuration is not UNSET:
            field_dict["apiConfiguration"] = api_configuration
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_standard_content is not UNSET:
            field_dict["isStandardContent"] = is_standard_content
        if item_definition_id is not UNSET:
            field_dict["itemDefinitionId"] = item_definition_id
        if metadata_object_type is not UNSET:
            field_dict["metadataObjectType"] = metadata_object_type
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if source_element is not UNSET:
            field_dict["sourceElement"] = source_element
        if version_metadata_workspace_id is not UNSET:
            field_dict["versionMetadataWorkspaceId"] = version_metadata_workspace_id
        if version_metadata_workspace_microversion_id is not UNSET:
            field_dict["versionMetadataWorkspaceMicroversionId"] = version_metadata_workspace_microversion_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_element_reference_725 import BTElementReference725
        from ..models.btpso_identity_2741 import BTPSOIdentity2741

        d = dict(src_dict)
        api_configuration = d.pop("apiConfiguration", UNSET)

        bt_type = d.pop("btType", UNSET)

        is_standard_content = d.pop("isStandardContent", UNSET)

        item_definition_id = d.pop("itemDefinitionId", UNSET)

        _metadata_object_type = d.pop("metadataObjectType", UNSET)
        metadata_object_type: BTMetadataObjectType | Unset
        if isinstance(_metadata_object_type, Unset):
            metadata_object_type = UNSET
        else:
            metadata_object_type = BTMetadataObjectType(_metadata_object_type)

        part_id = d.pop("partId", UNSET)

        _part_identity = d.pop("partIdentity", UNSET)
        part_identity: BTPSOIdentity2741 | Unset
        if isinstance(_part_identity, Unset):
            part_identity = UNSET
        else:
            part_identity = BTPSOIdentity2741.from_dict(_part_identity)

        _source_element = d.pop("sourceElement", UNSET)
        source_element: BTElementReference725 | Unset
        if isinstance(_source_element, Unset):
            source_element = UNSET
        else:
            source_element = BTElementReference725.from_dict(_source_element)

        version_metadata_workspace_id = d.pop("versionMetadataWorkspaceId", UNSET)

        version_metadata_workspace_microversion_id = d.pop("versionMetadataWorkspaceMicroversionId", UNSET)

        bt_bill_of_materials_unique_item_id_2029 = cls(
            api_configuration=api_configuration,
            bt_type=bt_type,
            is_standard_content=is_standard_content,
            item_definition_id=item_definition_id,
            metadata_object_type=metadata_object_type,
            part_id=part_id,
            part_identity=part_identity,
            source_element=source_element,
            version_metadata_workspace_id=version_metadata_workspace_id,
            version_metadata_workspace_microversion_id=version_metadata_workspace_microversion_id,
        )

        bt_bill_of_materials_unique_item_id_2029.additional_properties = d
        return bt_bill_of_materials_unique_item_id_2029

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
