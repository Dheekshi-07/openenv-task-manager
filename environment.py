from typing import Dict, Any
import random

class TaskEnv:
    def __init__(self):
        self.tasks = []
        self.current_index = 0

    def reset(self) -> Dict[str, Any]:
        self.tasks = [
            {"task": "Finish report", "priority": "high"},
            {"task": "Check emails", "priority": "low"},
            {"task": "Team meeting", "priority": "medium"},
        ]
        random.shuffle(self.tasks)
        self.current_index = 0
        return self.state()

    def step(self, action: str) -> Dict[str, Any]:
        correct = self.tasks[self.current_index]["priority"]
        reward = 1.0 if action == correct else 0.0
        self.current_index += 1
        done = self.current_index >= len(self.tasks)

        return {
            "reward": reward,
            "done": done,
            "state": self.state()
        }

    def state(self):
        if self.current_index < len(self.tasks):
            return self.tasks[self.current_index]
        return {"message": "All tasks completed"}