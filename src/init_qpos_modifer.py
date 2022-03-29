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
    _CLASS_MAPPING = {
        "abdomen_z": AbdomenZInitQposModifier,
        "abdomen_y": AbdomenYInitQposModifier,
        "abdomen_x": AbdomenXInitQposModifier,
    }

    @staticmethod
    def get(name: str) -> InitQposModifier:
        modifier_class = InitQposModifierFactory._CLASS_MAPPING.get(name, None)
        if modifier_class is None:
            raise ValueError(
                f"Unknown InitQposModifier: {name}, available options are: {InitQposModifierFactory._CLASS_MAPPING.keys()}")

        return modifier_class()

    @staticmethod
    def get_default() -> InitQposModifier:
        default = os.environ.get("DEFAULT_InitQposModifier")
        if default not in InitQposModifierFactory._CLASS_MAPPING.keys():
            raise ValueError(
                f"Unknown InitQposModifier: {default}, available options are: {InitQposModifierFactory._CLASS_MAPPING.keys()}")

        return InitQposModifierFactory.get(default)
