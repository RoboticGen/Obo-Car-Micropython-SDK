# Define the chip variant.
set(IDF_TARGET esp32)

# Set the sdkconfig fragments.
set(SDKCONFIG_DEFAULTS
    ${MICROPY_PORT_DIR}/boards/sdkconfig.base
    ${MICROPY_PORT_DIR}/boards/sdkconfig.ble
)

# Set the manifest file for frozen Python code.
set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)
