# Student Monthly Expense Assistant

## Overview

This project compares three different approaches for handling a student's monthly expense scenario:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The project demonstrates how each approach handles private student expense data, decision-making, tool usage, and multi-step tasks.

## Scenario

The project uses a student's monthly expense data:

* Monthly Allowance: ₹5000
* Food: ₹2000
* Travel: ₹800
* Study Materials: ₹700
* Other Expenses: ₹300
* Total Expenses: ₹3800
* Remaining Balance: ₹1200

## Approaches

### Plain Chatbot

The plain chatbot uses an LLM to answer general student budgeting questions. It does not have access to the student's private expense data.

### Rule-Based Workflow

The rule-based workflow uses predefined calculations and conditions to calculate total expenses, remaining balance, and budget status.

### AI Agent

The AI agent combines an LLM with tools that provide access to the student's private expense data. It can use the available data to answer expense-related questions.

## Project Files

* `chatbot.py` — Plain chatbot
* `workflow.py` — Rule-based workflow
* `tools.py` — Tools for accessing expense data
* `agent.py` — AI agent
* `challenge.py` — Runs all three approaches
* `config.py` — Configuration and student data
* `analysis.md` — Detailed comparison and suitability analysis
* `output/` — Screenshots of the three outputs

## Technologies Used

* Python
* OpenAI Python SDK
* Groq API
* Python-dotenv
* Git and GitHub

## Conclusion

This project demonstrates the differences between a plain chatbot, a rule-based workflow, and an AI agent using a student monthly expense scenario. It shows how private data and tools can make an AI agent more useful for task-specific applications.
