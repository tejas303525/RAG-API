<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a RAG API with FastAPI

**Project Link:** [View Project](http://nextwork.ai/projects/ai-devops-api)

**Author:** Tejas Kumar  
**Email:** tejas303525@gmail.com

---

---

## Introducing Today's Project!

In this project, I'm going to... This will help me... I'm interested in this because...

### Key tools and concepts

The key tools I used include... Key concepts I learnt include...FAST API, CHROMA DB, OLLAMA, SWAGGER UI

### Challenges and wins

This project took me approximately... The most challenging part was...today alone

---

## Performing RAG Manually

In this step, I'm going to... RAG stands for... retrieval augmented generation


### Understanding the three parts of RAG

I performed RAG manually by... The three parts are.Retrieval - You found the relevant text (some personal info).



Augmentation - You added that text to the prompt.



Generation - The AI used that context to generate an accurate answer..

### Comparing the two AI models

The key difference I noticed is... Embed gives me a mathematical vector of the English input I gave, its not a reply; meanwhile, Qwen gave me an output of in english, it replied to me.

---

## Building a Personal Knowledge Base

In this step, I'm going to... Embeddings are..Write a personal profile document.

Build a Python script that loads, chunks, and stores your profile as embeddings.

Run the script and verify your knowledge base is built..

![Image](http://nextwork.ai/satisfied_lavender_silly_loquat/uploads/ai-devops-api_g3h7m2r5)

### Creating the profile document

I included information about...my work, hobbies etc

### How semantic search finds relevant chunks

When I ask a question, questions are converted to vectors, then chreomadb finds the vector closest questions' vector. that is semantic search where answers are given based on context or meaning rather than keywords

---

## Creating the RAG API with FastAPI

In this step, I'm going to build an API that...creating a ask endpoint  I'll test it using...swagger ui

![Image](http://nextwork.ai/satisfied_lavender_silly_loquat/uploads/ai-devops-api_j5m1r8t2)

### How the /ask endpoint works

When a question comes in, my endpoint...gets result from the database

uses ollamas qwen2.5:0.5b model

and gives me answer based on result context and if itsa not availabl;e then it will say no

### Testing with Swagger UI

I tested my API by asking... whats my name The AI answered with the context user

---

## Extending to a Multi-User AI Directory

In this project extension, I'm adding multi-user support because... Multi-tenancy means...Multiple users can add their profile and the system can generete answer for that particular user but its not al;ways the case ifthe user is not mentioned. RAG may fail.

![Image](http://nextwork.ai/satisfied_lavender_silly_loquat/uploads/ai-devops-api_d5g9k3n7)

### Adding the POST /documents endpoint

In this project extension, I added a POST endpoint that... Metadata filtering allows...

![Image](http://nextwork.ai/satisfied_lavender_silly_loquat/uploads/ai-devops-api_r8t2w6y1)

### Verifying multi-user filtering

In this project extension, I tested multi-user queries by... The filter works because..

---

## Wrapping Up

I did this project today to learn how to work with RAG Another skill I want to learn is..DOCKER

---

---
