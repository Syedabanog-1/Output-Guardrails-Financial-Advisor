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



https://github.com/user-attachments/assets/62c4990b-2133-49af-9cce-aa0b0bf545bf



https://github.com/user-attachments/assets/94cbd340-3856-44fb-b49c-687030320530


<img width="1617" height="915" alt="response" src="https://github.com/user-attachments/assets/1edc1d04-5582-47cb-bad8-9fd8093d2053" />

<img width="1609" height="904" alt="FinancialGuardrails-LOG" src="https://github.com/user-attachments/assets/5c5581c0-681f-4a1b-bb2a-4b338fef705f" />
<img width="1610" height="908" alt="financialAdv-Log" src="https://github.com/user-attachments/assets/f4d7f26b-cb0d-484c-86fb-718ddd3fbf4f" />
<img width="1611" height="907" alt="FinanciaAdv_OutPut-Triggered-False" src="https://github.com/user-attachments/assets/260b0b5e-30af-494c-b399-f3bbbca48395" />
<img width="1611" height="905" alt="FinancialAdv_CodeOutPut-" src="https://github.com/user-attachments/assets/6cf2fce7-bce6-4484-938f-deaa24b87e5d" />



