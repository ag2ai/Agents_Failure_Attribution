<p align="center">
  <img src="https://img.shields.io/badge/Contributions-Welcome-278ea5" alt="Contributions Welcome">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen" alt="PRs Welcome">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat.svg" alt="Awesome"></a>
</p>

<h1 align="center">Awesome LLM Agent Failure Attribution</h1>

<p align="center">
  <b>A curated collection of research on failure attribution, root cause analysis, and error diagnosis in LLM-based agent systems.</b>
</p>

<p align="center">
  <a href="#failure-attribution-methods">Methods</a> •
  <a href="#failure-taxonomies">Taxonomies</a> •
  <a href="#benchmarks--datasets">Benchmarks</a> •
  <a href="#debugging-frameworks">Debugging</a> •
  <a href="#root-cause-analysis">RCA</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## Overview

Failure attribution—the process of identifying **which** agent or component caused a failure and **when** the decisive error occurred—is fundamental to building reliable LLM-based agent systems. As multi-agent systems grow in complexity, automated failure attribution becomes essential for efficient debugging, targeted improvements, and system reliability.

This collection focuses on research that directly addresses:
- **Automated Failure Attribution**: Methods for identifying responsible agents and error steps
- **Failure Taxonomies**: Systematic classification of agent failure modes
- **Failure Attribution Benchmarks**: Datasets with ground-truth failure annotations
- **Root Cause Analysis**: Techniques for tracing failures to their origins

---

## Table of Contents

