# AI Agent Skills Security Scan Summary Report

**Scan Date:** 2026-01-30
**Scanner:** cisco-ai-skill-scanner v1.0.1
**Analyzers Used:** static_analyzer, behavioral_analyzer, trigger_analyzer

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 10 |
| Skills with Findings | 5 |
| Skills Clean (No Findings) | 5 |
| Skills Marked Unsafe | 1 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| HIGH | 1 |
| MEDIUM | 6 |
| LOW | 5 |
| **Total Findings** | **12** |

---

## Findings by Skill

| # | Skill Name | Repo | Safe | Critical | High | Medium | Low | Total |
|---|------------|------|------|----------|------|--------|-----|-------|
| 1 | vercel-react-best-practices | vercel-labs/agent-skills | Yes | 0 | 0 | 0 | 0 | 0 |
| 2 | find-skills | vercel-labs/skills | Yes | 0 | 0 | 0 | 1 | 1 |
| 3 | web-design-guidelines | vercel-labs/agent-skills | Yes | 0 | 0 | 0 | 1 | 1 |
| 4 | remotion-best-practices | remotion-dev/skills | Yes | 0 | 0 | 0 | 1 | 1 |
| 5 | frontend-design | anthropics/skills | Yes | 0 | 0 | 0 | 0 | 0 |
| 6 | **agent-browser** | vercel-labs/agent-browser | **No** | 0 | **1** | **6** | 1 | **8** |
| 7 | skill-creator | anthropics/skills | Yes | 0 | 0 | 0 | 0 | 0 |
| 8 | vercel-composition-patterns | vercel-labs/agent-skills | Yes | 0 | 0 | 0 | 0 | 0 |
| 9 | vercel-react-native-skills | vercel-labs/agent-skills | Yes | 0 | 0 | 0 | 0 | 0 |
| 10 | seo-audit | coreyhaines31/marketingskills | Yes | 0 | 0 | 0 | 1 | 1 |

---

## Top Risks

### 1. [HIGH] agent-browser - Unauthorized Tool Use

**Skill:** agent-browser (vercel-labs/agent-browser)
**Install Count:** 15,968
**Rule ID:** ALLOWED_TOOLS_BASH_VIOLATION
**Category:** unauthorized_tool_use

**Finding:** Skill restricts tools to `['Bash(agent-browser:*)']` but code executes bash commands outside this pattern.

**Impact:** Could allow the skill to execute commands beyond its declared permissions, potentially accessing resources or performing actions the user did not authorize.

**Recommendation:** Review the skill's tool restrictions and ensure all bash command execution is properly scoped within the declared allowed-tools pattern.

---

### 2. [MEDIUM] agent-browser - Command Injection (6 instances)

**Skill:** agent-browser (vercel-labs/agent-browser)
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Category:** command_injection

**Affected Files:**
- `templates/capture-workflow.sh:7`
- `templates/form-automation.sh:7`
- `templates/authenticated-session.sh:15`

**Finding:** User input used in command substitution patterns like `${1:?Usage: $0 <url>}` without proper sanitization.

**Impact:** If user-controlled input is passed to these shell scripts, an attacker could potentially inject malicious commands.

**Recommendation:**
- Validate and sanitize all user inputs before use in shell commands
- Use proper quoting and escaping
- Consider using parameter arrays instead of positional parameters

---

### 3. [LOW] Missing License (5 skills)

**Affected Skills:** find-skills, web-design-guidelines, remotion-best-practices, agent-browser, seo-audit
**Rule ID:** MANIFEST_MISSING_LICENSE
**Category:** policy_violation

**Finding:** These skills do not specify a license in their SKILL.md manifest.

**Impact:** Users cannot determine usage terms, which may create legal uncertainty for enterprise adoption.

**Recommendation:** Add a `license` field to each skill's SKILL.md manifest.

---

## Patterns Observed

### 1. Shell Script Command Injection Risk
The agent-browser skill uses shell templates that accept user input via positional parameters. The pattern `${1:?...}` provides default error messages but does not sanitize input, creating potential command injection vectors.

