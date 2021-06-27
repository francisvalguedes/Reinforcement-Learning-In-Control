# Reinforcement-Learning-in-Control-Applications


## About
Apply state-of-the-art RL algorithms to control linear/nonlinear dynamical systems


## Installing
Install the package locally by running : ```pip3 install -e .```

## Training
- Check ```Examples/ex_training.py``` script. There is only few things you need to train your own dynamical system,
    1. Implement your own dynamical system from rlcontrol/systems/base class
    2. Use the RL algorithm from rlcontrol/agents/algorithm_name
    3. Gave them as parameter to the Organizer class which would handle all training process and log training events.

- Watch training process from tensorboard file which is created by date and time inside Logs/ folder automatically. 
- You can always change training parameters by the getting them with```get_default_training_config()``` function
    and giving config as parameter to ```train()``` function.

## Inference 
Check ```Examples/ex_inference.py``` script. There is only few things you need to test your own Rl controller,
    1. Specify the dynamical system you trained your RL agent with to Organizer class and specify rl algorithm as before.
    2. Give absolute path of the trained agent.
    3. Run organizer.run() and see plots. 

## TODO
    - Implement various dynamical systems examples.
    - Specify range for dynamical system parameters while training