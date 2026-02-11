import sys
import re

path = "_layouts/default.html"

# This template perfectly mirrors the Agiflow structure you wanted
new_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }} | Karthik Krishnamurthy</title>
    
    <link rel="stylesheet" href="https://rsms.me/inter/inter.css">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --text-main: #111827;
            --text-muted: #6b7280;
            --accent: #059669;
            --border: #f3f4f6;
            --bg-subtle: #f9fafb;
        }

        body {
            font-family: 'Inter', -apple-system, sans-serif;
            color: var(--text-main);
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: #ffffff;
            -webkit-font-smoothing: antialiased;
        }

        /* 1. LAYOUT: The Agiflow Grid */
        .site-container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        nav.main-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 100px;
        }

        nav.main-nav .logo {
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700;
            font-size: 1rem;
            text-decoration: none;
            color: #000;
            letter-spacing: -0.02em;
        }

        .grid-layout {
            display: grid;
            grid-template-columns: 1fr 240px;
            gap: 80px;
            align-items: start;
        }

        /* 2. TYPOGRAPHY: Clean & Technical */
        article {
            max-width: 720px;
        }

        .category-tag {
            background: var(--accent);
            color: white;
            padding: 4px 12px;
            border-radius: 99px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 16px;
        }

        h1 {
            font-family: 'JetBrains Mono', monospace;
            font-size: 2.5rem;
            font-weight: 700;
            line-height: 1.2;
            margin: 0 0 16px 0;
            letter-spacing: -0.03em;
            color: #111;
        }

        .post-meta {
            font-size: 0.95rem;
            color: var(--text-muted);
            margin-bottom: 48px;
            display: block;
        }

        h2 {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.6rem;
            font-weight: 700;
            margin: 3em 0 1.2em 0;
            color: #111;
        }

        p {
            margin-bottom: 1.6em;
            font-size: 1.1rem;
        }

        /* 3. SIDEBAR: Sticky TOC */
        .sidebar {
            position: sticky;
            top: 40px;
            border-left: 1px solid var(--border);
            padding-left: 24px;
        }

        .sidebar-title {
            font-size: 0.75rem;
            text-transform: uppercase;
            font-weight: 700;
            color: var(--text-muted);
            letter-spacing: 0.05em;
            margin-bottom: 20px;
        }

        #toc {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        #toc li {
            margin-bottom: 12px;
        }

        #toc a {
            text-decoration: none;
            color: var(--text-muted);
            font-size: 0.9rem;
            transition: color 0.2s;
        }

        #toc a:hover {
            color: #000;
        }

        /* 4. CODE: Documentation Style */
        pre {
            background: var(--bg-subtle) !important;
            border: 1px solid var(--border) !important;
            border-radius: 8px;
            padding: 24px !important;
            margin: 2.5em 0 !important;
            overflow-x: auto;
        }

        code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9em;
        }

        @media (max-width: 1000px) {
            .grid-layout { grid-template-columns: 1fr; }
            .sidebar { display: none; }
        }
    </style>
</head>
<body>

    <div class="site-container">
        <nav class="main-nav">
            <a href="/" class="logo">KARTHIK.DEV</a>
            <div style="display:flex; gap:32px;">
                <a href="/" style="text-decoration:none; color:var(--text-muted); font-size:0.95rem; font-weight:500;">Home</a>
                <a href="/about" style="text-decoration:none; color:var(--text-muted); font-size:0.95rem; font-weight:500;">About</a>
            </div>
        </nav>

        <div class="grid-layout">
            <article id="post-content">
                <header>
                    <span class="category-tag">Systems & AI</span>
                    <h1>{{ page.title }}</h1>
                    <span class="post-meta">
                        {{ page.date | date: "%B %d, %Y" }} • By Karthik Krishnamurthy
                    </span>
                </header>

                {{ content }}
            </article>

            <aside class="sidebar">
                <div class="sidebar-title">On this page</div>
                <ul id="toc"></ul>
            </aside>
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const toc = document.getElementById("toc");
            const headers = document.querySelectorAll("#post-content h2");
            headers.forEach(h => {
                const id = h.innerText.toLowerCase().replace(/[^a-z0-9]+/g, "-");
                h.setAttribute("id", id);
                const li = document.createElement("li");
                const a = document.createElement("a");
                a.href = "#" + id;
                a.innerText = h.innerText;
                li.appendChild(a);
                toc.appendChild(li);
            });
        });
    </script>
</body>
</html>
"""

with open(path, "w") as f:
    f.write(new_html)

print(f"Successfully updated {path} with the Agiflow template.")
