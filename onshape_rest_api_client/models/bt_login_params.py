from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_web_client_capabilities_params import BTWebClientCapabilitiesParams
    from ..models.bt_web_renderer_performance_measurement_params import BTWebRendererPerformanceMeasurementParams


T = TypeVar("T", bound="BTLoginParams")


@_attrs_define
class BTLoginParams:
    """
    Attributes:
        device_id (str | Unset):
        email (str | Unset):
        enable_totp (bool | Unset):
        is_recaptcha_v3 (bool | Unset):
        password (str | Unset):
        random_token (str | Unset):
        recaptcha_token (str | Unset):
        remember_totp (bool | Unset):
        renderer_performance_measurement (BTWebRendererPerformanceMeasurementParams | Unset):
        totp (str | Unset):
        web_client_capabilities (BTWebClientCapabilitiesParams | Unset):
    """

    device_id: str | Unset = UNSET
    email: str | Unset = UNSET
    enable_totp: bool | Unset = UNSET
    is_recaptcha_v3: bool | Unset = UNSET
    password: str | Unset = UNSET
    random_token: str | Unset = UNSET
    recaptcha_token: str | Unset = UNSET
    remember_totp: bool | Unset = UNSET
    renderer_performance_measurement: BTWebRendererPerformanceMeasurementParams | Unset = UNSET
    totp: str | Unset = UNSET
    web_client_capabilities: BTWebClientCapabilitiesParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        email = self.email

        enable_totp = self.enable_totp

        is_recaptcha_v3 = self.is_recaptcha_v3

        password = self.password

        random_token = self.random_token

        recaptcha_token = self.recaptcha_token

        remember_totp = self.remember_totp

        renderer_performance_measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.renderer_performance_measurement, Unset):
            renderer_performance_measurement = self.renderer_performance_measurement.to_dict()

        totp = self.totp

        web_client_capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.web_client_capabilities, Unset):
            web_client_capabilities = self.web_client_capabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if email is not UNSET:
            field_dict["email"] = email
        if enable_totp is not UNSET:
            field_dict["enableTotp"] = enable_totp
        if is_recaptcha_v3 is not UNSET:
            field_dict["isRecaptchaV3"] = is_recaptcha_v3
        if password is not UNSET:
            field_dict["password"] = password
        if random_token is not UNSET:
            field_dict["randomToken"] = random_token
        if recaptcha_token is not UNSET:
            field_dict["recaptchaToken"] = recaptcha_token
        if remember_totp is not UNSET:
            field_dict["rememberTotp"] = remember_totp
        if renderer_performance_measurement is not UNSET:
            field_dict["rendererPerformanceMeasurement"] = renderer_performance_measurement
        if totp is not UNSET:
            field_dict["totp"] = totp
        if web_client_capabilities is not UNSET:
            field_dict["webClientCapabilities"] = web_client_capabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_web_client_capabilities_params import BTWebClientCapabilitiesParams
        from ..models.bt_web_renderer_performance_measurement_params import BTWebRendererPerformanceMeasurementParams

        d = dict(src_dict)
        device_id = d.pop("deviceId", UNSET)

        email = d.pop("email", UNSET)

        enable_totp = d.pop("enableTotp", UNSET)

        is_recaptcha_v3 = d.pop("isRecaptchaV3", UNSET)

        password = d.pop("password", UNSET)

        random_token = d.pop("randomToken", UNSET)

        recaptcha_token = d.pop("recaptchaToken", UNSET)

        remember_totp = d.pop("rememberTotp", UNSET)

        _renderer_performance_measurement = d.pop("rendererPerformanceMeasurement", UNSET)
        renderer_performance_measurement: BTWebRendererPerformanceMeasurementParams | Unset
        if isinstance(_renderer_performance_measurement, Unset):
            renderer_performance_measurement = UNSET
        else:
            renderer_performance_measurement = BTWebRendererPerformanceMeasurementParams.from_dict(
                _renderer_performance_measurement
            )

        totp = d.pop("totp", UNSET)

        _web_client_capabilities = d.pop("webClientCapabilities", UNSET)
        web_client_capabilities: BTWebClientCapabilitiesParams | Unset
        if isinstance(_web_client_capabilities, Unset):
            web_client_capabilities = UNSET
        else:
            web_client_capabilities = BTWebClientCapabilitiesParams.from_dict(_web_client_capabilities)

        bt_login_params = cls(
            device_id=device_id,
            email=email,
            enable_totp=enable_totp,
            is_recaptcha_v3=is_recaptcha_v3,
            password=password,
            random_token=random_token,
            recaptcha_token=recaptcha_token,
            remember_totp=remember_totp,
            renderer_performance_measurement=renderer_performance_measurement,
            totp=totp,
            web_client_capabilities=web_client_capabilities,
        )

        bt_login_params.additional_properties = d
        return bt_login_params

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
