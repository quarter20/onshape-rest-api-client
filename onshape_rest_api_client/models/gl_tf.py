from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accessor import Accessor
    from ..models.animation import Animation
    from ..models.asset import Asset
    from ..models.buffer import Buffer
    from ..models.buffer_view import BufferView
    from ..models.camera import Camera
    from ..models.gl_tf_extensions import GlTFExtensions
    from ..models.gl_tf_extras import GlTFExtras
    from ..models.image import Image
    from ..models.material import Material
    from ..models.mesh import Mesh
    from ..models.node import Node
    from ..models.sampler import Sampler
    from ..models.scene import Scene
    from ..models.skin import Skin
    from ..models.texture import Texture


T = TypeVar("T", bound="GlTF")


@_attrs_define
class GlTF:
    """
    Attributes:
        accessors (list[Accessor] | Unset):
        animations (list[Animation] | Unset):
        asset (Asset | Unset):
        buffer_views (list[BufferView] | Unset):
        buffers (list[Buffer] | Unset):
        cameras (list[Camera] | Unset):
        extensions (GlTFExtensions | Unset):
        extensions_required (list[str] | Unset):
        extensions_used (list[str] | Unset):
        extras (GlTFExtras | Unset):
        images (list[Image] | Unset):
        materials (list[Material] | Unset):
        meshes (list[Mesh] | Unset):
        nodes (list[Node] | Unset):
        samplers (list[Sampler] | Unset):
        scene (int | Unset):
        scenes (list[Scene] | Unset):
        skins (list[Skin] | Unset):
        textures (list[Texture] | Unset):
    """

    accessors: list[Accessor] | Unset = UNSET
    animations: list[Animation] | Unset = UNSET
    asset: Asset | Unset = UNSET
    buffer_views: list[BufferView] | Unset = UNSET
    buffers: list[Buffer] | Unset = UNSET
    cameras: list[Camera] | Unset = UNSET
    extensions: GlTFExtensions | Unset = UNSET
    extensions_required: list[str] | Unset = UNSET
    extensions_used: list[str] | Unset = UNSET
    extras: GlTFExtras | Unset = UNSET
    images: list[Image] | Unset = UNSET
    materials: list[Material] | Unset = UNSET
    meshes: list[Mesh] | Unset = UNSET
    nodes: list[Node] | Unset = UNSET
    samplers: list[Sampler] | Unset = UNSET
    scene: int | Unset = UNSET
    scenes: list[Scene] | Unset = UNSET
    skins: list[Skin] | Unset = UNSET
    textures: list[Texture] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accessors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accessors, Unset):
            accessors = []
            for accessors_item_data in self.accessors:
                accessors_item = accessors_item_data.to_dict()
                accessors.append(accessors_item)

        animations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.animations, Unset):
            animations = []
            for animations_item_data in self.animations:
                animations_item = animations_item_data.to_dict()
                animations.append(animations_item)

        asset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset, Unset):
            asset = self.asset.to_dict()

        buffer_views: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buffer_views, Unset):
            buffer_views = []
            for buffer_views_item_data in self.buffer_views:
                buffer_views_item = buffer_views_item_data.to_dict()
                buffer_views.append(buffer_views_item)

        buffers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buffers, Unset):
            buffers = []
            for buffers_item_data in self.buffers:
                buffers_item = buffers_item_data.to_dict()
                buffers.append(buffers_item)

        cameras: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cameras, Unset):
            cameras = []
            for cameras_item_data in self.cameras:
                cameras_item = cameras_item_data.to_dict()
                cameras.append(cameras_item)

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extensions_required: list[str] | Unset = UNSET
        if not isinstance(self.extensions_required, Unset):
            extensions_required = self.extensions_required

        extensions_used: list[str] | Unset = UNSET
        if not isinstance(self.extensions_used, Unset):
            extensions_used = self.extensions_used

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        materials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.materials, Unset):
            materials = []
            for materials_item_data in self.materials:
                materials_item = materials_item_data.to_dict()
                materials.append(materials_item)

        meshes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.meshes, Unset):
            meshes = []
            for meshes_item_data in self.meshes:
                meshes_item = meshes_item_data.to_dict()
                meshes.append(meshes_item)

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        samplers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.samplers, Unset):
            samplers = []
            for samplers_item_data in self.samplers:
                samplers_item = samplers_item_data.to_dict()
                samplers.append(samplers_item)

        scene = self.scene

        scenes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scenes, Unset):
            scenes = []
            for scenes_item_data in self.scenes:
                scenes_item = scenes_item_data.to_dict()
                scenes.append(scenes_item)

        skins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skins, Unset):
            skins = []
            for skins_item_data in self.skins:
                skins_item = skins_item_data.to_dict()
                skins.append(skins_item)

        textures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.textures, Unset):
            textures = []
            for textures_item_data in self.textures:
                textures_item = textures_item_data.to_dict()
                textures.append(textures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accessors is not UNSET:
            field_dict["accessors"] = accessors
        if animations is not UNSET:
            field_dict["animations"] = animations
        if asset is not UNSET:
            field_dict["asset"] = asset
        if buffer_views is not UNSET:
            field_dict["bufferViews"] = buffer_views
        if buffers is not UNSET:
            field_dict["buffers"] = buffers
        if cameras is not UNSET:
            field_dict["cameras"] = cameras
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extensions_required is not UNSET:
            field_dict["extensionsRequired"] = extensions_required
        if extensions_used is not UNSET:
            field_dict["extensionsUsed"] = extensions_used
        if extras is not UNSET:
            field_dict["extras"] = extras
        if images is not UNSET:
            field_dict["images"] = images
        if materials is not UNSET:
            field_dict["materials"] = materials
        if meshes is not UNSET:
            field_dict["meshes"] = meshes
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if samplers is not UNSET:
            field_dict["samplers"] = samplers
        if scene is not UNSET:
            field_dict["scene"] = scene
        if scenes is not UNSET:
            field_dict["scenes"] = scenes
        if skins is not UNSET:
            field_dict["skins"] = skins
        if textures is not UNSET:
            field_dict["textures"] = textures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accessor import Accessor
        from ..models.animation import Animation
        from ..models.asset import Asset
        from ..models.buffer import Buffer
        from ..models.buffer_view import BufferView
        from ..models.camera import Camera
        from ..models.gl_tf_extensions import GlTFExtensions
        from ..models.gl_tf_extras import GlTFExtras
        from ..models.image import Image
        from ..models.material import Material
        from ..models.mesh import Mesh
        from ..models.node import Node
        from ..models.sampler import Sampler
        from ..models.scene import Scene
        from ..models.skin import Skin
        from ..models.texture import Texture

        d = dict(src_dict)
        _accessors = d.pop("accessors", UNSET)
        accessors: list[Accessor] | Unset = UNSET
        if _accessors is not UNSET:
            accessors = []
            for accessors_item_data in _accessors:
                accessors_item = Accessor.from_dict(accessors_item_data)

                accessors.append(accessors_item)

        _animations = d.pop("animations", UNSET)
        animations: list[Animation] | Unset = UNSET
        if _animations is not UNSET:
            animations = []
            for animations_item_data in _animations:
                animations_item = Animation.from_dict(animations_item_data)

                animations.append(animations_item)

        _asset = d.pop("asset", UNSET)
        asset: Asset | Unset
        if isinstance(_asset, Unset):
            asset = UNSET
        else:
            asset = Asset.from_dict(_asset)

        _buffer_views = d.pop("bufferViews", UNSET)
        buffer_views: list[BufferView] | Unset = UNSET
        if _buffer_views is not UNSET:
            buffer_views = []
            for buffer_views_item_data in _buffer_views:
                buffer_views_item = BufferView.from_dict(buffer_views_item_data)

                buffer_views.append(buffer_views_item)

        _buffers = d.pop("buffers", UNSET)
        buffers: list[Buffer] | Unset = UNSET
        if _buffers is not UNSET:
            buffers = []
            for buffers_item_data in _buffers:
                buffers_item = Buffer.from_dict(buffers_item_data)

                buffers.append(buffers_item)

        _cameras = d.pop("cameras", UNSET)
        cameras: list[Camera] | Unset = UNSET
        if _cameras is not UNSET:
            cameras = []
            for cameras_item_data in _cameras:
                cameras_item = Camera.from_dict(cameras_item_data)

                cameras.append(cameras_item)

        _extensions = d.pop("extensions", UNSET)
        extensions: GlTFExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = GlTFExtensions.from_dict(_extensions)

        extensions_required = cast(list[str], d.pop("extensionsRequired", UNSET))

        extensions_used = cast(list[str], d.pop("extensionsUsed", UNSET))

        _extras = d.pop("extras", UNSET)
        extras: GlTFExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = GlTFExtras.from_dict(_extras)

        _images = d.pop("images", UNSET)
        images: list[Image] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = Image.from_dict(images_item_data)

                images.append(images_item)

        _materials = d.pop("materials", UNSET)
        materials: list[Material] | Unset = UNSET
        if _materials is not UNSET:
            materials = []
            for materials_item_data in _materials:
                materials_item = Material.from_dict(materials_item_data)

                materials.append(materials_item)

        _meshes = d.pop("meshes", UNSET)
        meshes: list[Mesh] | Unset = UNSET
        if _meshes is not UNSET:
            meshes = []
            for meshes_item_data in _meshes:
                meshes_item = Mesh.from_dict(meshes_item_data)

                meshes.append(meshes_item)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[Node] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = Node.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        _samplers = d.pop("samplers", UNSET)
        samplers: list[Sampler] | Unset = UNSET
        if _samplers is not UNSET:
            samplers = []
            for samplers_item_data in _samplers:
                samplers_item = Sampler.from_dict(samplers_item_data)

                samplers.append(samplers_item)

        scene = d.pop("scene", UNSET)

        _scenes = d.pop("scenes", UNSET)
        scenes: list[Scene] | Unset = UNSET
        if _scenes is not UNSET:
            scenes = []
            for scenes_item_data in _scenes:
                scenes_item = Scene.from_dict(scenes_item_data)

                scenes.append(scenes_item)

        _skins = d.pop("skins", UNSET)
        skins: list[Skin] | Unset = UNSET
        if _skins is not UNSET:
            skins = []
            for skins_item_data in _skins:
                skins_item = Skin.from_dict(skins_item_data)

                skins.append(skins_item)

        _textures = d.pop("textures", UNSET)
        textures: list[Texture] | Unset = UNSET
        if _textures is not UNSET:
            textures = []
            for textures_item_data in _textures:
                textures_item = Texture.from_dict(textures_item_data)

                textures.append(textures_item)

        gl_tf = cls(
            accessors=accessors,
            animations=animations,
            asset=asset,
            buffer_views=buffer_views,
            buffers=buffers,
            cameras=cameras,
            extensions=extensions,
            extensions_required=extensions_required,
            extensions_used=extensions_used,
            extras=extras,
            images=images,
            materials=materials,
            meshes=meshes,
            nodes=nodes,
            samplers=samplers,
            scene=scene,
            scenes=scenes,
            skins=skins,
            textures=textures,
        )

        gl_tf.additional_properties = d
        return gl_tf

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