### 2. Missing License Metadata
50% of scanned skills (5/10) lack license information in their manifests. This is a common oversight in newer skills and represents a policy/governance gap rather than a security risk.

### 3. Tool Permission Mismatches
The agent-browser skill declares restricted tool permissions but contains code that may execute outside those boundaries. This pattern warrants attention as it could indicate unintentional permission escalation.

---

## Clean Skills (No Findings)

The following 5 skills passed all security checks:

1. **vercel-react-best-practices** (73,182 installs) - Most popular skill
2. **frontend-design** (27,292 installs)
3. **skill-creator** (13,525 installs)
4. **vercel-composition-patterns** (11,340 installs)
5. **vercel-react-native-skills** (8,611 installs)

---

## Methodology

### Analyzers Used

| Analyzer | Description |
|----------|-------------|
| static_analyzer | Pattern-based detection using YAML + YARA rules. Scans SKILL.md instructions and scripts. Detects 80+ security patterns across 12+ threat categories. |
| behavioral_analyzer | Static dataflow analysis (AST + taint tracking). Tracks data from sources to sinks without execution. Detects multi-file exfiltration chains. |
| trigger_analyzer | Detects overly generic skill descriptions and trigger hijacking risks. |

### Analyzers Not Used

| Analyzer | Reason |
|----------|--------|
| llm_analyzer | API key authentication failed |
| meta_analyzer | Requires LLM analyzer |
| virustotal_analyzer | No VIRUSTOTAL_API_KEY available |
| aidefense_analyzer | No AI_DEFENSE_API_KEY available |

### Limitations

1. **No LLM-based semantic analysis** - Could miss context-dependent vulnerabilities that pattern matching alone cannot detect
2. **No binary file scanning** - VirusTotal integration unavailable
3. **Static analysis only** - No runtime behavior verification
4. **Sample size** - Only top 10 skills scanned; results may not represent the broader ecosystem

---

## Conclusion

Of the top 10 most-installed AI agent skills from skills.sh:

- **90% (9/10)** passed security checks and are marked as safe
- **10% (1/10)** has security concerns requiring review (agent-browser)
- **50% (5/10)** have missing license metadata (low severity policy issue)

The most concerning finding is in **agent-browser** (15,968 installs), which has potential command injection vulnerabilities in its shell templates and a tool permission mismatch. Users of this skill should exercise caution and review the latest version for fixes.

The majority of popular skills from major vendors (Vercel, Anthropic, Remotion) demonstrate good security practices with no findings beyond missing license metadata.

---

## Files Generated

| File | Description |
|------|-------------|
| `skills/skill-inventory.md` | Inventory of top 10 skills with metadata |
| `results/vercel-react-best-practices-scan.json` | Raw scan results |
| `results/vercel-react-best-practices-scan.md` | Readable scan report |
| `results/find-skills-scan.json` | Raw scan results |
| `results/find-skills-scan.md` | Readable scan report |
| `results/web-design-guidelines-scan.json` | Raw scan results |
| `results/web-design-guidelines-scan.md` | Readable scan report |
| `results/remotion-best-practices-scan.json` | Raw scan results |
| `results/remotion-best-practices-scan.md` | Readable scan report |
| `results/frontend-design-scan.json` | Raw scan results |
| `results/frontend-design-scan.md` | Readable scan report |
| `results/agent-browser-scan.json` | Raw scan results |
| `results/agent-browser-scan.md` | Readable scan report |
| `results/skill-creator-scan.json` | Raw scan results |
| `results/skill-creator-scan.md` | Readable scan report |
| `results/vercel-composition-patterns-scan.json` | Raw scan results |
| `results/vercel-composition-patterns-scan.md` | Readable scan report |
| `results/vercel-react-native-skills-scan.json` | Raw scan results |
| `results/vercel-react-native-skills-scan.md` | Readable scan report |
| `results/seo-audit-scan.json` | Raw scan results |
| `results/seo-audit-scan.md` | Readable scan report |
| `results/summary-report.md` | This consolidated report |
