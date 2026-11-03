## Hedge Mode UI Upgrade (2026-05-12)

The dashboard UI and backend logic were upgraded to allow simultaneous Long and Short risk calculations.

### Implementation Details
- **UI:** Added a "Mode" dropdown (One-Way / Hedge) and conditional visibility for Short inputs.
- **Backend:** `risk_calc.py` updated to accept `--mode hedge`, `--short-entry`, and `--short-stop`.
- **Integration:** `pro_dashboard.py` collects these new inputs from the UI and passes them to the calculator.

### User Workflow
1. Select "Hedge" from the dropdown.
2. Input both Long and Short entry/stops.
3. Run Dashboard to see the combined risk profile.