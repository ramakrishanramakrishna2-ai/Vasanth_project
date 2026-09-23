"""
============================================================================
 EVERYTHING PERSONAL LIVES IN THIS ONE FILE.
============================================================================

Edit anything below and the whole experience changes. No other file in the
package contains personal content -- the rest is just stage lighting.

Formatting notes:
  * Plain strings are printed with a typewriter effect, line by line.
  * Use blank lines ("") inside a block to create a deliberate pause.
  * Keep lines under ~46 characters so they stay centered and readable
    in a small terminal window.
  * "{name}" anywhere in a line is replaced with NAME below.
============================================================================
"""

# ---------------------------------------------------------------------------
# 1. WHO THIS IS FOR
# ---------------------------------------------------------------------------

#: Shown spaced out on the reveal screen and in every header.
NAME = "Vasanth"

#: Subtitle under the main banner.
TAGLINE = "Happy anniversary, my love"

#: The small line that sits beneath the banner.
SIGNATURE_LINE = "for us, on our anniversary."


# ---------------------------------------------------------------------------
# 2. BOOT SEQUENCE
# ---------------------------------------------------------------------------

BOOT_LINES = [
    "Initializing anniversary mode...",
    "",
    "Loading our story...",
]

BOOT_CHECKS = [
    "Checking laughter shared...",
    "Checking dreams built together...",
    "Checking love still growing...",
]

BOOT_PROMPT = [
    "One final thing...",
    "",
    "Who is my anniversary star?",
]

BOOT_CONFIRMATION = [
    "Identity confirmed.",
    "",
    "Welcome, {name}.",
    "",
    "This isn't really a program.",
    "",
    "It's our anniversary gift...",
    "wrapped in code, just for you.",
]


# ---------------------------------------------------------------------------
# 3. MAIN SCREEN INTRO  (shown once, after the boot sequence)
# ---------------------------------------------------------------------------

INTRO_LINES = [
    "Another year with you, {name}.",
    "",
    "A card felt too small for this.",
    "",
    "So I wrote you a little world instead.",
    "",
    "Happy anniversary.",
]


# ---------------------------------------------------------------------------
# 4. OPTION 1 -- OPEN MY MESSAGE
# ---------------------------------------------------------------------------

MESSAGE_OPENING = "Opening my anniversary letter for you..."

MAIN_MESSAGE = [
    "{name},",
    "",
    "Look how far we have come together.",
    "",
    "Through ordinary days and big dreams,",
    "you stayed my favourite person.",
    "",
    "Thank you for your patience,",
    "your laughter, and your love.",
    "",
    "Every year with you feels like",
    "a gift I never want to return.",
    "",
    "Happy anniversary, my love.",
    "",
    "Here is to every year still to come.",
]

MESSAGE_CLOSING = "Forever yours, on our anniversary."


# ---------------------------------------------------------------------------
# 5. OPTION 2 -- WHY VASANTH?
#     Each entry is a list of lines. Add or remove freely; they are
#     numbered automatically.
# ---------------------------------------------------------------------------

REASONS_LOADING = "Loading anniversary reasons..."

REASONS = [
    ["Because every year with you feels better."],
    [
        "Because you turned ordinary days",
        "into our favourite memories.",
    ],
    [
        "Because you stood by me",
        "in easy times and hard ones.",
    ],
    [
        "Because your love made our home",
        "warmer than any place.",
    ],
    [
        "Because your laugh still fixes",
        "my longest days.",
    ],
    [
        "Because you believe in us,",
        "even when I forget to say thanks.",
    ],
    [
        "Because growing older with you",
        "feels like an adventure.",
    ],
    [
        "Because our little inside jokes",
        "are my favourite language.",
    ],
    [
        "Because you love me as I am,",
        "and inspire who I become.",
    ],
    [
        "Honestly...",
        "",
        "One more year, one more reason.",
        "",
        "Happy anniversary, {name}.",
    ],
]


# ---------------------------------------------------------------------------
# 6. OPTION 3 -- LOVE.EXE
# ---------------------------------------------------------------------------

LOVE_EXE_STEPS = [
    "Scanning our years together...",
    "Checking anniversary memories...",
    "Calculating love grown...",
]

LOVE_EXE_FAILING_STEP = "Checking ability to stop loving {name}..."

LOVE_EXE_ERROR = [
    "ERROR.",
    "",
    "Operation failed.",
]

LOVE_EXE_CAUSE = [
    "Cause:",
    "",
    "{name} detected.",
    "",
    "System cannot continue normally.",
]

