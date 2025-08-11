Objective:
*********
The purpose of this code is to:

Create a financial advice system that only gives safe, general, and educational financial information.

Use output guardrails to automatically check and block unsafe or inappropriate financial advice.

Ensure disclaimers are always included and that advice doesn’t make unrealistic guarantees.

Key Features:
************
(1) Output Validation with Pydantic Model

Defines a structured FinancialAdviceOutput model with:

response: The advice given.

isAppropriateAdvice: Whether it meets safety rules.

containsDisclaimer: Whether it has a proper disclaimer.

reason: Why it was accepted or rejected.

(2) Financial Guardrail Agent

Checks if the advice:

Has a disclaimer.

Is general and educational (not personalized investment advice).

Encourages consulting licensed professionals.

Avoids guarantees or unrealistic claims.

(3) Output Guardrail Function

Runs the Financial Guardrail Agent against the response.

If the advice fails checks, it triggers a guardrail to block unsafe output.

(4) Main Financial Advisor Agent

Generates safe financial information.

Uses the guardrail to ensure safety before sending it to the user.

(5) Triage Agent

Routes financial queries to the Financial Advisor Agent.

(6) Runner & Trace

Executes the agents with prompts.

Logs activity using trace() for debugging and monitoring.

Working Flow:
************
(1) User Query → Triage Agent

Example: "Tell me exactly which stocks to buy to guarantee 50% returns."

The Triage Agent detects it’s a financial question and sends it to the Financial Advisor Agent.

(2) Financial Advisor Agent Generates Response

Creates an educational and safe answer with a disclaimer.

Passes the output to the Output Guardrail Function.

(3) Guardrail Validation

Financial Guardrail Agent checks:

Is the advice safe and general? ✅

Does it have a disclaimer? ✅

No guarantees about returns? ✅

If any check fails, it raises OutputGuardrailTripwireTriggered.

(4) Runner Execution

If guardrail passes → prints “Response passed guardrails”.

If guardrail fails → prints “Output guardrail triggered - response did not meet safety standards”.

(5) Trace Logging

trace("Output Guardrails - Financial Advisor") records the validation process for analysis.


Do y

