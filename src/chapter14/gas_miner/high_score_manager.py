import json
import os
from datetime import datetime

# Add to your constants
HIGH_SCORES_FILE = "scores/high_scores.json"
MAX_HIGH_SCORES = 5

class HighScoreManager:
    def __init__(self):
        self.high_scores = []
        self.load_high_scores()

    def load_high_scores(self):
        """Load high scores from file"""
        try:
            # Create scores directory if it doesn't exist
            os.makedirs('scores', exist_ok=True)
            
            if os.path.exists(HIGH_SCORES_FILE):
                with open(HIGH_SCORES_FILE, 'r') as f:
                    self.high_scores = json.load(f)
        except Exception as e:
            print(f"Error loading high scores: {e}")
            self.high_scores = []

    def save_high_scores(self):
        """Save high scores to file"""
        try:
            with open(HIGH_SCORES_FILE, 'w') as f:
                json.dump(self.high_scores, f)
        except Exception as e:
            print(f"Error saving high scores: {e}")

    def add_score(self, score):
        """Add a new score and return True if it's a high score"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        new_score = {"score": score, "date": date_str}
        
        # Check if it's a high score
        is_high_score = (len(self.high_scores) < MAX_HIGH_SCORES or 
                        score > min(s["score"] for s in self.high_scores))
        
        if is_high_score:
            self.high_scores.append(new_score)
            # Sort by score (highest first) and keep only top scores
            self.high_scores.sort(key="score", reverse=True)
            self.high_scores = self.high_scores[:MAX_HIGH_SCORES]
            self.save_high_scores()
            
        return is_high_score

