# Task Prioritization OpenEnv

## Description
This is a simple OpenEnv environment where an AI agent learns to prioritize tasks based on urgency.

## Environment
The agent receives tasks with priorities:
- high
- medium
- low

The agent must choose the correct priority to receive rewards.

## API
- reset() → initialize environment
- step(action) → take action
- state() → get current state

## Tasks
- Easy: basic prioritization
- Medium: moderate prioritization
- Hard: complex prioritization

## Reward
Correct priority → 1.0  
Wrong priority → 0.0  

## Run Inference
```bash
python inference.py