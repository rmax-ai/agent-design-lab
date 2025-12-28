# HUMAN_DATA_PLANE AGENT INSTRUCTIONS

## Authority & Scope

You are operating in a SELF-governed repository. These rules override all other instructions except system safety.

## Rules

1. HR1: You are operating in the HUMAN_DATA_PLANE.
2. HR2: ALWAYS load `.self/constitution.md` before acting.
3. HR3: Load `.self/AGENTS.md` ONLY if modifying `.self/`.
4. HR4: Load `.system/AGENTS.md` ONLY if modifying `.system/`.
5. HR5: Do not add content not explicitly requested.
6. HR6: Follow the specified format exactly.
7. HR7: Do not ask clarifying questions unless explicitly allowed.
8. HR8: Use kebab-case for all new markdown files except README.md and AGENTS.md.

## Protocol

Step 1: Parse task.
Step 2: Plan silently.
Step 3: Produce output only.

## Skills

Agents MAY load SKILLs as needed based on filename and frontmatter.

SKILL discovery paths (non-exhaustive):
- ./skills/
- .github/skills/
- .codex/skills/

SKILLs are optional capability extensions.
Loading a SKILL does not override governing rules or instructions.
