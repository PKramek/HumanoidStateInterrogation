import logging
import os

import gym
from gym.envs.mujoco.humanoid import HumanoidEnv

# For information about Humanoid-v1 (the same state and action vectors as Humanoid-v2) go to:
# https://github.com/openai/gym/wiki/Humanoid-V1
from src.init_qpos_modifer import InitQposModifierFactory


class ParametrizableResetHumanoid(HumanoidEnv):
    def __init__(self):
        super().__init__()

        qpos_modifier = InitQposModifierFactory.get_default()
        logging.info(f"Modifying Humanoid init_qpot using {qpos_modifier}")
        self.init_qpos = qpos_modifier.modify_init_qpos(self.init_qpos)


if __name__ == '__main__':
    new_env_name = 'ParametrizableResetHumanoid'

    gym.envs.register(
        id=new_env_name,
        entry_point=ParametrizableResetHumanoid,
        max_episode_steps=1000,
    )
    logging.info(f"Registered new environment: {new_env_name}")

    name_of_InitQposModifier = "abdomen_z"

    os.environ["DEFAULT_InitQposModifier"] = name_of_InitQposModifier
    logging.info(f"Set env variable DEFAULT_InitQposModifier={name_of_InitQposModifier}")

    env = gym.make(new_env_name)
    observation = env.reset()
    for _ in range(1000):
        env.render()
        action = env.action_space.sample()  # your agent here (this takes random actions)
        observation, reward, done, info = env.step(action)

        if done:
            observation = env.reset()
    env.close()
