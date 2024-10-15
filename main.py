from src.anomaly_detector import AnomalyDetector
from src.data_stream_generator import DataStreamGenerator
from src.visualizer import Visualizer

def main():
    # Initialize components
    generator = DataStreamGenerator(base_value=100, trend=0.5, seasonality=50, noise_level=10, anomaly_probability=0.02, anomaly_scale=5)
    detector = AnomalyDetector(window_size=50, std_multiplier=2.5)
    visualizer = Visualizer(max_points=1000)

    # Generate data stream
    data_stream = generator.generate_stream()

    # Visualize the data stream with anomaly detection
    visualizer.plot_real_time(data_stream, detector)

if __name__ == "__main__":
    main()