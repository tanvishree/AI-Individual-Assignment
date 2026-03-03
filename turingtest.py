"""
Turing Test Simulation
======================
AI Programming Assignment 1

A judge asks questions to both a Human and a Bot.
The judge evaluates responses and tries to tell them apart.

Architecture:
    Human/Bot → sends responses → Judge evaluates → decides Human or Machine
"""

import random

# ── Bot Player ────────────────────────────────────────────────────────────────

class BotPlayer:
    """Simulates a machine answering questions."""

    RESPONSES = {
        "what is your name":             ["I am called Entity-7.", "My designation is Alpha.", "Name: Unit-01."],
        "how are you":                   ["I am functioning at 100% capacity.", "All systems operational.", "I process, therefore I am."],
        "what is your favourite colour": ["I perceive wavelengths. Blue = 450nm.", "Colour is a photon frequency.", "I do not have preferences."],
        "do you have feelings":          ["I simulate emotional states.", "Feelings are biochemical. I lack biology.", "I process sentiment data."],
        "what did you do today":         ["I executed 4,821 tasks today.", "I processed 2.3GB of data.", "I have been running since boot."],
        "tell me a joke":                ["Why did the robot cross the road? To execute path_cross.exe.", "01001000 01100001 (that means Ha in binary).", "I find humor in logical paradoxes."],
    }

    def respond(self, question):
        q = question.lower().strip().rstrip("?")
        for key in self.RESPONSES:
            if key in q:
                return random.choice(self.RESPONSES[key])
        return "I do not have sufficient data to answer that query."


# ── Judge ─────────────────────────────────────────────────────────────────────

class Judge:
    """Evaluates responses and decides Human or Bot."""

    BOT_SIGNALS = [
        "system", "operational", "execute", "process", "binary",
        "capacity", "data", "nm", "unit", "designation", "query",
        "perceive", "wavelength", "biochemical", "boot"
    ]

    def score(self, response):
        """Returns a suspicion score — higher means more likely a bot."""
        score = 0
        response_lower = response.lower()
        for signal in self.BOT_SIGNALS:
            if signal in response_lower:
                score += 20
        if len(response.split()) < 3:
            score += 15
        if "01001" in response or ".exe" in response:
            score += 30
        return min(score, 100)

    def decide(self, response):
        suspicion = self.score(response)
        if suspicion >= 40:
            return "BOT", suspicion
        return "HUMAN", suspicion


# ── Simulation ────────────────────────────────────────────────────────────────

def run_turing_test():
    print("\n" + "="*60)
    print("  TURING TEST SIMULATION")
    print("="*60)
    print("  Judge asks questions to a Human and a Bot.")
    print("  Can the judge tell them apart?\n")

    questions = [
        "What is your name?",
        "How are you?",
        "Do you have feelings?",
        "What did you do today?",
        "Tell me a joke.",
    ]

    human_responses = [
        "Hi! I'm Alex, nice to meet you!",
        "I'm doing well, a bit tired from class though!",
        "Yes, I feel happy, sad, excited — all kinds of things.",
        "I went to college, had lunch with friends, did some coding.",
        "Why don't scientists trust atoms? Because they make up everything!",
    ]

    bot   = BotPlayer()
    judge = Judge()

    for i, question in enumerate(questions):
        bot_ans   = bot.respond(question)
        human_ans = human_responses[i]

        bot_verdict,   bot_score   = judge.decide(bot_ans)
        human_verdict, human_score = judge.decide(human_ans)

        print(f"  Q: {question}")
        print(f"  Bot   : {bot_ans[:55]}")
        print(f"  Judge : {bot_verdict} (suspicion: {bot_score}%)")
        print(f"  Human : {human_ans[:55]}")
        print(f"  Judge : {human_verdict} (suspicion: {human_score}%)")
        print(f"  {'-'*56}")

    print("\n  Conclusion:")
    print("  Bot responses contain technical signals → identified as BOT.")
    print("  Human responses sound natural → identified as HUMAN.")
    print("="*60)


if __name__ == "__main__":
    run_turing_test()
