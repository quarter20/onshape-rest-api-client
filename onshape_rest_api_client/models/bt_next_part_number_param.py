from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_category_param import BTCategoryParam


T = TypeVar("T", bound="BTNextPartNumberParam")


@_attrs_define
class BTNextPartNumberParam:
    """Parameters for creating a part number.

    Attributes:
        categories (list[BTCategoryParam] | Unset):
        configuration (str | Unset): URL-encoded string of configuration values (separated by `;`). See the
            [Configurations API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for details.
        document_id (str | Unset): Document ID
        element_id (str | Unset): Element (tab) ID
        element_type (int | Unset): Element Type. Must be one of: `-1`: Unknown, `0`: Part Studio, `1`: Assembly, `2`:
            Drawing. `4` : Blob, `8`: Variable Studio
        id (str | Unset):
        mime_type (str | Unset):
        number_scheme_resource_type_id (str | Unset): Must be one of: `8c96700620f77935a0b2cddc`: Part Studio, assembly,
            or drawing, `29cd738cc6a8819fe84864e0`: Non-geometric items, `10f29fc285510ebc648108e6`: Standard content
        part_id (str | Unset): Part ID
        part_number (str | Unset): Current part number
        version_id (str | Unset): Version ID
        workspace_id (str | Unset): Workspace ID
    """

    categories: list[BTCategoryParam] | Unset = UNSET
    configuration: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    id: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    number_scheme_resource_type_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_number: str | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        configuration = self.configuration

        document_id = self.document_id

        element_id = self.element_id

        element_type = self.element_type

        id = self.id

        mime_type = self.mime_type

        number_scheme_resource_type_id = self.number_scheme_resource_type_id

        part_id = self.part_id

        part_number = self.part_number

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if number_scheme_resource_type_id is not UNSET:
            field_dict["numberSchemeResourceTypeId"] = number_scheme_resource_type_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_category_param import BTCategoryParam

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[BTCategoryParam] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = BTCategoryParam.from_dict(categories_item_data)

                categories.append(categories_item)

        configuration = d.pop("configuration", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        id = d.pop("id", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        number_scheme_resource_type_id = d.pop("numberSchemeResourceTypeId", UNSET)

        part_id = d.pop("partId", UNSET)

        part_number = d.pop("partNumber", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_next_part_number_param = cls(
            categories=categories,
            configuration=configuration,
            document_id=document_id,
            element_id=element_id,
            element_type=element_type,
            id=id,
            mime_type=mime_type,
            number_scheme_resource_type_id=number_scheme_resource_type_id,
            part_id=part_id,
            part_number=part_number,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_next_part_number_param.additional_properties = d
        return bt_next_part_number_param

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
