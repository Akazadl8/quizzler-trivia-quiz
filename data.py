import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

# Used when the Open Trivia DB can't be reached (no internet, rate limit, etc.)
FALLBACK_QUESTIONS = [
    {"question": "The HTML5 standard was published in 2014.", "correct_answer": "True"},
    {"question": "The first computer bug was formed by faulty wires.", "correct_answer": "False"},
    {"question": "FLAC stands for 'Free Lossless Audio Condenser'.", "correct_answer": "False"},
    {"question": "All program codes have to be compiled into an executable file in order to be run. "
                 "This file can then be executed on any machine.", "correct_answer": "False"},
    {"question": "Linus Torvalds created Linux and Git.", "correct_answer": "True"},
    {"question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
     "correct_answer": "False"},
    {"question": "AMD created the first consumer 64-bit processor.", "correct_answer": "True"},
    {"question": "'HTML' stands for Hypertext Markup Language.", "correct_answer": "True"},
    {"question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
     "correct_answer": "True"},
    {"question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
     "correct_answer": "False"},
]


def get_questions():
    """Fetch 10 random True/False questions, or fall back to the built-in set."""
    try:
        response = requests.get(url="https://opentdb.com/api.php", params=parameters, timeout=10)
        response.raise_for_status()
        results = response.json().get("results", [])
        if results:
            return results
    except (requests.RequestException, ValueError):
        pass
    print("Couldn't reach the Open Trivia DB - using the built-in questions instead.")
    return FALLBACK_QUESTIONS


question_data = get_questions()
