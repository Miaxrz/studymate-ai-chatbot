# StudyMate AI

## AI-Powered Educational Tutor Chatbot

**Project Type:** Artificial Intelligence / Chatbot Development
**Programming Language:** Python
**AI Platform:** OpenRouter
**Frontend Framework:** Streamlit
**AI Model Access:** OpenRouter Free Model Router
**Development Environment:** Visual Studio Code
**Deployment Platform:** Streamlit Community Cloud

---

# 1. Introduction

StudyMate AI is an AI-powered educational chatbot designed to assist students with academic and technical questions. The chatbot uses a large language model accessed through the OpenRouter API to understand user questions and generate relevant responses.

The application provides a conversational interface where users can ask questions, receive explanations, request examples, and ask follow-up questions. Conversation history is maintained during the session so that the chatbot can understand the context of previous questions.

The application was developed using Python and Streamlit. OpenRouter was selected as the AI integration platform because it provides access to AI models through an API and offers free-model access suitable for development and testing.

---

# 2. Project Objectives

The main objectives of the StudyMate AI project are:

1. Develop a practical AI-powered chatbot.
2. Provide students with explanations of academic and technical concepts.
3. Integrate an external AI model through an API.
4. Implement prompt engineering to control chatbot behaviour.
5. Maintain conversation history for contextual responses.
6. Create an interactive web-based frontend.
7. Test the chatbot for accuracy, usability, conversation quality, and performance.
8. Deploy the chatbot so that it can be accessed through a public URL.

---

# 3. Step 1 — Define Chatbot Purpose

## 3.1 Use Case

The selected use case for this project is an **Educational Tutor Chatbot**.

The chatbot is called **StudyMate AI** and is designed to support students when learning academic and technical subjects.

## 3.2 Purpose

The main purpose of StudyMate AI is to provide students with quick, understandable, and interactive explanations.

The chatbot can:

* Answer academic questions.
* Explain technical concepts.
* Provide simple examples.
* Explain programming concepts.
* Answer follow-up questions.
* Maintain conversation context.
* Break complex topics into smaller steps.

## 3.3 Target Users

The primary users are:

* College and university students.
* Computing students.
* Data analytics students.
* Beginners learning programming.
* Students learning artificial intelligence and machine learning.

## 3.4 Example Interaction

A user can ask:

**User:**

"What is supervised learning?"

**StudyMate AI:**

The chatbot provides an explanation of supervised learning.

The user can then ask:

"Can you give me a real-world example?"

The chatbot uses the previous conversation to understand that the user is asking for an example of supervised learning.

This demonstrates the conversational nature of the application.

---

# 4. Step 2 — AI Model Integration

## 4.1 Selected Technology

OpenRouter was selected as the AI integration platform.

The application communicates with OpenRouter through an API using Python. OpenRouter provides an OpenAI-compatible API interface, allowing the Python OpenAI library to communicate with the service.

The application currently uses:

```python
model="openrouter/free"
```

This allows OpenRouter to route requests to an available free model.

## 4.2 Why OpenRouter Was Selected

OpenRouter was selected because:

* It provides API access to AI models.
* It supports an OpenAI-compatible API format.
* It provides access to free models.
* It can be integrated with Python.
* It is suitable for an educational prototype.
* It avoids depending on a single AI model provider.

## 4.3 API Integration

The following code establishes the connection:

```python
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
```

The `base_url` directs API requests to OpenRouter rather than the default OpenAI API endpoint.

The API key is stored separately in a `.env` file rather than directly in the source code.

## 4.4 API Key Security

The API key is stored in:

```text
.env
```

The `.env` file contains:

```text
OPENROUTER_API_KEY=your_actual_api_key
```

The Python application loads the key using:

```python
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
```

The `.env` file is excluded from Git using `.gitignore`.

This prevents the API key from being accidentally uploaded to the GitHub repository.

---

# 5. Step 3 — Backend Development

The backend is responsible for processing user queries, preparing prompts, communicating with the AI model, generating responses, and managing conversation history.

## 5.1 Query Processing

The chatbot receives user input through the Streamlit chat interface:

```python
prompt = st.chat_input(
    "Ask me a question..."
)
```

When the user submits a question, the application checks whether a prompt has been provided:

```python
if prompt:
```

The question is then stored in the conversation history.

---

## 5.2 Prompt Engineering

Prompt engineering is used to define the chatbot's role and behaviour.

The application uses a system instruction:

```python
system_instruction = """
You are StudyMate AI, an educational tutor.

Your purpose is to help students understand
academic and technical concepts.

Follow these rules:

1. Explain concepts using simple and clear language.
2. Provide examples when useful.
3. Break difficult topics into smaller steps.
4. Avoid unnecessary technical jargon.
5. Use previous conversation context when answering
   follow-up questions.
6. Give accurate and relevant answers.
7. If you are uncertain, say so instead of making
   up information.
8. Keep answers focused on the student's question.
9. For programming questions, provide simple examples
   suitable for beginners.
"""
```

