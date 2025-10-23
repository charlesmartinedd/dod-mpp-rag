# SOP Reference System for Articulate Rise

A complete system for embedding beautiful SOP/Appendix I references into your DoD Mentor-Protégé Program training modules.

## Project Overview

This project provides:
1. Three professional compact design options for SOP references
2. A spreadsheet template for mapping references across all 10 modules
3. An automated HTML generator that creates Rise-ready embed code
4. Example files demonstrating the complete workflow

## Quick Start

### 1. Review the Design Options

Open `prototypes/compact/index.html` in your browser to see all three designs:

- **Design A: Inline Link** (~45px height, modal popup)
- **Design B: Expandable Bar** (DoD blue header, inline expansion) - **Recommended**
- **Design C: Minimal Accordion** (~40px height, ultra-subtle)

All designs are:
- Mobile-responsive
- Self-contained (no external dependencies)
- Accessible (keyboard navigation, ESC to close)
- Professional DoD corporate styling

### 2. Customize the Reference Mapping

Edit `reference_mapping_template.csv` with your actual SOP data:

**Column Guide:**
- **Module Number** - 1 through 10
- **Module Name** - Descriptive name (e.g., "Program Overview")
- **Lesson Section Title** - The specific section in Rise where this reference appears
- **Reference Trigger Text** - Text shown on the collapsed reference (e.g., "Where to find this in your SOP")
- **SOP Section** - Section number (e.g., "Section 1.2")
- **SOP Page Numbers** - Pages in the SOP (e.g., "8-10")
- **Appendix Section** - Appendix reference (e.g., "Appendix I") - leave blank if none
- **Appendix Page Numbers** - Pages in appendix - leave blank if none
- **Reference Description** - Brief description of what's covered
- **Design Choice** - A, B, or C (corresponds to the design options)
- **Notes** - Optional notes for your reference

**Example Row:**
```csv
1,Program Overview,Program Eligibility,Where to find this in your SOP,Section 1.2,8-10,Appendix I,1-3,Program overview and eligibility requirements,B,
```

**Tips:**
- Use 3-5 references per module
- Place references strategically where they add the most value
- Keep trigger text concise and action-oriented
- Design B is recommended for most use cases

### 3. Generate HTML Embeds

Run the generator script:

```bash
python generate_reference_embeds.py
```

This creates individual HTML files in the `generated_embeds/` folder, one for each row in your CSV.

**Output Files:**
- Naming convention: `module_{number}_{section}}_design_{A|B|C}.html`
- Example: `module_1_Program_Eligibility_design_B.html`

### 4. Embed in Articulate Rise

For each reference point in your Rise course:

1. **Add an Embed Block**
   - Navigate to the lesson section in Rise
   - Click the "+" button below the content
   - Select "Embed" from the block menu

2. **Copy the HTML**
   - Open the corresponding generated HTML file
   - Select all (Ctrl+A / Cmd+A)
   - Copy (Ctrl+C / Cmd+C)

3. **Paste into Rise**
   - In the Rise Embed block, paste the HTML
   - The reference will appear below your lesson content

4. **Preview and Publish**
   - Preview your course to test functionality
   - Ensure references expand/collapse properly
   - Check mobile responsiveness
   - Publish when satisfied

## File Structure

```
MPP DOD Rag/
├── prototypes/
│   ├── compact/
│   │   ├── index.html                        # Compare all 3 designs
│   │   ├── design_a_inline_link.html         # Design A demo
│   │   ├── design_b_expandable_bar.html      # Design B demo
│   │   └── design_c_minimal_accordion.html   # Design C demo
│   └── [original prototypes...]              # Full-page versions (superseded)
├── generated_embeds/                          # Generated HTML files (auto-created)
│   ├── module_1_Program_Eligibility_design_B.html
│   ├── module_1_Mentor_Requirements_design_B.html
│   └── ... (20 example files)
├── reference_mapping_template.csv             # YOUR DATA GOES HERE
├── generate_reference_embeds.py               # HTML generator script
└── README_SOP_REFERENCE_SYSTEM.md            # This file
```

## Customization Options

### Changing Colors

Each design uses DoD blue as the primary color. To customize:

1. Open the generated HTML file
2. Find the CSS `<style>` section
3. Replace color values:
   - DoD Blue: `#1e3a5f` → Your color
   - Accent Blue: `#0066cc` → Your color

### Changing Text

Edit the CSV template:
- **Reference Trigger Text**: Change the collapsed state text
- **Reference Description**: Update the expanded content

### Mixing Designs

You can use different designs for different modules:
- Simply change the "Design Choice" column in your CSV
- Run the generator again to create new files

## Example Workflow

Here's a complete example for Module 1:

1. **Review your Module 1 PDF** to identify 3-5 strategic reference points

2. **Add rows to CSV:**
   ```csv
   1,Program Overview,Program Eligibility,Where to find this in your SOP,Section 1.2,8-10,Appendix I,1-3,Program overview and eligibility requirements,B,
   1,Program Overview,Mentor Requirements,Where to find this in your SOP,Section 2.1,12-15,Appendix II,5-7,Detailed mentor qualification criteria,B,
   ```

3. **Run generator:**
   ```bash
   python generate_reference_embeds.py
   ```

4. **Open Rise:**
   - Navigate to Module 1 > Program Eligibility section
   - Add Embed block at the bottom
   - Copy/paste `module_1_Program_Eligibility_design_B.html`
   - Repeat for Mentor Requirements section

5. **Preview and adjust** as needed

## Technical Details

### Browser Compatibility
- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support
- Mobile browsers: Full support with touch-optimized interactions

### Accessibility Features
- Keyboard navigation (Tab, Enter, Escape)
- ARIA attributes for screen readers
- Focus indicators
- Semantic HTML structure

### Performance
- No external dependencies
- Minimal CSS/JS (< 10KB per embed)
- Smooth animations with CSS transitions
- No jQuery or large frameworks required

## Troubleshooting

### Generator Script Issues

**Problem:** CSV parsing errors
**Solution:** Ensure no commas in your descriptions, or wrap text in quotes

**Problem:** Unicode errors on Windows
**Solution:** Already handled in the script with UTF-8 encoding

### Rise Embedding Issues

**Problem:** HTML not displaying
**Solution:** Ensure you're copying the ENTIRE file contents, including `<!DOCTYPE html>`

**Problem:** Styling looks wrong
**Solution:** Rise may strip some styles - use the exact HTML from generated files without modifications

**Problem:** References too tall/short
**Solution:** Edit the max-height values in the CSS `<style>` section of the generated HTML

## Next Steps

1. **Review the compact designs** - Open `prototypes/compact/index.html` and pick your favorite
2. **Customize the CSV template** - Add your actual SOP references
3. **Generate your embeds** - Run the Python script
4. **Test in Rise** - Embed one file to verify it works
5. **Roll out to all modules** - Repeat for all 10 modules

## Support

For questions or customization requests, refer to:
- Design prototypes: `prototypes/compact/index.html`
- Generator script: `generate_reference_embeds.py`
- Example data: `reference_mapping_template.csv`
- Generated examples: `generated_embeds/` folder

## Version History

- **v1.0** - Initial release with three compact designs
- Full-page prototypes available in `prototypes/` folder (archived)
