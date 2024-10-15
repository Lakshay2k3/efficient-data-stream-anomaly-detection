# Efficient Data Stream Anomaly Detection

## Project Description
This project implements a Python script for detecting anomalies in a continuous data stream of floating-point numbers. It simulates real-time sequences that could represent various metrics such as financial transactions or system metrics, focusing on identifying unusual patterns like exceptionally high values or deviations from the norm.

## Features
- Algorithm: Implements a moving window approach with z-score calculation for anomaly detection.
- Data Stream Simulation: Generates a synthetic data stream with regular patterns, seasonal elements, and random noise.
- Real-time Anomaly Detection: Flags anomalies as the data is streamed.
- Visualization: Provides a real-time plot of the data stream and detected anomalies.
- Logging: Records detected anomalies in a log file.

## Installation
1. Ensure you have Python 3.x installed.
2. Clone this repository:
   ```
   git clone https://github.com/Lakshay2k3/efficient-data-stream-anomaly-detection.git
   cd efficient-data-stream-anomaly-detection
   ```
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the main script:
```
python main.py
```

This will start the data stream simulation and anomaly detection process, displaying a real-time plot of the data and detected anomalies.

## Testing
Run the tests using pytest:
```
python -m pytest tests/
```

## Project Structure
- `main.py`: Entry point of the application
- `src/`:
  - `anomaly_detector.py`: Contains the AnomalyDetector class
  - `data_stream_generator.py`: Implements the DataStreamGenerator class
  - `visualizer.py`: Handles real-time visualization
  - `logger.py`: Manages logging of detected anomalies
- `tests/`: Contains unit tests for each component
- `data/`: Stores generated data and logs
- `docs/`: Project documentation

## Algorithm Explanation
The anomaly detection algorithm uses a moving window approach with z-score calculation. It maintains a window of recent data points, calculates the mean and standard deviation, and flags a point as an anomaly if its z-score exceeds a specified threshold. This approach allows for adaptation to gradual changes in the data distribution while still detecting sudden anomalies.

## Author
Lakshay Garg

## License
This project is open source and available under the [MIT License](LICENSE).
