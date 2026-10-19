# Add new prompts and posts here (one dict per page). Cover image: images/<slug>.webp
# kind: "prompt" or "post". sections = [(h2, html)], faq = [(question, answer)]
POSTS = [
 {"slug": "chatgpt-cold-email-prompt", "kind": "prompt", "cat": "Marketing", "date": "2026-10-19", "hue": 150,
  "title": "ChatGPT Cold Email Prompt: Get More Replies in 2026",
  "meta": "Copy this free ChatGPT cold email prompt to rewrite any pitch into a short, human message that gets replies. Includes tips and examples.",
  "intro": "Most cold emails fail because they are long and about the sender. This free ChatGPT prompt rewrites your draft so it is short, specific and easy to answer.",
  "prompt": "Act as a senior copywriter. Rewrite my cold email in under 90 words. Open with something specific about the reader, explain my offer in one sentence, and end with one easy yes/no question. Keep a friendly tone and avoid buzzwords.\n\nMy draft:\n[paste your draft]",
  "sections": [
   ("How to use this prompt", "<p>Paste the prompt into ChatGPT, Gemini or Claude, then replace the brackets with your own draft. Add the reader's job title and one detail about their company for better results.</p>"),
   ("Why this prompt works", "<p>It gives the AI a role, a word limit and a clear ending. These three prompt engineering basics make the answer shorter and more useful.</p>"),
  ],
  "faq": [("Which AI tool works best for cold emails?", "ChatGPT, Gemini and Claude all work. Pick the one you already use and keep the same prompt.")]},
 {"slug": "how-to-write-better-ai-prompts", "kind": "post", "cat": "Guides", "date": "2026-10-19", "hue": 25,
  "title": "How to Write Better AI Prompts: 4 Simple Habits",
  "meta": "Learn how to write better AI prompts with four simple habits: role, goal, context and format. Beginner friendly, with examples.",
  "intro": "A prompt is the instruction you give an AI tool. Clear prompts get clear answers. Here are four habits that improve almost every result.",
  "sections": [
   ("1. Give the AI a role", "<p>Start with who the AI should be, for example a tutor, editor or marketer.</p>"),
   ("2. State the goal", "<p>Say exactly what you want back, such as five headlines or a one-page plan.</p>"),
   ("3. Add context", "<p>Share your audience, topic and limits so the AI does not guess.</p>"),
   ("4. Ask for a format", "<p>Request a list, table or word count. Formatting rules save editing time.</p>"),
  ],
  "faq": [("What is a prompt in AI?", "A prompt is the text instruction you type into an AI tool to get an answer, image or video.")]},
]
