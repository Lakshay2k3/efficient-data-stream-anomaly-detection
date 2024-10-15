import numpy as np
from collections import deque

class AnomalyDetector:
    def __init__(self, window_size=20, std_multiplier=2.5):
        self.data = deque(maxlen=window_size)
        self.window_size = window_size
        self.std_multiplier = std_multiplier
        self.mean = 0
        self.std_dev = 0

    def update(self, value):
        self.data.append(value)
        
        if len(self.data) < self.window_size:
            return False, 0
        
        self.mean = np.mean(self.data)
        self.std_dev = np.std(self.data)
        
        if self.std_dev == 0:
            return False, 0
        
        z_score = abs(value - self.mean) / self.std_dev
        is_anomaly = z_score > self.std_multiplier
        
        return is_anomaly, z_score

    def get_threshold(self):
        return self.mean + self.std_multiplier * self.std_dev