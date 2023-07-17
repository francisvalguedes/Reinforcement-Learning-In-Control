import numpy as np


class Agent(object):
    def __init__(self, observation_space, action_space):
        self.batch_size = 64
        self.algorithm_name = ""
        self.integral_error = False
        self.best_reward = -np.inf

    def apply(self, state_dict: dict, step: int):
        """Calculate control signal by two options: output/state feedback

        Parameters
        ----------
        state_dict : dict
            {
                'state':np.ndarray,
                'state_reference':np.ndarray
            }
        step : int
            Iteration of ongoing epoch
        is_output_feedback : bool, optional
            _description_, by default True

        Returns
        -------
        _type_
            _description_
        """
        action = None
        return action

    def load(self, agent_weight_abs):
        """Load trained agent weights"""
        pass

    def save(self, agent_weight_abs):
        """Save trained agent weights"""
        pass

    def get_batch_size(self):
        return self.batch_size

    def update_agent(self):
        pass

    def update_memory(self, state, action, reward, next_state, done):
        pass

    def reset(self):
        pass

    def get_default_params(self):
        return {}
