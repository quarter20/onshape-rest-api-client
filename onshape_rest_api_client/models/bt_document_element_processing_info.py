from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_element_type import GBTElementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_application_target_info import BTApplicationTargetInfo
    from ..models.bt_thumbnail_info import BTThumbnailInfo
    from ..models.bt_zip_file_info import BTZipFileInfo


T = TypeVar("T", bound="BTDocumentElementProcessingInfo")


@_attrs_define
class BTDocumentElementProcessingInfo:
    """
    Attributes:
        acceleration_units (str | Unset):
        angle_units (str | Unset):
        angular_velocity_units (str | Unset):
        application_target (BTApplicationTargetInfo | Unset):
        area_units (str | Unset):
        data_type (str | Unset):
        deleted (bool | Unset):
        density_units (str | Unset):
        element_type (GBTElementType | Unset):
        energy_units (str | Unset):
        filename (str | Unset):
        force_units (str | Unset):
        foreign_data_id (str | Unset):
        id (str | Unset):
        length_units (str | Unset):
        mass_units (str | Unset):
        microversion_id (str | Unset):
        moment_units (str | Unset):
        name (str | Unset):
        pressure_units (str | Unset):
        pretty_type (str | Unset):
        safe_to_show (bool | Unset):
        specified_unit (str | Unset):
        thumbnail_info (BTThumbnailInfo | Unset):
        thumbnails (str | Unset):
        time_units (str | Unset):
        translation_event_key (str | Unset):
        translation_id (str | Unset):
        type_ (str | Unset):
        unupdatable (bool | Unset):
        volume_units (str | Unset):
        zip_ (BTZipFileInfo | Unset):
    """

    acceleration_units: str | Unset = UNSET
    angle_units: str | Unset = UNSET
    angular_velocity_units: str | Unset = UNSET
    application_target: BTApplicationTargetInfo | Unset = UNSET
    area_units: str | Unset = UNSET
    data_type: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    density_units: str | Unset = UNSET
    element_type: GBTElementType | Unset = UNSET
    energy_units: str | Unset = UNSET
    filename: str | Unset = UNSET
    force_units: str | Unset = UNSET
    foreign_data_id: str | Unset = UNSET
    id: str | Unset = UNSET
    length_units: str | Unset = UNSET
    mass_units: str | Unset = UNSET
    microversion_id: str | Unset = UNSET
    moment_units: str | Unset = UNSET
    name: str | Unset = UNSET
    pressure_units: str | Unset = UNSET
    pretty_type: str | Unset = UNSET
    safe_to_show: bool | Unset = UNSET
    specified_unit: str | Unset = UNSET
    thumbnail_info: BTThumbnailInfo | Unset = UNSET
    thumbnails: str | Unset = UNSET
    time_units: str | Unset = UNSET
    translation_event_key: str | Unset = UNSET
    translation_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    unupdatable: bool | Unset = UNSET
    volume_units: str | Unset = UNSET
    zip_: BTZipFileInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acceleration_units = self.acceleration_units

        angle_units = self.angle_units

        angular_velocity_units = self.angular_velocity_units

        application_target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_target, Unset):
            application_target = self.application_target.to_dict()

        area_units = self.area_units

        data_type = self.data_type

        deleted = self.deleted

        density_units = self.density_units

        element_type: str | Unset = UNSET
        if not isinstance(self.element_type, Unset):
            element_type = self.element_type.value

        energy_units = self.energy_units

        filename = self.filename

        force_units = self.force_units

        foreign_data_id = self.foreign_data_id

        id = self.id

        length_units = self.length_units

        mass_units = self.mass_units

        microversion_id = self.microversion_id

        moment_units = self.moment_units

        name = self.name

        pressure_units = self.pressure_units

        pretty_type = self.pretty_type

        safe_to_show = self.safe_to_show

        specified_unit = self.specified_unit

        thumbnail_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail_info, Unset):
            thumbnail_info = self.thumbnail_info.to_dict()

        thumbnails = self.thumbnails

        time_units = self.time_units

        translation_event_key = self.translation_event_key

        translation_id = self.translation_id

        type_ = self.type_

        unupdatable = self.unupdatable

        volume_units = self.volume_units

        zip_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.zip_, Unset):
            zip_ = self.zip_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acceleration_units is not UNSET:
            field_dict["accelerationUnits"] = acceleration_units
        if angle_units is not UNSET:
            field_dict["angleUnits"] = angle_units
        if angular_velocity_units is not UNSET:
            field_dict["angularVelocityUnits"] = angular_velocity_units
        if application_target is not UNSET:
            field_dict["applicationTarget"] = application_target
        if area_units is not UNSET:
            field_dict["areaUnits"] = area_units
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if density_units is not UNSET:
            field_dict["densityUnits"] = density_units
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if energy_units is not UNSET:
            field_dict["energyUnits"] = energy_units
        if filename is not UNSET:
            field_dict["filename"] = filename
        if force_units is not UNSET:
            field_dict["forceUnits"] = force_units
        if foreign_data_id is not UNSET:
            field_dict["foreignDataId"] = foreign_data_id
        if id is not UNSET:
            field_dict["id"] = id
        if length_units is not UNSET:
            field_dict["lengthUnits"] = length_units
        if mass_units is not UNSET:
            field_dict["massUnits"] = mass_units
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if moment_units is not UNSET:
            field_dict["momentUnits"] = moment_units
        if name is not UNSET:
            field_dict["name"] = name
        if pressure_units is not UNSET:
            field_dict["pressureUnits"] = pressure_units
        if pretty_type is not UNSET:
            field_dict["prettyType"] = pretty_type
        if safe_to_show is not UNSET:
            field_dict["safeToShow"] = safe_to_show
        if specified_unit is not UNSET:
            field_dict["specifiedUnit"] = specified_unit
        if thumbnail_info is not UNSET:
            field_dict["thumbnailInfo"] = thumbnail_info
        if thumbnails is not UNSET:
            field_dict["thumbnails"] = thumbnails
        if time_units is not UNSET:
            field_dict["timeUnits"] = time_units
        if translation_event_key is not UNSET:
            field_dict["translationEventKey"] = translation_event_key
        if translation_id is not UNSET:
            field_dict["translationId"] = translation_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unupdatable is not UNSET:
            field_dict["unupdatable"] = unupdatable
        if volume_units is not UNSET:
            field_dict["volumeUnits"] = volume_units
        if zip_ is not UNSET:
            field_dict["zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_application_target_info import BTApplicationTargetInfo
        from ..models.bt_thumbnail_info import BTThumbnailInfo
        from ..models.bt_zip_file_info import BTZipFileInfo

        d = dict(src_dict)
        acceleration_units = d.pop("accelerationUnits", UNSET)

        angle_units = d.pop("angleUnits", UNSET)

        angular_velocity_units = d.pop("angularVelocityUnits", UNSET)

        _application_target = d.pop("applicationTarget", UNSET)
        application_target: BTApplicationTargetInfo | Unset
        if isinstance(_application_target, Unset):
            application_target = UNSET
        else:
            application_target = BTApplicationTargetInfo.from_dict(_application_target)

        area_units = d.pop("areaUnits", UNSET)

        data_type = d.pop("dataType", UNSET)

        deleted = d.pop("deleted", UNSET)

        density_units = d.pop("densityUnits", UNSET)

        _element_type = d.pop("elementType", UNSET)
        element_type: GBTElementType | Unset
        if isinstance(_element_type, Unset):
            element_type = UNSET
        else:
            element_type = GBTElementType(_element_type)

        energy_units = d.pop("energyUnits", UNSET)

        filename = d.pop("filename", UNSET)

        force_units = d.pop("forceUnits", UNSET)

        foreign_data_id = d.pop("foreignDataId", UNSET)

        id = d.pop("id", UNSET)

        length_units = d.pop("lengthUnits", UNSET)

        mass_units = d.pop("massUnits", UNSET)

        microversion_id = d.pop("microversionId", UNSET)

        moment_units = d.pop("momentUnits", UNSET)

        name = d.pop("name", UNSET)

        pressure_units = d.pop("pressureUnits", UNSET)

        pretty_type = d.pop("prettyType", UNSET)

        safe_to_show = d.pop("safeToShow", UNSET)

        specified_unit = d.pop("specifiedUnit", UNSET)

        _thumbnail_info = d.pop("thumbnailInfo", UNSET)
        thumbnail_info: BTThumbnailInfo | Unset
        if isinstance(_thumbnail_info, Unset):
            thumbnail_info = UNSET
        else:
            thumbnail_info = BTThumbnailInfo.from_dict(_thumbnail_info)

        thumbnails = d.pop("thumbnails", UNSET)

        time_units = d.pop("timeUnits", UNSET)

        translation_event_key = d.pop("translationEventKey", UNSET)

        translation_id = d.pop("translationId", UNSET)

        type_ = d.pop("type", UNSET)

        unupdatable = d.pop("unupdatable", UNSET)

        volume_units = d.pop("volumeUnits", UNSET)

        _zip_ = d.pop("zip", UNSET)
        zip_: BTZipFileInfo | Unset
        if isinstance(_zip_, Unset):
            zip_ = UNSET
        else:
            zip_ = BTZipFileInfo.from_dict(_zip_)

        bt_document_element_processing_info = cls(
            acceleration_units=acceleration_units,
            angle_units=angle_units,
            angular_velocity_units=angular_velocity_units,
            application_target=application_target,
            area_units=area_units,
            data_type=data_type,
            deleted=deleted,
            density_units=density_units,
            element_type=element_type,
            energy_units=energy_units,
            filename=filename,
            force_units=force_units,
            foreign_data_id=foreign_data_id,
            id=id,
            length_units=length_units,
            mass_units=mass_units,
            microversion_id=microversion_id,
            moment_units=moment_units,
            name=name,
            pressure_units=pressure_units,
            pretty_type=pretty_type,
            safe_to_show=safe_to_show,
            specified_unit=specified_unit,
            thumbnail_info=thumbnail_info,
            thumbnails=thumbnails,
            time_units=time_units,
            translation_event_key=translation_event_key,
            translation_id=translation_id,
            type_=type_,
            unupdatable=unupdatable,
            volume_units=volume_units,
            zip_=zip_,
        )

        bt_document_element_processing_info.additional_properties = d
        return bt_document_element_processing_info

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
