from src.anomaly_detector import AnomalyDetector
import numpy as np

def test_anomaly_detection_with_anomaly():
    detector = AnomalyDetector(window_size=10, std_multiplier=2.5)
    
    # Feed normal data
    for i in range(9):
        is_anomaly, score = detector.update(i)
        print(f"Value: {i}, Is Anomaly: {is_anomaly}, Score: {score}")
        assert not is_anomaly
    
    # Test with an outlier
    is_anomaly, score = detector.update(100)
    print(f"Value: 100, Is Anomaly: {is_anomaly}, Score: {score}")
    assert is_anomaly, f"Failed to detect anomaly for value 100. Score: {score}"

def test_anomaly_detector_initialization():
    detector = AnomalyDetector(window_size=20, std_multiplier=2.5)
    assert detector.window_size == 20
    assert detector.std_multiplier == 2.5

def test_get_threshold():
    detector = AnomalyDetector(window_size=5, std_multiplier=2)
    for i in range(5):
        detector.update(i)
    
    threshold = detector.get_threshold()
    expected_threshold = np.mean([0, 1, 2, 3, 4]) + 2 * np.std([0, 1, 2, 3, 4])
    np.testing.assert_almost_equal(threshold, expected_threshold, decimal=7)