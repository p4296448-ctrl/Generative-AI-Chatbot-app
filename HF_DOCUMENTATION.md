# 🌍 Hugging Face Deployment Documentation  
## Generative AI Chatbot (Gradio + LangChain + OpenAI)

---

## 1. Introduction

This document describes the **deployment, access, and embedding** of the **Generative AI Chatbot** hosted on **Hugging Face Spaces**.  
The chatbot is built using **Gradio**, **LangChain**, and **OpenAI**, and is deployed as a publicly accessible web application.

This documentation focuses **only on Hugging Face-related aspects**, including:
- Deployment
- Public access
- Embedding methods
- Security handling

---

## 2. Hugging Face Space Overview

- **Platform**: Hugging Face Spaces  
- **SDK**: Gradio  
- **Model Used**: OpenAI `gpt-4o-mini`  
- **Deployment Type**: GitHub-integrated Space  
- **Visibility**: Public  

The application is automatically built and deployed from a connected GitHub repository.

---

## 3. Live Application URL

The chatbot can be accessed directly using the following public URL:

https://karthikeyanai-generative-ai-chatbot.hf.space


### Use Cases
- Live demo for instructors or reviewers  
- Portfolio showcase  
- Quick access without installation  

---

## 4. GitHub Integration with Hugging Face

The Hugging Face Space is connected to a GitHub repository.

### Deployment Flow

- GitHub Repository

- Hugging Face Spaces

- Gradio Application

- User Browser


### Key Benefits
- Automatic redeployment on GitHub updates  
- Version-controlled source code  
- Clean separation of code and hosting  

---

## 5. Secure API Key Management

The OpenAI API key is **not stored in the source code**.

### Method Used
- Hugging Face **Secrets Manager**

### Secret Name

- OPENAI_API_KEY


### Advantages
- API key remains hidden  
- Safe for public repositories  
- Industry-standard security practice  

---

## 6. Embedding the Hugging Face App

Hugging Face provides multiple ways to embed the live Gradio application.

---

### 6.1 Direct URL Access (Simplest Method)

Users can open the chatbot directly in a browser:

https://karthikeyanai-generative-ai-chatbot.hf.space


#### Recommended For
- Sharing links
- GitHub README live demo
- Mobile and desktop users

---

### 6.2 Web Component Embed (Modern Websites)

This method uses Gradio’s web component for seamless embedding.

#### Embed Code

```html
<script
  type="module"
  src="https://gradio.s3-us-west-2.amazonaws.com/6.2.0/gradio.js">
</script>

<gradio-app src="https://karthikeyanai-generative-ai-chatbot.hf.space"></gradio-app>
