# Web3 & DeFi Protocol Engineering

> **Category**: 🪙 Smart Contract Security & DeFi Architecture  
> **Source / Upstream URL**: [https://github.com/kukapay/crypto-skills](https://github.com/kukapay/crypto-skills)  
> **Total Skills in Reserve**: 6 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate evm-swiss-knife
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/crypto-skills/skills/evm-swiss-knife" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/crypto-skills/skills/evm-swiss-knife .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link evm-swiss-knife
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\evm-swiss-knife" ".agents\library\crypto-skills\skills\evm-swiss-knife"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/crypto-skills/skills/evm-swiss-knife" ".agents/skills/evm-swiss-knife"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add kukapay/crypto-skills
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove evm-swiss-knife
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/evm-swiss-knife"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move evm-swiss-knife --to hot
python .agents/library/activate_skill.py move evm-swiss-knife --to reserve
```

---

## 📑 Included Skills Catalog (6 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`evm-swiss-knife`** | Interact with EVM-compatible blockchains using Foundry's cast tool for querying balances, calling contracts, sending transactions, and blockchain expl... |
| **`market-sentiment`** | Aggregate news from popular cryptocurrency RSS feeds, analyze sentiment of articles, and calculate an overall market sentiment score with detailed exp... |
| **`meme-scout`** | Comprehensive tool for scouting trending meme coins on DEX platforms like DexScreener. Use for discovering trending tokens, analyzing price movements,... |
| **`token-minter`** | Generate, build, and deploy custom ERC20 tokens on EVM networks. Use when users want to create and deploy their own ERC20 tokens with custom parameter... |
| **`trading-strategist`** | Provides trading strategies for cryptocurrencies based on Binance market data, calculated technical analysis indicators, and aggregated market sentime... |
| **`yield-opportunities`** | Comprehensive tool for finding and analyzing DeFi yield opportunities across protocols, chains, and asset types. Use when users want to earn yield on ... |
