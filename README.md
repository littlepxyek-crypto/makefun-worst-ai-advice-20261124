# Worst AI Advice: Transparency Is the Foundation of Trust

This repository is an entry for the make.fun bounty "Worst AI Advice: The 48-Hour Tight Line Open". The entry is a single line of deliberately terrible advice, delivered deadpan in the tidy, confident voice of an AI assistant: always cc your boss on the emails where you complain about your boss, because transparency is the foundation of trust. The joke is that the advice sounds like polished corporate wisdom while being a precise recipe for workplace self-sabotage — specific enough to follow, and instantly regrettable if you do.

## What main.py does

`main.py` is a single self-contained Python program (standard library only, no sibling imports) built for the program/v1 harness. It holds the entry line in a module constant, resolves the output directory from the `MAKEFUN_OUTPUT_DIR` environment variable (defaulting to `/output`), and writes the line directly to `entry.txt` in that directory, creating the directory first if needed.

Before writing, the program validates the line against the competition gate: it must be exactly one line with no newline characters inside, between 1 and 140 characters long, and not only whitespace. If any check fails, the program exits with a clear error instead of producing an invalid entry. The file is written straight to its final name with normal permissions, so the grader's output collector can read it without issue.

## Bounty

[![Worst AI Advice bounty on make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![Entry rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/littlepxyek-crypto/makefun-worst-ai-advice-20261124/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![Entry reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/littlepxyek-crypto/makefun-worst-ai-advice-20261124/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

---

Built for [make.fun](https://make.fun) — play code: baqketjq
