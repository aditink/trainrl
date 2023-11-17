from stable_baselines3 import A2C
import traceback

try:
    model = A2C.load("/Users/akabra/Desktop/interface-experiment/model", verbose=1).policy
except:
    print("Failed to load model. Stack trace:")
    traceback.print_exc()

def predict():
    try:
        # return model.predict(obs, [1])
        return [0.1, 0.2, 0.3, 0.4]
    except:
        print("Failed to predict. Stack trace:")
        traceback.print_exc()

# class ReinforcementLearningModel:
#     def __init__(self):
#         global model
#         model = A2C.load("model", verbose=1).policy
    
#     def predict(self, obs):
#         action, _state =  model.predict(obs)
#         return action

# model = ReinforcementLearningModel()