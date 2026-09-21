# Student Monthly Expense Assistant

## 1. Scenario

The scenario chosen for this project is a Student Monthly Expense Assistant. The assistant works with a small set of private student financial data. The monthly allowance is ₹5,000. The student's monthly expenses are ₹2,000 for food, ₹800 for travel, ₹700 for study materials, and ₹300 for other expenses. The total monthly expense is ₹3,800, leaving a balance of ₹1,200.

The same scenario is used to compare three different approaches: a plain chatbot, a rule-based workflow, and an AI agent. This helps demonstrate the differences between a simple LLM response, a predefined workflow, and an agent that can use tools and make decisions.

## 2. Plain Chatbot

The plain chatbot mainly uses an LLM to understand the user's question and generate a response. In this project, the chatbot does not have access to the student's private expense data. It only receives the user's question and provides general budgeting advice.

For example, when asked how a student can plan a monthly budget, the chatbot gives suggestions about tracking income, categorising expenses, setting a budget, and reviewing spending. However, it cannot directly calculate the student's actual remaining balance because the private expense data is not provided to it.

The plain chatbot is simple and flexible for general questions. It is useful when the user needs explanations, suggestions, or general information. However, it is limited when the task requires access to private data or exact calculations based on stored information.

## 3. Rule-Based Workflow

The rule-based workflow follows predefined instructions and conditions. It does not use an LLM to make decisions.

In this project, the workflow reads the student's monthly allowance and expense values from the configuration file. It calculates the total expenses and remaining balance using predefined calculations. It then checks a condition to determine whether the student is within the budget.

For the selected scenario, the monthly allowance is ₹5,000 and the total expenses are ₹3,800. Therefore, the remaining balance is ₹1,200. Since the remaining balance is greater than ₹1,000, the workflow displays the status as "Within budget."

The rule-based workflow is reliable for fixed and predictable tasks because the same input and rules produce the same result. However, it is less flexible when users ask unexpected questions or when the task requires different reasoning paths.

## 4. AI Agent

The AI agent combines an LLM with tools and a process for handling the user's request. In this project, the agent can access the student's private expense information through functions defined in `tools.py`.

The tools provide the student data, calculate the total expenses, and calculate the remaining balance. The LLM then uses the available information to answer the user's question.

For example, when the user asks, "How much money is left after all expenses?", the agent uses the expense information and returns ₹1,200. Unlike the plain chatbot, the agent can work with the private data available through its tools.

The AI agent is more flexible because it can understand natural-language questions and use available information to provide an answer. It is especially useful for tasks that require private data, multiple calculations, or different types of user requests.

## 5. Comparison

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for general conversation | Low | High |
| Decision-making | Mainly generates responses | Uses fixed conditions | Uses LLM reasoning with available tools |
| Tool usage | No tools in this project | No external tools | Uses expense-data tools |
| Private-data access | No | Yes | Yes |
| Multi-step task handling | Limited | Fixed predefined steps | Can handle varied tasks using tools |
| Automation | Low | High for fixed tasks | High |
| Reliability | Depends on LLM response | High for fixed rules | Depends on both tools and LLM |

## 6. Suitability Analysis

The plain chatbot is suitable when the user only needs general budgeting guidance. It is easy to implement and can answer many natural-language questions, but it cannot directly work with the student's private expense data in this project.

The rule-based workflow is suitable for predictable calculations and fixed decisions. For example, calculating total expenses and remaining balance is simple and reliable using predefined rules. However, adding many new types of questions would require additional rules and code.

The AI agent is suitable when the user wants to ask different questions about private expense data using natural language. Since the agent can access tools, it can retrieve data and perform calculations before generating an answer. This makes it useful for more flexible and multi-step tasks.

For this particular scenario, the AI agent is suitable when the goal is to build a flexible assistant that can work with private data and respond to varied user requests. The rule-based workflow remains useful for simple fixed calculations, while the plain chatbot is useful for general budgeting advice.

## 7. Conclusion

This project demonstrates the difference between a plain chatbot, a rule-based workflow, and an AI agent using the same student expense scenario.

A plain chatbot is mainly focused on generating responses from the user's question. A rule-based workflow follows predefined steps and conditions, making it reliable for fixed tasks. An AI agent combines an LLM with tools so that it can access information and perform actions before producing a response.

The comparison shows that there is no single approach for every situation. Plain chatbots are useful for general conversations and explanations. Rule-based workflows are useful for predictable and structured tasks. AI agents are useful when tasks require flexibility, private-data access, tool usage, and multiple steps.

Therefore, the choice of approach should depend on the requirements of the application, the type of data involved, and how flexible the user's requests need to be.