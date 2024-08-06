#!/usr/bin/env python3
import platform

def get_system_info():
    """Get basic system information."""
    return {
        'OS': platform.system(),
        'Version': platform.version(),
        'Release': platform.release(),
        'Architecture': platform.architecture(),
        'Machine': platform.machine(),
        'Processor': platform.processor()
    }

def system_main():
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    system_main()