LOVE_EXE_DIAGNOSTICS = [
    "Attempting recovery ............ failed",
    "Attempting to be normal ........ failed",
    "Attempting to play it cool ..... failed",
]

LOVE_EXE_STATUS = "RUNNING"

LOVE_EXE_FOOTER = [
    "This love has no expiry date.",
]


# ---------------------------------------------------------------------------
# 7. OPTION 4 -- MEMORY LANE
#     Placeholders on purpose. Replace with your own.
# ---------------------------------------------------------------------------

MEMORY_INTRO = "Loading our anniversary memories..."

MEMORIES = [
    "Our first anniversary we celebrated.",
    "That trip we still talk about.",
    "That festival we enjoyed together.",
    "That quiet dinner that felt perfect.",
]

MEMORY_CLOSING = [
    "So many years, so many smiles.",
    "",
    "And my favourite memory",
    "is still being made with you.",
]


# ---------------------------------------------------------------------------
# 8. OPTION 5 -- RANDOM LOVE
#     Each entry is a list of lines, shown as "Random Thought #NN".
# ---------------------------------------------------------------------------

RANDOM_THOUGHTS = [
    [
        "If I had to choose one notification",
        "to receive every day...",
        "",
        "I'd choose yours.",
    ],
    [
        "Some people make your day better",
        "without even trying.",
        "",
        "You are one of those people.",
    ],
    [
        "System notification:",
        "",
        "{name} is currently occupying",
        "an unreasonable amount of storage",
        "in someone's heart.",
    ],
    [
        "You are the only person",
        "I have ever written documentation for.",
    ],
    [
        "Most conversations end.",
        "",
        "Ours just pause.",
    ],
    [
        "Warning:",
        "",
        "Prolonged exposure to {name}",
        "causes permanent smiling.",
    ],
    [
        "I have a very good memory",
        "for things you said casually.",
    ],
    [
        "You are my favourite interruption.",
    ],
    [
        "Somewhere between 'hello'",
        "and 'goodnight',",
        "",
        "you became a habit",
        "I have no intention of breaking.",
    ],
    [
        "Query executed:",
        "",
        "SELECT * FROM people",
        "WHERE presence = 'effortless';",
        "",
        "1 row returned.",
    ],
    [
        "If overthinking about you",
        "were a skill,",
        "",
        "I would be dangerously employable.",
    ],
    [
        "You do not have to do anything",
        "to be the best part of a day.",
        "",
        "Which is unfair to everyone else.",
    ],
    [
        "There is a version of me",
        "that is calmer,",
        "",
        "and it exists mostly",
        "when I am talking to you.",
    ],
    [
        "Status report:",
        "",
        "Still thinking about you.",
        "Uptime: considerable.",
    ],
    [
        "Your name is the shortest sentence",
        "that makes me pay attention.",
    ],
    [
        "I like that you are a whole person",
        "with your own weather.",
        "",
        "I just like standing in it.",
    ],
    [
        "Some people are a mood.",
        "",
        "You are a climate.",
    ],
    [
        "Cache cleared.",
        "Cookies deleted.",
        "History wiped.",
        "",
        "You: still there.",
    ],
    [
        "I do not need a reason",
        "to want to talk to you.",
        "",
        "Which is, in itself, the reason.",
    ],
    [
        "You are not a distraction.",
        "",
        "You are the thing",
        "everything else distracts me from.",
    ],
    [
        "The nicest thing about you",
        "is that you would be embarrassed",
        "reading this.",
    ],
    [
        "Fun fact:",
        "",
        "this package has zero dependencies,",
        "",
        "and exactly one reason to exist.",
    ],
]


# ---------------------------------------------------------------------------
# 9. OPTION 6 -- THE QUESTION
# ---------------------------------------------------------------------------

QUESTION_WARNING = [
    "Warning.",
    "",
    "This section holds one anniversary wish.",
    "",
    "Are you ready, {name}?",
]

QUESTION_PREPARING = "Preparing anniversary wish..."

QUESTION_HEADER = [
    "On our anniversary,",
    "I want to ask you this.",
]

#: The question itself. Change this to whatever you actually want to ask.
QUESTION = [
    "Will you keep holding my hand,",
    "through every year to come,",
    "my love, my home,",
    "my always?",
]

QUESTION_OPTIONS = [
    "Yes",
    "Maybe",
    "I need time",
    "Go back",
]

ANSWER_YES = [
    "...",
    "",
    "You just made our anniversary",
    "even more special.",
    "",
    "Thank you for every year so far.",
    "Here is to all the ones ahead.",
]

ANSWER_MAYBE = [
    "That's okay, my love.",
    "",
    "Anniversaries are for remembering,",
    "",
    "not for rushing answers.",
]

