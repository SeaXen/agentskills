# Batch Publishing Workflow — mdsagar.com

## Use Case
When the user says "post next topic", "post next 3", or "continue the batch", use this automated approach.

## Implementation Pattern (Python)
Since the environment and auth details are stable, use a script like this to process multiple notes in one turn.

```python
import subprocess, re, os, json, urllib.request, base64, time

def publish_batch(topics):
    token = base64.b64encode(f"{os.environ.get('WP_USERNAME')}:{os.environ.get('WP_APP_PASSWORD')}".encode()).decode()
    
    for topic in topics:
        # 1. Run hybrid publisher
        cmd = [
            "python3", "/root/.hermes/scripts/wp_mdsagar_hybrid_publish.py",
            "--source-note", topic['source'],
            "--title", topic['title'],
            "--slug", topic['slug'],
            "--category", topic['category'],
            "--style", "exam-hybrid",
            "--status", "publish",
            "--html-out", "/tmp/current_post.html"
        ]
        for t in topic['tags']: cmd.extend(["--tag", t])
        
        res_json = subprocess.check_output(cmd).decode()
        post_id = json.loads(res_json)['post_id']
        
        # 2. Post-process HTML (Nuclear dark mode + Mermaid inject)
        # Use re.sub to inject CSS style block and Mermaid script
        # and convert standard H3 headers to .mp-box structures.
        
        # 3. Update content
        subprocess.run(["python3", "/root/.hermes/scripts/wp_mdsagar_poster.py", "update-post", str(post_id), "--content-file", "/tmp/fixed.html"])
        
        # 4. Update SEO via standard REST endpoint
        update_seo_payload = {'meta': {'rank_math_focus_keyword': topic['keyword'], 'rank_math_title': topic['seo_title'], 'rank_math_description': topic['seo_desc']}}
        # ... fetch code from SKILL.md for Rank Math standard REST update ...
```

## Critical Post-Processing Steps
1.  **CSS Injection**: Inject a `<style>` block containing the "nuclear" dark mode overrides (forced `!important` colors for `.mp-box` elements).
2.  **Specialty Check**: Search for and replace "Nephrology/renal/KDIGO" remnants if the topic is Cardiology/Stroke/etc.
3.  **Mermaid**: Replace ` ```mermaid ` fences with `<pre class="mermaid">` and inject the Mermaid JS runtime.
4.  **Box Conversion**: Ensure the standard generated headers like `### Exam Pearls` are converted to the styled `<div class="mp-box mp-box-yellow">` containers.
