<h1 align="center"> RlControl </h1>
<h3 align="center">  Designing Controllers via Deep Reinforcement Learning </h3>

</br>

<p align="center">
  <img src="files/project_icon.png" alt="Sample signal" width="10%" height="10%">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify">
    - The project aims to control linear/nonlinear dynamical systems
    in model-free and model-based setting
    with SOTA deep reinforcement learning algorithms
</p>


<!-- PREREQUISITES -->
<h2 id="prerequisites"> :fork_and_knife: Prerequisites</h2>
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) <br>

<!--This project is written in Python programming language. <br>-->
The following open source packages are used in this project:
* streamlit
* torch
* ray
* rllib
* control
* gymnasium
* tensorboardx
* tqdm
* numpy
* matplotlib
* plotly
* pandas
* pickle5

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)



<!-- FOLDER STRUCTURE -->
<h2 id="folder-structure"> :cactus: Folder Structure</h2>
--- Folder Structure ---
.gitignore
.pre-commit-config.yaml
[.streamlit]
    └── secrets.toml
[.vscode]
    └── launch.json
app.py
clean_req.py
Dockerfile
[files]
    ├── environment.yml
    ├── logic.drawio
    ├── pid_page.jpg
    ├── project_icon.png
    ├── test_page.jpg
    └── training_page.jpg
[gym_control]
    ├── [envs]
        ├── env_control.py
        ├── __init__.py
        └── [__pycache__]
            ├── env_control.cpython-38.pyc
            └── __init__.cpython-38.pyc
    ├── __init__.py
    └── [__pycache__]
        └── __init__.cpython-38.pyc
[gym_control.egg-info]
    ├── dependency_links.txt
    ├── PKG-INFO
    ├── requires.txt
    ├── SOURCES.txt
    └── top_level.txt
LICENSE
[pages_app]
    ├── common.py
    ├── page_pid.py
    ├── page_testing.py
    ├── page_training.py
    ├── plot_functions.py
README.md
requirements.txt
[rlc]
    ├── [agents]
        ├── base.py
        ├── ddpg.py
    ├── classical_control_mini_lecture.ipynb
    ├── configs.py
    ├── [control]
        ├── pid.py
    ├── [imgs]
        ├── feedback_block.png
        ├── Introduction_ControlPID_eq.png
        ├── mass_spring_damper.png
        ├── mass_spring_damper_eq.png
        ├── mass_spring_damper_eq_laplace.png
        └── msd_tf.png
    ├── [logger]
        ├── logger.py
        ├── __init__.py
    ├── rlcontrol.py
    ├── rllib.py
    ├── rllib_control.ipynb
    ├── rllib_inference.py
    ├── [utils]
        ├── plot.py
        ├── utils_path.py
[Runs]
    ├── [DDPG_2023_7_17_15_56_45]
        ├── [checkpoints]
            ├── agent_1.pth
            ├── agent_10.pth
            ├── agent_11.pth
            ├── agent_12.pth
            ├── agent_13.pth
            ├── agent_14.pth
            ├── agent_2.pth
            ├── agent_3.pth
            ├── agent_4.pth
            ├── agent_5.pth
            ├── agent_6.pth
            ├── agent_7.pth
            ├── agent_8.pth
            ├── agent_9.pth
            └── agent_best.pth
        └── experiment_config.pickle
setup.py

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- INSTALL HOW TO -->
<h2 id="install"> Installation Steps</h2>

<p align="justify">
  Follow steps below,
<!-- - `conda env export > environment.yml --no-builds`
- `conda list -e > requirements.txt` -->
    1. Create Conda environment:
        - 'conda env create --name rlcontrol --file=environment.yml'
    2. Install OpenAI Gym Environment
        - Install gym_control environment: `pip install -e .`

<h2 id="Run"> Run App</h2>
`streamlit run app.py`

## Build for Docker
- `docker build -t streamlit .`

## TODO-List
    - Add class diagram of project
    - Train environemnt with rllib
    - Track experiments from db (postgresql)
    - Fix seeds
