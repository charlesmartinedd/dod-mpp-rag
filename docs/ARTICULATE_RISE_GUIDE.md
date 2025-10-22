# Articulate Rise Integration Guide

## Quick Setup for Articulate Rise

### What You Have
✅ **glossary.html** - A complete, self-contained glossary with 30+ DoD Mentor-Protégé Program terms
- **File size**: ~35 KB
- **No external dependencies** - works completely offline
- **Fully responsive** - adapts to any screen size and container

### Why This Works Great in Articulate Rise
- Single HTML file (no server needed)
- Fits perfectly in Web Object component
- Professional DoD-style design
- Fully functional on all devices
- Print-friendly

## Step-by-Step Implementation

### Option A: Upload Locally (Easiest)

1. **Prepare the File**
   - You have `glossary.html` ready to go
   - It's already self-contained with all terms embedded

2. **In Articulate Rise**
   - Open your course
   - Click where you want to add the glossary
   - Click **+ Add content** → **Web Object**
   - Click **Browse** and select `glossary.html`
   - Click **Insert**

3. **Configure Size**
   - Set **Width**: 100% (or 800px)
   - Set **Height**: 600px minimum (800px+ recommended)
   - Save and preview

### Option B: Host on Web Server (For Multiple Courses)

1. **Upload the File**
   - Upload `glossary.html` to your web server
   - Note the full URL (e.g., `https://yourserver.com/courses/glossary.html`)

2. **In Articulate Rise**
   - Click **+ Add content** → **Web Object**
   - Select **Web address**
   - Paste the URL
   - Click **Insert**

3. **Configure Size**
   - Set **Width**: 100%
   - Set **Height**: 600px+
   - Save and preview

## Responsive Design Specifics

The glossary automatically adapts to:

| Device | Behavior |
|--------|----------|
| **Desktop** | Full controls, optimal spacing |
| **Tablet** | Touch-friendly buttons, responsive layout |
| **Mobile** | Stacked controls, single-column list |
| **Rise Frame** | Perfect fit, no overflow issues |

### Recommended Sizing in Articulate Rise

**For Embedded (Full Width)**
- Width: 100%
- Height: 700-800px
- Best for: Course middle/end sections

**For Lightbox**
- Width: 900px (or 100%)
- Height: 600-700px
- Best for: Tooltips, references

**For Sidebar**
- Width: 400px
- Height: 600px+
- Best for: Glossary sidebar

## Features Your Learners Get

### Search
- Ctrl+F or click search box
- Search by term name, definition text, or example
- Real-time filtering

### Filters
- **All Terms** - Complete glossary
- **Acronyms** - Just DFARS, FAR, SBA, etc.
- **Roles** - Mentor, Protégé, Program Manager
- **Processes** - Operational procedures
- **Financial** - Budget and money terms

### Views
- **List View** (≡) - Traditional glossary, organized by category
- **Grid View** (⊟) - Card-based browsing

### Interactions
- Click any term to expand/collapse examples
- Click related terms to jump to definitions
- Print-friendly layout

## Troubleshooting in Articulate Rise

### "Content is cut off"
→ Increase height to 700-800px

### "Search not working"
→ Check browser JavaScript is enabled

### "Layout looks weird"
→ Try different width/height ratio (16:9 works well)

### "Takes too long to load"
→ This shouldn't happen (35 KB file, no external calls)
→ Try clearing browser cache

## Mobile Considerations

The glossary is fully mobile-optimized:
- Touch-friendly buttons and spacing
- Stacked layout on small screens
- Readable font sizes
- Proper scrolling behavior

## Customization Options

### Add More Terms
Edit the `glossaryData` array in glossary.html:

```javascript
{
    term: "New Term",
    type: "Process",
    category: "Operations",
    definition: "What this term means...",
    example: "How it's used in practice...",
    related: ["Related Term 1", "Related Term 2"]
}
```

### Change Colors
Search for `#1a3a52` and `#2d5a7b` in the CSS to replace DoD navy blue

### Add More Categories
- Add terms with new `category` values
- They'll automatically appear in the List View organization

## Performance Notes

✅ **Fast Loading** - 35 KB file, instant rendering
✅ **No Network Calls** - Everything self-contained
✅ **Smooth Interactions** - Optimized JavaScript
✅ **Print Ready** - Excellent PDF output

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile Safari, Chrome Mobile

## Publishing Checklist

- [ ] glossary.html copied to project
- [ ] Web Object component added to course
- [ ] Height/width configured (600px+ height recommended)
- [ ] Preview tested on desktop
- [ ] Preview tested on tablet
- [ ] Preview tested on mobile
- [ ] Print to PDF works
- [ ] Search function verified

## Need Help?

**File location**: `C:\Users\MarieLexisDad\claudeflow\rag\docs\glossary.html`

**File details**:
- Format: HTML5
- Size: ~35 KB
- Encoding: UTF-8
- JavaScript: Yes (required for interactivity)
- CSS: All embedded (no external files)

**Quick test**: Open glossary.html in any browser to verify it works before adding to Articulate Rise.

---

**You're all set!** The glossary is ready to embed in Articulate Rise. Just copy `glossary.html` to your course and follow the steps above.
