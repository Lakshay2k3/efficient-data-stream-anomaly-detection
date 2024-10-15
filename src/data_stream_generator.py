import numpy as np

class DataStreamGenerator:
    def __init__(self, base_value=100, trend=0.1, seasonality=10, noise_level=5, anomaly_probability=0.01, anomaly_scale=3):
        self.base_value = base_value
        self.trend = trend
        self.seasonality = seasonality
        self.noise_level = noise_level
        self.anomaly_probability = anomaly_probability
        self.anomaly_scale = anomaly_scale
        self.time = 0

    def generate_stream(self):
        while True:
            self.time += 1
            trend_component = self.trend * self.time
            seasonal_component = self.seasonality * np.sin(2 * np.pi * self.time / 365)
            noise = np.random.normal(0, self.noise_level)
            
            value = self.base_value + trend_component + seasonal_component + noise
            
            is_anomaly = np.random.random() < self.anomaly_probability
            if is_anomaly:
                value += np.random.normal(0, self.anomaly_scale * self.noise_level)
            
            yield self.time, value, is_anomaly