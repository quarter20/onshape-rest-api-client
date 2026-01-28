from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_parts_export_filter_4308 import BTPartsExportFilter4308
    from ..models.btb_assembly_export_params import BTBAssemblyExportParams


T = TypeVar("T", bound="BTBExportAdvancedParams")


@_attrs_define
class BTBExportAdvancedParams:
    """Advanced element export options.

    Attributes:
        assembly_export_params (BTBAssemblyExportParams | Unset): Options for exporting assemblies.
        configuration (str | Unset): URL-encoded string of configuration values (separated by `;`). See the
            [Configurations API Guide](https://onshape-public.github.io/docs/api-adv/configs/) for details.
        element_ids (list[str] | Unset): An array of element ids for multi-element export.
        evaluate_export_rule (bool | Unset): Set to `true` to evaluate the export rule for the given `formatName` and to
            include an `exportRuleFileName` value in the response. Default: False.
        ignore_export_rules_for_contents (bool | Unset): For multiple elements export, use `true` if export rule
            shouldn't be applied for all elements. Default: False.
        link_document_id (str | Unset): The id of the document through which the above document should be accessed; only
            applicable when accessing a version of the document. This allows a user who has access to document a to see data
            from document b, as long as document b has been linked to document a by a user who has permission to both.
        link_document_workspace_id (str | Unset): The id of the workspace through which the above document should be
            accessed; only applicable when accessing a version of the document. This allows a user who has access to
            document a to see data from document b, as long as document b has been linked to document a by a user who has
            permission to both.
        part_ids (str | Unset): IDs of the parts to retrieve. Use comma-separated IDs for multiple parts (example:
            partIds=JHK,JHD).
        parts_export_filter (BTPartsExportFilter4308 | Unset): Skip mesh/curve foreign data creation in individual parts
            export
    """

    assembly_export_params: BTBAssemblyExportParams | Unset = UNSET
    configuration: str | Unset = UNSET
    element_ids: list[str] | Unset = UNSET
    evaluate_export_rule: bool | Unset = False
    ignore_export_rules_for_contents: bool | Unset = False
    link_document_id: str | Unset = UNSET
    link_document_workspace_id: str | Unset = UNSET
    part_ids: str | Unset = UNSET
    parts_export_filter: BTPartsExportFilter4308 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assembly_export_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assembly_export_params, Unset):
            assembly_export_params = self.assembly_export_params.to_dict()

        configuration = self.configuration

        element_ids: list[str] | Unset = UNSET
        if not isinstance(self.element_ids, Unset):
            element_ids = self.element_ids

        evaluate_export_rule = self.evaluate_export_rule

        ignore_export_rules_for_contents = self.ignore_export_rules_for_contents

        link_document_id = self.link_document_id

        link_document_workspace_id = self.link_document_workspace_id

        part_ids = self.part_ids

        parts_export_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parts_export_filter, Unset):
            parts_export_filter = self.parts_export_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assembly_export_params is not UNSET:
            field_dict["assemblyExportParams"] = assembly_export_params
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if element_ids is not UNSET:
            field_dict["elementIds"] = element_ids
        if evaluate_export_rule is not UNSET:
            field_dict["evaluateExportRule"] = evaluate_export_rule
        if ignore_export_rules_for_contents is not UNSET:
            field_dict["ignoreExportRulesForContents"] = ignore_export_rules_for_contents
        if link_document_id is not UNSET:
            field_dict["linkDocumentId"] = link_document_id
        if link_document_workspace_id is not UNSET:
            field_dict["linkDocumentWorkspaceId"] = link_document_workspace_id
        if part_ids is not UNSET:
            field_dict["partIds"] = part_ids
        if parts_export_filter is not UNSET:
            field_dict["partsExportFilter"] = parts_export_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parts_export_filter_4308 import BTPartsExportFilter4308
        from ..models.btb_assembly_export_params import BTBAssemblyExportParams

        d = dict(src_dict)
        _assembly_export_params = d.pop("assemblyExportParams", UNSET)
        assembly_export_params: BTBAssemblyExportParams | Unset
        if isinstance(_assembly_export_params, Unset):
            assembly_export_params = UNSET
        else:
            assembly_export_params = BTBAssemblyExportParams.from_dict(_assembly_export_params)

        configuration = d.pop("configuration", UNSET)

        element_ids = cast(list[str], d.pop("elementIds", UNSET))

        evaluate_export_rule = d.pop("evaluateExportRule", UNSET)

        ignore_export_rules_for_contents = d.pop("ignoreExportRulesForContents", UNSET)

        link_document_id = d.pop("linkDocumentId", UNSET)

        link_document_workspace_id = d.pop("linkDocumentWorkspaceId", UNSET)

        part_ids = d.pop("partIds", UNSET)

        _parts_export_filter = d.pop("partsExportFilter", UNSET)
        parts_export_filter: BTPartsExportFilter4308 | Unset
        if isinstance(_parts_export_filter, Unset):
            parts_export_filter = UNSET
        else:
            parts_export_filter = BTPartsExportFilter4308.from_dict(_parts_export_filter)

        btb_export_advanced_params = cls(
            assembly_export_params=assembly_export_params,
            configuration=configuration,
            element_ids=element_ids,
            evaluate_export_rule=evaluate_export_rule,
            ignore_export_rules_for_contents=ignore_export_rules_for_contents,
            link_document_id=link_document_id,
            link_document_workspace_id=link_document_workspace_id,
            part_ids=part_ids,
            parts_export_filter=parts_export_filter,
        )

        btb_export_advanced_params.additional_properties = d
        return btb_export_advanced_params

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
