from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_lazily_parsed_feature_script_references import BTLazilyParsedFeatureScriptReferences
    from ..models.bt_ui_feature_studio_checksum_2438 import BTUiFeatureStudioChecksum2438
    from ..models.btm_model_141 import BTMModel141
    from ..models.btp_module_234 import BTPModule234
    from ..models.btp_module_id_235 import BTPModuleId235
    from ..models.lines import Lines


T = TypeVar("T", bound="BTLazilyParsedFeatureScript")


@_attrs_define
class BTLazilyParsedFeatureScript:
    """
    Attributes:
        checksum (BTUiFeatureStudioChecksum2438 | Unset):
        language_version (int | Unset):
        lines (Lines | Unset):
        model (BTMModel141 | Unset):
        module (BTPModule234 | Unset):
        module_id (BTPModuleId235 | Unset):
        notice_module_ids (BTPModuleId235 | Unset):
        parent_language_version (int | Unset):
        references (BTLazilyParsedFeatureScriptReferences | Unset):
        source (str | Unset):
    """

    checksum: BTUiFeatureStudioChecksum2438 | Unset = UNSET
    language_version: int | Unset = UNSET
    lines: Lines | Unset = UNSET
    model: BTMModel141 | Unset = UNSET
    module: BTPModule234 | Unset = UNSET
    module_id: BTPModuleId235 | Unset = UNSET
    notice_module_ids: BTPModuleId235 | Unset = UNSET
    parent_language_version: int | Unset = UNSET
    references: BTLazilyParsedFeatureScriptReferences | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checksum, Unset):
            checksum = self.checksum.to_dict()

        language_version = self.language_version

        lines: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = self.lines.to_dict()

        model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        module: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module, Unset):
            module = self.module.to_dict()

        module_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_id, Unset):
            module_id = self.module_id.to_dict()

        notice_module_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notice_module_ids, Unset):
            notice_module_ids = self.notice_module_ids.to_dict()

        parent_language_version = self.parent_language_version

        references: dict[str, Any] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if language_version is not UNSET:
            field_dict["languageVersion"] = language_version
        if lines is not UNSET:
            field_dict["lines"] = lines
        if model is not UNSET:
            field_dict["model"] = model
        if module is not UNSET:
            field_dict["module"] = module
        if module_id is not UNSET:
            field_dict["moduleId"] = module_id
        if notice_module_ids is not UNSET:
            field_dict["noticeModuleIds"] = notice_module_ids
        if parent_language_version is not UNSET:
            field_dict["parentLanguageVersion"] = parent_language_version
        if references is not UNSET:
            field_dict["references"] = references
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_lazily_parsed_feature_script_references import BTLazilyParsedFeatureScriptReferences
        from ..models.bt_ui_feature_studio_checksum_2438 import BTUiFeatureStudioChecksum2438
        from ..models.btm_model_141 import BTMModel141
        from ..models.btp_module_234 import BTPModule234
        from ..models.btp_module_id_235 import BTPModuleId235
        from ..models.lines import Lines

        d = dict(src_dict)
        _checksum = d.pop("checksum", UNSET)
        checksum: BTUiFeatureStudioChecksum2438 | Unset
        if isinstance(_checksum, Unset):
            checksum = UNSET
        else:
            checksum = BTUiFeatureStudioChecksum2438.from_dict(_checksum)

        language_version = d.pop("languageVersion", UNSET)

        _lines = d.pop("lines", UNSET)
        lines: Lines | Unset
        if isinstance(_lines, Unset):
            lines = UNSET
        else:
            lines = Lines.from_dict(_lines)

        _model = d.pop("model", UNSET)
        model: BTMModel141 | Unset
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = BTMModel141.from_dict(_model)

        _module = d.pop("module", UNSET)
        module: BTPModule234 | Unset
        if isinstance(_module, Unset):
            module = UNSET
        else:
            module = BTPModule234.from_dict(_module)

        _module_id = d.pop("moduleId", UNSET)
        module_id: BTPModuleId235 | Unset
        if isinstance(_module_id, Unset):
            module_id = UNSET
        else:
            module_id = BTPModuleId235.from_dict(_module_id)

        _notice_module_ids = d.pop("noticeModuleIds", UNSET)
        notice_module_ids: BTPModuleId235 | Unset
        if isinstance(_notice_module_ids, Unset):
            notice_module_ids = UNSET
        else:
            notice_module_ids = BTPModuleId235.from_dict(_notice_module_ids)

        parent_language_version = d.pop("parentLanguageVersion", UNSET)

        _references = d.pop("references", UNSET)
        references: BTLazilyParsedFeatureScriptReferences | Unset
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = BTLazilyParsedFeatureScriptReferences.from_dict(_references)

        source = d.pop("source", UNSET)

        bt_lazily_parsed_feature_script = cls(
            checksum=checksum,
            language_version=language_version,
            lines=lines,
            model=model,
            module=module,
            module_id=module_id,
            notice_module_ids=notice_module_ids,
            parent_language_version=parent_language_version,
            references=references,
            source=source,
        )

        bt_lazily_parsed_feature_script.additional_properties = d
        return bt_lazily_parsed_feature_script

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
