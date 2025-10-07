#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    avg_heart_rate = data['heart_rate'].mean()
    avg_systolic_bp = data['blood_pressure_systolic'].mean()
    avg_glucose = data['glucose_level'].mean()

    return {
        "avg_heart_rate": f"{avg_heart_rate:.1f}",
        "avg_systolic_bp": f"{avg_systolic_bp:.1f}",
        "avg_glucose": f"{avg_glucose:.1f}"
    }
   


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    high_hr_count = (data['heart_rate'] > 90).sum()
    high_bp_count = (data['blood_pressure_systolic'] > 130).sum()
    high_glucose_count = (data['glucose_level'] > 110).sum()
    
    return {
        "high_heart_rate": int(high_hr_count),
        "high_blood_pressure": int(high_bp_count),
        "high_glucose": int(high_glucose_count)
    }
        


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    report = f"""Health Sensor Data Analysis Report
==================================

Dataset Summary:
- Total readings: {total_readings}

Average Measurements:
- Heart Rate: {stats['avg_heart_rate']} bpm
- Systolic Blood Pressure: {stats['avg_systolic_bp']} mmHg
- Glucose Level: {stats['avg_glucose']} mg/dL

Abnormal Readings:
- High Heart Rate (>90 bpm): {abnormal['high_heart_rate']} readings
- High Systolic Blood Pressure (>130 mmHg): {abnormal['high_blood_pressure']} readings
- High Glucose Level (>110 mg/dL): {abnormal['high_glucose']} readings

 """
    return report


def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    
    with open(filename, 'w') as f:
        f.write(report)


def main():
    """Main execution function."""

    data = load_data('health_data.csv')
    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    total_readings = len(data)
    report = generate_report(stats, abnormal, total_readings)
    save_report(report, 'output/analysis_report.txt')
    print("analysis report successfully saved to 'output/analysis_report.txt'")



if __name__ == "__main__":
    main()