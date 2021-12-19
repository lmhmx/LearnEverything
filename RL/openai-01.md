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

