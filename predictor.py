from stable_baselines3 import A2C
import traceback

model = None

def init():
    try:
        model = A2C.load("/Users/akabra/Desktop/trainrl/model", verbose=1).policy
    except:
        print("Failed to load model. Stack trace:")
        traceback.print_exc()

def predict(obs):
    try:
        model = A2C.load("/Users/akabra/Desktop/trainrl/model", verbose=1).policy
        model_observation = {
            "train1": [obs["train1pos"], obs["train1vel"]],
            "train2": [obs["train2pos"], obs["train2vel"]]
        }
        action, _state = model.predict(model_observation)
        return action
        # return [0.1, 0.2, 0.3, 0.4]
    except:
        print("Failed to predict. Stack trace:")
        traceback.print_exc()