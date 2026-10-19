# All site copy lives here. Edit freely, then commit; Netlify rebuilds automatically.
UPDATED = "October 19, 2026"

HOME_INTRO = """<section class="w sec intro"><h2>What is AI Workbench?</h2>
<p>AI Workbench is a free resource hub for people who want to use artificial intelligence without wasting hours searching. We collect, test and organise the best <strong>AI prompts</strong>, <strong>AI tools</strong> and <strong>step-by-step AI tutorials</strong> in one place, so you can find what works and use it today.</p>
<p>Think of us as a guide between you and the AI world. You tell us what you want to do, such as writing an email, planning a video or studying for an exam. We point you to a ready-made prompt or the right tool, and show you how to use it.</p></section>
<section class="w sec"><h2>How AI Workbench helps you</h2><div class="steps">
<div><h3>Find a prompt that works</h3><p>Browse free prompts for ChatGPT, Gemini and Claude. Copy one with a single tap, replace the brackets and paste it into your AI tool.</p></div>
<div><h3>Choose the right AI tool</h3><p>We compare AI tools in plain words, including what they do well, where they fall short and who they suit best.</p></div>
<div><h3>Learn the basics fast</h3><p>Our guides explain prompt engineering, AI writing, AI video and AI automation without jargon, so beginners can follow along.</p></div></div></section>
<section class="w sec"><h2>Who is AI Workbench for?</h2>
<p>Content creators who make TikTok, Instagram and YouTube videos. Freelancers and small business owners who want to save time. Students who want to study smarter. And anyone curious about AI who wants clear, practical help instead of hype.</p></section>"""

HOME_FAQ = [
 ("What is an AI prompt?", "An AI prompt is the instruction you type into an AI tool such as ChatGPT, Gemini or Claude. A clear prompt that names a role, a goal and a format gives you a much better answer."),
 ("Are the prompts on AI Workbench free?", "Yes. Every prompt and guide on the site is free to read and copy."),
 ("Which AI tools do the prompts work with?", "Most prompts work in ChatGPT, Google Gemini and Claude. Each prompt page says if it suits a particular tool."),
 ("How often is new content added?", "We publish new prompts and guides regularly. Follow us on TikTok, Instagram or Facebook to see them first."),
]

ABOUT = f"""<p class="lead">Our mission is simple: make AI easy to understand and useful in everyday life.</p>
<h2>Why AI Workbench exists</h2>
<p>New AI tools launch every week, and most advice online is either too technical or full of hype. Beginners end up with ten open tabs and no clear answer. AI Workbench was built to fix that by acting as a trusted guide between you and the AI world.</p>
<h2>What you will find here</h2>
<p><strong>AI prompts:</strong> ready-to-use prompts for writing, marketing, study, video and business. <strong>AI tool guides:</strong> plain-language explanations of popular tools and what each one is best for. <strong>Tutorials:</strong> step-by-step how-tos with real examples.</p>
<h2>How we create content</h2>
<p>We aim to publish only what is clear, useful and accurate. Prompts are tried before they go live, guides are written in simple words, and we update posts when tools change. If we recommend a paid tool, we say so openly (see our <a href="/disclaimer/">disclaimer</a>).</p>
<h2>How the site is funded</h2>
<p>AI Workbench is free to use. It is supported by advertising (Google AdSense) and, in some cases, affiliate links. This never changes what we recommend. If something is not good, we will say so.</p>
<h2>Join the community</h2>
<p>We share short AI tips on TikTok, Instagram and Facebook. Find the links in the footer, or <a href="/contact/">send us a message</a> with a prompt idea or a tool you want reviewed.</p>"""

CONTACT = """<p class="lead">Have a question, a prompt idea, a tool you want reviewed or a business enquiry? Send us a message and we will reply as soon as we can.</p>
<form name="contact" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="bot-field" class="form">
<input type="hidden" name="form-name" value="contact"><p hidden><label>Do not fill this in: <input name="bot-field"></label></p>
<label for="n">Your name</label><input id="n" name="name" required autocomplete="name">
<label for="em">Your email</label><input id="em" type="email" name="email" required autocomplete="email">
<label for="s">Subject</label><input id="s" name="subject" required>
<label for="m">Message</label><textarea id="m" name="message" rows="6" required></textarea>
<button class="btn" type="submit">Send message</button><div id="fm" role="status" aria-live="polite"></div></form>
<h2>Before you write</h2><p>We cannot give personal tech support, but we read every message about content ideas, corrections and partnerships.</p>"""

THANKS = "<p class=\"lead\">Thanks, your message has been sent. We will get back to you soon.</p><p><a class=\"btn\" href=\"/\">Back to home</a></p>"

