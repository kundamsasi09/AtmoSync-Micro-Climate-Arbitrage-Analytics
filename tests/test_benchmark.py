"""
Unit tests for src/benchmark.py
Validates high-velocity streaming generation, Arrhenius Q10 calculations, and pipeline metrics.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from benchmark import (
    simulate_high_frequency_stream,
    calculate_arrhenius_spoilage_multiplier,
    execute_pipeline_benchmark,
)


def test_simulate_stream_generation():
    events = simulate_high_frequency_stream(100)
    assert len(events) == 100
    first = events[0]
    assert "packet_id" in first
    assert "container_id" in first
    assert "telemetry" in first
    assert "temperature_celsius" in first["telemetry"]
    assert "relative_humidity_pct" in first["telemetry"]
    assert "compressor_status" in first["telemetry"]


def test_arrhenius_spoilage_calculation():
    # Optimal conditions: 5 deg C, 85% humidity -> multiplier should be close to 1.0
    optimal_mult = calculate_arrhenius_spoilage_multiplier(5.0, 85.0)
    assert 0.95 <= optimal_mult <= 1.05

    # Thermal breach: 15 deg C (10 deg above ideal) -> Q10 factor of 2.2
    breached_mult = calculate_arrhenius_spoilage_multiplier(15.0, 85.0)
    assert breached_mult > 2.0
    assert breached_mult > optimal_mult


def test_execute_pipeline_benchmark():
    report = execute_pipeline_benchmark(200)
    assert report["total_packets_ingested"] == 200
    assert report["throughput_packets_per_sec"] > 500  # Should process very fast in memory
    assert report["kafka_consumer_lag"] == 0
    assert report["pipeline_status"] == "OPTIMAL_ZERO_LAG"


if __name__ == "__main__":
    test_simulate_stream_generation()
    test_arrhenius_spoilage_calculation()
    test_execute_pipeline_benchmark()
    print("All benchmark tests passed successfully!")
