<p align="center">
  <img src="https://img.shields.io/badge/Contributions-Welcome-278ea5" alt="Contributions Welcome">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen" alt="PRs Welcome">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat.svg" alt="Awesome"></a>
</p>


<h1 align="center">Awesome Agentic Failure Attribution</h1>

<p align="center">
  <b>A curated collection of research on failure attribution from agentic traces.</b>
</p>

<p align="center">
  <a href="#failure-attribution-methods">Methods</a> •
  <a href="#failure-taxonomies">Taxonomies</a> •
  <a href="#benchmarks--datasets">Benchmarks</a> •
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="../assets/FA.png" alt="Agentic Failure Attribution" width="400">
</p>

## Overview

Agentic failure attribution is the process of identifying errors that occur in agentic systems and is fundamental to building reliable agentic systems. As these systems grow in complexity, accurate failure attribution becomes increasingly important for enabling targeted improvements and maintaining overall system reliability.

This collection focuses on research that directly addresses:
- **Automated Failure Attribution**: Methods for identifying failures from agentic trajectories.
- **Failure Taxonomies**: Systematic classification of agent failure modes.
- **Failure Attribution Benchmarks**: Datasets with ground-truth failure annotations.

---

## Table of Contents

- [Failure Attribution Methods](#failure-attribution-methods)
- [Failure Taxonomies](#failure-taxonomies)
- [Benchmarks \& Datasets](#benchmarks--datasets)
- [Contributing](#contributing)

---

## Failure Attribution Methods

Methods for automatically identifying the responsible agent and decisive error step in failed agent executions.

| Paper | Venue | Year | Links |
|-------|-------|------|-------|
| **Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems** | ICML | 2025 | [[Paper]](https://arxiv.org/abs/2505.00212) [[Code]](https://github.com/ag2ai/Agents_Failure_Attribution) |
| **AgentRx: Diagnosing AI Agent Failures from Execution Trajectories** | arXiv | 2026 | [[Paper]](https://arxiv.org/abs/2602.02475) |
| **Who is Introducing the Failure? Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.13782) |
| **AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems?** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.03312) |
| **Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems: Dataset, Taxonomy, and Benchmark** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.23735) |
| **Prioritizing Real-Time Failure Detection in AI Agents** | Whitepaper | 2025 | [[Paper]](https://partnershiponai.org/wp-content/uploads/2025/09/agents-real-time-failure-detection.pdf) |
| **DoVer: Intervention-Driven Auto Debugging for LLM-based Multi-Agent Systems** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2512.06749) |
| **LADYBUG: An LLM Agent DeBUGger for Data-Driven Applications** | EDBT | 2025 | [[Paper]](https://openproceedings.org/2025/conf/edbt/paper-313.pdf) |
| **UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging** | EMNLP | 2025 | [[Paper]](https://arxiv.org/abs/2404.17153) |
| **Interactive Debugging and Steering of Multi-Agent AI Systems** | CHI | 2025 | [[Paper]](https://arxiv.org/abs/2503.02068) [[Code]](https://github.com/microsoft/agdebugger) |
| **Where LLM Agents Fail and How They Can Learn From Failures** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.25370) [[Code]](https://github.com/ulab-uiuc/AgentDebug) |
| **OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?** | ICLR | 2025 | [[Paper]](https://openreview.net/forum?id=M4qNIzQYpd) [[Code]](https://github.com/microsoft/OpenRCA) |
| **Flow-of-Action: SOP Enhanced LLM-Based Multi-Agent System for Root Cause Analysis** | WWW | 2025 | [[Paper]](https://arxiv.org/abs/2502.08224) |
| **TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent with Multi-Modality Observation Data** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2504.20462) |
| **Towards LLM-Based Failure Localization in Production-Scale Networks** | SIGCOMM | 2025 | [[Paper]](https://dl.acm.org/doi/10.1145/3718958.3750505) |
| **Automatic Root Cause Analysis via Large Language Models for Cloud Incidents** | EuroSys | 2024 | [[Paper]](https://arxiv.org/abs/2305.15778) |
| **Exploring LLM-Based Agents for Root Cause Analysis** | arXiv | 2024 | [[Paper]](https://www.researchgate.net/publication/382158074_Exploring_LLM-Based_Agents_for_Root_Cause_Analysis) |
| **AgentFL: Scaling LLM-based Fault Localization to Project-Level Context** | arXiv | 2024 | [[Paper]](https://arxiv.org/abs/2403.16362) |
| **A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization** | FSE | 2024 | [[Paper]](https://arxiv.org/abs/2308.05487) [[Code]](https://github.com/coinse/autofl) |

---

## Failure Taxonomies

Systematic classification of how and why LLM agents fail.

| Paper | Venue | Year | Links |
|-------|-------|------|-------|
| **Why Do Multi-Agent LLM Systems Fail?** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2503.13657) [[Code]](https://github.com/multi-agent-systems-failure-taxonomy/MAST) |
| **AgentRx: Diagnosing AI Agent Failures from Execution Trajectories** | arXiv | 2026 | [[Paper]](https://arxiv.org/abs/2602.02475) |
| **Where LLM Agents Fail and How They Can Learn From Failures** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.25370) [[Code]](https://github.com/ulab-uiuc/AgentDebug) |
| **A Taxonomy of Failures in Tool-Augmented LLMs** | AST | 2025 | [[Paper]](https://homes.cs.washington.edu/~rjust/publ/tallm_testing_ast_2025.pdf) |
| **Taxonomy of Failure Mode in Agentic AI Systems** | Whitepaper | 2025 | [[Paper]](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf) |

---

## Benchmarks & Datasets

Datasets with ground-truth annotations for evaluating failure attribution methods.

| Benchmark | Description | Year | Links |
|-----------|-------------|------|-------|
| **Who&When** | Failure logs from 127 multi-agent systems with agent/step annotations | 2025 | [[Paper]](https://arxiv.org/abs/2505.00212) [[Dataset]](https://huggingface.co/datasets/Kevin355/Who_and_When) |
| **AgentRx** | 115 failed trajectories spanning API workflows, incident management, and web/file tasks | 2026 | [[Paper]](https://arxiv.org/abs/2602.02475) |
| **MAST-Data** | Annotated traces across 7 MAS frameworks with 14 failure modes | 2025 | [[Paper]](https://arxiv.org/abs/2503.13657) [[Code]](https://github.com/multi-agent-systems-failure-taxonomy/MAST) |
| **AgentFail** | Failure logs from 10 agentic systems with root cause annotations | 2025 | [[Paper]](https://arxiv.org/abs/2509.23735) |
| **AgentErrorBench** | Annotated failure trajectories from ALFWorld, GAIA, and WebShop | 2025 | [[Paper]](https://arxiv.org/abs/2509.25370) [[Code]](https://github.com/ulab-uiuc/AgentDebug) |
| **TracerTraj** | Counterfactual replay dataset for fine-grained error diagnosis | 2025 | [[Paper]](https://arxiv.org/abs/2509.03312) |
| **TRAIL** | Long-context agentic traces with 20+ error types | 2025 | [[Paper]](https://arxiv.org/abs/2505.08638) [[Code]](https://github.com/patronus-ai/trail-benchmark) |
| **OpenRCA** | Software failure logs with telemetry data (logs, metrics, traces) | 2025 | [[Paper]](https://openreview.net/forum?id=M4qNIzQYpd) [[Code]](https://github.com/microsoft/OpenRCA) |

---

## Contributing

Contributions are welcome. Please submit a Pull Request with papers related to agentic failure attribution.

### Paper Format
```markdown
| **Paper Title** | Venue | Year | [[Paper]](url) [[Code]](url) |
```

---

<p align="center">
  <sub>Last updated: February 2026</sub>
</p>

## Contributors Wall

<p align="center"><a href="https://github.com/ag2ai/Agents_Failure_Attribution">
  <img src="https://contributors-img.web.app/image?repo=ag2ai/Agents_Failure_Attribution" />
</a></p>