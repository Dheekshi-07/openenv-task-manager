from environment import TaskEnv
from graders import run_all_graders

def run():
    env = TaskEnv()
    state = env.reset()
    total_reward = 0

    done = False
    while not done:
        # simple baseline agent (random priority choice)
        action = state.get("priority", "medium")
        result = env.step(action)

        total_reward += result["reward"]
        done = result["done"]
        state = result["state"]

    scores = run_all_graders(total_reward)
    print("Scores:", scores)


if __name__ == "__main__":
    run()