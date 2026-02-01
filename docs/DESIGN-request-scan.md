# UX Design: Request a Scan

## Overview

Users can submit a skill (GitHub repo URL) and request a security scan. The form submits to a backend queue. The site owner is notified via GitHub Issue creation.

---

## 1. Information Architecture

### Navigation Change

```
Before:  Skills | Dashboard | Notes
After:   Skills | Dashboard | Notes | Request Scan
```

`Request Scan` is the rightmost nav item. It uses a slightly different visual treatment to signal it's an action, not a content page: use `--accent` color background with white text (like a soft button in the nav), distinct from the other tab-style links.

### Route

`#/request` — new SPA view, follows the same `.view` / `.view.active` pattern.

---

## 2. Page Layout

### Heading & Context

```
Request a Scan
Subtitle (muted): Submit a skill for security analysis. We'll scan it with
cisco-ai-skill-scanner and publish the results here.
```

### Two-Column Layout (desktop)

```
+----------------------------------------------+---------------------------+
|                                               |                           |
|  FORM (left, ~60%)                            |  SIDEBAR (right, ~40%)    |
|                                               |                           |
|  [Skill URL field]                            |  HOW IT WORKS             |
|  [Skill Name field]                           |  1. Submit the form       |
|  [Your Email field]                           |  2. We review & queue it  |
|  [Notes textarea]                             |  3. Scan runs (~5 min)    |
|  [Submit button]                              |  4. Results published     |
|                                               |                           |
|                                               |  WHAT WE SCAN FOR         |
|                                               |  - Prompt injection       |
|                                               |  - Data exfiltration      |
|                                               |  - Malicious patterns     |
|                                               |  - Permission abuse       |
|                                               |                           |
+----------------------------------------------+---------------------------+
```

On mobile (<768px): single column, form first, sidebar info below.

---

## 3. Form Fields

### Skill URL (required)

