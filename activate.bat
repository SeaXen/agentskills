@echo off
REM ==============================================================================
REM AgentSkills Universal Activator Launcher for Windows
REM Author: SeaXen (https://github.com/SeaXen/agentskills)
REM
REM Usage:
REM   activate.bat <skill-name>        - Link/activate skill into active workspace
REM   activate.bat search <keyword>    - Search across all 2,031 reserve skills
REM   activate.bat remove <skill-name> - Deactivate / unlink skill
REM   activate.bat categories          - List all 38 functional categories
REM ==============================================================================
python "%~dp0library\activate_skill.py" %*
