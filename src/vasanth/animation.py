"""Low-level terminal effects: colour, typewriter, progress bars, timing.

Pure standard library. Nothing here touches the network or the filesystem.
Everything degrades gracefully: no colour on dumb terminals, ASCII borders
where Unicode cannot be encoded, and instant output when animations are
disabled via the VASANTH_FAST environment variable.
"""

from __future__ import annotations

import os
import shutil
import sys
import time

# ---------------------------------------------------------------------------
# Capability detection
# ---------------------------------------------------------------------------

def _enable_windows_ansi() -> bool:
    """Turn on virtual-terminal processing in legacy Windows consoles."""
    if os.name != "nt":
        return True
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint32()
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        # ENABLE_VIRTUAL_TERMINAL_PROCESSING
        return bool(kernel32.SetConsoleMode(handle, mode.value | 0x0004))
    except Exception:
        return False


def _reconfigure_stdout() -> None:
    """Best-effort UTF-8 output so the borders render on Windows code pages."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")  # 3.7+
        except Exception:
            pass


def _supports_unicode() -> bool:
    encoding = getattr(sys.stdout, "encoding", None) or ""
    try:
        "╔═╗│╰".encode(encoding)
        return True
    except Exception:
        return False


def _supports_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    if not sys.stdout.isatty():
        return False
    if os.environ.get("TERM", "") == "dumb":
        return False
    if os.name == "nt":
        return _ANSI_OK or bool(os.environ.get("WT_SESSION") or os.environ.get("TERM"))
    return True


_ANSI_OK = _enable_windows_ansi()
_reconfigure_stdout()

UNICODE = _supports_unicode()
COLOR = _supports_color()

#: Set VASANTH_FAST=1 to skip every delay (used by tests and impatient authors).
FAST = bool(os.environ.get("VASANTH_FAST"))

#: Global multiplier for every delay. VASANTH_SPEED=0.5 runs twice as fast.
try:
    SPEED = max(0.0, float(os.environ.get("VASANTH_SPEED", "1")))
except ValueError:
    SPEED = 1.0


# ---------------------------------------------------------------------------
# Palette -- luminous yellow / warm amber / golden ivory
# ---------------------------------------------------------------------------

class _Palette:
    # Yellow & Gold theme
    ROSE = "\033[38;5;220m"       # Radiant golden yellow (accents, keys, highlights)
    DEEP_ROSE = "\033[38;5;214m"  # Warm amber gold (outer double frame, progress bar)
    PLUM = "\033[38;5;178m"       # Golden honey (menu frame, light boxes)
    WINE = "\033[38;5;172m"       # Deep amber / ochre (errors, warnings)
    IVORY = "\033[38;5;230m"      # Warm ivory cream (primary text)
    SOFT = "\033[38;5;222m"       # Soft golden cream (secondary lines)
    DIM = "\033[38;5;245m"        # Muted neutral grey
    FAINT = "\033[38;5;239m"      # Subtle rules and delimiters
    GOLD = "\033[38;5;220m"       # Bright gold
    YELLOW = "\033[38;5;226m"     # Pure vibrant yellow
    AMBER = "\033[38;5;214m"      # Deep golden amber
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    RESET = "\033[0m"


class _NoPalette:
    ROSE = DEEP_ROSE = PLUM = WINE = IVORY = SOFT = DIM = FAINT = GOLD = YELLOW = AMBER = ""
    BOLD = ITALIC = RESET = ""


C = _Palette() if COLOR else _NoPalette()


def paint(text: str, color: str) -> str:
    """Wrap text in a colour, or return it untouched when colour is off."""
    if not COLOR or not color:
        return text
    return "%s%s%s" % (color, text, C.RESET)


# ---------------------------------------------------------------------------
# Terminal helpers
# ---------------------------------------------------------------------------

def width(maximum: int = 62) -> int:
    """Usable content width, never wider than `maximum`."""
    try:
        cols = shutil.get_terminal_size(fallback=(80, 24)).columns
    except Exception:
        cols = 80
    return max(30, min(maximum, cols - 2))


def term_columns() -> int:
    try:
        return shutil.get_terminal_size(fallback=(80, 24)).columns
    except Exception:
        return 80


def clear() -> None:
    """Clear the screen without shelling out."""
    if not sys.stdout.isatty():
        write("\n")
        return
    write("\033[2J\033[H" if (COLOR or _ANSI_OK or os.name != "nt") else "\n" * 40)
    flush()


def hide_cursor() -> None:
    if sys.stdout.isatty():
        write("\033[?25l")
        flush()


def show_cursor() -> None:
    if sys.stdout.isatty():
        write("\033[?25h")
        flush()


def write(text: str) -> None:
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:  # pragma: no cover - very old consoles
        sys.stdout.write(text.encode("ascii", "replace").decode("ascii"))


def flush() -> None:
    try:
        sys.stdout.flush()
    except Exception:
        pass


def sleep(seconds: float) -> None:
    """A delay that respects VASANTH_FAST / VASANTH_SPEED."""
    if FAST or seconds <= 0:
        return
    time.sleep(seconds * SPEED)


def center(text: str, total: int | None = None) -> str:
    """Centre a single visible line inside the terminal."""
    total = total or term_columns()
    pad = max(0, (total - len(text)) // 2)
    return " " * pad + text


# ---------------------------------------------------------------------------
# Typewriter
# ---------------------------------------------------------------------------

#: Characters that earn a longer pause -- this is what makes it feel human.
_PUNCTUATION_PAUSE = {
    ".": 0.16,
    ",": 0.08,
    "?": 0.20,
    "!": 0.18,
    ":": 0.10,
    ";": 0.10,
    "-": 0.04,
}


def type_line(
    text: str,
    color: str = "",
    delay: float = 0.028,
    centered: bool = True,
    newline: bool = True,
    indent: int = 0,
) -> None:
    """Print one line character by character."""
    if centered:
        pad = max(0, (term_columns() - len(text)) // 2)
    else:
        pad = indent
    write(" " * pad)
    if COLOR and color:
        write(color)

    if FAST or delay <= 0:
        write(text)
    else:
        for char in text:
            write(char)
            flush()
            sleep(delay)
            extra = _PUNCTUATION_PAUSE.get(char)
            if extra and not text.endswith(char * 3):
                sleep(extra)
    if COLOR and color:
        write(C.RESET)
    if newline:
        write("\n")
    flush()


def type_block(
    lines,
    color: str = "",
    delay: float = 0.028,
    line_pause: float = 0.22,
    blank_pause: float = 0.38,
    centered: bool = True,
    indent: int = 0,
) -> None:
    """Type a list of lines, pausing a little longer on blank ones."""
    for line in lines:
        if line == "":
            write("\n")
            flush()
            sleep(blank_pause)
            continue
        type_line(line, color=color, delay=delay, centered=centered, indent=indent)
        sleep(line_pause)


def reveal_name(name: str, color: str = "") -> None:
    """Letter-by-letter reveal of the name, spaced out and slow."""
    color = color or C.ROSE
    spaced = " ".join(name.upper())
    pad = max(0, (term_columns() - len(spaced)) // 2)
    write("\n" * 2 + " " * pad)
    for char in spaced:
        write(paint(char, C.BOLD + color if COLOR else ""))
        flush()
        sleep(0.10 if char != " " else 0.04)
    write("\n\n")
    flush()
    sleep(0.9)


# ---------------------------------------------------------------------------
# Progress
# ---------------------------------------------------------------------------

BLOCK_FULL = "█" if UNICODE else "#"
BLOCK_EMPTY = "░" if UNICODE else "."


def progress(
    label: str = "",
    duration: float = 1.4,
    bar_width: int = 24,
    color: str = "",
    centered: bool = True,
    stall_at: float | None = None,
    show_percent: bool = True,
) -> None:
    """Draw a filling progress bar.

    `stall_at` (0..1) makes the bar hesitate near the end -- used by the
    Love.exe diagnostic, where the bar is supposed to fail dramatically.
    """
    color = color or C.DEEP_ROSE
    if label:
        type_line(label, color=C.SOFT, delay=0.02, centered=centered)
        sleep(0.12)

    steps = bar_width
    step_time = (duration / steps) if duration > 0 else 0
    pad = max(0, (term_columns() - (bar_width + (6 if show_percent else 0))) // 2)

    for i in range(steps + 1):
        ratio = i / steps
        if stall_at is not None and ratio >= stall_at:
            break
        filled = BLOCK_FULL * i
        empty = BLOCK_EMPTY * (steps - i)
        bar = paint(filled, color) + paint(empty, C.FAINT)
        pct = " %3d%%" % int(ratio * 100) if show_percent else ""
        write("\r" + " " * pad + bar + paint(pct, C.DIM))
        flush()
        if not FAST:
            sleep(step_time)

    write("\n")
    flush()


def failing_progress(label: str, stop_at: float = 0.72) -> None:
    """A progress bar that halts mid-flight and displays [FAILED]."""
    progress(label=label, duration=1.2, stall_at=stop_at, show_percent=False)
    sleep(0.4)
    pad = max(0, (term_columns() - 24) // 2)
    write("\r" + " " * pad + paint("[ FAILED ]", C.BOLD + C.WINE if COLOR else "") + "\n")
    flush()
    sleep(0.6)


# ---------------------------------------------------------------------------
# Subtle effects
# ---------------------------------------------------------------------------

def spinner(label: str = "", duration: float = 1.0, color: str = "") -> None:
    """A quiet braille/ascii spinner for non-progress waiting."""
    frames = ("⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏") if UNICODE else ("|", "/", "-", "\\")
    color = color or C.DEEP_ROSE
    end_time = time.time() + (0 if FAST else duration * SPEED)
    i = 0
    pad = max(0, (term_columns() - (len(label) + 4)) // 2)
    while time.time() < end_time:
        frame = frames[i % len(frames)]
        line = " " * pad + paint(frame, color) + " " + paint(label, C.DIM)
        write("\r" + line)
        flush()
        sleep(0.08)
        i += 1
    write("\r" + " " * (pad + len(label) + 4) + "\r")
    flush()


def dots(count: int = 3, delay: float = 0.35, color: str = "") -> None:
    """Type a few dots on the current line, then newline."""
    color = color or C.FAINT
    for _ in range(count):
        write(paint(".", color))
        flush()
        sleep(delay)
    write("\n")
    flush()


def transition(seconds: float = 0.45) -> None:
    """Short blackout between scenes."""
    clear()
    sleep(seconds)
