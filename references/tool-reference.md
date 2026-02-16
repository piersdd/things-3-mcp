# Things 3 MCP Server — Complete Tool Reference

## List View Tools

All list view tools share these parameters:
- `concise: bool = True` — One-line-per-item output
- `limit: int = 10` — Maximum items to return
- `include_details: bool = False` — Include notes, checklist, timestamps

### get_inbox
Get todos from the Things 3 Inbox. Unprocessed tasks live here.

### get_today
Get todos scheduled for Today. Filters out tasks that inherit Someday status.

### get_upcoming
Get upcoming scheduled todos. Excludes inherited-Someday tasks.

### get_anytime
Get Anytime todos. Available to work on at any time. Excludes inherited-Someday.

### get_someday
Get Someday todos. Includes both directly-Someday tasks AND tasks from Someday projects.

### get_logbook
Get completed todos.
- `period: str = "7d"` — Time period: '7d', '2w', '1m', '3m', '1y'

### get_trash
Get trashed todos.

### get_deadlines
Get todos with deadlines, sorted chronologically.

## Random Sampling Tools

### get_random_inbox / get_random_today / get_random_anytime / get_random_todos
- `count: int = 5` — Number of random items to sample
- `project_uuid: str | None = None` — (get_random_todos only) Filter by project

Always use concise format. Returns: `"Random N of M items:"` header + concise lines.

## Entity View Tools

### get_todos
- `project_uuid: str | None` — Filter by project UUID
- Standard concise/limit/include_details params

### get_projects
- `include_items: bool = False` — Include task list inside each project
- Concise mode shows project name + open/done counts

### get_areas
High-level categories (e.g., Work, Personal, Health).

### get_tags / get_tagged_items
- `tag: str` — (get_tagged_items) Tag name to filter by
- `include_items: bool = False` — (get_tags) Include tagged items

## Search & Detail Tools

### search_todos
- `query: str` — Search terms (matches title and notes)

### search_advanced
- `status: str | None` — 'incomplete', 'completed', 'canceled'
- `start_date: str | None` — e.g., '2026-01-01' or '>=2026-01-01'
- `deadline: str | None` — e.g., '<=2026-03-01'
- `tag: str | None` — Tag name
- `area: str | None` — Area UUID
- `item_type: str | None` — 'to-do', 'project', 'heading'
- `last: str | None` — Created within period: '3d', '1w', '2m'

### get_recent
- `period: str` — Time period: '3d', '1w', '2m', '1y'

### show_item
- `uuid: str` — UUID of item or built-in list name
- `include_details: bool = True` — Full details by default for single items

### get_summary
No parameters. Returns GTD overview: counts per list, upcoming deadlines.

## Write Tools

### add_todo
- `title: str` (required)
- `notes: str | None` — Supports Markdown; use checkboxes for subtasks
- `when: str | None` — 'today', 'tomorrow', 'evening', 'anytime', 'someday', or YYYY-MM-DD
- `deadline: str | None` — YYYY-MM-DD
- `tags: list[str] | None`
- `list_id: str | None` — UUID of project/area (precedence over list_title)
- `list_title: str | None` — Name of project/area
- `checklist_items: list[str] | None` — Uses URL scheme fallback

### add_project
- `title: str` (required)
- `notes, when, deadline, tags` — Same as add_todo
- `area_id: str | None` / `area_title: str | None`
- `todos: list[str] | None` — Todo titles to create inside

### update_todo
- `todo_id: str` (required)
- `title, notes, when, deadline, tags` — New values (replaces existing)
- `completed: bool | None` — True to complete, False to reopen
- `canceled: bool | None` — True to cancel, False to reopen
- `list_id: str | None` / `list_name: str | None` — Move to project/area

### update_project
- `project_id: str` (required)
- Same update fields as update_todo
- `area_id: str | None` / `area_title: str | None`

## Bulk / Navigation Tools

### json_import
- `data: str` — JSON string array of Things objects
- `reveal: bool = False` — Show first item in Things

### json_export
- `project_uuid: str | None` — Export specific project
- `limit: int = 50` — Max items

### show_in_things
- `item_id: str` — UUID or list name (inbox, today, upcoming, etc.)

### search_in_things
- `query: str` — Opens Things search UI
