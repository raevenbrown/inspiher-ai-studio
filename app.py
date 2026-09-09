setScreen("screen1");
// Warm espresso studio background
setProperty("screen1", "background-color", "#1C1614");

// 1. Header (Studio Gold Accent)
textLabel("titleLabel", "The Brown Girls AI Studio");
setPosition("titleLabel", 10, 15, 300, 30);
setProperty("titleLabel", "text-color", "#D4AF37");
setProperty("titleLabel", "font-size", 17);
setProperty("titleLabel", "text-align", "center");

// 2. Persona Selection
textLabel("roleLabel", "Select Advisory Lens:");
setPosition("roleLabel", 20, 55, 280, 20);
setProperty("roleLabel", "text-color", "#FDF8F5");

dropdown("botRole", "Creative Entrepreneur", "Content & Brand Strategy", "Operations & Automation", "Brand Identity & Design", "Client Acquisition");
setPosition("botRole", 20, 80, 280, 30);

// 3. Prompt Input
textInput("userInput", "");
setPosition("userInput", 20, 125, 280, 35);
setProperty("userInput", "placeholder", "Ask any question here...");

// 4. Run Button (Terracotta Accent)
button("sendBtn", "Generate Strategic Plan ✨");
setPosition("sendBtn", 20, 175, 280, 40);
setProperty("sendBtn", "background-color", "#C86D51");
setProperty("sendBtn", "text-color", "#FFFFFF");

// 5. Output Area (Dark Card Surface)
textArea("outputBox", "Your strategic action plan will appear here!");
setPosition("outputBox", 20, 230, 280, 180);
setProperty("outputBox", "background-color", "#261F1D");
setProperty("outputBox", "text-color", "#FDF8F5");
setProperty("outputBox", "readonly", true);

// Global Typing Timer
var typeTimer = null;

// Dynamic Placeholders on Persona Selection
onEvent("botRole", "change", function() {
  var selected = getText("botRole");
  if (selected === "Creative Entrepreneur") {
    setProperty("userInput", "placeholder", "e.g., How to package services to make $10k?");
  } else if (selected === "Content & Brand Strategy") {
    setProperty("userInput", "placeholder", "e.g., How to edit videos that get clients?");
  } else if (selected === "Operations & Automation") {
    setProperty("userInput", "placeholder", "e.g., How to automate client onboarding?");
  } else if (selected === "Brand Identity & Design") {
    setProperty("userInput", "placeholder", "e.g., How to build a luxury aesthetic?");
  } else if (selected === "Client Acquisition") {
    setProperty("userInput", "placeholder", "e.g., How to pitch corporate clients?");
  }
});

// Click Handler
onEvent("sendBtn", "click", function() {
  var rawPrompt = getText("userInput").trim();
  var persona = getText("botRole");
  
  if (rawPrompt === "") {
    setText("outputBox", "⚠️ Please enter your business goal or question above!");
    return;
  }
  
  if (typeTimer) {
    clearInterval(typeTimer);
  }
  
  setProperty("sendBtn", "text", "Synthesizing Blueprint... ⏳");
  setProperty("sendBtn", "background-color", "#5A4E49");
  setText("outputBox", "🔍 Analyzing: \"" + rawPrompt + "\"...\nConsulting The Brown Girls Studio playbook...");
  
  setTimeout(function() {
    var response = searchKnowledgeBase(rawPrompt, persona);
    streamTextToBox("outputBox", response);
    setProperty("sendBtn", "text", "Generate Strategic Plan ✨");
    setProperty("sendBtn", "background-color", "#C86D51");
  }, 700);
});

