from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_version_element_ids_1897 import BTDocumentVersionElementIds1897
    from ..models.bt_object_id import BTObjectId
    from ..models.btp_node_7 import BTPNode7


T = TypeVar("T", bound="BTLocationInfo226")


@_attrs_define
class BTLocationInfo226:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        character (int | Unset):
        column (int | Unset):
        document (str | Unset):
        element_microversion (str | Unset):
        end_character (int | Unset):
        end_column (int | Unset):
        end_line (int | Unset):
        from_node (BTPNode7 | Unset):
        from_template (BTLocationInfo226 | Unset):
        language_version (int | Unset):
        line (int | Unset):
        module_ids (BTDocumentVersionElementIds1897 | Unset):
        node_id (str | Unset):
        parse_node_id (str | Unset):
        parse_node_id_raw (BTObjectId | Unset):
        top_level (str | Unset):
        version (str | Unset):
    """

    bt_type: str | Unset = UNSET
    character: int | Unset = UNSET
    column: int | Unset = UNSET
    document: str | Unset = UNSET
    element_microversion: str | Unset = UNSET
    end_character: int | Unset = UNSET
    end_column: int | Unset = UNSET
    end_line: int | Unset = UNSET
    from_node: BTPNode7 | Unset = UNSET
    from_template: BTLocationInfo226 | Unset = UNSET
    language_version: int | Unset = UNSET
    line: int | Unset = UNSET
    module_ids: BTDocumentVersionElementIds1897 | Unset = UNSET
    node_id: str | Unset = UNSET
    parse_node_id: str | Unset = UNSET
    parse_node_id_raw: BTObjectId | Unset = UNSET
    top_level: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        character = self.character

        column = self.column

        document = self.document

        element_microversion = self.element_microversion

        end_character = self.end_character

        end_column = self.end_column

        end_line = self.end_line

        from_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_node, Unset):
            from_node = self.from_node.to_dict()

        from_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_template, Unset):
            from_template = self.from_template.to_dict()

        language_version = self.language_version

        line = self.line

        module_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_ids, Unset):
            module_ids = self.module_ids.to_dict()

        node_id = self.node_id

        parse_node_id = self.parse_node_id

        parse_node_id_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parse_node_id_raw, Unset):
            parse_node_id_raw = self.parse_node_id_raw.to_dict()

        top_level = self.top_level

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if character is not UNSET:
            field_dict["character"] = character
        if column is not UNSET:
            field_dict["column"] = column
        if document is not UNSET:
            field_dict["document"] = document
        if element_microversion is not UNSET:
            field_dict["elementMicroversion"] = element_microversion
        if end_character is not UNSET:
            field_dict["endCharacter"] = end_character
        if end_column is not UNSET:
            field_dict["endColumn"] = end_column
        if end_line is not UNSET:
            field_dict["endLine"] = end_line
        if from_node is not UNSET:
            field_dict["fromNode"] = from_node
        if from_template is not UNSET:
            field_dict["fromTemplate"] = from_template
        if language_version is not UNSET:
            field_dict["languageVersion"] = language_version
        if line is not UNSET:
            field_dict["line"] = line
        if module_ids is not UNSET:
            field_dict["moduleIds"] = module_ids
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parse_node_id is not UNSET:
            field_dict["parseNodeId"] = parse_node_id
        if parse_node_id_raw is not UNSET:
            field_dict["parseNodeIdRaw"] = parse_node_id_raw
        if top_level is not UNSET:
            field_dict["topLevel"] = top_level
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_version_element_ids_1897 import BTDocumentVersionElementIds1897
        from ..models.bt_object_id import BTObjectId
        from ..models.btp_node_7 import BTPNode7

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        character = d.pop("character", UNSET)

        column = d.pop("column", UNSET)

        document = d.pop("document", UNSET)

        element_microversion = d.pop("elementMicroversion", UNSET)

        end_character = d.pop("endCharacter", UNSET)

        end_column = d.pop("endColumn", UNSET)

        end_line = d.pop("endLine", UNSET)

        _from_node = d.pop("fromNode", UNSET)
        from_node: BTPNode7 | Unset
        if isinstance(_from_node, Unset):
            from_node = UNSET
        else:
            from_node = BTPNode7.from_dict(_from_node)

        _from_template = d.pop("fromTemplate", UNSET)
        from_template: BTLocationInfo226 | Unset
        if isinstance(_from_template, Unset):
            from_template = UNSET
        else:
            from_template = BTLocationInfo226.from_dict(_from_template)

        language_version = d.pop("languageVersion", UNSET)

        line = d.pop("line", UNSET)

        _module_ids = d.pop("moduleIds", UNSET)
        module_ids: BTDocumentVersionElementIds1897 | Unset
        if isinstance(_module_ids, Unset):
            module_ids = UNSET
        else:
            module_ids = BTDocumentVersionElementIds1897.from_dict(_module_ids)

        node_id = d.pop("nodeId", UNSET)

        parse_node_id = d.pop("parseNodeId", UNSET)

        _parse_node_id_raw = d.pop("parseNodeIdRaw", UNSET)
        parse_node_id_raw: BTObjectId | Unset
        if isinstance(_parse_node_id_raw, Unset):
            parse_node_id_raw = UNSET
        else:
            parse_node_id_raw = BTObjectId.from_dict(_parse_node_id_raw)

        top_level = d.pop("topLevel", UNSET)

        version = d.pop("version", UNSET)

        bt_location_info_226 = cls(
            bt_type=bt_type,
            character=character,
            column=column,
            document=document,
            element_microversion=element_microversion,
            end_character=end_character,
            end_column=end_column,
            end_line=end_line,
            from_node=from_node,
            from_template=from_template,
            language_version=language_version,
            line=line,
            module_ids=module_ids,
            node_id=node_id,
            parse_node_id=parse_node_id,
            parse_node_id_raw=parse_node_id_raw,
            top_level=top_level,
            version=version,
        )

        bt_location_info_226.additional_properties = d
        return bt_location_info_226

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
