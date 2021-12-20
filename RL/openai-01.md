# purpose

* There is no standard textbook for deep RL.
* The paper omits or inadvertently obscures key design drtails.
* The implmentations of an algorithm are hard to read.

# install

The installation needs Mojuco, which is a Physics Engine. The Mujoco is free for students and you can follow the readme of it to install. This is optional.

## mujoco 

follow the [readme](https://github.com/openai/mujoco-py) to install. When you meet the problems of missing path, follow the tips of `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/lm/.mujoco/mujoco210/bin` and `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia`. When you meet the problem of `FileNotFoundError: [Errno 2] No such file or directory: 'patchelf': 'patchelf'`, run `sudo apt-get install patchelf`

# algorithm

## On-policy

VPG(Vanilla policy gradient) is on-policy and it predates RL. Then there is TRPO and PPO. 

The on-policy's feature is that they don't use old data, which means they less sample efficency. But this is for a good reason: they directly optimize the objective: policy performance.

## Off-policy

VPG, DDPG, TD3, SAC

# key Concepts in RL

* be attention that observations and states are different.
* actions can be continuous or discrete which need different families of algorithm
* policy can be deterministic or stochastic
    * stochastic policies include diagonal Gaussian policies for continuous spaces and categorical policies for discrete spaces.
        * we have to do two things: sample and compute log likelyhoods
        * categorical sample: refer to the pytorch docs
        * categorical likelyhoods: it is just the indices
        * diagonal Gaussian sample: get the mean from nn, two ways to get the standard deviations
            * given the standard deviations
            * nn to get it
        * > note that the standard deviations are represented by log because it ranges from $-\infty$ to $+\infty$ and it is better to be calculated.
* Trajectory is a sequence of states and actions
   * > Trajectory are also called episodes or rollouts.
* reward is a function of $s_t,a_t,s_{t+1}$, but it is often be simplified by $s_t$ or $s_t, a_t$. return is the cumulative reward over a trajectory. $$R(\tau)=\sum_{t=0}^T r_t $$ it can also be discounted $$R(\tau)=\sum_{t=0}^T \gamma^t r_t$$
* value function
* advantage functions $$A^\pi (s,a)=Q^\pi(s,a)-V^\pi(s)$$

# kinds of RL Algorithms

* model-based and model-free

## what to learn

* policies
* action-value functions(Q-functions)
* value functions
* environment models

# papers

you can find the needed papers in the website
