# OpenNLP Sandbox – gRPC Experiments

This repository contains **experimental work around Apache OpenNLP’s gRPC infrastructure**, created to better understand the existing OpenNLP sandbox design and to explore how a **Python client integration** could interact with the official OpenNLP gRPC backend.

> ⚠️ **Important**  
> This is **not an official Apache OpenNLP repository** and **not a production-ready implementation**.  
> All work here is exploratory and intended to support future contributions to the Apache OpenNLP sandbox.

---

## Motivation

Apache OpenNLP already provides a **gRPC-capable backend** inside the `opennlp-sandbox` project.  
The goal of this repository is to:

- Study and understand the existing OpenNLP gRPC architecture
- Experiment with gRPC service usage and packaging
- Explore how a **Python-friendly client layer** could be built on top of the existing proto definitions
- Reduce friction for Python developers who want to use OpenNLP via gRPC

This work is part of a **long-term contribution effort** toward Apache OpenNLP.

---

## Scope of This Repository

### What this repo **does**
- Uses the existing OpenNLP gRPC proto definitions
- Experiments with building and running the OpenNLP gRPC services
- Explores Python-side gRPC client generation and usage
- Documents practical issues encountered (Docker, Maven, proto layout, packaging)

### What this repo **does NOT do**
- Replace or fork the official OpenNLP gRPC backend
- Provide a production-ready Python SDK
- Introduce new NLP models or algorithms
- Claim compatibility guarantees

> Structure may evolve as experimentation continues.

---

## Current Status

- ✔ Studied the OpenNLP gRPC sandbox layout
- ✔ Generated and tested gRPC stubs
- ✔ Built local gRPC experiments
- ✔ Identified build and Docker-related constraints
- ✔ Clarified that **only a Python client is needed**, not a Python server

Further work will be aligned with feedback from Apache OpenNLP maintainers.

---

## Relationship to Apache OpenNLP

- Apache OpenNLP Sandbox:  
  https://github.com/apache/opennlp-sandbox

All credit for the gRPC backend design and NLP functionality belongs to the **Apache OpenNLP community**.

This repository exists purely as:
- a learning artifact
- a contribution staging area
- a discussion aid for future upstream PRs

---

## Contribution Intent

The long-term plan is to:
1. Use this repo to iterate safely without breaking upstream
2. Get feedback from OpenNLP maintainers
3. Submit **focused, minimal, well-scoped PRs** to `opennlp-sandbox` when appropriate

---

## Disclaimer

This repository:
- Is experimental
- May contain incomplete or broken code
- Is not affiliated with the Apache Software Foundation

Use at your own discretion.

---



