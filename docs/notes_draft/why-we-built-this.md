# Exploring security testing capabilities in the AI Agent Skills Ecosystem

*An introduction to the AppSecHQ Skill Scanner Test project*

---

AI agent skills are having a moment. These modular packages—containing instructions, scripts, and resources that extend what AI coding assistants can do—have exploded in popularity. Registries like [skills.sh](https://skills.sh) and [clawhub.ai](https://clawhub.ai) now host thousands of community-contributed skills, promising everything from automated code review to cloud deployments.

But with great extensibility comes great risk. Skills execute with the agent's full permissions, often with minimal human oversight. A malicious or poorly-written skill can exfiltrate credentials, inject commands, or manipulate the agent into taking harmful actions—all while appearing to be a helpful productivity tool.

This project is our small contribution to understanding and mitigating that risk.

---

## Research: 26% of Skills Have Issues

The first large-scale academic study of agent skill security dropped in January 2026. Researchers analyzed over 31,000 skills from two major marketplaces and found the results "concerning":

> **"26.1% of skills contain at least one potential vulnerability, with data exfiltration patterns (13.3%) and privilege escalation risks (11.8%) most prevalent. We identified 14 distinct vulnerability patterns across 8 functional categories."**
>
> — Liu et al., *"Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale"* ([arXiv:2601.10338](https://arxiv.org/abs/2601.10338))

The study introduced a taxonomy of 14 vulnerability patterns across four categories: prompt injection, data exfiltration, privilege escalation, and supply chain risks. Crucially, they found that skills bundling executable scripts were **2.12× more likely** to contain vulnerabilities than instruction-only skills.

Their severity breakdown adds important nuance: only 5.2% of flagged skills showed high-severity patterns suggesting malicious intent. The majority (12.8%) exhibited low-severity issues like unpinned dependencies—poor hygiene rather than active threats. But even "negligent" vulnerabilities become exploitable when attackers find them first.

---

## Cisco's Open Source Skill Scanner

Around the same time, Cisco's AI Threat and Security Research team released [skill-scanner](https://github.com/cisco-ai-defense/skill-scanner), an open-source tool combining static analysis, behavioral dataflow tracking, and optional LLM-based semantic analysis.

Their motivation, articulated in an accompanying blog post, captures the core problem:

> **"Unlike MCP servers (which are often remote services), skills are local file packages that get installed and loaded directly from disk. Local packages are still untrusted inputs, and some of the most damaging behavior can hide inside the files themselves."**
>
> — Chang, Narajala & Habler, *"Personal AI Agents like OpenClaw Are a Security Nightmare"* ([Cisco Blogs](https://blogs.cisco.com/ai/personal-ai-agents-like-moltbot-are-a-security-nightmare))

The scanner detects prompt injection, data exfiltration, command injection, and other threat patterns using YAML and YARA rules, with optional LLM analysis for semantic threats that evade pattern matching. It outputs SARIF for CI/CD integration and includes a meta-analyzer that reduces false positives by ~65% while maintaining threat detection.

---

## What's Here: Automated Scanning Pipeline and Results Monitoring

The research paper gave us the "what"—a taxonomy and prevalence data. Cisco gave us the "how"—production-grade detection tooling.

That's what this project does.

**[AppSecHQ/skill-scanner-test](https://github.com/AppSecHQ/skill-scanner-test)** is an experimental pipeline that:

1. **Crawls public skill registries** (currently skills.sh and clawhub.ai)
2. **Runs Cisco's skill-scanner** against each skill
3. **Publishes results** as JSON and Markdown reports

It's intentionally simple, and an evolving exploration project. 

### Current Results

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 62 |
| Safe Skills | 57 (92%) |
| Skills with Issues | 5 (8%) |
| Critical Findings | 4 |
| High Findings | 10 |

Our 8% "issues" rate is notably lower than the paper's 26%. Why? Several factors:

- **Different registries**: We scan skills.sh and clawhub.ai; the paper scanned skills.rest and skillsmp.com. Curation matters.
- **Different thresholds**: The paper flagged low-severity patterns (unpinned dependencies); we're reporting based on the scanner's default severity levels.
- **Sample size**: *Drastically* smaller sample set at this stage. 62 skills vs. 31,132. We're just getting started.

When comparing high-severity findings only, the rates converge: the paper found 5.2% high-severity, we're seeing ~6.5% (4 critical out of 62). The ecosystem-wide risk profile appears consistent across registries.

---

## How This Complements Prior Work

| Work | Contribution | Gap |
|------|--------------|-----|
| **Research Paper** | Taxonomy, prevalence data, validation methodology | Snapshot in time; no ongoing monitoring |
| **Cisco Scanner** | Production detection tool | Requires manual invocation per skill |
| **This Project** | Automated pipeline + public results | Narrow registry coverage (for now) |

---

## What's Next

This is early-stage and evolving. Potential future investigation includes:

- **Expanding registry coverage**: Add skills.rest, skillsmp.com (the registries from the research paper), Anthropic Skills, and others
- **Historical tracking**: Monitor how vulnerability rates change over time as the ecosystem matures
- **Validation benchmarking**: Use the paper's ground-truth annotation dataset to measure scanner accuracy
- **Taxonomy alignment**: Map scanner findings to the paper's 14-pattern classification for research comparability, Map scanner findings to OWASP LLM Top 10, OWASP Agentic Top 10

---

*This post is part of the AppSecHQ Skill Scanner Test project documentation. See the [full scan results](../results/summary-report.md) for detailed findings.*
