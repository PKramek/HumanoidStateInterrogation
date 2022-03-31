import os
from abc import abstractmethod, ABC


class InitQposModifier(ABC):
    @abstractmethod
    def modify_init_qpos(self, init_qpos):
        raise NotImplementedError()


class AbdomenZInitQposModifier(InitQposModifier):
    def modify_init_qpos(self, init_qpos):
        init_qpos[5] = 30  # default is 0

        return init_qpos


class AbdomenYInitQposModifier(InitQposModifier):
    def modify_init_qpos(self, init_qpos):
        init_qpos[6] = 30  # default is 0

        return init_qpos


class AbdomenXInitQposModifier(InitQposModifier):
    def modify_init_qpos(self, init_qpos):
        init_qpos[7] = 30  # default is 0

        return init_qpos


class InitQposModifierFactory:
    _class_mapping = {
        "abdomen_z": AbdomenZInitQposModifier,
        "abdomen_y": AbdomenYInitQposModifier,
        "abdomen_x": AbdomenXInitQposModifier,
    }

    @staticmethod
    def get(name: str) -> InitQposModifier:
        modifier_class = InitQposModifierFactory._class_mapping.get(name, None)
        if modifier_class is None:
            raise ValueError(
                f"Unknown InitQposModifier: {name}, available options are: {InitQposModifierFactory._class_mapping.keys()}")

        return modifier_class()

    @staticmethod
    def register(name: str, modified_class: InitQposModifier):
        assert issubclass(modified_class, InitQposModifier), "Newly added class must be a subclass of InitQposModifier"
        assert isinstance(name, str), "Name of new class must be a string"
        assert InitQposModifierFactory._class_mapping.get(name, None) is None, "Can't register class because name is already taken"

        InitQposModifierFactory._class_mapping[name] = modified_class

    @staticmethod
    def get_default() -> InitQposModifier:
        default = os.environ.get("DEFAULT_InitQposModifier")
        assert default is not None, "Environmental variable DEFAULT_InitQposModifier not set"

        if default not in InitQposModifierFactory._class_mapping.keys():
            raise ValueError(
                f"Unknown InitQposModifier: {default}, available options are: {InitQposModifierFactory._class_mapping.keys()}")

        return InitQposModifierFactory.get(default)
