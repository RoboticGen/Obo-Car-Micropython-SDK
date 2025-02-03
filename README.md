# Micropython Custom Image for Obo Car
Customized Micropython Image inbuilt with Obo Car specific modules and configurations for Obo Car.


![Build Status](https://github.com/RoboticGen/Obo-Car-Micropython-SDK/actions/workflows/build_script.yml/badge.svg)
![Issues](https://img.shields.io/github/issues/RoboticGen/Obo-Car-Micropython-SDK)
![MicroPython](https://img.shields.io/badge/micropython-v1.23.0-blue)
![ESP-IDF](https://img.shields.io/badge/esp--idf-v5.3.2-orange)
![Board](https://img.shields.io/badge/Obo-Car-blue)
![Last Commit](https://img.shields.io/github/last-commit/RoboticGen/Obo-Car-Micropython-SDK)


## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Prerequisites

- [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/index.html) installed and environment set up.
- [Python 3.9 or later](https://www.python.org/downloads/) installed.
- [Git](https://git-scm.com/downloads) installed.

> [!TIP]
> If you have installed Docker, you may use [act](https://nektosact.com/) to run this GitHub Action locally. 💀✅

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RoboticGen/Obo-Car-Micropython-SDK.git
    ```
2. Change the directory:
    ```bash
    cd Obo-Car-Micropython-SDK
    ```
3. Initialize the submodules:
    ```bash
    git submodule update --init lib/micropython src/obo-car
    ```
> [!WARNING]
> Sometimes you may need to checkout the specfic branch or tag of the submodules. Currently micropython is checked out to `v1.23.0` and `obo-car` is checked out to `dev-micropython-image`.be sure to checkout the correct branch or tag.

4. Install micropython libraries:
    ```bash
    cd lib/micropython
    git submodule update --init lib/berkeley-db-1.xx lib/micropython-lib
    cd ../..
    ```

5. Build mpy-cross(Micropython cross compiler):
    ```bash
    make -C lib/micropython/mpy-cross
    ```

6. Run patch script:
    ```bash
    python3 patch.py
    ```

7. Build the firmware:
    ```bash
    cd boards/OBO_CAR
    idf.py build
    cd ../..
    ```

## Usage

1. Flash the firmware:
    ```bash
    cd lib/micropython
    idf.py -p <PORT> flash
    cd ../..
    ```
    Replace `<PORT>` with the port where the Obo-Car is connected.


## Credits
This repository is fork of [micropython-example-boards](https://github.com/micropython/micropython-example-boards)

## License
This project is maintained under MIT License.