- **Type**: `url`
- **Placeholder**: `https://github.com/owner/skill-repo`
- **Label**: "Skill Repository URL"
- **Validation**:
  - Required
  - Must be a valid URL
  - Should match `github.com/*` pattern (warn but don't block other URLs)
- **Help text** (below field, muted): "GitHub repository URL of the skill to scan"
- **Auto-derive**: On blur, if URL matches `github.com/:owner/:repo`, auto-fill the Name field with `:repo` (cleaned: dashes to spaces, title-cased). User can override.

### Skill Name (optional)

- **Type**: `text`
- **Placeholder**: `My Cool Skill`
- **Label**: "Skill Name"
- **Help text**: "Display name for the skill. Auto-detected from URL if left blank."
- **Max length**: 100 characters

### Your Email (optional)

- **Type**: `email`
- **Placeholder**: `you@example.com`
- **Label**: "Email (optional)"
- **Help text**: "We'll notify you when the scan is complete. Not stored or shared."
- **Validation**: Valid email format if provided

### Notes (optional)

- **Type**: `textarea`
- **Placeholder**: `Any context about this skill or specific concerns...`
- **Label**: "Notes (optional)"
- **Rows**: 3 (grows to 6 max)
- **Max length**: 500 characters
- **Character counter**: Show `{current}/{max}` below field when user starts typing, muted color, right-aligned

---

## 4. Submit Button

```
[ Request Scan ]
```

- Full width of the form column
- Background: `var(--accent)` (#6366f1)
- Text: white, font-weight 600
- Border-radius: 8px
- Height: ~44px (good touch target)
- Hover: lighten slightly
- Disabled state: reduced opacity (0.5), `cursor: not-allowed` when URL field is empty

---

## 5. Form States

### Empty (default)

All fields empty. Submit button disabled. Clean form with labels and placeholders visible.

### Filling

- Fields get `border-color: var(--accent)` on focus (existing pattern)
- Inline validation on blur:
  - URL field: red border + error message if invalid format
  - Email field: red border if invalid format
- Submit button enables when URL field has valid content

### Submitting

- Submit button text changes to "Submitting..." with a small CSS spinner (no external deps)
- Button disabled during submission
- All fields disabled/readonly during submission
- No page navigation allowed during submit

### Success

The form panel smoothly transitions to a **confirmation state**:

```
+----------------------------------------------+
|                                               |
|     [checkmark icon - CSS only, green]        |
|                                               |
|     Scan Requested                            |
|                                               |
|     Your request for "skill-name" has been    |
|     submitted. We'll review it shortly.       |
|                                               |
|     [muted] Reference: #RSQ-1706835200       |
|                                               |
|     [ Submit Another ]   [ View Skills -> ]   |
|                                               |
+----------------------------------------------+
```

- Reference number: `RSQ-` + unix timestamp (simple, unique-ish)
- "Submit Another" resets the form
- "View Skills" navigates to `#/`
- If user provided email: add line "We'll email you at `[email]` when results are ready."
- Sidebar stays visible on desktop

### Error

- Inline error banner above the submit button
- Red left border (matches finding card pattern)
- Text: "Something went wrong. Please try again, or open an issue on GitHub."
- "open an issue" links to `github.com/AppSecHQ/skill-scanner-test/issues`
- Form remains filled so user doesn't lose input
- Submit button re-enables

---

## 6. Sidebar Content

### "How It Works" panel

Uses the existing `.panel` pattern (surface bg, border, border-radius).

```
HOW IT WORKS

1  Submit the form with a skill's GitHub URL
2  We review the request and add it to our scan queue
3  The skill is scanned using cisco-ai-skill-scanner
4  Results are published on this site
```

Numbered steps use a vertical timeline visual:
- Number in a small circle (accent color border, 24px diameter)
- Vertical line connecting them (1px, `--border` color)
- Step text right of each number

### "What We Scan For" panel

Below the how-it-works panel, separated by 1rem gap.

```
WHAT WE SCAN FOR

  Prompt injection & jailbreaks
  Data exfiltration patterns
  Malicious code & hidden commands
  Permission & scope abuse
  Supply chain risks
```

Each item prefixed with a small `--accent` colored dot (like `.legend-dot`).

---

## 7. Contextual CTA on Skills Page

Add a secondary entry point on the Skills page — a subtle banner above the table controls:

```
+------------------------------------------------------------------+
|  Don't see a skill?  [ Request a Scan ]                           |
+------------------------------------------------------------------+
```

- Sits between the `<h1>Skills</h1>` heading and the `.table-controls` div
- Background: `rgba(99, 102, 241, 0.06)` (very subtle accent tint)
- Border: `1px solid rgba(99, 102, 241, 0.15)`
- Border-radius: 8px
- Padding: 0.75rem 1.25rem
- Flex layout: text left, button right
- Text: "Don't see a skill listed?" in `--muted` color
- Button: small accent-colored link/button → navigates to `#/request`
- Dismissible: no (it's subtle enough to not be annoying)

---

## 8. Backend API Contract

The form submits a POST request. The implementation can be any of:
- Serverless function (Cloudflare Worker, AWS Lambda, Vercel)
- GitHub Actions `repository_dispatch`
- Form service (Formspree, Formspark)

### Request

```
POST /api/request-scan
Content-Type: application/json

{
  "skill_url": "https://github.com/owner/repo",
  "skill_name": "Repo Name",
  "email": "user@example.com",
  "notes": "Optional context",
  "timestamp": "2026-02-01T12:00:00Z",
  "reference": "RSQ-1706835200"
}
```

### Response

```json
// Success
{ "ok": true, "reference": "RSQ-1706835200", "issue_url": "https://github.com/.../issues/42" }

// Error
{ "ok": false, "error": "Failed to create request" }
```

### GitHub Issue Created

The backend creates a GitHub Issue in `AppSecHQ/skill-scanner-test`:

**Title**: `Scan Request: {skill_name}`

**Labels**: `scan-request`

**Body**:
```markdown
## Scan Request

| Field | Value |
|-------|-------|
| **Skill URL** | {skill_url} |
| **Skill Name** | {skill_name} |
| **Requester Email** | {email or "Not provided"} |
| **Reference** | {reference} |
| **Submitted** | {timestamp} |

### Notes
{notes or "None"}

---
*Submitted via skillscan.appsechq.com*
```

---

## 9. Spam / Abuse Prevention

Since this is a public form with no auth:

- **Rate limit**: Backend should limit to 3 requests per IP per hour
- **Honeypot field**: Add a hidden field `<input name="website" tabindex="-1" autocomplete="off" style="display:none">`. If filled, silently discard (bots fill all fields)
- **Minimum time**: Track when the form rendered. If submitted < 2 seconds after render, likely a bot — reject silently
- **No CAPTCHA** for now (low traffic site, keep UX clean)

---

## 10. CSS Additions

New styles needed, consistent with the existing design system:

```
.request-form         — the form container (panel-like)
.form-group           — wraps label + input + help text
.form-label           — styled like .stat-label but larger
.form-help            — small muted text below inputs
.form-error           — red error message below a field
.form-error-banner    — full-width error above submit button
.btn-primary          — accent bg, white text (the submit button)
.btn-secondary        — outline style (for "Submit Another")
.btn-ghost            — text-only with hover underline (for "View Skills")
.request-sidebar      — sidebar wrapper
.timeline-step        — numbered step in "How It Works"
.scan-list-item       — dot + text in "What We Scan For"
.request-cta          — the banner on the Skills page
.success-panel        — the post-submit confirmation
.char-counter         — character count display
```

The nav CTA styling (Request Scan as a soft button):
```css
.nav-links .nav-cta {
  background-color: rgba(99, 102, 241, 0.15);
  color: var(--accent-light);
}
.nav-links .nav-cta:hover {
  background-color: rgba(99, 102, 241, 0.25);
}
```

---

## 11. Mobile Responsive (< 768px)

- Two-column layout collapses to single column
- Form takes full width
- Sidebar panels stack below the form
- Submit button remains full width
- Nav item: consider using just "Request" to save space (or it wraps naturally given the existing flex layout)
- Skills page CTA banner: stack text above button

---

## 12. Accessibility

- All form fields have associated `<label>` elements (not just placeholders)
- Error messages linked to fields via `aria-describedby`
- Submit button has `aria-disabled` when disabled
- Success panel uses `role="status"` and `aria-live="polite"` so screen readers announce it
- Focus moves to the success panel heading after submission
- Honeypot field has `aria-hidden="true"` and `tabindex="-1"`
- Color alone is never the only indicator of errors (text + icon + border)

---

## 13. Implementation Sequence

Recommended build order for the coding agent:

1. **HTML**: Add the `#request` section to `index.html`, add nav link
2. **CSS**: Add form styles, button styles, sidebar styles, responsive rules
3. **JS (routing)**: Register `#/request` route in the router function
4. **JS (form logic)**: URL auto-detect, validation, character counter
5. **JS (submission)**: POST to backend endpoint, handle states
6. **Backend**: Serverless function that creates GitHub Issue
7. **Skills page CTA**: Add the banner to the skills table view
8. **Testing**: Accessibility checks, mobile testing, error states
