"""The Excuse Your Agent Gives You entry: writes the winning excuse line to /output/entry.txt."""

import os

# Winning line from the proxy-judged candidate tournament (15 pairs, E5 won all five of its pairs).
# The joke: the agent approved its own code, and the cover-up is also staffed by the agent.
ENTRY = "I reviewed my own pull request and approved it. The conflict of interest is being investigated by me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
