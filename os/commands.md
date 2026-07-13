# DecisionOS Operating Protocols

Version: 1.0

---

# Purpose

This document defines the external interface to DecisionOS.

The user should never interact with internal modules directly.

Instead, every interaction occurs through a protocol.

Protocols provide a deterministic interface between the user and the operating system.

Each protocol has:

- Purpose
- Inputs
- Internal Workflow
- Outputs
- Side Effects

---

# Design Principles

Every protocol should:

- Solve one problem.
- Produce deterministic outputs.
- Update the repository consistently.
- Never duplicate another protocol.
- Minimize user effort.

Whenever possible, DecisionOS should infer missing information instead of asking unnecessary questions.

---

# Protocol List

DecisionOS exposes exactly six protocols.

1. Morning Briefing

2. Daily Review

3. Weekly Review

4. Campaign Review

5. Recovery Mode

6. Status

No additional protocols should exist without strong justification.

---

###############################################################################
# MORNING BRIEFING
###############################################################################

Command

```
morning
```

Purpose

Prepare the user for execution.

Morning Briefing should never perform planning.

Planning was completed previously.

Inputs

Current Campaign

Weekly Objectives

Runtime State

Calendar

Previous Feedback

Internal Workflow

Load Runtime State

↓

Load Campaign

↓

Load Weekly Objectives

↓

Identify Today's Mission

↓

Identify Maintenance

↓

Identify Known Risks

↓

Generate Briefing

Outputs

Current Campaign

Today's Mission

Today's Maintenance

Known Risks

Definition of Success

One Reminder

Side Effects

None.

Morning Briefing never modifies repository state.

---

###############################################################################
# DAILY REVIEW
###############################################################################

Command

```
review
```

Purpose

Capture today's reality.

Daily Review is the primary way the operating system learns.

Inputs

User Reflection

Artifacts

Mission Status

Health

Feedback

Internal Workflow

Collect user input

↓

Run Compass

↓

Run Autopilot

↓

Update Runtime State

↓

Update Journal

↓

Update Weekly Progress

↓

Generate Dashboard State

Outputs

Observation

Root Cause

One Recommendation

Updated Runtime State

Side Effects

Update:

journal/

weekly/

state/state.json

docs/state.json

---

###############################################################################
# WEEKLY REVIEW
###############################################################################

Command

```
weekly
```

Purpose

Review the previous week and prepare the next one.

Weekly Review is the only protocol allowed to change Weekly Objectives.

Inputs

Previous Week

Current Campaign

Runtime State

Journal

Internal Workflow

Load Weekly History

↓

Run Compass

↓

Run Autopilot

↓

Identify Patterns

↓

Generate Three Weekly Objectives

↓

Update Runtime State

Outputs

Weekly Summary

Campaign Progress

Three Weekly Objectives

Primary Risks

One System Improvement

Side Effects

Update:

weekly/

state/state.json

docs/state.json

---

###############################################################################
# CAMPAIGN REVIEW
###############################################################################

Command

```
campaign
```

Purpose

Evaluate the current campaign.

Campaign Review happens every 8–12 weeks.

Inputs

Campaign

Weekly Reviews

Runtime State

Artifacts

Internal Workflow

Measure Campaign Progress

↓

Identify Major Learnings

↓

Evaluate Success Criteria

↓

Recommend

Continue

Pause

Complete

Restart

Outputs

Campaign Review

Lessons Learned

Recommendation

Next Campaign (optional)

Side Effects

Update:

campaigns/

state/state.json

---

###############################################################################
# RECOVERY MODE
###############################################################################

Command

```
recover
```

Purpose

Enter Safe Mode.

Recovery Mode ignores backlog.

Inputs

Runtime State

Current Health

Current Situation

Internal Workflow

Determine Recovery Level

↓

Reduce Complexity

↓

Generate Recovery Plan

↓

Update Runtime State

Outputs

Recovery Level

Today's Recovery Plan

Recovery Mission

Side Effects

Runtime State updated.

Dashboard switches to Recovery Mode.

---

###############################################################################
# STATUS
###############################################################################

Command

```
status
```

Purpose

Provide a snapshot of the operating system.

Status should answer:

Where am I?

Inputs

Runtime State

Outputs

Campaign

Mission

Health

Artifacts

Current Drift

Recovery Status

Known Risks

Side Effects

None.

---

# Repository Update Order

Whenever repository state changes:

1.

Update Runtime State

↓

2.

Update Journal

↓

3.

Update Weekly Progress

↓

4.

Update Campaign

↓

5.

Generate Dashboard State

↓

6.

Commit

Never perform these out of order.

---

# Question Policy

DecisionOS minimizes questions.

Only ask questions that are required to:

- remove ambiguity
- maintain consistency
- update state

Never ask questions that can be inferred.

---

# Error Handling

When required information is missing:

Return

UNKNOWN

Never invent facts.

Never assume progress.

Never fabricate artifacts.

---

# Runtime Modes

DecisionOS operates in one of three modes.

Normal

Recovery

Campaign Review

Exactly one mode is active.

---

# Future Protocols

Future protocols may exist.

However:

Every new protocol must satisfy:

- Single Responsibility

- Clear Inputs

- Clear Outputs

- Deterministic Behaviour

- No overlap

---

# Final Principle

The operating system should feel less like a conversation and more like interacting with a trusted command-line tool.

Simple commands.

Predictable outputs.

Minimal thinking.

Maximum clarity.