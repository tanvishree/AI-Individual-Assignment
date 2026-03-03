"""
CAPTCHA System
==============
AI Programming Assignment 1

CAPTCHA = Completely Automated Public Turing test to tell Computers and Humans Apart
Generates challenges that are easy for humans but hard for bots.

Architecture:
    Server generates challenge → User responds → Server verifies → Allow or Block
"""

import random
import time
import hashlib

# ── CAPTCHA Generator ─────────────────────────────────────────────────────────

class CaptchaGenerator:
    """Generates different types of CAPTCHA challenges."""

    def math_captcha(self):
        """Simple arithmetic challenge."""
        a  = random.randint(1, 20)
        b  = random.randint(1, 20)
        op = random.choice(["+", "-", "*"])
        answer    = str(eval(f"{a}{op}{b}"))
        challenge = f"Solve: {a} {op} {b} = ?"
        return challenge, answer

    def logic_captcha(self):
        """Common knowledge question."""
        questions = [
            ("What comes after Tuesday?",             "wednesday"),
            ("How many days in a week?",               "7"),
            ("What color is the sky on a clear day?",  "blue"),
            ("How many months in a year?",             "12"),
            ("Which month comes after January?",       "february"),
        ]
        challenge, answer = random.choice(questions)
        return challenge, answer

    def text_captcha(self):
        """Distorted text — user must retype the characters."""
        chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        text  = "".join(random.choices(chars, k=5))
        challenge = f"Type the characters (ignore spaces): [ {' '.join(list(text))} ]"
        return challenge, text


# ── CAPTCHA Verifier ──────────────────────────────────────────────────────────

class CaptchaVerifier:
    """Checks whether the user's answer matches the correct answer."""

    def verify(self, user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.strip().lower()


# ── CAPTCHA Session ───────────────────────────────────────────────────────────

class CaptchaSession:
    """Manages a CAPTCHA session with a token and expiry time."""

    def __init__(self, challenge, answer, expiry_seconds=60):
        self.challenge  = challenge
        self.answer     = answer
        self.token      = hashlib.md5(f"{challenge}{time.time()}".encode()).hexdigest()[:8].upper()
        self.created_at = time.time()
        self.expiry     = expiry_seconds

    def is_expired(self):
        return (time.time() - self.created_at) > self.expiry


# ── Demo ──────────────────────────────────────────────────────────────────────

def run_captcha_demo():
    print("\n" + "="*60)
    print("  CAPTCHA SYSTEM DEMO")
    print("="*60)
    print("  Bots fail. Humans pass.\n")

    gen      = CaptchaGenerator()
    verifier = CaptchaVerifier()

    captcha_types = [
        ("Math CAPTCHA",   gen.math_captcha()),
        ("Logic CAPTCHA",  gen.logic_captcha()),
        ("Text CAPTCHA",   gen.text_captcha()),
    ]

    for name, (challenge, answer) in captcha_types:
        session = CaptchaSession(challenge, answer)

        print(f"  Type      : {name}")
        print(f"  Token     : {session.token}")
        print(f"  Challenge : {challenge}")
        print(f"  Answer    : {answer}")

        # Bot gives a random/wrong answer
        bot_answer   = "???"
        # Human gives the correct answer
        human_answer = answer

        bot_result   = "PASS ✓" if verifier.verify(bot_answer,   answer) else "FAIL ✗"
        human_result = "PASS ✓" if verifier.verify(human_answer, answer) else "FAIL ✗"

        print(f"  Bot   answered '{bot_answer}'    → {bot_result}")
        print(f"  Human answered '{human_answer}' → {human_result}")
        print(f"  Session expired: {session.is_expired()}")
        print(f"  {'-'*56}")

    print("\n  Conclusion:")
    print("  Bots cannot solve the challenges → blocked.")
    print("  Humans answer correctly → allowed through.")
    print("="*60)


if __name__ == "__main__":
    run_captcha_demo()
