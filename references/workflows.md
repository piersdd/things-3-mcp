# Things 3 MCP Server — Extended Workflows

## GTD Processing Workflow

The full Getting Things Done processing flow:

1. **Capture**: `get_inbox()` to see what needs processing
2. **Clarify**: For each item, decide:
   - Is it actionable? If no → `update_todo(id, canceled=True)` or move to Someday
   - Can it be done in 2 minutes? Do it now and `update_todo(id, completed=True)`
   - Is it a project (multi-step)? `add_project(...)` and move tasks into it
3. **Organize**: `update_todo(id, when="today")` or assign to project/area
4. **Reflect**: `get_summary()` + `get_logbook(period="1w")` for weekly review
5. **Engage**: `get_today()` to see what to work on

## Project Planning Workflow

1. `get_areas()` — identify the right area
2. `add_project(title="...", area_title="...", when="anytime")`
3. Add tasks one by one with `add_todo(title="...", list_id="<project_uuid>")`
4. Or bulk: `add_project(title="...", todos=["Phase 1", "Phase 2", "Phase 3"])`
5. Verify: `show_item(project_uuid, include_details=True)`

## Email-to-Tasks Workflow

When user shares email content:
1. Parse action items from the email
2. `add_todo(title="...", notes="From email: <sender>", when="today", tags=["email"])`
3. Or bulk: `json_import(data='[{"type":"to-do","attributes":{"title":"...","tags":["email"]}}]')`

## Task Enrichment Workflow

Improve task quality with AI:
1. `get_random_todos(count=5)` — sample a batch
2. For each task, suggest improvements:
   - Better title (specific, action-oriented)
   - Add missing context in notes
   - Set appropriate deadlines
   - Add relevant tags
3. `update_todo(id, title="...", notes="...", tags=[...])` — apply improvements

## Context Switching Workflow

When user switches between work contexts:
1. `get_areas()` — see available contexts
2. `search_advanced(area="<area_uuid>", status="incomplete")` — tasks in that context
3. `get_projects(concise=True)` — projects to focus on
4. `get_tagged_items(tag="priority")` — high-priority items

## Cleanup Workflow

Periodic maintenance:
1. `get_logbook(period="30d")` — what was done last month
2. `get_someday(limit=20)` — review Someday items
3. `search_advanced(status="incomplete", last="90d")` — stale items
4. For each: update, reschedule, or cancel

## Deadline Management Workflow

1. `get_deadlines()` — see all items with deadlines, sorted by date
2. `search_advanced(deadline="<=2026-02-23")` — due this week
3. For overdue: `update_todo(id, when="today")` or `update_todo(id, deadline="2026-03-01")`