This prompt helps ensure that the chatbot behaves as an educational tutor rather than a general-purpose conversational system.

The prompt specifies:

* The chatbot's role.
* The target audience.
* The expected communication style.
* The desired level of explanation.
* How follow-up questions should be handled.
* How uncertainty should be handled.

---

## 5.3 Conversation History Management

Conversation history is implemented using Streamlit session state.

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

The user's message is stored as:

```python
st.session_state.messages.append(
    {
        "role": "user",
        "content": prompt
    }
)
```

The AI response is stored as:

```python
st.session_state.messages.append(
    {
        "role": "assistant",
        "content": answer
    }
)
```

The previous conversation is then included when generating the next response:

```python
messages = [
    {
        "role": "system",
        "content": system_instruction
    }
]

messages.extend(
    st.session_state.messages
)
```

This allows the AI model to receive the previous conversation and answer follow-up questions with greater context.

---

## 5.4 Response Generation

The chatbot sends the prepared messages to OpenRouter:

```python
response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages
)
```

The generated response is extracted using:

```python
answer = response.choices[0].message.content
```

The response is then displayed to the user.

---

## 5.5 Error Handling

The API request is placed inside a `try` block:

```python
try:
    ...
```

If an error occurs, the application displays a user-friendly message:

```python
except Exception as e:

    st.error(
        "Sorry, I was unable to generate a response. "
        "Please try again."
    )
```

This prevents the application from simply displaying an unhandled Python error to the user.

---

# 6. Step 4 — Frontend Development

## 6.1 Selected Framework

Streamlit was selected for the frontend.

Streamlit allows Python developers to create interactive web applications without requiring extensive HTML, CSS, or JavaScript development.

## 6.2 Interface Design

The application includes:

* Application title.
* Description.
* Chat input.
* User messages.
* AI responses.
* Sidebar.
* About section.
* Feature list.
* Clear Conversation button.
* Loading indicator.

The main title is created using:

```python
st.title("StudyMate AI")
```

The chatbot input is created using:

```python
st.chat_input(
    "Ask me a question..."
)
```

Chat messages are displayed using:

```python
st.chat_message()
```

## 6.3 Clear Conversation Feature

The application provides a button that allows the user to clear the current conversation:

```python
if st.button("Clear Conversation"):

    st.session_state.messages = []

    st.rerun()
```

This resets the conversation history and allows the user to begin a new session.

---

# 7. System Architecture

The overall system architecture is:

```text
                    User
                     |
                     v
            +------------------+
            | Streamlit        |
            | Frontend         |
            +--------+---------+
                     |
                     v
            +------------------+
            | User Query       |
            | Processing       |
            +--------+---------+
                     |
                     v
            +------------------+
            | Prompt           |
            | Engineering      |
            +--------+---------+
                     |
                     v
            +------------------+
            | Conversation     |
            | History          |
            +--------+---------+
                     |
                     v
            +------------------+
            | OpenRouter API   |
            +--------+---------+
                     |
                     v
            +------------------+
            | AI Model         |
            +--------+---------+
                     |
                     v
            +------------------+
            | Generated        |
            | Response         |
            +--------+---------+
                     |
                     v
            +------------------+
            | Streamlit        |
            | Interface        |
            +------------------+
```

---

# 8. Step 5 — Deployment

After local development and testing, the chatbot can be deployed using Streamlit Community Cloud.

## 8.1 Project Structure

The project uses the following structure:

