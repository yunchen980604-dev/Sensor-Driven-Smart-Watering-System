# Sensor-Driven Smart Watering System

# From Smart Agriculture Research to an Automatic Watering Prototype

I first created a school science-communication project about climate change, SCL water-retention technology, and smart agriculture. I made a poster, recorded an introduction video, displayed the project at school, and collected 30 survey responses.

I then turned one idea from that project into a working computer-science prototype: a low-cost ESP32 smart watering system.

The system checks whether soil is dry. If the soil is too dry, it automatically turns on a small water pump for a few seconds. An LCD screen shows the soil reading and current system status.

## How It Works

Soil moisture sensor → ESP32 → dryness threshold → water pump → plant

In this project, I tested the sensor with real soil, calibrated the moisture threshold, assembled the hardware, debugged connection problems, and documented the process.
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

## Survey Results

I also conducted a small student questionnaire about SCL technology, climate change, and sensor-guided smart agriculture. The survey received 30 valid responses and provided context for the design of this prototype.
[View the survey results]

## License

MIT License
