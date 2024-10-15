import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class Visualizer:
    def __init__(self, max_points=1000):
        self.max_points = max_points
        self.times = []
        self.values = []
        self.anomalies = []
        self.thresholds = []

    def update(self, data_point, threshold):
        time, value, is_anomaly = data_point
        self.times.append(time)
        self.values.append(value)
        self.anomalies.append(value if is_anomaly else np.nan)
        self.thresholds.append(threshold)

        if len(self.times) > self.max_points:
            self.times = self.times[-self.max_points:]
            self.values = self.values[-self.max_points:]
            self.anomalies = self.anomalies[-self.max_points:]
            self.thresholds = self.thresholds[-self.max_points:]

    def plot_real_time(self, data_stream, detector):
        fig, ax = plt.subplots(figsize=(12, 6))
        line, = ax.plot([], [], lw=2, marker='.', markersize=4, label='Data Stream')
        anomaly_points, = ax.plot([], [], 'ro', markersize=8, label='Anomalies')
        threshold_line, = ax.plot([], [], 'r--', lw=1, label='Threshold')

        ax.set_xlim(0, self.max_points)
        ax.set_ylim(0, 1000)  # Initial y-axis limits
        ax.set_title("Real-time Data Stream with Anomaly Detection")
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        ax.legend(loc='upper left')

        def init():
            return line, anomaly_points, threshold_line

        def update(frame):
            data_point = next(data_stream)
            is_anomaly, _ = detector.update(data_point[1])
            threshold = detector.get_threshold()
            self.update((data_point[0], data_point[1], is_anomaly), threshold)

            line.set_data(self.times, self.values)
            anomaly_points.set_data(self.times, self.anomalies)
            threshold_line.set_data(self.times, self.thresholds)

            # Dynamically adjust y-axis limits
            ax.set_ylim(min(self.values) - 10, max(self.values) + 10)
            ax.relim()
            ax.autoscale_view()

            return line, anomaly_points, threshold_line

        ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True, interval=50)
        plt.show()