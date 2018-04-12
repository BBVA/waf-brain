

def get_log_level(level: int) -> int:

    # If quiet mode selected -> decrease log level
    input_level = level * 10

    if input_level > 50:
        input_level = 50

    return 60 - input_level


__all__ = ("get_log_level", )