```text
studymate-ai/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

The `.env` file is used during local development and should not be uploaded to GitHub.

## 8.2 Requirements File

The project uses the following dependencies:

```text
streamlit
openai
python-dotenv
```

The `requirements.txt` file allows the deployment environment to install the required Python packages.

## 8.3 Deployment Process

The deployment process consists of:

1. Create a GitHub repository.
2. Add `app.py`.
3. Add `requirements.txt`.
4. Add `.gitignore`.
5. Ensure `.env` is not uploaded.
6. Connect the repository to Streamlit Community Cloud.
7. Configure the OpenRouter API key using Streamlit secrets.
8. Deploy the application.
9. Test the public URL.

## 8.4 API Key During Deployment

The local `.env` file should not be used as the primary secret-management method in the deployed application.

Instead, the OpenRouter API key should be added through the deployment platform's secrets configuration.

The deployed application should retrieve the secret securely rather than exposing the key in the GitHub repository.

---

# 9. Step 6 — Testing and Optimization

Testing was performed to evaluate the chatbot's response accuracy, user experience, conversation quality, and system performance.

## 9.1 Testing Objectives

The testing process evaluates whether:

* The chatbot generates relevant responses.
* The chatbot maintains conversation context.
* The interface is easy to use.
* The chatbot handles multiple questions.
* The Clear Conversation feature works.
* API errors are handled appropriately.
* Response performance is acceptable.

---

# 10. Functional Testing

| Test ID | Test Case                          | Expected Result                 | Actual Result        | Status |
| ------- | ---------------------------------- | ------------------------------- | -------------------- | ------ |
| T01     | Ask "What is Python?"              | Provides a relevant explanation | Record actual result | Record |
| T02     | Ask "What is supervised learning?" | Provides a correct explanation  | Record actual result | Record |
| T03     | Ask a follow-up question           | Uses previous context           | Record actual result | Record |
| T04     | Request a programming example      | Provides an appropriate example | Record actual result | Record |
| T05     | Ask multiple questions             | Maintains conversation          | Record actual result | Record |
| T06     | Click Clear Conversation           | Removes conversation history    | Record actual result | Record |
| T07     | API request fails                  | Displays an error message       | Record actual result | Record |

The actual results should be completed after running the tests.

---

# 11. Response Accuracy Testing

The chatbot should be tested using questions for which the expected information is already known.

Example questions include:

### Test Question 1

"What is supervised learning?"

Expected behaviour:

The chatbot should explain that supervised learning uses labelled data to learn a relationship between inputs and known outputs.

### Test Question 2

"What is the difference between classification and regression?"

Expected behaviour:

The chatbot should explain that classification predicts categories/classes while regression predicts numerical or continuous values.

### Test Question 3

"What is a Python list?"

Expected behaviour:

The chatbot should explain that a Python list is an ordered, mutable collection that can contain multiple values.

The responses should be reviewed for correctness and relevance.

---

# 12. Conversation Quality Testing

Conversation quality was evaluated using multi-turn conversations.

Example:

**User:**
What is machine learning?

**Chatbot:**
Provides an explanation.

**User:**
What are its main types?

**Chatbot:**
Explains the main types of machine learning.

**User:**
Give me an example of the first type.

**Chatbot:**
Uses the previous conversation to determine what "the first type" refers to.

This test evaluates the chatbot's ability to maintain context between multiple messages.

---

# 13. User Experience Testing

The following areas should be evaluated:

| Area                       | Evaluation    |
| -------------------------- | ------------- |
| Interface clarity          | Record result |
| Input accessibility        | Record result |
| Response readability       | Record result |
| Conversation navigation    | Record result |
| Clear Conversation feature | Record result |
| Loading feedback           | Record result |

The `st.spinner()` feature provides visual feedback while the chatbot is waiting for the AI response.

---

# 14. System Performance Testing

Response time can be measured during testing.

For example:

| Test   |      Response Time |
| ------ | -----------------: |
| Test 1 | Record actual time |
| Test 2 | Record actual time |
| Test 3 | Record actual time |
| Test 4 | Record actual time |
| Test 5 | Record actual time |

The average response time can then be calculated:

```text
Average Response Time =
Total Response Time / Number of Tests
```

Actual measurements should be recorded during testing rather than estimated.

---

# 15. Optimization

Based on testing, possible improvements include:

* Improving prompt instructions.
* Improving response clarity.
* Adding additional error handling.
* Improving interface design.
* Monitoring API usage.
* Selecting a more suitable model if required.
* Adding more specialized educational features.
* Improving conversation history management.

The prompt can be adjusted based on observed response quality.

For example, if responses are too technical, the system instruction can be modified to explicitly request beginner-friendly explanations.

---

# 16. Security Considerations

API key security is an important part of the project.

The API key is not included directly in the Python source code.

Instead, it is stored in an environment variable:

```text
OPENROUTER_API_KEY
```

The `.env` file is excluded from version control through `.gitignore`.

The API key should never be:

* Published in GitHub.
* Included in screenshots.
* Shared with other users.
* Written directly into the application source code.

For deployment, the API key should be stored using the deployment platform's secrets management system.

---

# 17. Limitations

Although StudyMate AI provides useful educational assistance, it has several limitations.

### 17.1 AI Accuracy

AI-generated responses may occasionally contain incorrect or incomplete information. Students should verify important academic information using reliable sources.

### 17.2 Free Model Availability

The application relies on OpenRouter's free-model routing. Availability and rate limits can change.

### 17.3 Conversation Memory

Conversation history is maintained during the current application session. It is not intended to provide permanent user memory.

### 17.4 API Dependency

The chatbot requires an internet connection and access to the OpenRouter API.

### 17.5 Educational Scope

StudyMate AI is designed as a learning assistant rather than a replacement for teachers, textbooks, or formal academic resources.

---

# 18. Ethical and Responsible AI Considerations

The chatbot should be used as a learning support tool rather than a system that completes academic work without student involvement.

Users should:

* Verify important information.
* Avoid submitting sensitive personal information.
* Use generated explanations as learning assistance.
* Follow their institution's academic integrity policies.
* Review AI-generated content before using it in academic work.

---

# 19. Conclusion

StudyMate AI demonstrates the development of a practical AI-powered chatbot using Python, Streamlit, and OpenRouter.

The project implements the major components required for a conversational AI application, including query processing, prompt engineering, AI response generation, conversation history management, and an interactive frontend.

Testing focuses on response accuracy, user experience, conversation quality, and system performance. The application can subsequently be deployed online so that users can access the chatbot through a public web interface.

The project demonstrates how AI APIs can be integrated into a practical educational application while considering usability, security, testing, and responsible use of AI.
