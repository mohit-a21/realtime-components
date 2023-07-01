from env import env


def pretty_log(str):
    print(f"{START}🥞: {str}{END}")


# Terminal codes for pretty-printing.
START, END = "\033[1;38;5;214m", "\033[0m"

debug = env.bool("DEBUG_SERVER", default=False)


def debug_log(str):
    if debug:
        pretty_log(str)


def limiter_storage():
    return env.str("LIMITER_STORAGE", default="memory://")
