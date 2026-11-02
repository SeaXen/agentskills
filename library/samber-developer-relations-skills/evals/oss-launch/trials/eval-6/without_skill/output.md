Plan breaks in 3 spots. Fix before Thursday:

**1. Repo stays private 8am-1pm while blog + Twitter link to it.**
Blog post and tweet almost surely link the GitHub repo. Private repo = 404 for 5 hours, right when you want buzz building. Fix: flip repo public at 8am, same moment as blog+tweet. No reason tied to HN timing.

**2. Same text, same moment, across HN + r/golang + r/programming + Slack.**
Three problems:
- r/programming polices self-promo harder than r/golang — identical copy-paste reads as spam there, risks removal.
- Reddit's spam filter flags cross-posting identical content to multiple subs in a short window.
- You can't personally cover 4 live threads at once. First hour matters most on HN — comment velocity decides front-page survival. Fix: tailor text per community, stagger slightly, prioritize HN for your attention in hour one.

**3. Never ask your Twitter followers to go upvote the HN post.**
Vote manipulation, HN detects it, penalizes ranking or bans accounts. Let them find it organically.

**Before flipping public** (2 min check): scan commit history / CI logs / config for secrets or internal hostnames. Once public, history is public too — cannot undo by re-privating after the fact.

**Timing check:** confirm which timezone "1pm" is. Best HN window: 6-9am PT (catches US East morning + Europe afternoon). If 1pm is your Nantes time, that's ~4am PT — too early for US West, fine for East/Europe. State timezone so this doesn't land dead.

**Revised order:**
1. 8am: audit repo for secrets → flip public → publish blog → post Twitter thread (all links now live)
2. 1pm (confirm timezone against 6-9am PT window): submit "Show HN: [name] – [one-line description]" + immediately post a first comment with backstory/technical context
3. Same window, slight stagger: post tailored (not identical) text to r/golang, r/programming, Gophers Slack
4. Next 2-3 hours: stay on HN thread, answer every comment

Next: tell me the actual timezone for "1pm" so I confirm the HN slot lands in window.