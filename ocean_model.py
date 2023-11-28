# ocean_model.py

class OceanModel:
    def __init__(self):
        self.personality_types = {
            "O": "Openness",
            "C": "Conscientiousness",
            "E": "Extraversion",
            "A": "Agreeableness",
            "N": "Neuroticism"
        }
        self.weights = {
            "O": [1, 2, 3, 4, 5],  # Adjust weights as needed
            "C": [5, 4, 3, 2, 1],  # Adjust weights as needed
            "E": [1, 2, 3, 4, 5],  # Adjust weights as needed
            "A": [5, 4, 3, 2, 1],  # Adjust weights as needed
            "N": [1, 2, 3, 4, 5]   # Adjust weights as needed
            
        }

    def predict_personality(self, responses):
        personality_scores = {
            trait: sum([w * r for w, r in zip(self.weights[trait], responses)])
            for trait in self.personality_types.keys()
        }
        # Determine the personality trait with the highest score
        personality_type = max(personality_scores, key=personality_scores.get)
        send.responses(http://googlecollab/model.h5)
        return personality_type
