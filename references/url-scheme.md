# Things 3 URL Scheme Reference

## Overview

Things 3 supports `things:///` URLs for automation. This server uses the URL scheme
as a fallback for writes when AppleScript is unavailable, and as the primary method
for checklist items and bulk JSON operations.

## Commands

### things:///add
Create a new to-do.

Parameters: title, notes, when, deadline, tags, checklist-items, list-id, list,
heading-id, heading, completed, canceled, creation-date, completion-date, reveal.

### things:///add-project
Create a new project.

Parameters: title, notes, when, deadline, tags, area-id, area, to-dos, headings,
completed, canceled, creation-date, completion-date, reveal.

### things:///update (requires auth-token)
Update an existing to-do.

Parameters: id (required), auth-token (required), plus all add params, plus:
prepend-notes, append-notes, add-tags, prepend-checklist-items, append-checklist-items.

### things:///update-project (requires auth-token)
Update an existing project. Same as update but with area-id/area.

### things:///show
Navigate to a list or item. Parameter: id (UUID or list name).

### things:///search
Open search. Parameter: query.

### things:///json
Bulk create/update via JSON.

Parameters: data (JSON string), reveal, auth-token (if updates included).

## JSON Format

```json
[
  {
    "type": "to-do",
    "attributes": {
      "title": "Task name",
      "when": "today",
      "tags": ["tag1", "tag2"],
      "checklist-items": [
        {"title": "Step 1", "completed": false}
      ]
    }
  },
  {
    "type": "project",
    "attributes": {
      "title": "Project name",
      "items": [
        {"type": "heading", "attributes": {"title": "Phase 1"}},
        {"type": "to-do", "attributes": {"title": "First task"}}
      ]
    }
  }
]
```

## Auth Token

Required for update and update-project commands.
Location: Things > Settings > General > Enable Things URLs > Manage.
Set via `THINGS_AUTH_TOKEN` env var or auto-detected via `things.token()`.

## Rate Limit

250 items per 10-second period for JSON bulk operations.

## When Values

- Keywords: `today`, `tomorrow`, `evening`, `anytime`, `someday`
- Date: `2026-03-15` (YYYY-MM-DD)
- Date+time: `2026-03-15@14:00`
