# sepsis-mdp

Python version: 3.9.6

This repository contains the MDP for sepsis treatment based on the paper `Counterfactual Off-Policy Evaluation with Gumbel-Max Structural Causal Models` ([arXiv](https://arxiv.org/abs/1905.05824)) by Michael Oberst and David Sontag. The data is taken from their [GitHub repo](https://github.com/clinicalml/gumbel-max-scm.git).

The dependencies are listed in `requirements.txt`. They can be installed using `pip install -r requirements.txt`.

The MDP is implemented using [Gymnasium](https://gymnasium.farama.org/). The source code is in
the script `mdps/envs/gumbel_max_diabetes.py`.

The maximum number of steps per episode can be changed in `mdps/__init__.py`. The current value is 30.

The `main.py` script is a simple demonstration of how to use the MDP. It runs one episode and prints the reward and the state at each step using a deterministic policy.