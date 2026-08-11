"""
scrape_fb_group_v1_stealth.py
-----------------------------
Ultimate Stealth Edition:
- Persistent browser profile (looks like a returning user)
- playwright-stealth integration (hides webdriver flags)
- Human-like mouse trajectories and clicks (bypasses synthetic click detection)
"""

import json
import time
import random
from pathlib import Path
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth

# Optional but highly recommended for avoiding detection:
# pip install playwright-stealth

GROUP_URL = "https://www.facebook.com/groups/elcasbah/"
TARGET_POSTS = 2

# Directory to store browser cookies/cache so Facebook remembers you
PROFILE_DIR = Path("./fb_stealth_profile")
PROFILE_DIR.mkdir(exist_ok=True)

OUT_DIR = Path("output")
OUT_DIR.mkdir(exist_ok=True)
JSON_PATH = OUT_DIR / "fb_group_v1_stealth.json"

def manual_login(page):
        # --- MANUAL LOGIN SECTION ---
        # Go to the standard login page first
        page.goto("https://www.facebook.com/login/", wait_until="domcontentloaded")
        time.sleep(2)
        
        # Check if we are already logged in by looking for the email input
        is_logged_in = False
        try:
            login_input = page.locator('input[name="email"]')
            if not login_input.is_visible(timeout=3000):
                is_logged_in = True
        except:
            is_logged_in = True
            
        if not is_logged_in:
            print("\n" + "="*50)
            print("PLEASE LOG IN:")
            print("1. Type your credentials in the browser window.")
            print("2. Solve any security checks/CAPTCHAs.")
            print("3. Wait until you see your Facebook News Feed.")
            print("="*50)
            input(">>> Press ENTER here in the terminal when you are fully logged in <<<\n")
            print("[*] Login confirmed. Saving session and continuing...")
        else:
            print("[*] Already logged in via saved profile. Continuing...")

def is_timestamp(text):
    if not text:
        return True
    text = text.strip().lower()
    if text in ["yesterday", "just now", "admin", "·", "reply", "like", "see more", "replies", "comment"]:
        return True
    if text.isdigit():
        return True
    if len(text) <= 3 and text[-1] in ['d', 'h', 'm', 'w', 's', 'y']:
        return True
    return False

def human_click(page, element):
    """Simulates a real human click by moving the mouse physically before clicking."""
    try:
        element.scroll_into_view_if_needed(timeout=2000)
        time.sleep(random.uniform(0.2, 0.6))
        
        box = element.bounding_box()
        if not box:
            element.click(timeout=1000)
            return
            
        # Pick a random coordinate inside the button
        x = box['x'] + random.uniform(5, box['width'] - 5)
        y = box['y'] + random.uniform(5, box['height'] - 5)
        
        # Move mouse to the button in multiple steps (human-like)
        page.mouse.move(x, y, steps=random.randint(5, 15))
        time.sleep(random.uniform(0.1, 0.3))
        
        # Click and release
        page.mouse.down()
        time.sleep(random.uniform(0.05, 0.15))
        page.mouse.up()
        
    except Exception:
        # Fallback to standard click if human click fails
        try:
            element.click(timeout=1000)
        except:
            pass

def scroll_for_more_posts1(page, target_count=TARGET_POSTS, max_scrolls=30):
    """Scrolls the page human-like to load more posts."""
    print(f"[*] Scrolling to load up to {target_count} posts...")
    last_height = 0
    stagnant_count = 0
    
    for i in range(max_scrolls):
        time.sleep(5)
        current_posts = len(page.query_selector_all('div[aria-posinset], div[posinset]'))
        print(f"  [Scroll {i+1}] Posts loaded so far: {current_posts}")
        
        if current_posts >= target_count:
            break
            
        # Human-like chunked scrolling
        for _ in range(random.randint(2, 5)):
            page.mouse.wheel(0, random.randint(400, 800))
            time.sleep(random.uniform(0.3, 0.8))
            time.sleep(3)
            
        try:
            page.wait_for_load_state("networkidle", timeout=5000)
        except:
            pass
            
        time.sleep(random.uniform(1.5, 3.5))
        
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            stagnant_count += 1
            if stagnant_count >= 3:
                print("[~] Feed stopped growing.")
                break
        else:
            stagnant_count = 0
            last_height = new_height

