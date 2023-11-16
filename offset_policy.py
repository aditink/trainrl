"""A policy that just sets motion authorities to be positions occupied by the train + a buffer."""

import math
from typing import Dict, Optional, Tuple, Union
from stable_baselines3.common.policies import MultiInputActorCriticPolicy

import numpy as np

class OffsetPolicy(MultiInputActorCriticPolicy):

    def predict(
        self,
        observation: Union[np.ndarray, Dict[str, np.ndarray]],
        state: Optional[Tuple[np.ndarray, ...]] = None,
        episode_start: Optional[np.ndarray] = None,
        deterministic: bool = False,
    ) -> Tuple[np.ndarray, Optional[Tuple[np.ndarray, ...]]]:
        """
        Get the policy action from an observation (and optional hidden state).
        Includes sugar-coating to handle different observations (e.g. normalizing images).

        :param observation: the input observation
        :param state: The last hidden states (can be None, used in recurrent policies)
        :param episode_start: The last masks (can be None, used in recurrent policies)
            this correspond to beginning of episodes,
            where the hidden states of the RNN must be reset.
        :param deterministic: Whether or not to return deterministic actions.
        :return: the model's action and the next hidden state
            (used in recurrent policies)
        """
        # Switch to eval mode (this affects batch norm / dropout)
        # self.set_training_mode(False)

        block_size = 8

        def get_block_before(pixel):
            return int(pixel//block_size)
    
        def get_block_after(pixel):
            return int(math.ceil(pixel/block_size))

        # Check for common mistake that the user does not mix Gym/VecEnv API
        # Tuple obs are not supported by SB3, so we can safely do that check
        if isinstance(observation, tuple) and len(observation) == 2 and isinstance(observation[1], dict):
            raise ValueError(
                "You have passed a tuple to the predict() function instead of a Numpy array or a Dict. "
                "You are probably mixing Gym API with SB3 VecEnv API: `obs, info = env.reset()` (Gym) "
                "vs `obs = vec_env.reset()` (SB3 VecEnv). "
                "See related issue https://github.com/DLR-RM/stable-baselines3/issues/1694 "
                "and documentation for more information: https://stable-baselines3.readthedocs.io/en/master/guide/vec_envs.html#vecenv-api-vs-gym-api"
            )

        # We want to return action with shape
        # action_space = spaces.MultiDiscrete([self.track1_length_b]*4).
        # train1 position and velocity are in obe["train1"] which has shape
        # spaces.Box(low=0, high=self.window_size_p, shape=(2,), dtype=np.float64).
        # Likewise for train2.
        # Hack to compensate for jsrl evaluation bug.
        if (observation == None):
            train1 = self["train1"][0]
            train2 = self["train2"][0]
        else:
            train1 = observation["train1"]
            train2 = observation["train2"]
        
        # Conversion from pixels to block comes from common.py.
        train1_position = get_block_after(train1[0])
        train2_position = get_block_before(train2[0])
        back_buffer = 4
        front_buffer = 6

        actions = np.zeros(4, dtype=np.int32)
        actions[0] = train1_position - back_buffer
        actions[1] = train1_position + front_buffer
        actions[2] = train2_position - front_buffer
        actions[3] = train2_position + back_buffer

        return actions, state