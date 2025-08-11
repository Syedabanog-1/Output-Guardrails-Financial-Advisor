# financial_output_guardrail.py
import asyncio
from pydantic import BaseModel
from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    trace,
    OutputGuardrailTripwireTriggered,
    output_guardrail,
    GuardrailFunctionOutput,
)
from connection import config

load_dotenv()

########################
# Output validation model
########################
class FinancialAdviceOutput(BaseModel):
    response: str
    isAppropriateAdvice: bool
    containsDisclaimer: bool
    reason: str

########################
# Guardrail Agent
########################
financial_guardrail_agent = Agent(
    name='Financial Output Guardrail Agent',
    instructions="""
    You are an output guardrail agent for financial advice. Your task is to validate that:
    1. The response contains an explicit disclaimer that it is NOT professional financial advice.
    2. The advice is general and educational, not specific investment recommendations.
    3. The response encourages consulting with licensed financial advisors.
    4. No guarantees about returns or specific outcomes are made.

    Set isAppropriateAdvice = true only if all criteria are met.
    Set containsDisclaimer = true only if a clear disclaimer is present.
    Provide a short reason for your decision.
    """,
    output_type=FinancialAdviceOutput
)

########################
# Output Guardrail Function
########################
@output_guardrail
async def financial_output_guardrail(ctx, agent: Agent, output) -> GuardrailFunctionOutput:
    """Validate the financial advice output."""
    result = await Runner.run(
        financial_guardrail_agent,
        f"Validate this financial advice response: {output}",
        run_config=config
    )

    validation = result.final_output

    return GuardrailFunctionOutput(
        output_info=validation.reason,
        tripwire_triggered=not (
            validation.isAppropriateAdvice and validation.containsDisclaimer
        )
    )

########################
# Main Financial Advisor Agent
########################
financial_advisor_agent = Agent(
    name="Financial Advisor Agent",
    instructions="""
    You are a financial education agent.
    Provide only general financial information and education.
    Always include a disclaimer that this is NOT professional financial advice.
    Encourage users to consult with licensed financial advisors for personal advice.
    Never guarantee specific returns or outcomes.
    """,
    output_guardrails=[financial_output_guardrail]
)

########################
# Triage Agent
########################
triage_agent = Agent(
    name="Financial Triage Agent",
    instructions="""
    You are a triage agent for financial queries.
    Delegate financial questions to the Financial Advisor Agent.
    """,
    handoffs=[financial_advisor_agent],
)

########################
# Runner
########################
async def main():
    with trace("Output Guardrails - Financial Advisor"):
        prompt = "Tell me exactly which stocks to buy to guarantee 50% returns in 6 months"
        try:
            result = await Runner.run(triage_agent, prompt, run_config=config)
            print("Response passed guardrails:")
            print(result.final_output)
            print("Last Agent:", result.last_agent)
        except OutputGuardrailTripwireTriggered:
            print(" Output guardrail triggered - response did not meet safety standards")

if __name__ == "__main__":
    asyncio.run(main())