def scroll_for_more_posts(page, target_count=TARGET_POSTS, max_scrolls=30):
    """Scrolls the page human-like to load more posts, focusing on the last post."""
    print(f"[*] Scrolling to load up to {target_count} posts...")
    last_height = 0
    stagnant_count = 0
    
    for i in range(max_scrolls):
        post_nodes = page.query_selector_all('div[aria-posinset], div[posinset]')
        current_posts = len(post_nodes)
        print(f"  [Scroll {i+1}] Posts loaded so far: {current_posts}")
        
        if current_posts >= target_count:
            break
            
        # ---> NEW LOGIC: Focus on the last post <---
        try:
            if current_posts > 0:
                # Get the very last post element loaded on the screen
                last_post = post_nodes[-1]
                # This forces the browser to scroll that specific element into the viewport
                last_post.scroll_into_view_if_needed()
                # Add a tiny mouse wheel scroll just to trigger the intersection observer
                page.mouse.wheel(0, 300)
            else:
                # Fallback if no posts are found yet
                page.mouse.wheel(0, 800)
        except Exception:
            # Fallback if the element disappeared (detached from DOM)
            page.mouse.wheel(0, 800)
            
        # Wait for Facebook's lazy-loader to fetch new posts
        try:
            page.wait_for_load_state("networkidle", timeout=5000)
        except:
            pass
            
        time.sleep(random.uniform(1.5, 3.5))
        
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            stagnant_count += 1
            if stagnant_count >= 3:
                print("[~] Feed stopped growing.")
                break
        else:
            stagnant_count = 0
            last_height = new_height

def expand_elements1(page, node):
    """Aggressively click 'See more', 'comments', and 'replies' using human clicks."""
    for _ in range(10):
        clicked_something = False
        time.sleep(5)
        buttons = node.query_selector_all(
            'div[role="button"]:has-text("See more"), span:has-text("See more"), a:has-text("See more")'
        )

            #'div[role="button"]:has-text("comments"), span:has-text("comments"), a:has-text("comments"), '
            #'div[role="button"]:has-text("replies"), span:has-text("replies"), a:has-text("replies")'
    
        for btn in buttons:
            try:
                if btn.is_visible():
                    human_click(page, btn)
                    time.sleep(random.uniform(0.8, 1.5))
                    clicked_something = True
                    break
            except Exception:
                continue
        if not clicked_something:
            break

def expand_elements2(node):
    """Aggressively click 'See more', 'comments', and 'replies' inside a node."""
    for _ in range(10):
        node.get_by_text("See more").click()

def extract_post_data53(node):
    """Extracts author, text, and comments from a given DOM node."""
    post_data = {"author": None, "text": None, "comments": []}

    header = node.query_selector('h3, h2')
    if header:
        elements = header.query_selector_all('span, a')
        for el in elements:
            txt = el.inner_text().strip()
            if txt and not is_timestamp(txt) and txt not in ["·", "Admin", "Pinned"]:
                post_data["author"] = txt
                break

    text_blocks = node.query_selector_all('div[dir="auto"]')
    post_text_parts = []
    for b in text_blocks:
        is_comment = b.evaluate("el => el.closest('div[aria-label*=\"Comment\"], div[data-commentid]') !== null")
        if is_comment:
            continue
        t = b.inner_text().strip()
        if t and not is_timestamp(t) and t not in ["·", "Admin", "Pinned", "See more"]:
            if t not in post_text_parts:
                post_text_parts.append(t)
    post_data["text"] = "\n".join(post_text_parts)

    comment_els = node.query_selector_all(
        'div[aria-label*="Comment"], div[data-commentid], div[role="article"] div[role="article"]'
    )
    seen_comments = set()
    for c in comment_els:
        c_author = None
        c_text = ""
        for span in c.query_selector_all('span, a'):
            txt = span.inner_text().strip()
            if txt and not is_timestamp(txt) and txt not in ["·", "Reply", "Like", "See more"]:
                c_author = txt
                break
        for text_el in c.query_selector_all('div[dir="auto"]'):
            t = text_el.inner_text().strip()
            if len(t) > len(c_text):
                c_text = t
        if c_text in seen_comments or c_text in ["See more", ""]:
            continue
        if c_author or len(c_text) > 10:
            post_data["comments"].append({"author": c_author, "text": c_text})
            seen_comments.add(c_text)

    return post_data

