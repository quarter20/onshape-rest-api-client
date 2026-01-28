from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_acl_params_doc_state_params import BTAclParamsDocStateParams


T = TypeVar("T", bound="BTAclParams")


@_attrs_define
class BTAclParams:
    """
    Attributes:
        anonymous_access_allowed (bool | Unset):
        anonymous_allows_export (bool | Unset):
        doc_state_params (BTAclParamsDocStateParams | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        public (bool | Unset):
        workspace_id (str | Unset):
    """

    anonymous_access_allowed: bool | Unset = UNSET
    anonymous_allows_export: bool | Unset = UNSET
    doc_state_params: BTAclParamsDocStateParams | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    public: bool | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anonymous_access_allowed = self.anonymous_access_allowed

        anonymous_allows_export = self.anonymous_allows_export

        doc_state_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doc_state_params, Unset):
            doc_state_params = self.doc_state_params.to_dict()

        document_id = self.document_id

        element_id = self.element_id

        public = self.public

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anonymous_access_allowed is not UNSET:
            field_dict["anonymousAccessAllowed"] = anonymous_access_allowed
        if anonymous_allows_export is not UNSET:
            field_dict["anonymousAllowsExport"] = anonymous_allows_export
        if doc_state_params is not UNSET:
            field_dict["docStateParams"] = doc_state_params
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if public is not UNSET:
            field_dict["public"] = public
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_acl_params_doc_state_params import BTAclParamsDocStateParams

        d = dict(src_dict)
        anonymous_access_allowed = d.pop("anonymousAccessAllowed", UNSET)

        anonymous_allows_export = d.pop("anonymousAllowsExport", UNSET)

        _doc_state_params = d.pop("docStateParams", UNSET)
        doc_state_params: BTAclParamsDocStateParams | Unset
        if isinstance(_doc_state_params, Unset):
            doc_state_params = UNSET
        else:
            doc_state_params = BTAclParamsDocStateParams.from_dict(_doc_state_params)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        public = d.pop("public", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_acl_params = cls(
            anonymous_access_allowed=anonymous_access_allowed,
            anonymous_allows_export=anonymous_allows_export,
            doc_state_params=doc_state_params,
            document_id=document_id,
            element_id=element_id,
            public=public,
            workspace_id=workspace_id,
        )

        bt_acl_params.additional_properties = d
        return bt_acl_params

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
