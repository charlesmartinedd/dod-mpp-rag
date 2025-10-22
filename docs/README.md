# DoD Mentor-Protégé Program Glossary

A beautifully designed, fully self-contained, interactive HTML glossary for learning key terms and acronyms used in the DoD Mentor-Protégé Program. Perfect for embedding in Articulate Rise!

## ✨ Features

### **Professional Design**
- Navy blue and white DoD-style color scheme
- Fully responsive (desktop, tablet, mobile, embedded frames)
- Optimized for Articulate Rise Web Objects
- Smooth animations and transitions
- Beautiful typography and spacing

### **Self-Contained**
- All 30+ terms embedded directly in the HTML file
- No external dependencies or API calls needed
- Works completely offline once loaded
- Single file - just copy and paste!

### **Interactive Search & Navigation**
- Real-time search across terms, definitions, and examples
- Filter by type: All, Acronyms, Roles, Processes, Financial
- Toggle between List (categorized) and Grid (card) views
- Click any term to show/hide examples
- Click related terms to jump to related glossary entries

### **30+ Terms Covered**
- Legal Framework (10 U.S.C. 4902, DFARS, FAR)
- Roles (Mentor, Protégé, Program Manager, Prime Contractor)
- Processes (Agreements, Compliance, Audits, Monitoring)
- Financial Management (Reimbursement, Budgets, Goals, Credits)
- Operations (Developmental Assistance, Quality Systems, Training)
- Participants (SBA, DoD OSBP)

### **Articulate Rise Ready**
- Responsive to any container size
- No scrollbar conflicts with Rise frame
- Professional appearance in lightbox or embedded
- Mobile-friendly interaction patterns

### **Print Ready**
- Optimized for printing to PDF
- Professional layout on paper
- All details visible when printed

## 🚀 How to Use

### Quick Start - Direct File Access
Simply open `glossary.html` in any modern web browser - that's it!

### Embedding in Articulate Rise

**Step 1: Place the File**
- Copy `glossary.html` to your course assets folder, or
- Place it on a web server and note the URL

**Step 2: Add Web Object to Articulate Rise**
1. In your Articulate Rise course, click **+ Add content**
2. Select **Web Object**
3. Choose how to add the content:
   - **Local file**: Upload `glossary.html` from your computer
   - **Web address**: Enter the URL (e.g., `http://yourserver.com/glossary.html`)
4. Click **Insert**

**Step 3: Configure Display**
1. In the properties panel, set:
   - **Width**: 100% (or 800px minimum)
   - **Height**: 600px (or higher for more visible content)
   - **Launch in lightbox**: Optional (looks great either way!)
2. Click **Preview** to see it in action

**Step 4: Optimize (Optional)**
- Test on different screen sizes
- Adjust height based on your layout preferences
- Recommended: 800+ pixels wide, 600+ pixels tall

## Features Details

### Search (Ctrl+F)
- Click the search box or press Ctrl+F to focus
- Type any term, definition word, or acronym
- Results filter in real-time

### Filters
- Click filter buttons to show specific types of terms
- Filters work with search results

### Views
- **List View**: Organized by category, traditional glossary style
- **Grid View**: Card-based layout for visual browsing

### Expandable Details
- Click any term to show/hide examples
- Examples show practical usage context
- Related terms link to other glossary items

## Customization

To add more terms, edit the `glossaryData` array in the HTML file:

```javascript
{
    term: "Your Term",
    type: "Acronym|Role|Process|Financial|Compliance",
    category: "Category Name",
    definition: "Clear definition here",
    example: "Example of how it's used",
    related: ["Related Term 1", "Related Term 2"]
}
```

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (responsive design)

## File Structure

```
docs/
├── glossary.html          # Main glossary file
├── start_server.bat       # Windows server startup script
└── README.md              # This file
```

## Tips

- Use keyboard shortcut Ctrl+F to quickly jump to search
- Click terms in "Related Terms" section to jump between definitions
- Grid view is great for browsing, List view for studying
- Print to PDF for offline access and sharing
- Works completely offline once loaded (no external dependencies)

---

**Version**: 1.0
**Last Updated**: October 2025
**Program**: DoD Mentor-Protégé Program Learning Hub