- [Failure Attribution Methods](#failure-attribution-methods)
- [Failure Taxonomies](#failure-taxonomies)
- [Benchmarks \& Datasets](#benchmarks--datasets)
- [Debugging Frameworks](#debugging-frameworks)
- [Root Cause Analysis](#root-cause-analysis)
- [Surveys](#surveys)
- [Related Resources](#related-resources)
- [Contributing](#contributing)

---

## Failure Attribution Methods

Methods for automatically identifying the responsible agent and decisive error step in failed agent executions.

| Paper | Venue | Year | Links |
|-------|-------|------|-------|
| **Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems** | ICML | 2025 | [[Paper]](https://arxiv.org/abs/2505.00212) [[Code]](https://github.com/ag2ai/Agents_Failure_Attribution) |
| **Who is Introducing the Failure? Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis** (FAMAS) | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.13782) |
| **AgenTracer: Failure Attribution in LLM Systems** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.03312) |
| **Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems** (AgentFail) | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.23735) |
| **Automatic Failure Attribution and Critical Step Prediction Method for Multi-Agent Systems** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.08682) |

---

## Failure Taxonomies

Systematic classification of how and why LLM agents fail.

| Paper | Venue | Year | Links |
|-------|-------|------|-------|
| **Why Do Multi-Agent LLM Systems Fail?** (MAST Taxonomy) | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2503.13657) |
| **Where LLM Agents Fail and How They Can Learn From Failures** (AgentErrorTaxonomy) | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2509.25370) |
| **A Taxonomy of Failures in Tool-Augmented LLMs** | AST | 2025 | [[Paper]](https://homes.cs.washington.edu/~rjust/publ/tallm_testing_ast_2025.pdf) |
| **Taxonomy of Failure Mode in Agentic AI Systems** | Microsoft | 2025 | [[Paper]](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf) |
| **Prioritizing Real-Time Failure Detection in AI Agents** | Partnership on AI | 2025 | [[Paper]](https://partnershiponai.org/wp-content/uploads/2025/09/agents-real-time-failure-detection.pdf) |

---

## Benchmarks & Datasets

Datasets with ground-truth annotations for evaluating failure attribution methods.

| Benchmark | Description | Scale | Year | Links |
|-----------|-------------|-------|------|-------|
| **Who&When** | Failure logs from 127 multi-agent systems with agent/step annotations | 184 tasks | 2025 | [[Paper]](https://arxiv.org/abs/2505.00212) [[Dataset]](https://huggingface.co/datasets/Kevin355/Who_and_When) |
| **MAST-Data** | Annotated traces across 7 MAS frameworks with 14 failure modes | 1600+ traces | 2025 | [[Paper]](https://arxiv.org/abs/2503.13657) |
| **AgentFail** | Failure logs from 10 agentic systems with root cause annotations | 307 logs | 2025 | [[Paper]](https://arxiv.org/abs/2509.23735) |
| **TracerTraj** | Counterfactual replay dataset for fine-grained error diagnosis | - | 2025 | [[Paper]](https://arxiv.org/abs/2509.03312) |
| **TRAIL** | Long-context agentic traces with 20+ error types | 148 traces, 841 errors | 2025 | [[Blog]](https://www.patronus.ai/blog/introducing-trail-a-benchmark-for-agentic-evaluation) |
| **OpenRCA** | Software failure logs with telemetry data (logs, metrics, traces) | 335 failures, 68GB | 2025 | [[Paper]](https://openreview.net/forum?id=M4qNIzQYpd) |

---

## Debugging Frameworks

Tools and frameworks specifically designed for debugging and diagnosing agent failures.

| Paper | Venue | Year | Links |
|-------|-------|------|-------|
| **DoVer: Intervention-Driven Auto Debugging for LLM-based Multi-Agent Systems** | OpenReview | 2025 | [[Paper]](https://openreview.net/pdf/5f5c3ff3d0dd6e5f435f2a0333d49d63a7ae241b.pdf) |
| **LADYBUG: An LLM Agent DeBUGger for Data-Driven Applications** | EDBT | 2025 | [[Paper]](https://openproceedings.org/2025/conf/edbt/paper-313.pdf) |
| **UniDebugger: A Unified Debugging Approach via LLM-Based Multi-Agent Synergy** | EMNLP | 2025 | [[Paper]](https://arxiv.org/abs/2404.17153) |
| **Interactive Debugging and Steering of Multi-Agent AI Systems** | CHI | 2025 | [[Paper]](https://dl.acm.org/doi/10.1145/3613904.3642283) |
| **Exposing Weak Links in Multi-Agent Systems** | OpenReview | 2025 | [[Paper]](https://openreview.net/pdf?id=WHVk2qoCIY) |

---

## Root Cause Analysis

LLM-based approaches for identifying root causes in complex systems.

| Paper | Venue | Year | Links |
|-------|-------|------|-------|
| **OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?** | ICLR | 2025 | [[Paper]](https://openreview.net/forum?id=M4qNIzQYpd) |
| **Flow-of-Action: SOP Enhanced LLM-Based Multi-Agent System for Root Cause Analysis** | WWW | 2025 | [[Paper]](https://dl.acm.org/doi/10.1145/3701716.3715225) |
| **TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent with Multi-Modality Observation Data** | arXiv | 2025 | [[Paper]](https://arxiv.org/abs/2504.20462) |
| **Towards LLM-Based Failure Localization in Production-Scale Networks** | SIGCOMM | 2025 | [[Paper]](https://dl.acm.org/doi/10.1145/3718958.3750505) |
| **Automatic Root Cause Analysis via Large Language Models for Cloud Incidents** | EuroSys | 2024 | [[Paper]](https://dl.acm.org/doi/10.1145/3627703.3629553) |
| **Exploring LLM-Based Agents for Root Cause Analysis** | - | 2024 | [[Paper]](https://www.researchgate.net/publication/382158074_Exploring_LLM-Based_Agents_for_Root_Cause_Analysis) |

---

## Fault Localization

Agent-based approaches for localizing faults in software systems.

| Paper | Venue | Year | Links |
|-------|-------|------|-------|
| **AgentFL: Scaling LLM-based Fault Localization to Project-Level Context** | arXiv | 2024 | [[Paper]](https://arxiv.org/abs/2403.16362) |
| **Agentless: Demystifying LLM-based Software Engineering Agents** | ICSE | 2025 | [[Paper]](https://arxiv.org/abs/2407.01489) [[Code]](https://github.com/OpenAutoCoder/Agentless) |
| **HyperAgent: Generalist Software Engineering Agents to Solve Coding Tasks at Scale** | OpenReview | 2025 | [[Paper]](https://openreview.net/forum?id=PZf4RsPMBG) |
| **A Quantitative and Qualitative Evaluation of LLM-based Explainable Fault Localization** | PACMSE | 2024 | [[Paper]](https://dl.acm.org/doi/10.1145/3678723) |

---

## Surveys

Comprehensive surveys covering related topics.

| Paper | Venue | Year | Links |
|-------|-------|------|-------|
| **Evaluation and Benchmarking of LLM Agents: A Survey** | KDD | 2025 | [[Paper]](https://arxiv.org/abs/2507.21504) |
| **LLM-Based Multi-Agent Systems for Software Engineering: Vision and the Road Ahead** | arXiv | 2024 | [[Paper]](https://arxiv.org/abs/2404.04834) |
| **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** | arXiv | 2024 | [[Paper]](https://arxiv.org/abs/2409.02977) |

---

## Related Resources

### Paper Collections
| Repository | Description |
|------------|-------------|
| [Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) | Comprehensive LLM agent papers |
| [Awesome-Multi-Agent-Papers](https://github.com/kyegomez/awesome-multi-agent-papers) | Multi-agent systems papers |
| [Agent4SE-Paper-List](https://github.com/FudanSELab/Agent4SE-Paper-List) | LLM agents for software engineering |
| [Awesome-Foundation-Agents](https://github.com/FoundationAgents/awesome-foundation-agents) | Foundation agents research |

### Observability Tools
| Tool | Description | Links |
|------|-------------|-------|
| **Langfuse** | Open-source LLM observability | [[GitHub]](https://github.com/langfuse/langfuse) |
| **LangSmith** | LangChain observability platform | [[Website]](https://smith.langchain.com) |
| **OpenLLMetry** | OpenTelemetry for LLMs | [[GitHub]](https://github.com/traceloop/openllmetry) |

---

## Contributing

Contributions are welcome. Please submit a Pull Request with papers related to LLM agent failure attribution.

### Paper Format
```markdown
| **Paper Title** | Venue | Year | [[Paper]](url) [[Code]](url) |
```

### Scope
Papers should directly address failure attribution, root cause analysis, or error diagnosis in LLM-based agent systems.

---

<p align="center">
  <sub>Last updated: January 2026</sub>
</p>
