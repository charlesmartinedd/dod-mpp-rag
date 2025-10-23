"""
SOP Reference Embed Generator
Reads the reference mapping CSV and generates HTML embeds for Articulate Rise
"""

import csv
import os
from pathlib import Path


class ReferenceEmbedGenerator:
    """Generates HTML embeds from reference mapping data"""

    def __init__(self, csv_path, output_dir):
        self.csv_path = csv_path
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def read_references(self):
        """Read reference data from CSV file"""
        references = []
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                references.append(row)
        return references

    def generate_design_a(self, ref_data):
        """Generate Design A: Inline Link with Modal"""

        # Build reference items for modal
        ref_items = []

        if ref_data['SOP Section']:
            ref_items.append(f"""
                <div class="reference-item">
                    <div class="reference-label">MPP SOP</div>
                    <div class="reference-location">{ref_data['SOP Section']}, Pages {ref_data['SOP Page Numbers']}</div>
                    <div class="reference-description">
                        {ref_data['Reference Description']}
                    </div>
                </div>
            """)

        if ref_data['Appendix Section']:
            ref_items.append(f"""
                <div class="reference-item">
                    <div class="reference-label">{ref_data['Appendix Section']}</div>
                    <div class="reference-location">Pages {ref_data['Appendix Page Numbers']}</div>
                    <div class="reference-description">
                        {ref_data['Reference Description']}
                    </div>
                </div>
            """)

        ref_items_html = '\n'.join(ref_items)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOP Reference</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }}

        .sop-reference-compact {{
            margin-top: 20px;
            padding: 12px 16px;
            background: linear-gradient(135deg, #e8f4f8 0%, #f0f8fc 100%);
            border-left: 4px solid #0066cc;
            border-radius: 6px;
        }}

        .sop-reference-link {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #0066cc;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s ease;
            padding: 4px 8px;
            border-radius: 4px;
        }}

        .sop-reference-link:hover {{
            background: rgba(0, 102, 204, 0.1);
            color: #004999;
        }}

        .sop-reference-link svg {{
            width: 18px;
            height: 18px;
        }}

        .modal-overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            z-index: 1000;
            animation: fadeIn 0.2s ease;
            align-items: center;
            justify-content: center;
        }}

        .modal-overlay.active {{
            display: flex;
        }}

        .modal-content {{
            background: white;
            border-radius: 12px;
            width: 90%;
            max-width: 550px;
            max-height: 80vh;
            overflow-y: auto;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            animation: slideUp 0.3s ease;
        }}

        .modal-header {{
            background: linear-gradient(135deg, #1e3a5f 0%, #2a5082 100%);
            color: white;
            padding: 20px 24px;
            border-radius: 12px 12px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .modal-header h3 {{
            font-size: 18px;
            font-weight: 600;
        }}

        .close-btn {{
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            font-size: 20px;
        }}

        .close-btn:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: rotate(90deg);
        }}

        .modal-body {{
            padding: 24px;
        }}

        .reference-item {{
            background: #f8f9fa;
            border-left: 4px solid #0066cc;
            padding: 16px;
            border-radius: 6px;
            margin-bottom: 12px;
        }}

        .reference-item:last-child {{
            margin-bottom: 0;
        }}

        .reference-label {{
            color: #0066cc;
            font-weight: 600;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }}

        .reference-location {{
            color: #1e3a5f;
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 6px;
        }}

        .reference-description {{
            color: #555;
            font-size: 14px;
            line-height: 1.5;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        @keyframes slideUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @media (max-width: 768px) {{
            .modal-content {{
                width: 95%;
            }}
        }}
    </style>
</head>
<body>
    <div class="sop-reference-compact">
        <a class="sop-reference-link" onclick="openModal()">
            <svg fill="currentColor" viewBox="0 0 20 20">
                <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z"/>
            </svg>
            {ref_data['Reference Trigger Text']}
        </a>
    </div>

    <div class="modal-overlay" id="modalOverlay" onclick="closeModalOnOverlay(event)">
        <div class="modal-content" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3>SOP Reference</h3>
                <button class="close-btn" onclick="closeModal()">&times;</button>
            </div>
            <div class="modal-body">
                {ref_items_html}
            </div>
        </div>
    </div>

    <script>
        function openModal() {{
            document.getElementById('modalOverlay').classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeModal() {{
            document.getElementById('modalOverlay').classList.remove('active');
            document.body.style.overflow = 'auto';
        }}

        function closeModalOnOverlay(event) {{
            if (event.target === event.currentTarget) {{
                closeModal();
            }}
        }}

        document.addEventListener('keydown', function(event) {{
            if (event.key === 'Escape') {{
                closeModal();
            }}
        }});
    </script>
</body>
</html>"""
        return html

    def generate_design_b(self, ref_data):
        """Generate Design B: Expandable Bar"""

        # Build reference cards
        ref_cards = []
        ref_count = 0

        if ref_data['SOP Section']:
            ref_count += 1
            ref_cards.append(f"""
                <div class="reference-card">
                    <div class="card-label">MPP SOP</div>
                    <div class="card-location">{ref_data['SOP Section']}, Pages {ref_data['SOP Page Numbers']}</div>
                    <div class="card-description">
                        {ref_data['Reference Description']}
                    </div>
                </div>
            """)

        if ref_data['Appendix Section']:
            ref_count += 1
            ref_cards.append(f"""
                <div class="reference-card">
                    <div class="card-label">{ref_data['Appendix Section']}</div>
                    <div class="card-location">Pages {ref_data['Appendix Page Numbers']}</div>
                    <div class="card-description">
                        {ref_data['Reference Description']}
                    </div>
                </div>
            """)

        ref_cards_html = '\n'.join(ref_cards)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOP Reference</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }}

        .sop-reference-bar {{
            margin-top: 20px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}

        .sop-reference-header {{
            background: linear-gradient(135deg, #1e3a5f 0%, #2a5082 100%);
            color: white;
            padding: 12px 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.3s ease;
        }}

        .sop-reference-header:hover {{
            background: linear-gradient(135deg, #2a5082 0%, #1e3a5f 100%);
        }}

        .header-left {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .header-icon {{
            width: 20px;
            height: 20px;
        }}

        .header-text {{
            font-weight: 600;
            font-size: 14px;
        }}

        .header-badge {{
            background: rgba(255, 255, 255, 0.2);
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 600;
            margin-left: 8px;
        }}

        .expand-icon {{
            width: 20px;
            height: 20px;
            transition: transform 0.3s ease;
        }}

        .sop-reference-header.expanded .expand-icon {{
            transform: rotate(180deg);
        }}

        .sop-reference-body {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease;
            background: white;
        }}

        .sop-reference-body.expanded {{
            max-height: 500px;
        }}

        .reference-content {{
            padding: 20px;
        }}

        .reference-card {{
            background: #f8f9fa;
            border-left: 4px solid #0066cc;
            padding: 14px;
            border-radius: 6px;
            margin-bottom: 12px;
        }}

        .reference-card:last-child {{
            margin-bottom: 0;
        }}

        .card-label {{
            color: #0066cc;
            font-weight: 700;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }}

        .card-location {{
            color: #1e3a5f;
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 6px;
        }}

        .card-description {{
            color: #555;
            font-size: 13px;
            line-height: 1.5;
        }}

        @media (max-width: 768px) {{
            .header-text {{
                font-size: 13px;
            }}

            .header-badge {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="sop-reference-bar">
        <div class="sop-reference-header" onclick="toggleReference(this)">
            <div class="header-left">
                <svg class="header-icon" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z"/>
                </svg>
                <span class="header-text">SOP Reference</span>
                <span class="header-badge">{ref_count} ref{"s" if ref_count > 1 else ""}</span>
            </div>
            <svg class="expand-icon" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/>
            </svg>
        </div>
        <div class="sop-reference-body">
            <div class="reference-content">
                {ref_cards_html}
            </div>
        </div>
    </div>

    <script>
        function toggleReference(header) {{
            const body = header.nextElementSibling;
            header.classList.toggle('expanded');
            body.classList.toggle('expanded');
        }}
    </script>
</body>
</html>"""
        return html

    def generate_design_c(self, ref_data):
        """Generate Design C: Minimal Accordion"""

        # Build reference items
        ref_items = []
        ref_count = 0

        if ref_data['SOP Section']:
            ref_count += 1
            ref_items.append(f"""
                <div class="ref-item">
                    <div class="ref-meta">
                        <span class="ref-tag">SOP</span>
                        <span class="ref-location">{ref_data['SOP Section']}, Pages {ref_data['SOP Page Numbers']}</span>
                    </div>
                    <div class="ref-desc">
                        {ref_data['Reference Description']}
                    </div>
                </div>
            """)

        if ref_data['Appendix Section']:
            ref_count += 1
            ref_items.append(f"""
                <div class="ref-item">
                    <div class="ref-meta">
                        <span class="ref-tag">{ref_data['Appendix Section']}</span>
                        <span class="ref-location">Pages {ref_data['Appendix Page Numbers']}</span>
                    </div>
                    <div class="ref-desc">
                        {ref_data['Reference Description']}
                    </div>
                </div>
            """)

        ref_items_html = '\n'.join(ref_items)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOP Reference</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }}

        .sop-reference-minimal {{
            margin-top: 20px;
            border: 1px solid #dee2e6;
            border-radius: 6px;
            overflow: hidden;
        }}

        .minimal-trigger {{
            background: white;
            padding: 10px 14px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.2s ease;
            border-left: 3px solid #0066cc;
        }}

        .minimal-trigger:hover {{
            background: #f8f9fa;
        }}

        .trigger-content {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .trigger-icon {{
            width: 16px;
            height: 16px;
            color: #0066cc;
        }}

        .trigger-text {{
            color: #495057;
            font-size: 13px;
            font-weight: 600;
        }}

        .trigger-count {{
            background: #e8f4f8;
            color: #0066cc;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 11px;
            font-weight: 600;
            margin-left: 6px;
        }}

        .chevron {{
            width: 16px;
            height: 16px;
            color: #6c757d;
            transition: transform 0.3s ease;
        }}

        .minimal-trigger.expanded .chevron {{
            transform: rotate(180deg);
        }}

        .minimal-body {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
            background: #fafafa;
        }}

        .minimal-body.expanded {{
            max-height: 400px;
        }}

        .minimal-content {{
            padding: 16px;
        }}

        .ref-item {{
            background: white;
            border-left: 3px solid #0066cc;
            padding: 12px;
            border-radius: 4px;
            margin-bottom: 10px;
        }}

        .ref-item:last-child {{
            margin-bottom: 0;
        }}

        .ref-meta {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 6px;
        }}

        .ref-tag {{
            background: #0066cc;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .ref-location {{
            color: #1e3a5f;
            font-size: 14px;
            font-weight: 600;
        }}

        .ref-desc {{
            color: #6c757d;
            font-size: 13px;
            line-height: 1.4;
        }}

        @media (max-width: 768px) {{
            .trigger-text {{
                font-size: 12px;
            }}

            .trigger-count {{
                font-size: 10px;
                padding: 2px 6px;
            }}
        }}
    </style>
</head>
<body>
    <div class="sop-reference-minimal">
        <div class="minimal-trigger" onclick="toggleMinimal(this)">
            <div class="trigger-content">
                <svg class="trigger-icon" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
                </svg>
                <span class="trigger-text">{ref_data['Reference Trigger Text']}</span>
                <span class="trigger-count">{ref_count}</span>
            </div>
            <svg class="chevron" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/>
            </svg>
        </div>
        <div class="minimal-body">
            <div class="minimal-content">
                {ref_items_html}
            </div>
        </div>
    </div>

    <script>
        function toggleMinimal(trigger) {{
            const body = trigger.nextElementSibling;
            trigger.classList.toggle('expanded');
            body.classList.toggle('expanded');
        }}
    </script>
</body>
</html>"""
        return html

    def generate_all_embeds(self):
        """Generate all HTML embeds from CSV data"""
        references = self.read_references()

        print(f"Generating embeds for {len(references)} references...")

        for idx, ref in enumerate(references, 1):
            module_num = ref['Module Number']
            section_safe = ref['Lesson Section Title'].replace(' ', '_').replace('/', '_')
            design = ref['Design Choice'].upper()

            # Generate filename
            filename = f"module_{module_num}_{section_safe}_design_{design}.html"
            filepath = self.output_dir / filename

            # Generate HTML based on design choice
            if design == 'A':
                html = self.generate_design_a(ref)
            elif design == 'B':
                html = self.generate_design_b(ref)
            elif design == 'C':
                html = self.generate_design_c(ref)
            else:
                print(f"Warning: Unknown design '{design}' for row {idx}, using Design B")
                html = self.generate_design_b(ref)

            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)

            print(f"  [OK] Generated: {filename}")

        print(f"\nAll embeds generated successfully in: {self.output_dir}")
        print(f"\nTo use in Articulate Rise:")
        print("1. Open your Rise course")
        print("2. Add an 'Embed' block below the lesson section")
        print("3. Copy the HTML content from the generated file")
        print("4. Paste into the Rise embed block")
        print("5. Publish and preview!")


def main():
    """Main execution"""
    csv_path = "reference_mapping_template.csv"
    output_dir = "generated_embeds"

    generator = ReferenceEmbedGenerator(csv_path, output_dir)
    generator.generate_all_embeds()


if __name__ == "__main__":
    main()
