from stable_baselines3 import A2C

def predict():
    print("Predicting")

print("Loading model")
model = A2C.load("/Users/akabra/Desktop/interface-experiment/model", verbose=1).policy
print("Loaded model")

# class ReinforcementLearningModel:
#     def __init__(self):
#         global model
#         model = A2C.load("model", verbose=1).policy
    
#     def predict(self, obs):
#         action, _state =  model.predict(obs)
#         return action

# model = ReinforcementLearningModel()
# def predict(obs):
#     return model.predict(obs)