from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bt_role import BTRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_billing_plan_info import BTBillingPlanInfo
    from ..models.bt_company_summary_info import BTCompanySummaryInfo
    from ..models.bt_device_login_secret_info import BTDeviceLoginSecretInfo
    from ..models.bt_discount import BTDiscount
    from ..models.bt_discount_info import BTDiscountInfo
    from ..models.bt_privacy_consent_info import BTPrivacyConsentInfo
    from ..models.bt_purchase_info import BTPurchaseInfo
    from ..models.bt_session_credential_info import BTSessionCredentialInfo
    from ..models.bt_trial_info import BTTrialInfo
    from ..models.bt_user_metrics_info import BTUserMetricsInfo
    from ..models.global_permission_info import GlobalPermissionInfo


T = TypeVar("T", bound="BTUserAdminInfo")


@_attrs_define
class BTUserAdminInfo:
    """
    Attributes:
        json_type (str):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        image (str | Unset):
        is_onshape_support (bool | Unset):
        state (int | Unset):
        documentation_name (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        company (BTCompanySummaryInfo | Unset):
        documentation_name_override (str | Unset):
        global_permissions (GlobalPermissionInfo | Unset):
        invitation_state (int | Unset):
        is_external (bool | Unset):
        is_guest (bool | Unset):
        is_light (bool | Unset):
        last_login_time (datetime.datetime | Unset):
        personal_message_allowed (bool | Unset):
        source (int | Unset):
        active_plan (BTBillingPlanInfo | Unset):
        active_plan_id (str | Unset):
        active_purchases (list[BTPurchaseInfo] | Unset):
        active_trial_info (BTTrialInfo | Unset):
        b_2_c_id (str | Unset):
        billing_update_required (bool | Unset):
        cad_system_at_signup (str | Unset):
        country_code (str | Unset):
        created_at (datetime.datetime | Unset):
        credential (BTSessionCredentialInfo | Unset):
        default_company_name (str | Unset):
        description (str | Unset):
        device_info (BTDeviceLoginSecretInfo | Unset):
        discounts (list[BTDiscountInfo] | Unset):
        enterprise (bool | Unset):
        eula_id (str | Unset):
        eula_required (bool | Unset):
        eval_center (bool | Unset):
        forum_id (str | Unset):
        intended_use (int | Unset):
        last_trial_info (BTTrialInfo | Unset):
        need_to_reset_client_cache_time (datetime.datetime | Unset):
        need_to_show_new_walkthrough (bool | Unset):
        own_purchase (BTPurchaseInfo | Unset):
        phone_number (str | Unset):
        pro_discovery_trial_rejected (bool | Unset):
        product_type (list[str] | Unset):
        redirect_url (str | Unset):
        role (int | Unset):
        roles (list[BTRole] | Unset):
        rum_enabled (bool | Unset):
        show_renew_student_pages (bool | Unset):
        startup_page (int | Unset):
        system_user (bool | Unset):
        totp_enabled (bool | Unset):
        tracing_enabled (bool | Unset):
        trial_infos (list[BTTrialInfo] | Unset):
        discount (BTDiscount | Unset):
        invitation_id (str | Unset):
        invited_by_email (str | Unset):
        invited_document_id (str | Unset):
        is_trial_request (bool | Unset):
        privacy_consents (list[BTPrivacyConsentInfo] | Unset):
        user_metrics (BTUserMetricsInfo | Unset):
    """

    json_type: str
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    image: str | Unset = UNSET
    is_onshape_support: bool | Unset = UNSET
    state: int | Unset = UNSET
    documentation_name: str | Unset = UNSET
    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    company: BTCompanySummaryInfo | Unset = UNSET
    documentation_name_override: str | Unset = UNSET
    global_permissions: GlobalPermissionInfo | Unset = UNSET
    invitation_state: int | Unset = UNSET
    is_external: bool | Unset = UNSET
    is_guest: bool | Unset = UNSET
    is_light: bool | Unset = UNSET
    last_login_time: datetime.datetime | Unset = UNSET
    personal_message_allowed: bool | Unset = UNSET
    source: int | Unset = UNSET
    active_plan: BTBillingPlanInfo | Unset = UNSET
    active_plan_id: str | Unset = UNSET
    active_purchases: list[BTPurchaseInfo] | Unset = UNSET
    active_trial_info: BTTrialInfo | Unset = UNSET
    b_2_c_id: str | Unset = UNSET
    billing_update_required: bool | Unset = UNSET
    cad_system_at_signup: str | Unset = UNSET
    country_code: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    credential: BTSessionCredentialInfo | Unset = UNSET
    default_company_name: str | Unset = UNSET
    description: str | Unset = UNSET
    device_info: BTDeviceLoginSecretInfo | Unset = UNSET
    discounts: list[BTDiscountInfo] | Unset = UNSET
    enterprise: bool | Unset = UNSET
    eula_id: str | Unset = UNSET
    eula_required: bool | Unset = UNSET
    eval_center: bool | Unset = UNSET
    forum_id: str | Unset = UNSET
    intended_use: int | Unset = UNSET
    last_trial_info: BTTrialInfo | Unset = UNSET
    need_to_reset_client_cache_time: datetime.datetime | Unset = UNSET
    need_to_show_new_walkthrough: bool | Unset = UNSET
    own_purchase: BTPurchaseInfo | Unset = UNSET
    phone_number: str | Unset = UNSET
    pro_discovery_trial_rejected: bool | Unset = UNSET
    product_type: list[str] | Unset = UNSET
    redirect_url: str | Unset = UNSET
    role: int | Unset = UNSET
    roles: list[BTRole] | Unset = UNSET
    rum_enabled: bool | Unset = UNSET
    show_renew_student_pages: bool | Unset = UNSET
    startup_page: int | Unset = UNSET
    system_user: bool | Unset = UNSET
    totp_enabled: bool | Unset = UNSET
    tracing_enabled: bool | Unset = UNSET
    trial_infos: list[BTTrialInfo] | Unset = UNSET
    discount: BTDiscount | Unset = UNSET
    invitation_id: str | Unset = UNSET
    invited_by_email: str | Unset = UNSET
    invited_document_id: str | Unset = UNSET
    is_trial_request: bool | Unset = UNSET
    privacy_consents: list[BTPrivacyConsentInfo] | Unset = UNSET
    user_metrics: BTUserMetricsInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        href = self.href

        id = self.id

        name = self.name

        view_ref = self.view_ref

        image = self.image

        is_onshape_support = self.is_onshape_support

        state = self.state

        documentation_name = self.documentation_name

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        documentation_name_override = self.documentation_name_override

        global_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_permissions, Unset):
            global_permissions = self.global_permissions.to_dict()

        invitation_state = self.invitation_state

        is_external = self.is_external

        is_guest = self.is_guest

        is_light = self.is_light

        last_login_time: str | Unset = UNSET
        if not isinstance(self.last_login_time, Unset):
            last_login_time = self.last_login_time.isoformat()

        personal_message_allowed = self.personal_message_allowed

        source = self.source

        active_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_plan, Unset):
            active_plan = self.active_plan.to_dict()

        active_plan_id = self.active_plan_id

        active_purchases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.active_purchases, Unset):
            active_purchases = []
            for active_purchases_item_data in self.active_purchases:
                active_purchases_item = active_purchases_item_data.to_dict()
                active_purchases.append(active_purchases_item)

        active_trial_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_trial_info, Unset):
            active_trial_info = self.active_trial_info.to_dict()

        b_2_c_id = self.b_2_c_id

        billing_update_required = self.billing_update_required

        cad_system_at_signup = self.cad_system_at_signup

        country_code = self.country_code

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        credential: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

        default_company_name = self.default_company_name

        description = self.description

        device_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = self.device_info.to_dict()

        discounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)

        enterprise = self.enterprise

        eula_id = self.eula_id

        eula_required = self.eula_required

        eval_center = self.eval_center

        forum_id = self.forum_id

        intended_use = self.intended_use

        last_trial_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_trial_info, Unset):
            last_trial_info = self.last_trial_info.to_dict()

        need_to_reset_client_cache_time: str | Unset = UNSET
        if not isinstance(self.need_to_reset_client_cache_time, Unset):
            need_to_reset_client_cache_time = self.need_to_reset_client_cache_time.isoformat()

        need_to_show_new_walkthrough = self.need_to_show_new_walkthrough

        own_purchase: dict[str, Any] | Unset = UNSET
        if not isinstance(self.own_purchase, Unset):
            own_purchase = self.own_purchase.to_dict()

        phone_number = self.phone_number

        pro_discovery_trial_rejected = self.pro_discovery_trial_rejected

        product_type: list[str] | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type

        redirect_url = self.redirect_url

        role = self.role

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value
                roles.append(roles_item)

        rum_enabled = self.rum_enabled

        show_renew_student_pages = self.show_renew_student_pages

        startup_page = self.startup_page

        system_user = self.system_user

        totp_enabled = self.totp_enabled

        tracing_enabled = self.tracing_enabled

        trial_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.trial_infos, Unset):
            trial_infos = []
            for trial_infos_item_data in self.trial_infos:
                trial_infos_item = trial_infos_item_data.to_dict()
                trial_infos.append(trial_infos_item)

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        invitation_id = self.invitation_id

        invited_by_email = self.invited_by_email

        invited_document_id = self.invited_document_id

        is_trial_request = self.is_trial_request

        privacy_consents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.privacy_consents, Unset):
            privacy_consents = []
            for privacy_consents_item_data in self.privacy_consents:
                privacy_consents_item = privacy_consents_item_data.to_dict()
                privacy_consents.append(privacy_consents_item)

        user_metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_metrics, Unset):
            user_metrics = self.user_metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if image is not UNSET:
            field_dict["image"] = image
        if is_onshape_support is not UNSET:
            field_dict["isOnshapeSupport"] = is_onshape_support
        if state is not UNSET:
            field_dict["state"] = state
        if documentation_name is not UNSET:
            field_dict["documentationName"] = documentation_name
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company is not UNSET:
            field_dict["company"] = company
        if documentation_name_override is not UNSET:
            field_dict["documentationNameOverride"] = documentation_name_override
        if global_permissions is not UNSET:
            field_dict["globalPermissions"] = global_permissions
        if invitation_state is not UNSET:
            field_dict["invitationState"] = invitation_state
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_guest is not UNSET:
            field_dict["isGuest"] = is_guest
        if is_light is not UNSET:
            field_dict["isLight"] = is_light
        if last_login_time is not UNSET:
            field_dict["lastLoginTime"] = last_login_time
        if personal_message_allowed is not UNSET:
            field_dict["personalMessageAllowed"] = personal_message_allowed
        if source is not UNSET:
            field_dict["source"] = source
        if active_plan is not UNSET:
            field_dict["activePlan"] = active_plan
        if active_plan_id is not UNSET:
            field_dict["activePlanId"] = active_plan_id
        if active_purchases is not UNSET:
            field_dict["activePurchases"] = active_purchases
        if active_trial_info is not UNSET:
            field_dict["activeTrialInfo"] = active_trial_info
        if b_2_c_id is not UNSET:
            field_dict["b2cId"] = b_2_c_id
        if billing_update_required is not UNSET:
            field_dict["billingUpdateRequired"] = billing_update_required
        if cad_system_at_signup is not UNSET:
            field_dict["cadSystemAtSignup"] = cad_system_at_signup
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if credential is not UNSET:
            field_dict["credential"] = credential
        if default_company_name is not UNSET:
            field_dict["defaultCompanyName"] = default_company_name
        if description is not UNSET:
            field_dict["description"] = description
        if device_info is not UNSET:
            field_dict["deviceInfo"] = device_info
        if discounts is not UNSET:
            field_dict["discounts"] = discounts
        if enterprise is not UNSET:
            field_dict["enterprise"] = enterprise
        if eula_id is not UNSET:
            field_dict["eulaId"] = eula_id
        if eula_required is not UNSET:
            field_dict["eulaRequired"] = eula_required
        if eval_center is not UNSET:
            field_dict["evalCenter"] = eval_center
        if forum_id is not UNSET:
            field_dict["forumId"] = forum_id
        if intended_use is not UNSET:
            field_dict["intendedUse"] = intended_use
        if last_trial_info is not UNSET:
            field_dict["lastTrialInfo"] = last_trial_info
        if need_to_reset_client_cache_time is not UNSET:
            field_dict["needToResetClientCacheTime"] = need_to_reset_client_cache_time
        if need_to_show_new_walkthrough is not UNSET:
            field_dict["needToShowNewWalkthrough"] = need_to_show_new_walkthrough
        if own_purchase is not UNSET:
            field_dict["ownPurchase"] = own_purchase
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if pro_discovery_trial_rejected is not UNSET:
            field_dict["proDiscoveryTrialRejected"] = pro_discovery_trial_rejected
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if role is not UNSET:
            field_dict["role"] = role
        if roles is not UNSET:
            field_dict["roles"] = roles
        if rum_enabled is not UNSET:
            field_dict["rumEnabled"] = rum_enabled
        if show_renew_student_pages is not UNSET:
            field_dict["showRenewStudentPages"] = show_renew_student_pages
        if startup_page is not UNSET:
            field_dict["startupPage"] = startup_page
        if system_user is not UNSET:
            field_dict["systemUser"] = system_user
        if totp_enabled is not UNSET:
            field_dict["totpEnabled"] = totp_enabled
        if tracing_enabled is not UNSET:
            field_dict["tracingEnabled"] = tracing_enabled
        if trial_infos is not UNSET:
            field_dict["trialInfos"] = trial_infos
        if discount is not UNSET:
            field_dict["discount"] = discount
        if invitation_id is not UNSET:
            field_dict["invitationId"] = invitation_id
        if invited_by_email is not UNSET:
            field_dict["invitedByEmail"] = invited_by_email
        if invited_document_id is not UNSET:
            field_dict["invitedDocumentId"] = invited_document_id
        if is_trial_request is not UNSET:
            field_dict["isTrialRequest"] = is_trial_request
        if privacy_consents is not UNSET:
            field_dict["privacyConsents"] = privacy_consents
        if user_metrics is not UNSET:
            field_dict["userMetrics"] = user_metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_billing_plan_info import BTBillingPlanInfo
        from ..models.bt_company_summary_info import BTCompanySummaryInfo
        from ..models.bt_device_login_secret_info import BTDeviceLoginSecretInfo
        from ..models.bt_discount import BTDiscount
        from ..models.bt_discount_info import BTDiscountInfo
        from ..models.bt_privacy_consent_info import BTPrivacyConsentInfo
        from ..models.bt_purchase_info import BTPurchaseInfo
        from ..models.bt_session_credential_info import BTSessionCredentialInfo
        from ..models.bt_trial_info import BTTrialInfo
        from ..models.bt_user_metrics_info import BTUserMetricsInfo
        from ..models.global_permission_info import GlobalPermissionInfo

        d = dict(src_dict)
        json_type = d.pop("jsonType")

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        image = d.pop("image", UNSET)

        is_onshape_support = d.pop("isOnshapeSupport", UNSET)

        state = d.pop("state", UNSET)

        documentation_name = d.pop("documentationName", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _company = d.pop("company", UNSET)
        company: BTCompanySummaryInfo | Unset
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = BTCompanySummaryInfo.from_dict(_company)

        documentation_name_override = d.pop("documentationNameOverride", UNSET)

        _global_permissions = d.pop("globalPermissions", UNSET)
        global_permissions: GlobalPermissionInfo | Unset
        if isinstance(_global_permissions, Unset):
            global_permissions = UNSET
        else:
            global_permissions = GlobalPermissionInfo.from_dict(_global_permissions)

        invitation_state = d.pop("invitationState", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_guest = d.pop("isGuest", UNSET)

        is_light = d.pop("isLight", UNSET)

        _last_login_time = d.pop("lastLoginTime", UNSET)
        last_login_time: datetime.datetime | Unset
        if isinstance(_last_login_time, Unset):
            last_login_time = UNSET
        else:
            last_login_time = isoparse(_last_login_time)

        personal_message_allowed = d.pop("personalMessageAllowed", UNSET)

        source = d.pop("source", UNSET)

        _active_plan = d.pop("activePlan", UNSET)
        active_plan: BTBillingPlanInfo | Unset
        if isinstance(_active_plan, Unset):
            active_plan = UNSET
        else:
            active_plan = BTBillingPlanInfo.from_dict(_active_plan)

        active_plan_id = d.pop("activePlanId", UNSET)

        _active_purchases = d.pop("activePurchases", UNSET)
        active_purchases: list[BTPurchaseInfo] | Unset = UNSET
        if _active_purchases is not UNSET:
            active_purchases = []
            for active_purchases_item_data in _active_purchases:
                active_purchases_item = BTPurchaseInfo.from_dict(active_purchases_item_data)

                active_purchases.append(active_purchases_item)

        _active_trial_info = d.pop("activeTrialInfo", UNSET)
        active_trial_info: BTTrialInfo | Unset
        if isinstance(_active_trial_info, Unset):
            active_trial_info = UNSET
        else:
            active_trial_info = BTTrialInfo.from_dict(_active_trial_info)

        b_2_c_id = d.pop("b2cId", UNSET)

        billing_update_required = d.pop("billingUpdateRequired", UNSET)

        cad_system_at_signup = d.pop("cadSystemAtSignup", UNSET)

        country_code = d.pop("countryCode", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _credential = d.pop("credential", UNSET)
        credential: BTSessionCredentialInfo | Unset
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = BTSessionCredentialInfo.from_dict(_credential)

        default_company_name = d.pop("defaultCompanyName", UNSET)

        description = d.pop("description", UNSET)

        _device_info = d.pop("deviceInfo", UNSET)
        device_info: BTDeviceLoginSecretInfo | Unset
        if isinstance(_device_info, Unset):
            device_info = UNSET
        else:
            device_info = BTDeviceLoginSecretInfo.from_dict(_device_info)

        _discounts = d.pop("discounts", UNSET)
        discounts: list[BTDiscountInfo] | Unset = UNSET
        if _discounts is not UNSET:
            discounts = []
            for discounts_item_data in _discounts:
                discounts_item = BTDiscountInfo.from_dict(discounts_item_data)

                discounts.append(discounts_item)

        enterprise = d.pop("enterprise", UNSET)

        eula_id = d.pop("eulaId", UNSET)

        eula_required = d.pop("eulaRequired", UNSET)

        eval_center = d.pop("evalCenter", UNSET)

        forum_id = d.pop("forumId", UNSET)

        intended_use = d.pop("intendedUse", UNSET)

        _last_trial_info = d.pop("lastTrialInfo", UNSET)
        last_trial_info: BTTrialInfo | Unset
        if isinstance(_last_trial_info, Unset):
            last_trial_info = UNSET
        else:
            last_trial_info = BTTrialInfo.from_dict(_last_trial_info)

        _need_to_reset_client_cache_time = d.pop("needToResetClientCacheTime", UNSET)
        need_to_reset_client_cache_time: datetime.datetime | Unset
        if isinstance(_need_to_reset_client_cache_time, Unset):
            need_to_reset_client_cache_time = UNSET
        else:
            need_to_reset_client_cache_time = isoparse(_need_to_reset_client_cache_time)

        need_to_show_new_walkthrough = d.pop("needToShowNewWalkthrough", UNSET)

        _own_purchase = d.pop("ownPurchase", UNSET)
        own_purchase: BTPurchaseInfo | Unset
        if isinstance(_own_purchase, Unset):
            own_purchase = UNSET
        else:
            own_purchase = BTPurchaseInfo.from_dict(_own_purchase)

        phone_number = d.pop("phoneNumber", UNSET)

        pro_discovery_trial_rejected = d.pop("proDiscoveryTrialRejected", UNSET)

        product_type = cast(list[str], d.pop("productType", UNSET))

        redirect_url = d.pop("redirectUrl", UNSET)

        role = d.pop("role", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: list[BTRole] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = BTRole(roles_item_data)

                roles.append(roles_item)

        rum_enabled = d.pop("rumEnabled", UNSET)

        show_renew_student_pages = d.pop("showRenewStudentPages", UNSET)

        startup_page = d.pop("startupPage", UNSET)

        system_user = d.pop("systemUser", UNSET)

        totp_enabled = d.pop("totpEnabled", UNSET)

        tracing_enabled = d.pop("tracingEnabled", UNSET)

        _trial_infos = d.pop("trialInfos", UNSET)
        trial_infos: list[BTTrialInfo] | Unset = UNSET
        if _trial_infos is not UNSET:
            trial_infos = []
            for trial_infos_item_data in _trial_infos:
                trial_infos_item = BTTrialInfo.from_dict(trial_infos_item_data)

                trial_infos.append(trial_infos_item)

        _discount = d.pop("discount", UNSET)
        discount: BTDiscount | Unset
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = BTDiscount.from_dict(_discount)

        invitation_id = d.pop("invitationId", UNSET)

        invited_by_email = d.pop("invitedByEmail", UNSET)

        invited_document_id = d.pop("invitedDocumentId", UNSET)

        is_trial_request = d.pop("isTrialRequest", UNSET)

        _privacy_consents = d.pop("privacyConsents", UNSET)
        privacy_consents: list[BTPrivacyConsentInfo] | Unset = UNSET
        if _privacy_consents is not UNSET:
            privacy_consents = []
            for privacy_consents_item_data in _privacy_consents:
                privacy_consents_item = BTPrivacyConsentInfo.from_dict(privacy_consents_item_data)

                privacy_consents.append(privacy_consents_item)

        _user_metrics = d.pop("userMetrics", UNSET)
        user_metrics: BTUserMetricsInfo | Unset
        if isinstance(_user_metrics, Unset):
            user_metrics = UNSET
        else:
            user_metrics = BTUserMetricsInfo.from_dict(_user_metrics)

        bt_user_admin_info = cls(
            json_type=json_type,
            href=href,
            id=id,
            name=name,
            view_ref=view_ref,
            image=image,
            is_onshape_support=is_onshape_support,
            state=state,
            documentation_name=documentation_name,
            email=email,
            first_name=first_name,
            last_name=last_name,
            company=company,
            documentation_name_override=documentation_name_override,
            global_permissions=global_permissions,
            invitation_state=invitation_state,
            is_external=is_external,
            is_guest=is_guest,
            is_light=is_light,
            last_login_time=last_login_time,
            personal_message_allowed=personal_message_allowed,
            source=source,
            active_plan=active_plan,
            active_plan_id=active_plan_id,
            active_purchases=active_purchases,
            active_trial_info=active_trial_info,
            b_2_c_id=b_2_c_id,
            billing_update_required=billing_update_required,
            cad_system_at_signup=cad_system_at_signup,
            country_code=country_code,
            created_at=created_at,
            credential=credential,
            default_company_name=default_company_name,
            description=description,
            device_info=device_info,
            discounts=discounts,
            enterprise=enterprise,
            eula_id=eula_id,
            eula_required=eula_required,
            eval_center=eval_center,
            forum_id=forum_id,
            intended_use=intended_use,
            last_trial_info=last_trial_info,
            need_to_reset_client_cache_time=need_to_reset_client_cache_time,
            need_to_show_new_walkthrough=need_to_show_new_walkthrough,
            own_purchase=own_purchase,
            phone_number=phone_number,
            pro_discovery_trial_rejected=pro_discovery_trial_rejected,
            product_type=product_type,
            redirect_url=redirect_url,
            role=role,
            roles=roles,
            rum_enabled=rum_enabled,
            show_renew_student_pages=show_renew_student_pages,
            startup_page=startup_page,
            system_user=system_user,
            totp_enabled=totp_enabled,
            tracing_enabled=tracing_enabled,
            trial_infos=trial_infos,
            discount=discount,
            invitation_id=invitation_id,
            invited_by_email=invited_by_email,
            invited_document_id=invited_document_id,
            is_trial_request=is_trial_request,
            privacy_consents=privacy_consents,
            user_metrics=user_metrics,
        )

        bt_user_admin_info.additional_properties = d
        return bt_user_admin_info

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
