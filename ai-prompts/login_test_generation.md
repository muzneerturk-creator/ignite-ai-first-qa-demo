AI-First Login API Test Design Prompt

You are acting as a Senior QA Engineer with an AI-first mindset.

Analyze the following system and generate a comprehensive test design.

System Description:
- A REST-based Login API
- Endpoint: POST /login
- Request fields:
  - email (string)
  - password (string)
- Successful response:
  - HTTP 200
  - auth_token (string)
  - token_expiry (timestamp)
- Failed responses may include:
  - HTTP 400 (validation errors)
  - HTTP 401 (authentication failure)
  - HTTP 429 (rate limiting)

Tasks:
1. Generate detailed test cases covering:
   - Positive scenarios
   - Negative scenarios
   - Boundary and edge cases
   - Security-focused scenarios
   - Stress and abuse scenarios
2. Clearly describe the intent of each test case.
3. Identify areas that are most likely to produce production defects.
4. Highlight which scenarios are high-risk and should be prioritized during testing.

Focus on quality risks that traditional QA approaches often miss.
Avoid UI-level assumptions; focus on API behavior and system robustness.
