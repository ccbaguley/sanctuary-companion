import os
import sys
import hashlib
import time
import json
import urllib.request
import urllib.error

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:latest"

NL = chr(10)
ESC = chr(27)

VERIFIED_RESOURCES = {
    "NATIONAL_US": NL.join([
        "",
        "--- VERIFIED NATIONAL FINANCIAL & SUPPORT DIRECTORIES (U.S.) ---",
        "* General Local Bill, Rent & Utility Relief: Dial 211 or visit https://211.org",
        "* Federal Benefits & Financial Assistance Finder: https://benefits.gov",
        "* Pediatric Cancer Travel & Family Grants (Alex's Lemonade Stand): https://alexslemonade.org",
        "* Free Family Lodging Near Hospitals (Ronald McDonald House): https://rmhc.org",
        "* Pediatric Cancer Financial Aid (National Children's Cancer Society): https://thenccs.org",
        "* Medical Co-Pay & Prescription Relief (Patient Advocate Foundation): https://patientadvocate.org",
        "* 24/7 Free Confidential Crisis & Emotional Support: Call or text 988 | Text HOME to 741741"
    ]),
    "MINNESOTA": NL.join([
        "",
        "--- VERIFIED MINNESOTA FINANCIAL & MEDICAL RECOVERY RESOURCES ---",
        "* Minnesota 211 (Emergency Housing, Food & Utility Grants): Dial 211 or visit https://211unitedway.org",
        "* MN Medical Assistance & TEFRA Waiver (Pediatric Disability/Illness): https://mn.gov (Search: TEFRA)",
        "* Children & Youth with Special Health Needs (MDH): https://health.state.mn.us",
        "* Angel Foundation (Minnesota Adult & Pediatric Cancer Financial Relief): https://mnangel.org",
        "* Pinky Swear Foundation (MN-Based Pediatric Cancer Family Financial Aid): https://pinkyswear.org",
        "* Crime Victim & Safety Financial Reimbursement (MN DPS): https://mn.gov"
    ]),
    "INTERNATIONAL": NL.join([
        "",
        "--- VERIFIED INTERNATIONAL SUPPORT DIRECTORIES ---",
        "* Global Crisis & Mental Health Helplines: https://findahelpline.com",
        "* International Childhood Cancer Parent Organizations: https://childhoodcancerinternational.org"
    ])
}

