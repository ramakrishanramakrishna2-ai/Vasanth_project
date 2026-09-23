# vasanth-love

A small terminal experience.

```bash
pip install vasanth-love
```

Then:

```bash
vasanth
```

(`vasanth-love` works too — same thing.)

That's the whole thing. It runs in the terminal, works offline, and takes a
few minutes to read through.

> If `vasanth-love` is already taken on PyPI when publishing, you can name the distribution
> `vasanth-love-cli`. The command he actually types remains `vasanth-love` (`vasanth` also works).

---

## What it is

A Python package that opens a quiet, animated letter in the terminal: a boot
sequence, a menu, a few scenes to wander through, and one question at the end.
There is also a way to write a message back.

It is a standard console application. It installs like any other package,
runs like any other command, and uninstalls with `pip uninstall vasanth-love`.

## Requirements

* Python 3.9 or newer
* Any terminal: Windows PowerShell, Windows Terminal, CMD, macOS Terminal,
  iTerm2, or any Linux terminal

**Zero runtime dependencies.** Everything is standard library, so the install
is instant and there is nothing to audit.

## Usage

```bash
vasanth                 # the full experience (vasanth-love works too)
python -m vasanth       # identical, if the command isn't on PATH
vasanth --skip-intro    # straight to the menu
vasanth --fast          # no animation delays
vasanth --version
```

Environment knobs:

| Variable | Effect |
| --- | --- |
| `VASANTH_SPEED` | Delay multiplier. `0.5` is twice as fast, `2` is slower. |
| `VASANTH_FAST` | Set to anything to remove all delays. |
| `NO_COLOR` | Standard opt-out; renders without colour. |
| `VASANTH_ENDPOINT` | Points the message feature at a different backend. |

`Ctrl+C` exits gracefully at any point.

---

## Customising it

**Every personal word lives in exactly one file:** `src/vasanth/messages.py`.
Nothing personal is scattered through the code, so you can edit that one file
without reading any of the rest.

What's in there, in order:

| Section | What it controls |
| --- | --- |
| `NAME`, `TAGLINE` | The name on every screen. `{name}` anywhere expands to it. |
| `BOOT_*` | The opening sequence and the reveal. |
| `INTRO_LINES` | The lines shown once after boot. |
| `MAIN_MESSAGE` | Option 1 — the letter itself. |
| `REASONS` | Option 2 — numbered automatically; add as many as you like. |
| `LOVE_EXE_*` | Option 3 — the fake diagnostic. |
| `MEMORIES` | Option 4 — **placeholders; replace with your own.** |
| `RANDOM_THOUGHTS` | Option 5 — the random pool. |
| `QUESTION`, `ANSWER_*` | Option 6 — the question and every reply. |
| `SEND_*` | Option 7 — the message-back screens and privacy notice. |
| `SECRET_*` | The hidden screen, and what triggers it. |
| `EXIT_*` | The goodbye. |
| `MENU_ITEMS` | Menu labels and order. |

Formatting rules, which the test suite enforces:

* A block is a list of lines. `""` is a deliberate pause, not a blank string.
* Keep lines under ~46 characters so they stay centred and never wrap.
* `{name}` is the only placeholder.

Change the name in one place:

```python
NAME = "Vasanth"
```

Add a reason — numbering is automatic:

```python
REASONS = [
    ["Because talking to you never feels ordinary."],
    ["Because of the way you", "explain things you love."],
]
```

Replace the placeholder memories with real ones:

```python
MEMORIES = [
    "That conversation I still remember.",
    "That day we laughed for no reason.",
]
```

Change the question:

```python
QUESTION = [
    "Would you like to be",
    "a little more than",
    "just a beautiful part",
    "of my life?",
]
```

After editing, check your work:

```bash
pip install -e ".[dev]"
pytest              # catches unbalanced braces, over-long lines, dead menu entries
vasanth --fast      # read it end to end in a few seconds
```

---

## Local development

```bash
git clone <your-repo-url>
cd Vasanth_project
pip install -e ".[dev]"
vasanth-love
```

Run the tests:

```bash
pytest                    # the CLI
cd backend && pytest      # the message relay
```

Build a distribution:

```bash
pip install build
python -m build           # writes dist/*.whl and dist/*.tar.gz
pip install dist/vasanth_love-1.0.0-py3-none-any.whl
```

Publish:

```bash
pip install twine
twine upload dist/*
```

---

## The message feature

Option 7 lets him write a message and send it to you by email.

The important constraint: **this package is public, so it contains no
credentials.** It knows one public HTTPS URL and nothing else. The email
provider's API key lives only in the backend's environment variables.

```
vasanth CLI  ──HTTPS──▶  your backend  ──API──▶  email provider  ──▶  your inbox
 (public,                 (holds the
  no secrets)              secret)
```

What is sent: the message he typed, and nothing else. No files, contacts,
location, system information, credentials, or identifiers. No analytics, no
tracking, no logging to disk. Every other feature works with the network
unplugged, and a privacy notice is shown before anything leaves the machine.

If the backend can't be reached, the CLI says the message was **not**
delivered. It only claims success on a confirmed 2xx response.

### Running the backend

See [`backend/README.md`](backend/README.md) for the full deployment guide.
The short version:

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env          # then fill in your real values
uvicorn app.main:app --reload
```

Then point the CLI at it while testing:

```bash
VASANTH_ENDPOINT=http://127.0.0.1:8000/api/message vasanth-love
```

Before publishing, set the deployed URL in `src/vasanth/api.py`:

```python
DEFAULT_ENDPOINT = "https://your-backend.example.com/api/message"
```

### Never commit

`.env` is in `.gitignore` and must stay there. `.env.example` holds the shape
of the configuration, never the values.

---

## Privacy

* No telemetry, no analytics, no tracking, no identifiers.
* Nothing is written to disk. No config file, no history, no cache.
* No network access at all unless he chooses to send a message and confirms.
* Uninstalling removes everything: `pip uninstall vasanth-love`.

## License

MIT. See [LICENSE](LICENSE).