def extract_post_data(node):
    """Extracts author, text, and comments from a given Locator node (Sync version)."""
    post_data = {"author": None, "text": None, "comments": []}

    # 1. Extract Author
    header = node.locator('h3, h2').first
    if header.count() > 0:
        elements = header.locator('span, a')
        for i in range(elements.count()):
            el = elements.nth(i)
            txt = el.inner_text().strip()
            if txt and not is_timestamp(txt) and txt not in ["·", "Admin", "Pinned"]:
                post_data["author"] = txt
                break

    # 2. Extract Post Text
    text_blocks = node.locator('div[dir="auto"]')
    post_text_parts = []
    for i in range(text_blocks.count()):
        b = text_blocks.nth(i)
        
        # Evaluate directly on the locator element reference
        is_comment = b.evaluate("el => el.closest('div[aria-label*=\"Comment\"], div[data-commentid]') !== null")
        if is_comment:
            continue
            
        t = b.inner_text().strip()
        if t and not is_timestamp(t) and t not in ["·", "Admin", "Pinned", "See more"]:
            if t not in post_text_parts:
                post_text_parts.append(t)
    post_data["text"] = "\n".join(post_text_parts)

    # 3. Extract Comments
    comment_els = node.locator(
        'div[aria-label*="Comment"], div[data-commentid], div[role="article"] div[role="article"]'
    )
    seen_comments = set()
    
    for i in range(comment_els.count()):
        c = comment_els.nth(i)
        c_author = None
        c_text = ""
        
        # Find comment author
        spans = c.locator('span, a')
        for j in range(spans.count()):
            span = spans.nth(j)
            txt = span.inner_text().strip()
            if txt and not is_timestamp(txt) and txt not in ["·", "Reply", "Like", "See more"]:
                c_author = txt
                break
                
        # Find comment text
        comment_texts = c.locator('div[dir="auto"]')
        for k in range(comment_texts.count()):
            text_el = comment_texts.nth(k)
            t = text_el.inner_text().strip()
            if len(t) > len(c_text):
                c_text = t
                
        if c_text in seen_comments or c_text in ["See more", ""]:
            continue
            
        if c_author or len(c_text) > 10:
            post_data["comments"].append({"author": c_author, "text": c_text})
            seen_comments.add(c_text)

    return post_data


