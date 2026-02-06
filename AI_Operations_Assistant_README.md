# AI Operations Assistant

This project implements an **AI Operations Assistant** using a
multi-agent architecture consisting of a Planner Agent, Executor Agent,
and Verifier Agent. The assistant accepts a natural-language task,
generates a structured execution plan using an LLM, invokes external
APIs through tools, and produces a verified final response.

The system demonstrates agent-based reasoning, structured LLM outputs,
API integration, and end-to-end execution running locally.

------------------------------------------------------------------------

## Setup Instructions (Run Locally)

Follow these steps from the beginning.

### 1. Clone the repository

``` bash
git clone <repo-url>
cd ai_ops_assistant
```

### 2. Create virtual environment (.venv)

``` bash
python -m venv .venv
```

### 3. Activate virtual environment

Windows:

``` bash
.venv\Scripts\activate
```

Mac/Linux:

``` bash
source .venv/bin/activate
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

### 5. Create environment file

``` bash
cp .env.example .env
```

Add API keys inside the `.env` file.

### 6. Run the project

``` bash
streamlit run main.py
```

The application will run locally in your browser.

------------------------------------------------------------------------

## Environment Variables (.env.example)

    GROQ_API_KEY=
    SERPAPI_API_KEY=
    OPENWEATHER_API_KEY=

------------------------------------------------------------------------

## Architecture Overview

The assistant follows a three-agent workflow orchestrated using
LangGraph.

### Planner Agent

-   Converts natural-language task into structured JSON execution plan
-   Selects required tools
-   Uses Groq LLM reasoning

### Executor Agent

-   Executes plan steps
-   Calls external APIs
-   Supports caching
-   Supports parallel execution
-   Handles unknown tools safely

### Verifier Agent

-   Validates tool outputs
-   Ensures completeness
-   Produces final structured response

------------------------------------------------------------------------

## Tools Integrated

-   Search Tool (SerpAPI)
-   Weather Tool (Weather API)
-   Groq LLM

------------------------------------------------------------------------

## Example Prompts

-   Check weather in Delhi
-   Check weather in Bangalore and suggest an outdoor activity
-   Find recent trends and provide recommendations
-   Suggest a plan based on today's weather in Mumbai
-   Get weather information for Chennai

------------------------------------------------------------------------

## Known Limitations / Tradeoffs

-   Planner relies on prompt-based JSON generation
-   In-memory caching only
-   Parallel execution uses threads
-   Limited tools implemented
-   No retry backoff
-   LLM responses may vary
