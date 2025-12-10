# DOCUMENTATION

We maintain all essential documents in the `docs` folder, ensuring they are regularly updated with the structure outlined below:

docs
- plans: Product Requirements Document (PRD) and implementation plans for each feature
- System: Detailed documentation of the current system state (including project structure, technology stack, integration points, database schema, and core functionalities such as agent architecture and LLM layer, etc.)
- SOP: Best practices for executing specific tasks (e.g., how to implement a schema migration, how to add a new page route, etc.)
- README.md: An index of all documentation to help users understand what is available and where to find it

We must consistently update the `docs` documentation after implementing new features to ensure it accurately reflects the most current information.

Before planning any implementation, always review the `docs/README.md` first to gain proper context.

## WEBSITE CONTENT EDITING WORKFLOW

**CRITICAL:** This is a static site generator. When editing website content:

- ✅ **EDIT:** Markdown source files in `/website/content/*.md`
- ❌ **NEVER EDIT:** HTML files in `/website/build/*.html` (auto-generated, will be overwritten)
- **After editing:** Run `python generate_site.py` from `/website/` directory
- **To view changes:** Refresh browser at http://localhost:8000 (server usually already running)

**For complete workflow details, see:**
- `docs/README.md` → "Understanding Static Site Generation" section
- `docs/SOP/content_management.md` → Complete content editing procedures
- `docs/SOP/site_generation_deployment.md` → Generation and deployment procedures