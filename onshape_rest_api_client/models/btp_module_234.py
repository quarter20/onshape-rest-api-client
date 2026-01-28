from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_lazily_parsed_feature_script import BTLazilyParsedFeatureScript
    from ..models.btp_literal_number_258 import BTPLiteralNumber258
    from ..models.btp_module_234_deep_imports import BTPModule234DeepImports
    from ..models.btp_module_234_path_map import BTPModule234PathMap
    from ..models.btp_space_10 import BTPSpace10
    from ..models.btp_top_level_import_285 import BTPTopLevelImport285
    from ..models.btp_top_level_node_286 import BTPTopLevelNode286


T = TypeVar("T", bound="BTPModule234")


@_attrs_define
class BTPModule234:
    """
    Attributes:
        atomic (bool | Unset):
        bt_type (str | Unset): Type of JSON object.
        documentation_type (GBTPDefinitionType | Unset):
        end_source_location (int | Unset):
        node_id (str | Unset):
        short_descriptor (str | Unset):
        space_after (BTPSpace10 | Unset):
        space_before (BTPSpace10 | Unset):
        space_default (bool | Unset):
        start_source_location (int | Unset):
        deep_imports (BTPModule234DeepImports | Unset):
        fully_parsed (bool | Unset):
        imports (list[BTPTopLevelImport285] | Unset):
        is_blob (bool | Unset):
        is_internal_module (bool | Unset):
        may_have_implicit_imports (bool | Unset):
        path_map (BTPModule234PathMap | Unset):
        to_be_parsed (BTLazilyParsedFeatureScript | Unset):
        top_level (list[BTPTopLevelNode286] | Unset):
        version (BTPLiteralNumber258 | Unset):
        version_number (int | Unset):
    """

    atomic: bool | Unset = UNSET
    bt_type: str | Unset = UNSET
    documentation_type: GBTPDefinitionType | Unset = UNSET
    end_source_location: int | Unset = UNSET
    node_id: str | Unset = UNSET
    short_descriptor: str | Unset = UNSET
    space_after: BTPSpace10 | Unset = UNSET
    space_before: BTPSpace10 | Unset = UNSET
    space_default: bool | Unset = UNSET
    start_source_location: int | Unset = UNSET
    deep_imports: BTPModule234DeepImports | Unset = UNSET
    fully_parsed: bool | Unset = UNSET
    imports: list[BTPTopLevelImport285] | Unset = UNSET
    is_blob: bool | Unset = UNSET
    is_internal_module: bool | Unset = UNSET
    may_have_implicit_imports: bool | Unset = UNSET
    path_map: BTPModule234PathMap | Unset = UNSET
    to_be_parsed: BTLazilyParsedFeatureScript | Unset = UNSET
    top_level: list[BTPTopLevelNode286] | Unset = UNSET
    version: BTPLiteralNumber258 | Unset = UNSET
    version_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        atomic = self.atomic

        bt_type = self.bt_type

        documentation_type: str | Unset = UNSET
        if not isinstance(self.documentation_type, Unset):
            documentation_type = self.documentation_type.value

        end_source_location = self.end_source_location

        node_id = self.node_id

        short_descriptor = self.short_descriptor

        space_after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after, Unset):
            space_after = self.space_after.to_dict()

        space_before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before, Unset):
            space_before = self.space_before.to_dict()

        space_default = self.space_default

        start_source_location = self.start_source_location

        deep_imports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deep_imports, Unset):
            deep_imports = self.deep_imports.to_dict()

        fully_parsed = self.fully_parsed

        imports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.imports, Unset):
            imports = []
            for imports_item_data in self.imports:
                imports_item = imports_item_data.to_dict()
                imports.append(imports_item)

        is_blob = self.is_blob

        is_internal_module = self.is_internal_module

        may_have_implicit_imports = self.may_have_implicit_imports

        path_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path_map, Unset):
            path_map = self.path_map.to_dict()

        to_be_parsed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_be_parsed, Unset):
            to_be_parsed = self.to_be_parsed.to_dict()

        top_level: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_level, Unset):
            top_level = []
            for top_level_item_data in self.top_level:
                top_level_item = top_level_item_data.to_dict()
                top_level.append(top_level_item)

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        version_number = self.version_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if atomic is not UNSET:
            field_dict["atomic"] = atomic
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if documentation_type is not UNSET:
            field_dict["documentationType"] = documentation_type
        if end_source_location is not UNSET:
            field_dict["endSourceLocation"] = end_source_location
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if short_descriptor is not UNSET:
            field_dict["shortDescriptor"] = short_descriptor
        if space_after is not UNSET:
            field_dict["spaceAfter"] = space_after
        if space_before is not UNSET:
            field_dict["spaceBefore"] = space_before
        if space_default is not UNSET:
            field_dict["spaceDefault"] = space_default
        if start_source_location is not UNSET:
            field_dict["startSourceLocation"] = start_source_location
        if deep_imports is not UNSET:
            field_dict["deepImports"] = deep_imports
        if fully_parsed is not UNSET:
            field_dict["fullyParsed"] = fully_parsed
        if imports is not UNSET:
            field_dict["imports"] = imports
        if is_blob is not UNSET:
            field_dict["isBlob"] = is_blob
        if is_internal_module is not UNSET:
            field_dict["isInternalModule"] = is_internal_module
        if may_have_implicit_imports is not UNSET:
            field_dict["mayHaveImplicitImports"] = may_have_implicit_imports
        if path_map is not UNSET:
            field_dict["pathMap"] = path_map
        if to_be_parsed is not UNSET:
            field_dict["toBeParsed"] = to_be_parsed
        if top_level is not UNSET:
            field_dict["topLevel"] = top_level
        if version is not UNSET:
            field_dict["version"] = version
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_lazily_parsed_feature_script import BTLazilyParsedFeatureScript
        from ..models.btp_literal_number_258 import BTPLiteralNumber258
        from ..models.btp_module_234_deep_imports import BTPModule234DeepImports
        from ..models.btp_module_234_path_map import BTPModule234PathMap
        from ..models.btp_space_10 import BTPSpace10
        from ..models.btp_top_level_import_285 import BTPTopLevelImport285
        from ..models.btp_top_level_node_286 import BTPTopLevelNode286

        d = dict(src_dict)
        atomic = d.pop("atomic", UNSET)

        bt_type = d.pop("btType", UNSET)

        _documentation_type = d.pop("documentationType", UNSET)
        documentation_type: GBTPDefinitionType | Unset
        if isinstance(_documentation_type, Unset):
            documentation_type = UNSET
        else:
            documentation_type = GBTPDefinitionType(_documentation_type)

        end_source_location = d.pop("endSourceLocation", UNSET)

        node_id = d.pop("nodeId", UNSET)

        short_descriptor = d.pop("shortDescriptor", UNSET)

        _space_after = d.pop("spaceAfter", UNSET)
        space_after: BTPSpace10 | Unset
        if isinstance(_space_after, Unset):
            space_after = UNSET
        else:
            space_after = BTPSpace10.from_dict(_space_after)

        _space_before = d.pop("spaceBefore", UNSET)
        space_before: BTPSpace10 | Unset
        if isinstance(_space_before, Unset):
            space_before = UNSET
        else:
            space_before = BTPSpace10.from_dict(_space_before)

        space_default = d.pop("spaceDefault", UNSET)

        start_source_location = d.pop("startSourceLocation", UNSET)

        _deep_imports = d.pop("deepImports", UNSET)
        deep_imports: BTPModule234DeepImports | Unset
        if isinstance(_deep_imports, Unset):
            deep_imports = UNSET
        else:
            deep_imports = BTPModule234DeepImports.from_dict(_deep_imports)

        fully_parsed = d.pop("fullyParsed", UNSET)

        _imports = d.pop("imports", UNSET)
        imports: list[BTPTopLevelImport285] | Unset = UNSET
        if _imports is not UNSET:
            imports = []
            for imports_item_data in _imports:
                imports_item = BTPTopLevelImport285.from_dict(imports_item_data)

                imports.append(imports_item)

        is_blob = d.pop("isBlob", UNSET)

        is_internal_module = d.pop("isInternalModule", UNSET)

        may_have_implicit_imports = d.pop("mayHaveImplicitImports", UNSET)

        _path_map = d.pop("pathMap", UNSET)
        path_map: BTPModule234PathMap | Unset
        if isinstance(_path_map, Unset):
            path_map = UNSET
        else:
            path_map = BTPModule234PathMap.from_dict(_path_map)

        _to_be_parsed = d.pop("toBeParsed", UNSET)
        to_be_parsed: BTLazilyParsedFeatureScript | Unset
        if isinstance(_to_be_parsed, Unset):
            to_be_parsed = UNSET
        else:
            to_be_parsed = BTLazilyParsedFeatureScript.from_dict(_to_be_parsed)

        _top_level = d.pop("topLevel", UNSET)
        top_level: list[BTPTopLevelNode286] | Unset = UNSET
        if _top_level is not UNSET:
            top_level = []
            for top_level_item_data in _top_level:
                top_level_item = BTPTopLevelNode286.from_dict(top_level_item_data)

                top_level.append(top_level_item)

        _version = d.pop("version", UNSET)
        version: BTPLiteralNumber258 | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = BTPLiteralNumber258.from_dict(_version)

        version_number = d.pop("versionNumber", UNSET)

        btp_module_234 = cls(
            atomic=atomic,
            bt_type=bt_type,
            documentation_type=documentation_type,
            end_source_location=end_source_location,
            node_id=node_id,
            short_descriptor=short_descriptor,
            space_after=space_after,
            space_before=space_before,
            space_default=space_default,
            start_source_location=start_source_location,
            deep_imports=deep_imports,
            fully_parsed=fully_parsed,
            imports=imports,
            is_blob=is_blob,
            is_internal_module=is_internal_module,
            may_have_implicit_imports=may_have_implicit_imports,
            path_map=path_map,
            to_be_parsed=to_be_parsed,
            top_level=top_level,
            version=version,
            version_number=version_number,
        )

        btp_module_234.additional_properties = d
        return btp_module_234

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