ANSWER_TIME = [
    "Take all the time you need.",
    "",
    "My love is patient.",
    "",
    "Today we simply celebrate us.",
]

ANSWER_BACK = [
    "Of course.",
    "",
    "This wish stays open.",
    "",
    "Just like my heart, always.",
]


# ---------------------------------------------------------------------------
# 10. OPTION 7 -- SEND ME A MESSAGE
# ---------------------------------------------------------------------------

SEND_INTRO = [
    "If you want to say something back,",
    "this is where you say it.",
    "",
    "Write as much or as little as you like.",
]

SEND_PROMPT_HELP = [
    "Type your message. Enter starts a new line.",
    "Finish with a single '.' on its own line",
    "or press Enter twice.",
]

SEND_PROMPT_LABEL = "{name}'s message:"

#: Shown before sending. Keep it honest and plain.
SEND_PRIVACY_NOTICE = [
    "Your message will be sent to the person",
    "who created this surprise.",
    "",
    "Only the message you choose to send will",
    "be submitted.",
]

SEND_CONFIRM_TITLE = "Send this message?"

SEND_SENDING_STEPS = [
    "Connecting...",
    "Sending your message...",
]

SEND_SENT_LINES = [
    "Message sent successfully.",
    "",
    "Your message is on its way.",
]

SEND_SUCCESS_TITLE = "MESSAGE DELIVERED"

SEND_SUCCESS = [
    "Your message has been sent.",
    "",
    "Now...",
    "",
    "someone is probably smiling",
    "at their inbox.",
]

SEND_FAILURE = [
    "Unable to send the message right now.",
    "",
    "Your message was NOT delivered.",
    "",
    "Please check your internet connection",
    "and try again later.",
]

SEND_CANCELLED = [
    "Nothing was sent.",
    "",
    "The offer stays open.",
]

SEND_EMPTY = [
    "There's nothing there yet.",
    "",
    "Write something first.",
]

SEND_TOO_LONG = [
    "That's a beautiful amount of words.",
    "",
    "Slightly more than the envelope holds,",
    "though. Trim it a little?",
]


# ---------------------------------------------------------------------------
# 11. SECRET  (menu option, or type 143 / the name at the menu)
# ---------------------------------------------------------------------------

SECRET_TITLE = "HAPPY ANNIVERSARY SECRET"

SECRET_MESSAGE = [
    "You found our anniversary secret.",
    "",
    "But honestly...",
    "",
    "you already knew it.",
    "",
    "Every year, every smile,",
    "every memory...",
    "",
    "was always leading back",
    "to you, {name}.",
    "",
    "You are my celebration.",
]

SECRET_CLOSING = "Happy anniversary, my love."

#: Typing any of these at the main menu opens the secret.
SECRET_TRIGGERS = ["143", "vasanth", "secret", "love"]


# ---------------------------------------------------------------------------
# 12. EXIT
# ---------------------------------------------------------------------------

EXIT_STEPS = [
    "Closing anniversary.exe...",
    "Saving our memories...",
]

EXIT_MESSAGE = [
    "Before you go...",
    "",
    "Remember this always:",
    "",
    "You are loved more each year,",
    "and celebrated today most of all.",
    "",
    "Happy anniversary, {name}.",
    "",
    "Until our next year together...",
]

EXIT_FINAL = [
    "Anniversary closed.",
    "",
    "But our love story continues.",
]


# ---------------------------------------------------------------------------
# 13. MENU
#     (key, label, handler-name). Reorder or rename labels freely; the
#     handler names are wired up in cli.py.
# ---------------------------------------------------------------------------

MENU_TITLE = "OUR ANNIVERSARY MENU"

MENU_ITEMS = [
    ("1", "Our Anniversary Letter", "message"),
    ("2", "Why {name}, Always", "reasons"),
    ("3", "Love.exe", "love_exe"),
    ("4", "Our Memory Lane", "memories"),
    ("5", "Sweet Anniversary Notes", "random_love"),
    ("6", "My Anniversary Wish", "question"),
    ("7", "Secret", "secret"),
    ("8", "Exit", "exit"),
]

MENU_HINT = "Choose a number, then press Enter."

INVALID_CHOICE = "That isn't one of the options. Try again."

CONTINUE_HINT = "Press Enter to continue"


def fmt(text):
    """Substitute {name} / {tagline} into a line or a list of lines."""
    values = {"name": NAME, "tagline": TAGLINE}
    if isinstance(text, (list, tuple)):
        return [fmt(item) for item in text]
    return text.format(**values)