class UnifiedSanctuaryApp:
    def __init__(self):
        self.storage_dir = os.path.expanduser("~/sovereign_core/sanitized_data/")
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

        self.G = ESC + "[32m"
        self.S = ESC + "[37m"
        self.O = ESC + "[33m"
        self.W = ESC + "[1;37m"
        self.B = ESC + "[34m"
        self.R = ESC + "[0m"

    def clear_screen(self):
        os.system("clear")

    def clean_input(self, text):
        allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?'-"
        return "".join(c for c in text if c in allowed).strip()

    def display_ui(self):
        self.clear_screen()
        print(f"{self.G}==========================================================================")
        print("   THE SANCTUARY & SUPPORT COMPANION v5.0 | LOCAL & PRIVATE WORKSPACE")
        print("==========================================================================")
        print(f"{NL}  {self.O}[1]{self.G} Trauma-Informed Support Companion (Local Ollama AI Chat)")
        print(f"  {self.O}[2]{self.G} Evening Slumber: Visual Anchor & Box Breathing Pacer")
        print(f"  {self.O}[3]{self.G} Morning Dawning: Log Dream Recall & Observer Status")
        print(f"  {self.O}[4]{self.G} Clear Mind: Sift Daily Stressors & Sanitize Text Noise")
        print(f"  {self.O}[5]{self.G} View Verified Crisis & Financial Support Directories")
        print(f"  {self.O}[6]{self.G} Close the Gateway (Exit Application)")
        print(f"{NL}{self.G}=========================================================================={self.R}")

    def get_verified_footer(self, country, state):
        country_clean = country.strip().upper()
        state_clean = state.strip().upper()

        footer = ""
        if country_clean in ["US", "USA", "UNITED STATES", "AMERICA"]:
            footer += VERIFIED_RESOURCES["NATIONAL_US"]
            if state_clean in VERIFIED_RESOURCES:
                footer += VERIFIED_RESOURCES[state_clean]
            elif state_clean:
                footer += f"{NL}--- {state_clean} STATE-SPECIFIC STARTING POINTS ---{NL}"
                footer += f"* Search '{state.title()} Title V Children with Special Health Care Needs' or '{state.title()} TEFRA Medicaid Waiver'{NL}"
                footer += f"* Search '{state.title()} Crime Victim Compensation Program' or dial 211 for local emergency funds.{NL}"
        else:
            footer += VERIFIED_RESOURCES["INTERNATIONAL"]
            if country_clean:
                footer += f"* Search '{country.title()} national health financial assistance' or local patient advocacy foundations.{NL}"
        return footer

    def chat_with_ollama(self, messages):
        payload = {
            "model": MODEL_NAME,
            "messages": [{"role": "system", "content": "You are a gentle, trauma-informed support companion. Respond with calm warmth, validation, and practical grounding steps."}] + messages,
            "stream": True, "keep_alive": "15m", "options": {"num_ctx": 1024}
        }
        req = urllib.request.Request(
            OLLAMA_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                print(f"{self.G}Companion:{self.W}")
                out = []
                for line in response:
                    if line.strip():
                        t = json.loads(line.decode("utf-8")).get("message", {}).get("content", "")
                        if t: print(t, end="", flush=True); out.append(t)
                print()
                return "".join(out)
            if False:
                result = json.loads(response.read().decode("utf-8"))
                return result["message"]["content"]
        except urllib.error.URLError:
            return "[Error: Could not connect to Ollama. Make sure Ollama is running in the background with 'ollama serve'.]"

    def run_support_companion(self):
        self.clear_screen()
        print(f"{self.O}=================================================================")
        print("  TRAUMA-INFORMED SUPPORT & RECOVERY COMPANION (LOCAL & PRIVATE) ")
        print("  Note: This is an AI support tool, not a doctor or emergency line.")
        print(f"================================================================={self.R}{NL}")

        country = input(f"{self.S}Enter your Country (e.g., USA, Canada, UK) [Press Enter to skip]: {self.W}")
        state = input(f"{self.S}Enter your State or Province (e.g., Minnesota, Texas) [Press Enter to skip]: {self.W}")

        location_context = ""
        if country or state:
            c_val = country if country else "Not specified"
            s_val = state if state else "Not specified"
            location_context = f"[User Location Context: Country={c_val}, State/Province={s_val}. Tailor Phase 2 financial and practical resources to this region.]{NL}{NL}"

        verified_footer = self.get_verified_footer(country, state)
        messages = []
        first_turn = True

        print(f"{NL}{self.G}Share whatever is on your mind below. Type 'exit' anytime to clear the chat and return to the menu.{self.R}{NL}")

        while True:
            user_input = input(f"{self.O}You: {self.W}").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "/bye", "menu"]:
                print(f"{NL}{self.S}Session ended. No chat history was saved to your computer. Returning to sanctuary...{self.R}")
                time.sleep(2)
                break

            prompt_to_send = (location_context + user_input) if first_turn else user_input
            first_turn = False

            messages.append({"role": "user", "content": prompt_to_send})
            print(f"{NL}{self.S}Companion is thinking...{self.R}{NL}")

            reply = self.chat_with_ollama(messages)
            messages.append({"role": "assistant", "content": reply})

            print(f"{self.G}Companion:{self.W}{NL}{reply}")
            print(f"{self.S}{verified_footer}")
            print(f"{self.G}-----------------------------------------------------------------{self.R}{NL}")

    def print_coded_landscape(self):
        bs = chr(92)
        fs = chr(47)
        print(f"             {self.O}*                  {self.S}.             *")
        print(f"    {self.S}.              .              {self.O}{fs}{bs}     .")
        print(f"           {self.W}{fs}{bs}{self.S}      .              {self.O}{fs}  {bs}          {self.S}.")
        print(f"          {self.W}{fs}  {bs}{self.G}__{self.O}___________{self.G}___{self.O}{fs}    {bs}_")
        print(f"         {self.G}{fs}   {fs}  {bs}  {bs}   {bs}   {bs}   {bs}   {bs}   {bs}")
        print(f"  {self.G}======{fs}___{fs}__  {bs}__{bs}___{bs}___{bs}___{bs}___{bs}___{bs}================")
        print(f"    {self.G}~~~  {self.B}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  {self.G}~~~{self.R}")

    def cognitive_anchor(self):
        self.clear_screen()
        print(f"{self.O}--- EVENING ANCHOR & BOX BREATHING ---{self.R}{NL}")
        user_input = input(f"{self.S}Enter your creative focus or peaceful setting for tonight:{NL}{self.G}> {self.W}")
        clean_focus = self.clean_input(user_input)

        print(f"{NL}{self.S}Provide a YouTube Video URL to act as your visual anchor.")
        print("(Or hit Enter to use your default Little Women creative sovereignty anchor):")
        yt_url = input(f"{self.G}> {self.W}").strip()

        if not yt_url:
            yt_url = "https://youtu.be"

        print(f"{NL}{self.G}[*] Visual Anchor Ready: {self.W}{yt_url}{self.R}")
        print(f"{self.S}(Ensure your browser window is open side-by-side if playing video){self.R}")

        input(f"{NL}{self.S}[Press Enter to begin 4 smooth cycles of Box Breathing...]{self.R}")

        for cycle in range(1, 5):
            self.clear_screen()
            print(f"{self.G}--- CYCLE {cycle} / 4 ---{self.R}{NL}")
            self.print_coded_landscape()
            print(f"{NL}{self.G}[+] INHALE slowly...  (4 Seconds){self.R}")
            time.sleep(4)
            print(f"{self.W}[*] HOLD your breath... (4 Seconds){self.R}")
            time.sleep(4)
            print(f"{self.S}[-] EXHALE completely... (4 Seconds){self.R}")
            time.sleep(4)
        self.clear_screen()
        print(f"{self.O}=== COGNITIVE ANCHOR PROTOCOLS LOCKED ==={self.R}")
        print(f"{NL}{self.G}[Axiom 1] Focus Intention: {self.W}{clean_focus}{self.G}")
        print("[Axiom 2] If sleep paralysis occurs, the mind identifies it as a safe biological loop.")
        print(f"[Axiom 3] Your avatar remains an {self.W}Invisible Passenger{self.G}, passing through unseen.{self.R}")
        anchor_file = os.path.join(self.storage_dir, "active_anchor.cfg")
        with open(anchor_file, "w") as f:
            f.write(f"SOVEREIGN STATE: TRUE{NL}ANCHOR: {clean_focus}{NL}YT_LINK: {yt_url}")
        input(f"{NL}{self.O}Press Enter to return to main menu...{self.R}")
    def morning_tracker(self):
        self.clear_screen()
        print(f"{self.O}--- MORNING DREAM RECALL TRACKER ---{self.R}\n")
        dream = input(f"{self.S}Log your dream recall notes:\n{self.G}> {self.W}")
        print(f"\n{self.O}Rate your level of detachment: 1=Invisible Observer, 2=Partial, 3=Reactive{self.R}")
        rating = input(f"{self.G}> {self.W}")
        status_map = {"1": "ABSOLUTE INVISIBLE OBSERVER", "2": "PARTIAL OBSERVER", "3": "HIGHLY REACTIVE STATE"}
        current_status = status_map.get(rating, "UNRATED")
        with open(os.path.join(self.storage_dir, f"recall_{int(time.time())}.log"), "w") as f:
            f.write(f"CONTENT: {dream}\nSTATUS: {current_status}")
        print(f"\n{self.G}[SUCCESS] Morning metrics saved: {current_status}{self.R}")
        time.sleep(3)

    def trigger_demolition(self):
        self.clear_screen()
        print(f"{self.O}--- SIFTING DAILY NOISE AND STRESSORS ---{self.R}\n")
        user_input = input(f"{self.S}Enter any intrusive thought or trigger to dissolve:\n{self.G}> {self.W}")
        clean_text = self.clean_input(user_input)
        token = hashlib.sha256(clean_text.encode()).hexdigest()
        with open(os.path.join(self.storage_dir, f"purged_{token[:8]}.log"), "w") as f:
            f.write(f"DISSOLVED: {clean_text}\nTOKEN: {token}")
        print(f"\n{self.G}[DISSOLVED] Text sanitized and cleared from active focus.{self.R}")
        time.sleep(2.5)

    def view_directories(self):
        self.clear_screen()
        print(f"{self.O}--- VERIFIED RESOURCE DIRECTORIES ---{self.R}")
        print(f"{self.S}{VERIFIED_RESOURCES['NATIONAL_US']}")
        print(f"{VERIFIED_RESOURCES['MINNESOTA']}")
        print(f"{VERIFIED_RESOURCES['INTERNATIONAL']}{self.R}")
        input(f"\n{self.O}Press Enter to return to main menu...{self.R}")

    def execute(self):
        while True:
            self.display_ui()
            choice = input(f"\n{self.O}Select your path: {self.W}").strip()
            if choice == "1":
                self.run_support_companion()
            elif choice == "2":
                self.cognitive_anchor()
            elif choice == "3":
                self.morning_tracker()
            elif choice == "4":
                self.trigger_demolition()
            elif choice == "5":
                self.view_directories()
            elif choice == "6":
                self.clear_screen()
                print(f"{self.S}Sanctuary closed. Take gentle care.{self.R}")
                break

if __name__ == "__main__":
    app = UnifiedSanctuaryApp()
    app.execute()
