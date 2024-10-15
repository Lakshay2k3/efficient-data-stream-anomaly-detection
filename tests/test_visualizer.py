import pytest
import numpy as np
from src.visualizer import Visualizer

@pytest.fixture
def visualizer():
    return Visualizer(max_points=100)

def test_visualizer_initialization(visualizer):
    assert visualizer.max_points == 100
    assert len(visualizer.times) == 0
    assert len(visualizer.values) == 0
    assert len(visualizer.anomalies) == 0
    assert len(visualizer.thresholds) == 0

def test_visualizer_update(visualizer):
    visualizer.update((0, 10, False), 15)
    assert len(visualizer.times) == 1
    assert len(visualizer.values) == 1
    assert len(visualizer.anomalies) == 1
    assert len(visualizer.thresholds) == 1
    assert visualizer.times[0] == 0
    assert visualizer.values[0] == 10
    assert np.isnan(visualizer.anomalies[0])
    assert visualizer.thresholds[0] == 15

    visualizer.update((1, 20, True), 25)
    assert len(visualizer.times) == 2
    assert len(visualizer.values) == 2
    assert len(visualizer.anomalies) == 2
    assert len(visualizer.thresholds) == 2
    assert visualizer.times[1] == 1
    assert visualizer.values[1] == 20
    assert visualizer.anomalies[1] == 20
    assert visualizer.thresholds[1] == 25

def test_visualizer_max_points(visualizer):
    for i in range(200):
        visualizer.update((i, i, i % 2 == 0), i + 10)
    
    assert len(visualizer.times) == 100
    assert len(visualizer.values) == 100
    assert len(visualizer.anomalies) == 100
    assert len(visualizer.thresholds) == 100
    assert visualizer.times[0] == 100
    assert visualizer.times[-1] == 199