PRIVACY = f"""<p><em>Last updated: {UPDATED}</em></p>
<p>This Privacy Policy explains how AI Workbench ("we", "us") collects, uses and protects information when you visit our website. By using the site you agree to this policy.</p>
<h2>Information we collect</h2>
<p>We do not require you to create an account. We may collect <strong>information you give us</strong>, such as your name, email address and message when you use our contact form, and <strong>information collected automatically</strong>, such as your browser type, device, pages viewed and approximate location, through cookies and similar technologies.</p>
<h2>How we use information</h2>
<p>We use information to reply to your messages, understand which content is helpful, keep the site secure and show advertising that supports the site.</p>
<h2>Cookies</h2>
<p>Cookies are small files stored on your device. We and our partners use them to remember preferences, measure traffic and serve ads. You can block or delete cookies in your browser settings, though some features may not work as expected.</p>
<h2>Google AdSense and advertising</h2>
<p>We use Google AdSense to display ads. Google and its partners use cookies, including the DoubleClick cookie, to show ads based on your visits to this and other websites. You can opt out of personalised advertising at <a href="https://adssettings.google.com" rel="noopener">Google Ads Settings</a> or at <a href="https://www.aboutads.info" rel="noopener">aboutads.info</a>. Learn how Google uses data at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com/technologies/partner-sites</a>. Visitors in the European Economic Area, the United Kingdom and Switzerland may see a consent message before personalised ads are shown.</p>
<h2>Analytics</h2>
<p>We may use Google Analytics to understand how visitors use the site. It collects anonymous usage data such as pages visited and time on site.</p>
<h2>Affiliate links</h2>
<p>Some links on the site are affiliate links. If you buy through them we may earn a commission at no extra cost to you. Those partners may set their own cookies.</p>
<h2>Third-party links and services</h2>
<p>Our site links to other websites and uses services such as Netlify for hosting and form handling. We are not responsible for the privacy practices of other sites.</p>
<h2>Children's privacy</h2>
<p>AI Workbench is not directed at children under 13, and we do not knowingly collect their personal information.</p>
<h2>Your rights</h2>
<p>Depending on where you live, you may have the right to access, correct or delete your personal data, or object to its use. Contact us through the <a href="/contact/">contact page</a> to make a request.</p>
<h2>Changes to this policy</h2>
<p>We may update this policy from time to time. The date at the top shows the latest version.</p>
<h2>Contact</h2><p>Questions about this policy? Use our <a href="/contact/">contact form</a>.</p>"""

TERMS = f"""<p><em>Last updated: {UPDATED}</em></p>
<p>Welcome to AI Workbench. By using this website you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Use of the website</h2><p>You may read, share and use the content for personal, non-commercial purposes. You agree not to misuse the site, attempt to disrupt it, scrape it at scale or use it for anything unlawful.</p>
<h2>Content and intellectual property</h2><p>Unless stated otherwise, the text, design and graphics on AI Workbench belong to us. You may quote short excerpts with a clear link back to the original page. You may not republish full articles without permission. Prompts may be freely copied and used in your own AI tools.</p>
<h2>AI-generated output</h2><p>Results from AI tools can be wrong or incomplete. Always check important information before relying on it. We do not control third-party AI tools and are not responsible for what they generate.</p>
<h2>Third-party links, ads and affiliate links</h2><p>The site contains links to other websites, advertisements and affiliate links. We do not control or endorse every third-party site, and we are not responsible for their content, products or policies.</p>
<h2>No warranties</h2><p>The site and its content are provided "as is" without warranties of any kind. We do not guarantee that content is always accurate, complete or up to date.</p>
<h2>Limitation of liability</h2><p>To the fullest extent allowed by law, AI Workbench is not liable for any loss or damage arising from your use of the site or reliance on its content.</p>
<h2>Changes</h2><p>We may update these terms at any time. Continued use of the site means you accept the updated terms.</p>
<h2>Contact</h2><p>Questions? Reach us through the <a href="/contact/">contact page</a>.</p>"""

DISCLAIMER = f"""<p><em>Last updated: {UPDATED}</em></p>
<h2>General information only</h2><p>Everything on AI Workbench is provided for general information and educational purposes. It is not professional, legal, financial, medical or business advice. Use your own judgement and consult a qualified professional when needed.</p>
<h2>Affiliate disclosure</h2><p>Some links on this site are affiliate links. If you click one and make a purchase or sign up, we may earn a commission at no extra cost to you. Affiliate relationships never decide what we recommend, and we only link to tools we believe are useful.</p>
<h2>Advertising disclosure</h2><p>AI Workbench displays ads through Google AdSense. Ads are served by Google and are not endorsements by us.</p>
<h2>AI tools and accuracy</h2><p>AI tools change quickly. Features, prices and limits may differ from what we describe. Prompts do not guarantee a particular result, and AI output may contain errors. Please verify important facts yourself.</p>
<h2>Trademarks</h2><p>ChatGPT, Gemini, Claude, CapCut, Canva and other names mentioned are trademarks of their owners. AI Workbench is independent and is not affiliated with or endorsed by them.</p>
<h2>External links</h2><p>We are not responsible for the content or practices of websites we link to.</p>"""
