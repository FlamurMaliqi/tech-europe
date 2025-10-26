# MCPs Folder Location

The MCPs folder has been copied into the tech-europe repository:
- **Current location**: `MCPs/` (in the tech-europe workspace)
- **Full path**: `/Users/flamurmaliqi/git/tech-europe/MCPs`

## Configuration

The agent code has been configured to use relative paths to the MCPs folder.

### Files That Reference MCPs:
1. `agent/drive_thru/agent.py` - KontextUserProfileManager class
2. `agent/scripts/generate_fake_user_profiles.py` - Profile generator script

Both files now use relative paths:
```python
current_file = Path(__file__)
self.mcp_path = (current_file.parent.parent.parent / "MCPs" / "kontext").resolve()
```

This dynamically resolves the path to `MCPs/kontext` from within the repository structure.

## Structure

The MCPs folder contains:
- `kontext/` - Kontext MCP memory agent implementation
  - `src/agent.js` - Main agent implementation
  - `src/memory-manager.js` - Memory operations wrapper
  - `package.json` - Node.js dependencies
  - `README.md` - Kontext agent documentation

