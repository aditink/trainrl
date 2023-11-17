from stable_baselines3 import A2C
import traceback

try:
    model = A2C.load("/Users/akabra/Desktop/interface-experiment/model", verbose=1).policy
except:
    print("Failed to load model. Stack trace:")
    traceback.print_exc()

def predict(obs):
    try:
        print(obs)
        # return model.predict(obs, [1])
        return [0.1, 0.2, 0.3, 0.4]
    except:
        print("Failed to predict. Stack trace:")
        traceback.print_exc()