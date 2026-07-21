# Sensor-Driven Smart Watering System

## Overview

This project is a low-cost ESP32-based smart watering system. It uses a soil moisture sensor to measure soil conditions and automatically controls a small water pump when the soil becomes dry.

The project explores how sensor data and simple programming logic can support more efficient and data-driven irrigation.

## Research Question

How can calibrated soil-moisture readings be used in a low-cost ESP32 system to reduce unnecessary watering?

## Main Features

- ESP32 programmed with MicroPython
- Soil moisture sensor for real-time readings
- LCD screen for soil values and system status
- LED indicator during watering
- Automatic water pump control
- Sensor calibration based on experimental data

## System Logic

1. The ESP32 reads the soil moisture sensor.
2. If the soil reading is below 100, the system shows `SENSOR CHECK`.
3. If the soil reading is 2200 or higher, the soil is considered dry.
4. The water pump runs for 3 seconds.
5. The system waits for 60 seconds before measuring again.
6. If the soil is not dry, the LCD shows `MOIST OK`.

## Testing and Calibration Results

| Soil condition | Raw ADC reading | System response |
|---|---:|---|
| Wet soil | About 1000-1500 | Do not water |
| Slightly dry soil | About 1700-1800 | Do not water yet |
| Very dry soil | About 2900 | Watering is needed |
| Final watering threshold | 2200 or higher | Pump runs for 3 seconds |
| Unstable sensor signal | Below 100 or repeatedly 0 | Show `SENSOR CHECK` and do not water |

**Note:** These values are raw ADC readings from 0 to 4095. They are not percentages or millilitres.

## Hardware

- ESP32 development board
- Capacitive soil moisture sensor
- 16x2 I2C LCD display
- Small water pump and tubing
- LED
- Jumper wires and power supply

## Current Status

The core prototype has been built and tested successfully:

- Soil sensor reading and calibration
- LCD display
- Manual pump test
- Automatic watering logic
## Limitations

- Soil readings vary with soil type, sensor placement, and environmental conditions.
- The current prototype does not use the water-level sensor for automatic safety shutdown.
## Future Improvements

- Add a more reliable water-level safety system
- Add Wi-Fi data logging
- Create a mobile dashboard
- Compare water use with fixed-schedule watering
- Add anonymized user-survey results about smart agriculture

## Project Context

This prototype developed from my earlier science-communication project about climate change, smart agriculture, SCL water-retention technology, and data-driven irrigation.

## License

MIT License
