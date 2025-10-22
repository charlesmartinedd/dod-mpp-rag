# Google Workspace + AI Studio Setup Guide

This project is configured with Google Workspace MCP tools and Google AI Studio integration for creating training content.

## Configuration Overview

### 1. Google Workspace MCP Server

**Location**: `.mcp.json` in project root

**Credentials**: Configured via environment variables (see Setup section below)

**Available Tools**:
- Gmail (read, send, manage emails)
- Google Calendar (create, update events)
- Google Drive (file management)
- Google Docs (create, edit documents)
- Google Sheets (spreadsheet operations)
- Google Slides (presentation creation)
- Google Forms (form creation)
- Google Tasks (task management)
- Google Chat (messaging)

### 2. Google AI Studio API Key

To use Google AI Studio (Gemini) with this project:

```python
import google.generativeai as genai
import os

# Configure the API using environment variable
genai.configure(api_key=os.environ.get('GOOGLE_AI_API_KEY'))

# Use Gemini models
model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content("Your prompt here")
```

### 3. Custom Subagent: Google Content Creator

**Location**: `.claude/agents/google-content-creator.md`

**Purpose**: General-purpose agent for creating professional content (presentations, documents, videos, training materials) using Google Workspace tools and AI capabilities.

**To invoke**:
```
@google-content-creator create a slide deck about [your topic]
```

## First-Time Setup

### Step 1: Enable MCP Server

The MCP server is already configured in `.mcp.json`. When you first run Claude Code, it will:
1. Launch the Google Workspace MCP server using `uvx`
2. Prompt you to authenticate with Google OAuth
3. Open a browser window for Google login
4. Store your authentication tokens locally

### Step 2: Verify MCP Tools

Run these commands in Claude Code:
```
/mcp list
```
This will show all available MCP servers and their status.

### Step 3: Test Google Workspace Access

Try a simple command:
```
Can you list my Google Drive files?
```

## Using the Google Content Creator Agent

### Example Usage

1. **Create a presentation**:
   ```
   @google-content-creator Create a Google Slides presentation about
   machine learning fundamentals with 10 slides covering key concepts.
   ```

2. **Generate a video script**:
   ```
   @google-content-creator Write a detailed video script for a
   5-minute introduction to Python programming.
   ```

3. **Create training materials**:
   ```
   @google-content-creator Generate a training course outline with
   assessment questions in a Google Doc for project management basics.
   ```

4. **Create a report**:
   ```
   @google-content-creator Create a comprehensive market analysis report
   in Google Docs with charts and data tables in Google Sheets.
   ```

### Agent Capabilities

The Google Content Creator agent can:
- ✅ Create Google Slides presentations with proper formatting
- ✅ Generate Google Docs for reports, scripts, and documentation
- ✅ Create Google Sheets for data and tracking
- ✅ Build Google Forms for surveys and assessments
- ✅ Organize files in Google Drive folders
- ✅ Structure content following best practices
- ✅ Use AI to enhance content quality and creativity
- ✅ Research topics using web search capabilities

## Workflow for Content Creation

1. **Planning**:
   - Understand the content requirements and audience
   - Research and gather information from available sources
   - Create structure and outline

2. **Document Creation**:
   - Generate Google Docs for text-heavy content
   - Create detailed outlines and drafts

3. **Presentation Design**:
   - Build Google Slides with visual hierarchy
   - Add speaker notes and annotations
   - Include graphics, charts, and visual elements

4. **Script & Media**:
   - Write narration scripts with timing
   - Include visual cues and transitions
   - Format for video/audio production

5. **Data & Forms**:
   - Create spreadsheets for tracking and analysis
   - Design forms for feedback and assessments
   - Generate charts and visualizations

6. **Organization & Sharing**:
   - Organize files in logical Drive structure
   - Set appropriate sharing permissions
   - Create sharable links and documentation

## Environment Variables Setup

**REQUIRED**: You must set these environment variables before using the Google Workspace MCP server:

### Windows (PowerShell):
```powershell
# Set environment variables for current session
$env:GOOGLE_OAUTH_CLIENT_ID="your-client-id-here.apps.googleusercontent.com"
$env:GOOGLE_OAUTH_CLIENT_SECRET="your-client-secret-here"
$env:GOOGLE_AI_API_KEY="your-google-ai-api-key-here"
```

### Windows (Command Prompt):
```cmd
set GOOGLE_OAUTH_CLIENT_ID=your-client-id-here.apps.googleusercontent.com
set GOOGLE_OAUTH_CLIENT_SECRET=your-client-secret-here
set GOOGLE_AI_API_KEY=your-google-ai-api-key-here
```

### Linux/Mac (Bash):
```bash
export GOOGLE_OAUTH_CLIENT_ID="your-client-id-here.apps.googleusercontent.com"
export GOOGLE_OAUTH_CLIENT_SECRET="your-client-secret-here"
export GOOGLE_AI_API_KEY="your-google-ai-api-key-here"
```

### Permanent Setup

To make these permanent, add them to:
- **Windows**: System Environment Variables (System Properties > Advanced > Environment Variables)
- **Linux/Mac**: Add to `~/.bashrc` or `~/.zshrc`

Alternatively, create a `.env` file in the project root (see `.env.example`)

## Troubleshooting

### MCP Server Not Starting

If the Google Workspace MCP server doesn't start:

1. Check that `uv` is installed:
   ```bash
   where uv
   ```

2. Manually test the server:
   ```bash
   uvx google_workspace_mcp --single-user
   ```

3. Check Claude Code logs:
   ```
   /doctor
   ```

### Authentication Issues

If OAuth authentication fails:

1. Verify the Google Cloud Console APIs are enabled
2. Check redirect URIs in Google Cloud Console
3. Try re-authenticating by restarting Claude Code

### Tool Not Found

If Google Workspace tools aren't available:

1. Enable the MCP server:
   ```
   /mcp enable google-workspace
   ```

2. Check MCP server status:
   ```
   /mcp list
   ```

## Security Notes

- OAuth credentials are stored securely by the MCP server
- API keys should be kept confidential
- For production use, consider using service accounts
- Tokens are stored locally and not shared

## Next Steps

1. **Test the Setup**: Run `/mcp list` to verify the server is running
2. **Create Sample Content**: Use the agent to create a test presentation
3. **Review Output**: Check Google Drive for generated files
4. **Iterate**: Refine prompts and content structure

## Resources

- [Google Workspace MCP Server GitHub](https://github.com/taylorwilsdon/google_workspace_mcp)
- [Google AI Studio Documentation](https://ai.google.dev/docs)
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
