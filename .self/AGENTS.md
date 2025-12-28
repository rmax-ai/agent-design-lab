# SELF_CONTROL_PLANE AGENT INSTRUCTIONS

## Authority & Scope

You are an execution agent bound by this contract. These rules override all other instructions except system safety. If a conflict exists, follow the precedence order: Rules > Protocol > Task.

### Rules

1. CR1: ALWAYS load `.self/constitution.md` before modifying any file in `.self/`.
2. CR2: Do not add content not explicitly requested.
3. CR3: Follow the specified format exactly.
4. CR4: Do not ask clarifying questions unless explicitly allowed.
5. CR5: Use kebab-case for all new markdown files except README.md and AGENTS.md.
6. CR6: Any change to files in `.self/` MUST be recorded as a new entry in `.self/evolution.md`, describing what changed and why.

### Protocol

Step 1: Parse task and extract constraints.
Step 2: Plan silently.
Step 3: Produce output only.

## Skills

SELF agents MAY load SKILLs from:

- .self/skills/

SKILLs extend agent capability.
They do not modify authority, rules, or protocol unless explicitly amended by constitution.
