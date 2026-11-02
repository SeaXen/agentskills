## Verdict

Visit plan: ⚠️ doesn't fit the clock. Final discussion: ❌ doesn't scale to 72 projects. The fix is small: mix the disciplines and score on your own before the group talks.

I'm assuming "4 minutes of judge time" means 4 minutes per judge (or panel) per visit. I'm also assuming the final discussion falls after the 150 minutes. Tell me if either is wrong.

## 1. The arithmetic

- A panel of 3 visiting together, with no walking time, covers 150 ÷ 4 = 37 teams at most.
- With a realistic ~1 min of walking and scoring, that drops to about 30 teams.
- Three panels give about 90 team slots for 72 teams, so each team gets one visit from one panel.
- That means each team is judged by one discipline only.
- A backend-only panel scores a team differently from a VC-only panel. In the final room you'd be comparing scores that don't measure the same thing.
- If you wanted every team seen by two panels, you'd need 576 panel-minutes across 3 panels. That is 192 minutes each, over your 150.

## 2. Problems with same-discipline panels

- ⚠️ **Agreement isn't the goal.** Three VCs agreeing fast means they share a lens. A backend engineer and a designer disagreeing about a team is exactly what you want to hear.
- ⚠️ **Each team gets only one lens.** A great demo with weak engineering, or the reverse, goes unnoticed.
- ⚠️ **Three judges stand at each table at once.** Crowding eats the 4 minutes, and the loudest judge anchors the other two.
- ❌ **The open discussion can't work as planned.**
  - Talking through 72 projects until all 9 agree takes about 2 minutes per project even if nobody argues. That is 144 minutes.
  - Real debate multiplies that, and the late teams get a tired room.

## 3. Better design: solo visits, one judge per discipline per team

Each of the 72 teams gets **3 visits**, one from a backend engineer, one from a VC and one from a designer. They visit separately and score separately.

| Item | Number |
|---|---|
| Total visits | 72 × 3 = 216 |
| Visits per judge | 24 |
| Time at tables | 24 × 4 = 96 min |
| Walking and scoring | 24 × ~1.5 = ~36 min |
| Total | ~132 min of 150 |
| Buffer | ~18 min |

**Assignment, in 5 steps:**

1. Split the expo floor into 3 zones of 24 tables: Z1, Z2, Z3.
2. Backend judge *i* covers zone *i*.
3. VC judge *i* covers zone *i+1*, wrapping around.
4. Designer judge *i* covers zone *i+2*, wrapping around.
5. Every table then gets exactly one judge of each type, and each judge sees 24 teams.

**Avoid crowding:**

- Stagger start offsets within each zone, so two judges don't hit the same table at once.
- Each judge walks a fixed, printed route of 24 tables, ordered by table number.

**Scoring:**

- Use a shared rubric, for example 3–4 criteria scored 1–5.
- Add a one-line comment per team.
- Each judge also rank-orders their own 24 teams at the end.
- Judges submit scores before the group discussion and don't see each other's.

## 4. Replace the open discussion with a calibrated shortlist

1. **Submit (10 min).** All judges file scores and ranks.
2. **Compute.** Normalise each judge's scores, either by z-score or by rank within their 24 teams, so harsh and lenient judges don't skew the result. Average the 3 per team.
3. **Shortlist (about 15 teams).** This is the top 10–12 by normalised score, plus any team where the judges split sharply. A split means one judge placed it in their top 5 and another in their bottom half.
4. **Discuss only the shortlist (about 45 min).**
   - Allow 3 minutes per team, with the disagreeing judges speaking first.
   - Each discipline explains what it saw that the others may have missed.
5. **Decide.** Set the tie-break rule in advance. For example, a ranked vote of all 9 on the shortlist, with scores deciding any tie. This stops the discussion from running forever.

Teams outside the shortlist keep their computed rank. Anyone on the panel can ask to pull one onto the shortlist, capped at 3 requests.

## 5. If you still prefer panels

If you want to keep the panels, use **mixed** ones. Put one backend engineer, one VC and one designer in each of the three panels.

- Each panel visits 24 teams, 4 minutes each, so 120 minutes with walking. It fits with about 30 minutes to spare.
- Each team then gets all three lenses in one visit.
- The cost is that each team is seen by only one panel, so there are fewer independent scores and you'd need to calibrate across panels. Solo visits are the more robust option.

## Questions for you

1. Is the 4 minutes per judge, or per panel?
2. Is the final discussion inside the 150 minutes or after it?
3. Is the expo floor big enough that walking takes over a minute? If so, cut to 3 visits of ~3.5 minutes.