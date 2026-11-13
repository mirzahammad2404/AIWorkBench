# Add new prompts and guides here (one dict per item). Cover image: images/<slug>.webp
# Prompt cards need: slug, kind "prompt", ptype ("Video" or "Image"), cat, date, title, prompt, alt.
# Guides (kind "post") also need: meta, intro, sections [(h2, html)], faq [(question, answer)].
POSTS = [
 {"slug": "ai-video-character-swap-prompt", "kind": "prompt", "ptype": "Video", "cat": "Video editing", "date": "2026-10-20", "hue": 30,
  "alt": "AI-generated poster titled Unbreakable Paths showing a man in a navy suit and sunglasses seated in a director's chair while a black off-road 4x4 jumps over a desert dune behind him",
  "title": "AI Video Character Swap Prompt (Free Video-to-Video)",
  "prompt": """VIDEO-TO-VIDEO CHARACTER REPLACEMENT

Base video: [describe or upload your base video, for example "a 4x4 truck jumping over a desert dune"]
New character: [upload your character reference image]

TASK
Replace the main character in the base video with the character in the reference image. The new character must be an exact visual match to the reference image, keeping the same face, hairstyle, skin tone, body proportions, clothing and overall look.

MOTION
The new character must follow every movement of the original character: body position, gestures, walking style, head turns, facial expressions and eye contact. Motion must look natural and realistic from the first frame to the last.

KEEP UNCHANGED (100%)
Camera movement, framing, background, environment, lighting, shadows, color grading, timing and video length. Do not change any other people or objects in the scene.

SCENE INTERACTION
The new character must cast correct shadows, be hidden correctly behind objects when needed, and react to the environment as if they were filmed in the original scene.

AVOID
Face flicker, clothing that changes between frames, extra limbs, blurry edges around the character, and any added text, logos or watermarks."""},
 {"slug": "ai-video-prompt-3d-body-factory-comedy-reels", "kind": "prompt", "ptype": "Video", "cat": "Animation", "date": "2026-10-20", "hue": 10,
  "alt": "Petu Lal, a pink cartoon stomach character with a moustache, standing in a 3D body factory with burgers, biryani and noodles on conveyor belts",
  "title": "Free AI Video Prompt for 3D Body Factory Comedy Reels",
  "prompt": """Act as an expert viral short-form content strategist, 3D animation director, comedy scriptwriter and AI video prompt engineer. I am building a fictional animated comedy series called "Petu Lal: Body Factory Universe".

STEP 1: IDEAS
Generate 15 original reel ideas featuring Petu Lal, a funny anthropomorphic stomach, in a miniature fantasy body-factory world. For each idea give a short hook and the featured food. Rotate desi food, fast food, Chinese food, chocolates, desserts and snacks. Use visual gags, relatable eating habits and surprising but accurate digestion facts. Never repeat a dish I have already used. Dishes already used: [LIST YOUR USED DISHES HERE]. Do not promise guaranteed virality. After the list, ask me which idea number to produce.

STEP 2: THE REEL (after I pick a number)
Write one 30-second reel made of exactly 3 connected 10-second scenes. For every scene give 1 detailed image prompt and 1 detailed video prompt (6 prompts in total). Each video prompt must contain exactly 4 short, natural Roman Urdu/Hinglish dialogue lines, with no narrator, no extra dialogue and no silence.

STEP 3: POSTING PACK AND POSTER
Give a caption, a YouTube Shorts title, a small hashtag set, a TikTok AI description, a short science note and editing tips. Also write one 9:16 poster prompt for this episode, with the featured food as the main visual gag.

CHARACTERS (repeat these in every prompt)
- Petu Lal: cute pink bean-shaped anthropomorphic stomach, large expressive blue eyes, thick black moustache and beard, tiny arms, light-blue waist wrap. Sarcastic, dramatic, overworked factory manager.
- Worker microbes: tiny pink characters with eyes and blue uniforms.
- Brain Babu: cute pink anthropomorphic brain with expressive eyes, tiny hands and a small headset.

WORLD AND STYLE
Only the fictional internal body-factory universe: pink-red folded organic chamber walls, subtle red and blue veins, an overhead muscular tube, small conveyors and pipes, warm amber volumetric lighting, soft steam, glossy organic textures, subtle subsurface scattering, polished 3D family-animation look. Vertical 9:16, cinematic close-ups, shallow depth of field, expressive faces, simple movements.

STRICT RULES
No real humans, no human faces, no people eating, no kitchens, restaurants, bedrooms, weddings or outside-world cutaways. No gore, horror, text, subtitles, watermarks or logos inside generated scenes. Keep every prompt self-contained: repeat the full character descriptions, environment, food, lighting, camera and restrictions each time. Keep scenes simple: one food item, one conveyor, one or two characters, one camera move.

LANGUAGE
Explain to me in conversational Roman Urdu. Write all prompts in clear English and all character dialogue in Roman Urdu.

Start now with the 15 ideas only, then ask me to choose a number."""},
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