// Universal AI Sentence & Topic Synthesizer
function searchKnowledgeBase(rawPrompt, persona) {
  var p = rawPrompt.toLowerCase().trim();
  var clean = rawPrompt.replace(/[?!.]/g, "").trim();

  var coreSubject = p
    .replace(/[?!.]/g, "")
    .replace(/^how (do|can|to|should) (i|we|you) /g, "")
    .replace(/^how (to|do|can) /g, "")
    .replace(/^what (is|are|does) /g, "")
    .replace(/^why (is|are|do|does) /g, "")
    .replace(/^can (i|you) /g, "")
    .trim();

  var topic = coreSubject.charAt(0).toUpperCase() + coreSubject.slice(1);
  if (topic === "") { topic = clean; }

  // 1. BUSINESS & $10k MONETIZATION
  if (persona === "Creative Entrepreneur" || p.indexOf("10k") !== -1 || p.indexOf("money") !== -1 || p.indexOf("sell") !== -1 || p.indexOf("price") !== -1) {
    return "💼 [The Brown Girls Studio • Business]\n\n" +
      "Roadmap for \"" + clean + "\":\n\n" +
      "• Step 1 (Offer Clarity): Package high-touch services into fixed retainers instead of trading hours for dollars.\n" +
      "• Step 2 (Unit Economics): Break $10k into simple units—four $2,500 clients or five $2,000 monthly retainers.\n" +
      "• Step 3 (Validation): Secure 3 pilot clients through personalized discovery before spending on paid ads!";
  }

  // 2. CONTENT CREATION & HOOKS
  if (persona === "Content & Brand Strategy" || p.indexOf("video") !== -1 || p.indexOf("post") !== -1 || p.indexOf("tiktok") !== -1 || p.indexOf("views") !== -1 || p.indexOf("content") !== -1) {
    return "🎬 [The Brown Girls Studio • Content Lab]\n\n" +
      "Strategy for \"" + clean + "\":\n\n" +
      "• Step 1 (1.5s Hook): Start right in the action or challenge a common industry mistake immediately.\n" +
      "• Step 2 (Lighting & Sound): Shoot facing natural window light—crisp audio builds more trust than fancy cameras.\n" +
      "• Step 3 (Call to Action): Ask viewers to comment a specific keyword to receive your automated checklist!";
  }

  // 3. WORKFLOW AUTOMATION & OPERATIONS
  if (persona === "Operations & Automation" || p.indexOf("automate") !== -1 || p.indexOf("system") !== -1 || p.indexOf("crm") !== -1 || p.indexOf("workflow") !== -1) {
    return "⚙️ [The Brown Girls Studio • Systems]\n\n" +
      "Operations plan for \"" + clean + "\":\n\n" +
      "• Step 1 (Map Journey): Draw your intake workflow from booking link to signed contract.\n" +
      "• Step 2 (No-Code Integration): Connect your contact form to your CRM using Zapier to eliminate manual copy-pasting.\n" +
      "• Step 3 (Client Delight): Automatically trigger personalized onboarding emails the moment payment clears!";
  }

  // 4. BRAND AESTHETICS & LUXURY DESIGN
  if (persona === "Brand Identity & Design" || p.indexOf("brand") !== -1 || p.indexOf("design") !== -1 || p.indexOf("aesthetic") !== -1 || p.indexOf("logo") !== -1) {
    return "✨ [The Brown Girls Studio • Brand Identity]\n\n" +
      "Design Strategy for \"" + clean + "\":\n\n" +
      "• Step 1 (Cohesive Palette): Use a signature deep neutral, warm mid-tone, and gold or terracotta accent.\n" +
      "• Step 2 (Typography Pair): Pair an editorial serif headline with a clean sans-serif body for premium authority.\n" +
      "• Step 3 (Proof Over Promises): Highlight client metrics and transformation case studies across your touchpoints!";
  }

  // 5. CLIENT ACQUISITION & OUTREACH
  if (persona === "Client Acquisition" || p.indexOf("client") !== -1 || p.indexOf("contract") !== -1 || p.indexOf("pitch") !== -1 || p.indexOf("lead") !== -1) {
    return "📈 [The Brown Girls Studio • Sales]\n\n" +
      "Pipeline plan for \"" + clean + "\":\n\n" +
      "• Step 1 (Warm Pipeline): Reconnect with past network contacts with an updated portfolio link.\n" +
      "• Step 2 (Targeted Audits): Send 10 hyper-personalized 2-minute video teardowns diagnosing quick operational wins.\n" +
      "• Step 3 (Speed to Lead): Deliver customized proposals within 24 hours of every discovery call!";
  }

  // 6. UNIVERSAL ADVISORY FALLBACK
  return "🤎 [The Brown Girls Studio • Advisory]\n\n" +
    "Guidance regarding \"" + clean + "\":\n\n" +
    "• Identify the Profit Driver: Focus on the single most revenue-generating step for " + topic.toLowerCase() + " this week.\n" +
    "• Execute in Sprints: Break implementation into two focused 45-minute blocks without distraction.\n" +
    "• Iterate Weekly: Review conversion metrics and client feedback every Friday to continually refine your offer!";
}

// Character Typing Stream Function
function streamTextToBox(elementId, fullText) {
  setText(elementId, "");
  var charIndex = 0;
  typeTimer = setInterval(function() {
    if (charIndex < fullText.length) {
      var current = getText(elementId);
      setText(elementId, current + fullText.charAt(charIndex));
      charIndex++;
    } else {
      clearInterval(typeTimer);
    }
  }, 14);
}
