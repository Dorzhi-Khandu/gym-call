# gym-call

The Call environment is a multiagent domain featuring continuous state and action spaces. Currently, several tasks are supported:

Caller
The caller task initializes a single offensive agent on the field and rewards +1 for scoring a goal and 0 otherwise. In order to score a goal, the agent will need to know how to approach the ball and kick towards the goal. The sparse nature of the goal reward makes this task very difficult to accomplish.


Installation
cd gym-call
pip install -e .
