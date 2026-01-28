from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalPermissionInfo")


@_attrs_define
class GlobalPermissionInfo:
    """
    Attributes:
        access_reports (bool | Unset):
        admin_enterprise (bool | Unset):
        allow_app_store_access (bool | Unset):
        allow_public_documents_access (bool | Unset):
        approve_releases (bool | Unset):
        branch_lock_permissions (bool | Unset):
        create_documents_in_root (bool | Unset):
        create_project (bool | Unset):
        create_releases (bool | Unset):
        create_tasks (bool | Unset):
        delete_permanently (bool | Unset):
        export_files (bool | Unset):
        import_files (bool | Unset):
        manage_guest_users (bool | Unset):
        manage_non_geometric_items (bool | Unset):
        manage_rbac (bool | Unset):
        manage_standard_content_metadata (bool | Unset):
        manage_users (bool | Unset):
        manage_workflows (bool | Unset):
        share_for_anonymous_access (bool | Unset):
        transfer_documents_from_enterprise (bool | Unset):
        use_revision_tools (bool | Unset):
    """

    access_reports: bool | Unset = UNSET
    admin_enterprise: bool | Unset = UNSET
    allow_app_store_access: bool | Unset = UNSET
    allow_public_documents_access: bool | Unset = UNSET
    approve_releases: bool | Unset = UNSET
    branch_lock_permissions: bool | Unset = UNSET
    create_documents_in_root: bool | Unset = UNSET
    create_project: bool | Unset = UNSET
    create_releases: bool | Unset = UNSET
    create_tasks: bool | Unset = UNSET
    delete_permanently: bool | Unset = UNSET
    export_files: bool | Unset = UNSET
    import_files: bool | Unset = UNSET
    manage_guest_users: bool | Unset = UNSET
    manage_non_geometric_items: bool | Unset = UNSET
    manage_rbac: bool | Unset = UNSET
    manage_standard_content_metadata: bool | Unset = UNSET
    manage_users: bool | Unset = UNSET
    manage_workflows: bool | Unset = UNSET
    share_for_anonymous_access: bool | Unset = UNSET
    transfer_documents_from_enterprise: bool | Unset = UNSET
    use_revision_tools: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_reports = self.access_reports

        admin_enterprise = self.admin_enterprise

        allow_app_store_access = self.allow_app_store_access

        allow_public_documents_access = self.allow_public_documents_access

        approve_releases = self.approve_releases

        branch_lock_permissions = self.branch_lock_permissions

        create_documents_in_root = self.create_documents_in_root

        create_project = self.create_project

        create_releases = self.create_releases

        create_tasks = self.create_tasks

        delete_permanently = self.delete_permanently

        export_files = self.export_files

        import_files = self.import_files

        manage_guest_users = self.manage_guest_users

        manage_non_geometric_items = self.manage_non_geometric_items

        manage_rbac = self.manage_rbac

        manage_standard_content_metadata = self.manage_standard_content_metadata

        manage_users = self.manage_users

        manage_workflows = self.manage_workflows

        share_for_anonymous_access = self.share_for_anonymous_access

        transfer_documents_from_enterprise = self.transfer_documents_from_enterprise

        use_revision_tools = self.use_revision_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_reports is not UNSET:
            field_dict["accessReports"] = access_reports
        if admin_enterprise is not UNSET:
            field_dict["adminEnterprise"] = admin_enterprise
        if allow_app_store_access is not UNSET:
            field_dict["allowAppStoreAccess"] = allow_app_store_access
        if allow_public_documents_access is not UNSET:
            field_dict["allowPublicDocumentsAccess"] = allow_public_documents_access
        if approve_releases is not UNSET:
            field_dict["approveReleases"] = approve_releases
        if branch_lock_permissions is not UNSET:
            field_dict["branchLockPermissions"] = branch_lock_permissions
        if create_documents_in_root is not UNSET:
            field_dict["createDocumentsInRoot"] = create_documents_in_root
        if create_project is not UNSET:
            field_dict["createProject"] = create_project
        if create_releases is not UNSET:
            field_dict["createReleases"] = create_releases
        if create_tasks is not UNSET:
            field_dict["createTasks"] = create_tasks
        if delete_permanently is not UNSET:
            field_dict["deletePermanently"] = delete_permanently
        if export_files is not UNSET:
            field_dict["exportFiles"] = export_files
        if import_files is not UNSET:
            field_dict["importFiles"] = import_files
        if manage_guest_users is not UNSET:
            field_dict["manageGuestUsers"] = manage_guest_users
        if manage_non_geometric_items is not UNSET:
            field_dict["manageNonGeometricItems"] = manage_non_geometric_items
        if manage_rbac is not UNSET:
            field_dict["manageRbac"] = manage_rbac
        if manage_standard_content_metadata is not UNSET:
            field_dict["manageStandardContentMetadata"] = manage_standard_content_metadata
        if manage_users is not UNSET:
            field_dict["manageUsers"] = manage_users
        if manage_workflows is not UNSET:
            field_dict["manageWorkflows"] = manage_workflows
        if share_for_anonymous_access is not UNSET:
            field_dict["shareForAnonymousAccess"] = share_for_anonymous_access
        if transfer_documents_from_enterprise is not UNSET:
            field_dict["transferDocumentsFromEnterprise"] = transfer_documents_from_enterprise
        if use_revision_tools is not UNSET:
            field_dict["useRevisionTools"] = use_revision_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_reports = d.pop("accessReports", UNSET)

        admin_enterprise = d.pop("adminEnterprise", UNSET)

        allow_app_store_access = d.pop("allowAppStoreAccess", UNSET)

        allow_public_documents_access = d.pop("allowPublicDocumentsAccess", UNSET)

        approve_releases = d.pop("approveReleases", UNSET)

        branch_lock_permissions = d.pop("branchLockPermissions", UNSET)

        create_documents_in_root = d.pop("createDocumentsInRoot", UNSET)

        create_project = d.pop("createProject", UNSET)

        create_releases = d.pop("createReleases", UNSET)

        create_tasks = d.pop("createTasks", UNSET)

        delete_permanently = d.pop("deletePermanently", UNSET)

        export_files = d.pop("exportFiles", UNSET)

        import_files = d.pop("importFiles", UNSET)

        manage_guest_users = d.pop("manageGuestUsers", UNSET)

        manage_non_geometric_items = d.pop("manageNonGeometricItems", UNSET)

        manage_rbac = d.pop("manageRbac", UNSET)

        manage_standard_content_metadata = d.pop("manageStandardContentMetadata", UNSET)

        manage_users = d.pop("manageUsers", UNSET)

        manage_workflows = d.pop("manageWorkflows", UNSET)

        share_for_anonymous_access = d.pop("shareForAnonymousAccess", UNSET)

        transfer_documents_from_enterprise = d.pop("transferDocumentsFromEnterprise", UNSET)

        use_revision_tools = d.pop("useRevisionTools", UNSET)

        global_permission_info = cls(
            access_reports=access_reports,
            admin_enterprise=admin_enterprise,
            allow_app_store_access=allow_app_store_access,
            allow_public_documents_access=allow_public_documents_access,
            approve_releases=approve_releases,
            branch_lock_permissions=branch_lock_permissions,
            create_documents_in_root=create_documents_in_root,
            create_project=create_project,
            create_releases=create_releases,
            create_tasks=create_tasks,
            delete_permanently=delete_permanently,
            export_files=export_files,
            import_files=import_files,
            manage_guest_users=manage_guest_users,
            manage_non_geometric_items=manage_non_geometric_items,
            manage_rbac=manage_rbac,
            manage_standard_content_metadata=manage_standard_content_metadata,
            manage_users=manage_users,
            manage_workflows=manage_workflows,
            share_for_anonymous_access=share_for_anonymous_access,
            transfer_documents_from_enterprise=transfer_documents_from_enterprise,
            use_revision_tools=use_revision_tools,
        )

        global_permission_info.additional_properties = d
        return global_permission_info

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
