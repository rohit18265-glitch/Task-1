# Task-1: Telemetry Data Converter

## Overview
A Python utility that converts IoT device telemetry data between two different JSON formats into a unified canonical format.

## Project Structure
- `solution.py` — Main converter logic and unit tests
- `data-1.json` — Sample input in Format 1 (flat device fields with nested measurements)
- `data-2.json` — Sample input in Format 2 (time/device/data structure)
- `data-result.json` — Expected unified output (used as test reference)

## Converter Functions
- `convertFromFormat1(data)` — Converts Format 1 input to unified output
- `convertFromFormat2(data)` — Converts Format 2 input to unified output
- `convert(data)` — Smart auto-detector that picks the right converter
- `to_millis(iso_time)` — Converts ISO 8601 timestamp to Unix milliseconds

## Running the Tests
```
python3 solution.py -v
```
Runs 3 unit tests: `test_format1`, `test_format2`, `test_auto` — all should pass.

## Language & Runtime
- Python 3.11
- No external dependencies (uses only standard library: `json`, `unittest`, `datetime`)