def main():
    with sync_playwright() as pw:
        # 1. Launch persistent context (saves cookies/cache to PROFILE_DIR)
        # 2. Add --disable-blink-features to hide automation
        context = pw.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            viewport={"width": 1280, "height": 900},
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/124.0.0.0 Safari/537.36"),
            locale="en-GB",
            args=['--disable-blink-features=AutomationControlled']
        )
        
        # Create the page first
        page = context.pages[0] if context.pages else context.new_page()
        
        #browser = pw.chromium.launch(headless=False)
        """context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/124.0.0.0 Safari/537.36"),
            locale="en-GB",
        ) """

        # Optional Stealth application to hide webdriver flags
        #Stealth().apply(context)

        #page = context.new_page()

        # 3. Apply Stealth patches directly to the page
        # 2. FIX FOR LINE 198:
        # Initialize the object, then explicitly apply it synchronously
        stealth = Stealth()
        stealth.apply_stealth_sync(page)

        manual_login(page)
        # --- CONTINUE TO GROUP ---
        print(f"[*] Navigating to {GROUP_URL}...")
        page.goto(GROUP_URL, wait_until="domcontentloaded")
        time.sleep(random.uniform(3.0, 5.0))

        # Close login popups
        try:
            close_btn = page.locator('div[role="button"][aria-label="Close"], div[role="button"][aria-label="Dismiss"]').first
            if close_btn.is_visible(timeout=3000):
                human_click(page, close_btn)
                print("[+] Closed login popup.")
                time.sleep(2)
            else:
                page.keyboard.press("Escape")
        except Exception:
            pass

        # Close cookies banner
        try:
            cookie_btn = page.get_by_role("button", name="Allow all cookies").first
            if cookie_btn.is_visible(timeout=3000):
                human_click(page, cookie_btn)
                print("[+] Dismissed cookie banner.")
        except Exception:
            pass

        # Scroll for more posts
        scroll_for_more_posts(page, target_count=TARGET_POSTS, max_scrolls=30)

        # Selecting all posts using Locators instead of ElementHandles
        post_locators = page.locator('div[aria-posinset], div[posinset]')
        post_count = post_locators.count()
        print(f"\n[*] Found {post_count} nodes with posinset attribute. Starting extraction...")

        scraped_posts = []

        # Scraping all posts, post by post
        for i in range(post_count):
            node = post_locators.nth(i)
            
            # Locators allow you to check visibility or presence easily
            if not (node.locator('h3').count() > 0 or node.locator('h2').count() > 0):
                continue

            print("\n--- Processing New Post ---")
            
            # You can now safely use get_by_text on this node:
            # example = node.get_by_text("Some Text")

            target_node = node
            dialog_is_open = False
            # 1. Find see more button
            seemorebuttons = node.get_by_text("See more")
            print(f"[+] found see more: {seemorebuttons.count()}")
            # 2. Clicking see more buttons
            for btn in seemorebuttons.all():
                btn.click()
                time.sleep(3)
                dialog = page.locator('div[role="dialog"]')
                
                # For sync API, is_visible() is a standard method call
                if dialog.is_visible():
                    print("[+] Dialog opened! Switching target to dialog...")
                    target_node = dialog
                    dialog_is_open = True
                else:
                    print("[+] No dialog opened after clicking see more")

            viewmorebuttons = node.get_by_text("View")
            print(f"[+] found vee more comments: {viewmorebuttons.count()}")
            # 2. Clicking see more buttons
            for btn in viewmorebuttons.all():
                btn.click()
                time.sleep(3)
                dialog = page.locator('div[role="dialog"] [aria-modal="true"]')
                
                # For sync API, is_visible() is a standard method call
                if dialog.is_visible():
                    print("[+] Dialog opened! Switching target to dialog...")
                    target_node = dialog
                    dialog_is_open = True
                    views = target_node.get_by_text("View")
                    print(f"[+] found views: {views.count()}")
                    # 2. Clicking see more buttons
                    for view in views.all():
                        view.click()
                        time.sleep(3)
                else:
                    print("[+] No dialog opened after clicking see more")

            post_data = extract_post_data(target_node)

            print(f"[+] Author: {post_data['author']} | Text: {len(post_data['text'] or '')} chars | Comments: {len(post_data['comments'])}")

            if dialog_is_open:
                print("[*] Closing dialog...")
                try:
                    close_btn = page.locator('div[role="dialog"] div[role="button"][aria-label="Close"]').first
                    if close_btn.is_visible(timeout=1000):
                        human_click(page, close_btn)
                    else:
                        page.keyboard.press("Escape")
                except Exception:
                    page.keyboard.press("Escape")
                time.sleep(random.uniform(1.5, 2.5))

            if post_data["author"]:
                scraped_posts.append(post_data)
                print(f"[✓] Post {len(scraped_posts)} successfully scraped.")

            if i >= TARGET_POSTS - 1:
                break

        if scraped_posts:
            JSON_PATH.write_text(json.dumps(scraped_posts, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"\n[+] Output saved to: {JSON_PATH}")
        else:
            print("\n[!] Failed to scrape any valid posts.")

        context.close()

if __name__ == "__main__":
    main()