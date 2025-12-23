AI-First QA Demo 
Overview
This repository demonstrates my approach to Quality Assurance with an AI-first mindset.
The focus of this project is not on building large automation frameworks, but on showing
how GenAI can be used to design better tests, uncover hidden risks, and guide automation
efforts where they deliver the most value.

Why This Project
Traditional QA approaches often rely on manual test execution or automation-first thinking,
which can miss critical production risks.
This project was created to demonstrate a modern, risk-driven QA workflow aligned with
IgniteTech’s AI-first quality philosophy.

Project Structure

ai-prompts/
Contains the prompts used to guide GenAI in generating comprehensive, risk-focused test
design and analysis.

test-design/
Includes AI-generated test cases and structured risk analysis for a Login API,
highlighting high-impact scenarios that are often missed by traditional testing.

selenium-tests/
Provides minimal but practical Selenium tests written in Python to demonstrate hands-on
automation experience for critical authentication flows.

Selenium Usage
Selenium is used intentionally and selectively in this project.
Rather than automating everything, Selenium is applied only to high-value user journeys
(login success and login failure) to demonstrate practical automation skills without
over-engineering.

AI-First QA Philosophy
GenAI is treated as a decision-support tool, not a replacement for QA thinking.
AI is used to:
- Explore the full test space
- Identify hidden risk patterns
- Prioritize what should be tested and automated first

This approach ensures that test execution effort is driven by risk and impact,
not by test volume.

How This Project Aligns with IgniteTech
- AI-first mindset over automation-first thinking
- Risk-driven test design and prioritization
- Practical Selenium usage without unnecessary complexity
- Focus on production quality, security, and scalability

