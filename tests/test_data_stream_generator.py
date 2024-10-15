import pytest
from src.data_stream_generator import DataStreamGenerator

def test_data_stream_generator_initialization():
    generator = DataStreamGenerator()
    assert generator.base_value == 100
    assert generator.trend == 0.1
    assert generator.seasonality == 10
    assert generator.noise_level == 5
    assert generator.anomaly_probability == 0.01
    assert generator.anomaly_scale == 3

def test_data_stream_generation():
    generator = DataStreamGenerator()
    stream = generator.generate_stream()
    values = [next(stream) for _ in range(1000)]
    
    assert len(values) == 1000
    assert all(isinstance(v, tuple) and len(v) == 3 for v in values)
    assert all(isinstance(v[0], int) and isinstance(v[1], float) and isinstance(v[2], bool) for v in values)

def test_anomaly_generation():
    generator = DataStreamGenerator(anomaly_probability=0.5)
    stream = generator.generate_stream()
    values = [next(stream) for _ in range(1000)]
    
    anomalies = [v for v in values if v[2]]
    assert len(anomalies) > 0  # Should have some anomalies
    assert 400 < len(anomalies) < 600  # Roughly 50% should be anomalies