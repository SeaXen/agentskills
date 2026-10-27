# Magentosh Agent Superpowers Suite

> **Category**: ⚡ Multi-Agent Workflows, Planning & Parallel Execution  
> **Source / Upstream URL**: [https://github.com/magentosh/superpowers](https://github.com/magentosh/superpowers)  
> **Total Skills in Reserve**: 86 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate affirmations
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/magentosh-superpowers/skills/affirmations" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/magentosh-superpowers/skills/affirmations .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link affirmations
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\affirmations" ".agents\library\magentosh-superpowers\skills\affirmations"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/magentosh-superpowers/skills/affirmations" ".agents/skills/affirmations"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add magentosh/superpowers
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove affirmations
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/affirmations"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move affirmations --to hot
python .agents/library/activate_skill.py move affirmations --to reserve
```

---

## 📑 Included Skills Catalog (86 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`affirmations`** | "Reset your own trajectory when you're stuck, looping, or demoralized — read these affirmations, then re-ground and take one clean step. Use when: you... |
| **`agent-browser`** | "Browser automation for AI agents via inference.sh. Navigate web pages, interact with elements using @e refs, take screenshots, record video. Capabili... |
| **`agent-tools`** | "Run AI apps via inference.sh CLI - image generation, video creation, LLMs, search, 3D, Twitter automation. Models: FLUX, Veo, Gemini, Grok, Claude, S... |
| **`agent-ui`** | "Batteries-included agent component for React/Next.js from ui.inference.sh. One component with runtime, tools, streaming, approvals, and widgets built... |
| **`ai-automation-workflows`** | "Build automated AI workflows combining multiple models and services. Patterns: batch processing, scheduled tasks, event-driven pipelines, agent loops... |
| **`ai-avatar-video`** | "Create AI avatar and talking head videos via inference.sh CLI. Recommended: P-Video-Avatar (fastest, cheapest, built-in TTS). Also: OmniHuman, Fabric... |
| **`ai-content-pipeline`** | "Build multi-step AI content creation pipelines combining image, video, audio, and text. Workflow examples: generate image -> animate -> add voiceover... |
| **`ai-image-generation`** | "Generate AI images with GPT-Image-2, FLUX, Gemini, Grok, Seedream, Reve and 50+ models via inference.sh CLI. Models: GPT-Image-2, FLUX Dev LoRA, FLUX... |
| **`ai-marketing-videos`** | "Create AI marketing videos for ads, promos, product launches, and brand content. Models: Veo, Seedance, Wan, FLUX for visuals, Kokoro for voiceover. ... |
| **`ai-music-generation`** | "Generate AI music and songs with ElevenLabs, Diffrythm, Tencent Song Generation via inference.sh CLI. Models: ElevenLabs Music (up to 10 min, commerc... |
| **`ai-podcast`** | "Generate multi-person talking head podcast videos from scratch using AI — character creation, TTS, avatar animation, and video stitching. Use when th... |
| **`ai-podcast-creation`** | "Create AI-powered podcasts with text-to-speech, music, and audio editing. Tools: Kokoro TTS, DIA TTS, Chatterbox, AI music generation, media merger. ... |
| **`ai-product-photography`** | "Generate professional AI product photography and commercial images. Models: FLUX, Imagen 3, Grok, Seedream for product shots, lifestyle images, mocku... |
| **`ai-rag-pipeline`** | "Build RAG (Retrieval Augmented Generation) pipelines with web search and LLMs. Tools: Tavily Search, Exa Search, Exa Answer, Claude, GPT-4, Gemini vi... |
| **`ai-social-media-content`** | "Create AI-powered social media content for TikTok, Instagram, YouTube, Twitter/X. Generate: images, videos, reels, shorts, thumbnails, captions, hash... |
| **`ai-video-generation`** | "Generate AI videos with Google Veo, Seedance 2.0, HappyHorse, Wan, Grok and 40+ models via inference.sh CLI. Models: Veo 3.1, Veo 3, Seedance 2.0, Ha... |
| **`ai-voice-cloning`** | "AI voice generation, text-to-speech, and voice synthesis via inference.sh CLI. Models: Inworld TTS-2 (100+ languages, emotion/non-verbal steering), I... |
| **`app-store-screenshots`** | "App Store and Google Play screenshot creation with exact platform specs. Covers iOS/Android dimensions, gallery ordering, device mockups, and preview... |
| **`background-removal`** | "Remove backgrounds from images with BiRefNet via inference.sh CLI. Model: BiRefNet (high accuracy background removal). Use for: product photos, portr... |
| **`book-cover-design`** | "Book cover design with genre-specific conventions, typography rules, and AI image generation. Covers fiction and non-fiction genres, sizing, thumbnai... |
| **`building-inferencesh-apps`** | "Build and deploy applications on inference.sh. Use when getting started, understanding the platform, creating apps, configuring resources, or needing... |
| **`case-study-writing`** | "B2B case study writing with STAR framework, data visualization, and research. Covers structure, customer quotes, metrics presentation, and distributi... |
| **`character-design-sheet`** | "Character consistency across AI-generated images with reference sheets and LoRA techniques. Covers turnaround views, expression sheets, color palette... |
| **`chat-ui`** | "Chat UI building blocks for React/Next.js from ui.inference.sh. Components: container, messages, input, typing indicators, avatars. Capabilities: cha... |
| **`competitor-teardown`** | "Structured competitive analysis with feature matrices, SWOT, positioning maps, and UX review. Covers research frameworks, pricing comparison, review ... |
| **`content-repurposing`** | "Content atomization — turn one piece of content into many formats. Covers blog-to-thread, blog-to-carousel, podcast-to-blog, video-to-quotes, and mor... |
| **`customer-persona`** | "Research-backed customer persona creation with market data and avatar generation. Covers demographics, psychographics, jobs-to-be-done, journey mappi... |
| **`data-visualization`** | "Data visualization with chart selection, color theory, and annotation best practices. Covers chart types (bar, line, scatter, heatmap), axes rules, a... |
| **`dialogue-audio`** | "Multi-speaker dialogue audio creation with ElevenLabs and Dia TTS. Covers speaker tags, emotion control, pacing, conversation flow, and post-producti... |
| **`elevenlabs-dialogue`** | "ElevenLabs multi-speaker dialogue generation - create conversations with different voices in a single audio file via inference.sh CLI. Capabilities: ... |
| **`elevenlabs-dubbing`** | "ElevenLabs automatic dubbing - translate and dub audio/video into 29 languages while preserving speaker voice via inference.sh CLI. Capabilities: aut... |
| **`elevenlabs-music`** | "ElevenLabs AI music generation - create original music from text prompts via inference.sh CLI. Capabilities: text-to-music, custom duration up to 10 ... |
| **`elevenlabs-sound-effects`** | "Generate AI sound effects from text descriptions with ElevenLabs via inference.sh CLI. Capabilities: text-to-sound-effect, custom duration, royalty-f... |
| **`elevenlabs-stt`** | "ElevenLabs speech-to-text with Scribe models and forced alignment via inference.sh CLI. Models: Scribe v1/v2 (98%+ accuracy, 90+ languages). Capabili... |
| **`elevenlabs-tts`** | "ElevenLabs text-to-speech with 22+ premium voices, multilingual support, and voice tuning via inference.sh CLI. Models: eleven_multilingual_v2 (highe... |
| **`elevenlabs-voice-changer`** | "ElevenLabs voice changer - transform any voice to a different voice while preserving speech content and emotion via inference.sh CLI. Models: eleven_... |
| **`elevenlabs-voice-isolator`** | "ElevenLabs voice isolator - remove background noise and isolate vocals from audio via inference.sh CLI. Capabilities: noise removal, voice extraction... |
| **`email-design`** | "Email marketing design with layout patterns, subject line formulas, and deliverability rules. Covers welcome sequences, promotional emails, transacti... |
| **`explainer-video-guide`** | "Explainer video production guide: scripting, voiceover, visuals, and assembly. Covers script formulas, pacing rules, scene planning, and multi-tool p... |
| **`flux-image`** | "Generate images with FLUX models (Black Forest Labs) via inference.sh CLI. Models: FLUX Dev LoRA, FLUX.2 Klein LoRA with custom style adaptation. Cap... |
| **`google-veo`** | "Generate videos with Google Veo models via inference.sh CLI. Models: Veo 3.1, Veo 3.1 Fast, Veo 3, Veo 3 Fast, Veo 2. Capabilities: text-to-video, ci... |
| **`gpt-image`** | "Generate and edit images with OpenAI GPT-Image-2 via inference.sh CLI. Models: GPT-Image-2. Capabilities: text-to-image, image editing, inpainting, m... |
| **`happyhorse`** | "Generate and edit videos with Alibaba HappyHorse 1.0 models via inference.sh CLI. Models: HappyHorse T2V, I2V, R2V, Video Edit. Capabilities: text-to... |
| **`image-to-video`** | "Still-to-video conversion guide: model selection, motion prompting, and camera movement. Covers Wan 2.5 i2v, Seedance, Fabric, Grok Video with when t... |
| **`image-upscaling`** | "Upscale and enhance images with Real-ESRGAN, Thera, Topaz, FLUX Upscaler via inference.sh CLI. Models: Real-ESRGAN, Thera (any size), FLUX Dev Upscal... |
| **`infsh-cli`** | "Run AI apps via inference.sh CLI - image generation, video creation, LLMs, search, 3D, Twitter automation. Models: FLUX, Veo, Gemini, Grok, Claude, S... |
| **`javascript-sdk`** | "JavaScript/TypeScript SDK for inference.sh - run AI apps, build agents, integrate with all models. Package: @inferencesh/sdk (npm install). Full Type... |
| **`landing-page-design`** | "Landing page conversion optimization with layout rules, hero section design, and CTA psychology. Covers above-the-fold formula, social proof placemen... |
| **`linkedin-content`** | "LinkedIn post writing with hook formulas, formatting rules, and engagement patterns. Covers post types, algorithm signals, character limits, and cont... |
| **`llm-models`** | "Access Claude, Gemini, Kimi, GLM and 100+ LLMs via inference.sh CLI using OpenRouter. Models: Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, G... |
| **`logo-design-guide`** | "Logo design principles and AI image generation best practices for creating logos. Covers logo types, prompting techniques, scalability rules, and ite... |
| **`nano-banana`** | "Generate images with Google Gemini native image models via inference.sh CLI. Models: Gemini 3 Pro Image, Gemini 2.5 Flash Image. Capabilities: text-t... |
| **`nano-banana-2`** | "Generate images with Google Gemini 3.1 Flash Image Preview (Nano Banana 2) via inference.sh CLI. Capabilities: text-to-image, image editing, multi-im... |
| **`newsletter-curation`** | "Newsletter curation with content sourcing, editorial structure, and subscriber growth strategies. Covers issue formatting, link roundups, commentary ... |
| **`og-image-design`** | "Open Graph and social sharing image design with platform specs, text placement, and branding. Covers OG meta tags, Twitter cards, LinkedIn previews, ... |
| **`p-image`** | "Generate images with Pruna P-Image models via inference.sh CLI. Models: P-Image, P-Image-LoRA, P-Image-Edit, P-Image-Edit-LoRA. Capabilities: text-to... |
| **`p-video`** | "Generate videos with Pruna P-Video and WAN models via inference.sh CLI. Models: P-Video, WAN-T2V, WAN-I2V. Capabilities: text-to-video, image-to-vide... |
| **`p-video-avatar`** | "Generate talking head avatar videos with Pruna P-Video-Avatar via inference.sh CLI. Turn a portrait image into a realistic speaking video with built-... |
| **`pitch-deck-visuals`** | "Investor pitch deck structure with slide-by-slide framework, visual design rules, and data presentation. Covers the 12-slide framework, chart types, ... |
| **`press-release-writing`** | "Press release writing in AP style with inverted pyramid structure. Covers formatting, datelines, quotes, boilerplates, and fact-checking. Use for: pr... |
| **`product-changelog`** | "Product changelog and release notes that users actually read. Covers categorization, user-facing language, visuals, and distribution. Use for: releas... |
| **`product-hunt-launch`** | "Product Hunt launch optimization with specific specs, timing, and gallery strategy. Covers taglines, gallery images, maker comments, and launch day t... |
| **`product-photography`** | "AI product photography with studio lighting, lifestyle shots, and packshot conventions. Covers angles, backgrounds, shadow types, hero shots, and e-c... |
| **`prompt-engineering`** | "Master prompt engineering for AI models: LLMs, image generators, video models. Techniques: chain-of-thought, few-shot, system prompts, negative promp... |
| **`python-executor`** | "Execute Python code in a safe sandboxed environment via [inference.sh](https://inference.sh). Pre-installed: NumPy, Pandas, Matplotlib, requests, Bea... |
| **`python-sdk`** | "Python SDK for inference.sh - run AI apps, build agents, and integrate with all models. Package: inferencesh (pip install inferencesh). Supports sync... |
| **`qwen-image-2`** | "Generate and edit images with Alibaba Qwen-Image-2.0 models via inference.sh CLI. Models: Qwen-Image-2.0 (fast), Qwen-Image-2.0-Pro (professional tex... |
| **`qwen-image-2-pro`** | "Generate images with Alibaba Qwen-Image-2.0-Pro via inference.sh CLI. Professional text rendering, fine-grained realism, enhanced semantic adherence.... |
| **`related-skill`** | "Discover and install related skills from inference.sh skill registry. Helps find complementary skills for your AI workflow. Use for: skill discovery,... |
| **`remotion-render`** | "Render videos from React/Remotion component code via inference.sh. Pass TSX code, get MP4. Supports all Remotion APIs: useCurrentFrame, useVideoConfi... |
| **`seedance`** | "Generate videos with ByteDance Seedance 2.0 via inference.sh CLI. Unified model for text-to-video, image-to-video, and reference-to-video with synchr... |
| **`seo-content-brief`** | "SEO content brief creation with keyword research, search intent analysis, and content structure. Covers SERP analysis, heading hierarchy, word count ... |
| **`social-media-carousel`** | "Multi-slide carousel design for Instagram, LinkedIn, and Twitter/X with layout rules and hooks. Covers slide structure, text hierarchy, swipe psychol... |
| **`speech-to-text`** | "Transcribe audio to text with ElevenLabs Scribe and Whisper models via inference.sh CLI. Models: ElevenLabs Scribe v2 (98%+ accuracy, diarization), F... |
| **`storyboard-creation`** | "Film and video storyboarding with shot vocabulary, continuity rules, and panel layout. Covers shot types, camera angles, movement, 180-degree rule, a... |
| **`talking-head-production`** | "Talking head video production with AI avatars, lipsync, and voiceover. Recommended: P-Video-Avatar (fastest, cheapest, built-in TTS). Also covers Omn... |
| **`technical-blog-writing`** | "Technical blog post writing with structure, code examples, and developer audience conventions. Covers post types, code formatting, explanation depth,... |
| **`text-to-speech`** | "Convert text to natural speech with Inworld TTS, ElevenLabs, DIA TTS, Kokoro, Chatterbox, and more via inference.sh CLI. Models: Inworld TTS-2 (100+ ... |
| **`tools-ui`** | "Tool lifecycle UI components for React/Next.js from ui.inference.sh. Display tool calls: pending, progress, approval required, results. Capabilities:... |
| **`twitter-automation`** | "Automate Twitter/X with posting, engagement, and user management via inference.sh CLI. Apps: x/post-tweet, x/post-create (with media), x/post-like, x... |
| **`twitter-thread-creation`** | "Twitter/X thread writing with hook tweets, thread structure, and engagement optimization. Covers tweet formatting, character limits, media attachment... |
| **`video-ad-specs`** | "Video ad creation with exact platform-specific specs for TikTok, Instagram, YouTube, Facebook, LinkedIn. Covers dimensions, duration limits, AIDA fra... |
| **`video-prompting-guide`** | "Best practices and techniques for writing effective AI video generation prompts. Covers: Veo, Seedance, Wan, Grok, Kling, Runway, Pika, Sora promptin... |
| **`web-search`** | "Web search and content extraction with Tavily and Exa via inference.sh CLI. Apps: Tavily Search, Tavily Extract, Exa Search, Exa Answer, Exa Extract.... |
| **`widgets-ui`** | "Declarative UI widgets from JSON for React/Next.js from ui.inference.sh. Render rich interactive UIs from structured agent responses. Capabilities: f... |
| **`youtube-thumbnail-design`** | "YouTube thumbnail design with specific dimensions, contrast rules, and mobile preview optimization. Covers safe zones, text placement, face expressio... |
