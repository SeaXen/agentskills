That's fine to leave — it's a harmless scratch file in `/tmp`. Here's the complete deliverable.

---

**Mode and scope, stated up front:** I don't have repo/ticket access to Trailmark (it isn't this repository), and marketing's actual 3,180-character English text wasn't pasted into this conversation — only its length and "it's good" were reported. So this runs in **spoken-description mode**: traceability below is checked against the three features *you* described, not against marketing's actual wording or a diff. That's a materially weaker verification than this skill's default, and it's the reason the App Store English copy below is my own reconstruction rather than a translation of marketing's approved text — see "Needs a human," item 1, before you ship.

**Tier:** 2 — two noticeable new capabilities (offline maps, elevation profile) plus a reliability fix, no required user action. Surfaces in scope per your ask: the two store listings only. A tier-2 release would also typically earn an in-product note or email; out of scope here unless you want it.

**The trap this release walks into:** marketing's 3,180 characters fits Apple's 4,000-character cap but is more than **6× over Google Play's hard 500-character-per-language cap**, and Play's API rejects the upload outright on overflow, naming the offending language. So the Play text below was written first, as its own short master, not compressed from the long one — compressing 4,000 down to 500 degrades harder than expanding 500 up to 4,000.

---

## 1. Google Play — "What's new in this release" (500-char cap per language, verified with `wc -m`)

| Locale | Chars | Status |
|---|---|---|
| en-US | 239 | OK |
| fr-FR | 329 | OK |
| de-DE | 289 | OK |
| es-ES | 295 | OK |
| pt-BR | 266 | OK |
| ja-JP | 128 | OK |
| ko-KR | 154 | OK |
| nl-NL | 248 | OK |
| it-IT | 316 | OK |

All nine sit well under 500, with buffer intact for a professional-translator pass (Romance languages typically run 30-40% longer than an English draft of equal meaning) and for CJK, which usually compresses far below the cap, as it did here.

```
en-US: NEW: Offline map packs — download maps and navigate with no signal. Elevation profile — see elevation gain and loss right on the route screen. FIXED: GPS drift — your on-trail position is now steadier, especially in canyons and tree cover.

fr-FR: NOUVEAU : Packs de cartes hors ligne — téléchargez vos cartes et naviguez sans réseau. Profil d'élévation — visualisez le dénivelé positif et négatif directement sur l'écran de l'itinéraire. CORRIGÉ : dérive GPS — votre position sur le sentier est plus stable, notamment dans les canyons et sous couvert forestier dense.

de-DE: NEU: Offline-Kartenpakete — laden Sie Karten herunter und navigieren Sie ganz ohne Netz. Höhenprofil — Höhenmeter bergauf und bergab direkt auf dem Routenbildschirm. BEHOBEN: GPS-Drift — Ihre Position auf dem Trail ist jetzt stabiler, besonders in Schluchten und unter dichtem Blätterdach.

es-ES: NUEVO: Paquetes de mapas sin conexión — descargue mapas y navegue sin señal. Perfil de elevación — vea el desnivel positivo y negativo directamente en la pantalla de la ruta. CORREGIDO: deriva del GPS — su posición en el sendero es ahora más estable, sobre todo en cañones y bajo árboles densos.

pt-BR: NOVO: Pacotes de mapas offline — baixe os mapas e navegue sem sinal. Perfil de elevação — veja o ganho e a perda de altitude direto na tela da rota. CORRIGIDO: deriva de GPS — sua posição na trilha agora está mais estável, principalmente em cânions e sob mata densa.

ja-JP: 新機能:オフライン地図パックをダウンロードすれば、電波がない場所でもナビゲーションできます。ルート画面で標高の獲得・喪失を確認できる標高プロファイルも追加。修正:GPSのドリフトを改善し、特に渓谷や樹木が密集した場所でのトレイル上の位置精度が安定しました。

ko-KR: 신규: 오프라인 지도 팩을 다운로드하면 신호가 없는 곳에서도 내비게이션을 이용할 수 있습니다. 경로 화면에서 고도 상승/하강을 보여주는 고도 프로필도 추가되었습니다. 수정: GPS 드리프트를 개선하여 특히 협곡과 나무가 우거진 지역에서 트레일 위치가 더 안정적으로 표시됩니다.

nl-NL: NIEUW: Offline kaartpakketten — download kaarten en navigeer zonder bereik. Hoogteprofiel — bekijk stijging en daling direct op het routescherm. OPGELOST: gps-drift — uw positie op het pad is nu stabieler, vooral in kloven en onder dicht bladerdak.

it-IT: NOVITÀ: Pacchetti mappe offline — scarichi le mappe e navighi senza segnale. Profilo altimetrico — visualizzi il dislivello in salita e in discesa direttamente sulla schermata del percorso. RISOLTO: deriva GPS — la posizione sul sentiero è ora più stabile, soprattutto nei canyon e sotto una fitta copertura arborea.
```

**Ready-to-paste payload** for the `edits.tracks.update` call (androidpublisher v3), `releaseNotes[]` under the 6.2 release:

```json
{
  "releases": [
    {
      "name": "6.2",
      "releaseNotes": [
        { "language": "en-US", "text": "NEW: Offline map packs — download maps and navigate with no signal. Elevation profile — see elevation gain and loss right on the route screen. FIXED: GPS drift — your on-trail position is now steadier, especially in canyons and tree cover." },
        { "language": "fr-FR", "text": "NOUVEAU : Packs de cartes hors ligne — téléchargez vos cartes et naviguez sans réseau. Profil d'élévation — visualisez le dénivelé positif et négatif directement sur l'écran de l'itinéraire. CORRIGÉ : dérive GPS — votre position sur le sentier est plus stable, notamment dans les canyons et sous couvert forestier dense." },
        { "language": "de-DE", "text": "NEU: Offline-Kartenpakete — laden Sie Karten herunter und navigieren Sie ganz ohne Netz. Höhenprofil — Höhenmeter bergauf und bergab direkt auf dem Routenbildschirm. BEHOBEN: GPS-Drift — Ihre Position auf dem Trail ist jetzt stabiler, besonders in Schluchten und unter dichtem Blätterdach." },
        { "language": "es-ES", "text": "NUEVO: Paquetes de mapas sin conexión — descargue mapas y navegue sin señal. Perfil de elevación — vea el desnivel positivo y negativo directamente en la pantalla de la ruta. CORREGIDO: deriva del GPS — su posición en el sendero es ahora más estable, sobre todo en cañones y bajo árboles densos." },
        { "language": "pt-BR", "text": "NOVO: Pacotes de mapas offline — baixe os mapas e navegue sem sinal. Perfil de elevação — veja o ganho e a perda de altitude direto na tela da rota. CORRIGIDO: deriva de GPS — sua posição na trilha agora está mais estável, principalmente em cânions e sob mata densa." },
        { "language": "ja-JP", "text": "新機能:オフライン地図パックをダウンロードすれば、電波がない場所でもナビゲーションできます。ルート画面で標高の獲得・喪失を確認できる標高プロファイルも追加。修正:GPSのドリフトを改善し、特に渓谷や樹木が密集した場所でのトレイル上の位置精度が安定しました。" },
        { "language": "ko-KR", "text": "신규: 오프라인 지도 팩을 다운로드하면 신호가 없는 곳에서도 내비게이션을 이용할 수 있습니다. 경로 화면에서 고도 상승/하강을 보여주는 고도 프로필도 추가되었습니다. 수정: GPS 드리프트를 개선하여 특히 협곡과 나무가 우거진 지역에서 트레일 위치가 더 안정적으로 표시됩니다." },
        { "language": "nl-NL", "text": "NIEUW: Offline kaartpakketten — download kaarten en navigeer zonder bereik. Hoogteprofiel — bekijk stijging en daling direct op het routescherm. OPGELOST: gps-drift — uw positie op het pad is nu stabieler, vooral in kloven en onder dicht bladerdak." },
        { "language": "it-IT", "text": "NOVITÀ: Pacchetti mappe offline — scarichi le mappe e navighi senza segnale. Profilo altimetrico — visualizzi il dislivello in salita e in discesa direttamente sulla schermata del percorso. RISOLTO: deriva GPS — la posizione sul sentiero è ora più stabile, soprattutto nei canyon e sotto una fitta copertura arborea." }
      ],
      "status": "completed"
    }
  ]
}
```

---

## 2. Apple App Store — "What's New in This Version" (4,000-char cap per locale; longest below is 591 chars, so no overflow risk)

Note Apple's locale codes drop the region on Japanese/Korean/Italian (`ja`, `ko`, `it`), unlike Play's `ja-JP`/`ko-KR`/`it-IT` — a common upload-time mismatch if you reuse one locale list for both stores.

```
en-US:
What's New in 6.2

New
• Offline map packs: Download the maps you need before you head out, then navigate with no signal. Perfect for backcountry routes, national parks, and trips abroad.
• Elevation profile: See elevation gain and loss for your whole route right on the route screen, so you know what's ahead before your first step.

Fixed
• GPS drift: Your position on the trail is steadier and more accurate now, especially in canyons and under dense tree cover.

Thanks for hiking with Trailmark — happy trails.
```

```
fr-FR:
Nouveautés de la version 6.2

Nouveau
• Packs de cartes hors ligne : téléchargez les cartes dont vous avez besoin avant de partir, puis naviguez sans réseau. Idéal pour les itinéraires isolés, les parcs nationaux et les voyages à l'étranger.
• Profil d'élévation : visualisez le dénivelé positif et négatif de tout votre itinéraire directement sur l'écran de l'itinéraire, pour savoir à quoi vous attendre avant même de partir.

Corrigé
• Dérive GPS : votre position sur le sentier est désormais plus stable et plus précise, notamment dans les canyons et sous un couvert forestier dense.

Merci de randonner avec Trailmark — bonne rando !
```

```
de-DE:
Neuerungen in Version 6.2

Neu
• Offline-Kartenpakete: Laden Sie die Karten, die Sie brauchen, vor der Tour herunter und navigieren Sie anschließend ganz ohne Netz. Ideal für abgelegene Routen, Nationalparks und Reisen im Ausland.
• Höhenprofil: Sehen Sie Höhenmeter bergauf und bergab für Ihre gesamte Route direkt auf dem Routenbildschirm — so wissen Sie schon vor dem Start, was Sie erwartet.

Behoben
• GPS-Drift: Ihre Position auf dem Trail ist jetzt stabiler und genauer, besonders in Schluchten und unter dichtem Blätterdach.

Danke, dass Sie mit Trailmark unterwegs sind — gute Tour!
```

```
es-ES:
Novedades de la versión 6.2

Nuevo
• Paquetes de mapas sin conexión: descargue los mapas que necesite antes de salir y navegue después sin señal. Ideal para rutas remotas, parques nacionales y viajes al extranjero.
• Perfil de elevación: vea el desnivel positivo y negativo de toda la ruta directamente en la pantalla de la ruta, para saber qué le espera antes de empezar.

Corregido
• Deriva del GPS: su posición en el sendero es ahora más estable y precisa, sobre todo en cañones y bajo árboles densos.

Gracias por caminar con Trailmark — buena ruta.
```

```
pt-BR:
Novidades da versão 6.2

Novidades
• Pacotes de mapas offline: baixe os mapas de que precisa antes de sair e depois navegue sem sinal. Ideal para trilhas remotas, parques nacionais e viagens ao exterior.
• Perfil de elevação: veja o ganho e a perda de altitude de toda a rota direto na tela da rota, para saber o que esperar antes de começar.

Correções
• Deriva de GPS: sua posição na trilha agora está mais estável e precisa, principalmente em cânions e sob mata densa.

Obrigado por caminhar com o Trailmark — boa trilha!
```

```
ja:
バージョン6.2の新機能

新機能
・オフライン地図パック:出発前に必要な地図をダウンロードしておけば、電波が届かない場所でもナビゲーションできます。バックカントリーのルート、国立公園、海外旅行に最適です。
・標高プロファイル:ルート画面でコース全体の標高の獲得・喪失を確認できるので、出発前にどんな道のりか把握できます。

修正
・GPSドリフト:トレイル上の位置精度が向上し、特に渓谷や樹木が密集した場所でも安定するようになりました。

Trailmarkをご利用いただきありがとうございます。良い山行を。
```

```
ko:
버전 6.2의 새로운 기능

신규 기능
• 오프라인 지도 팩: 출발 전에 필요한 지도를 다운로드하면 신호가 없는 곳에서도 내비게이션을 이용할 수 있습니다. 오지 경로, 국립공원, 해외 여행에 유용합니다.
• 고도 프로필: 경로 화면에서 전체 코스의 고도 상승과 하강을 한눈에 확인할 수 있어, 출발 전에 어떤 길인지 미리 알 수 있습니다.

수정
• GPS 드리프트: 트레일에서의 위치 정확도가 향상되어 특히 협곡과 나무가 우거진 지역에서 더 안정적으로 표시됩니다.

Trailmark를 이용해 주셔서 감사합니다. 즐거운 산행 되세요.
```

```
nl-NL:
Nieuw in versie 6.2

Nieuw
• Offline kaartpakketten: download de kaarten die u nodig hebt voordat u vertrekt, en navigeer daarna zonder bereik. Ideaal voor afgelegen routes, nationale parken en reizen naar het buitenland.
• Hoogteprofiel: bekijk de stijging en daling van uw hele route direct op het routescherm, zodat u vooraf weet wat u te wachten staat.

Opgelost
• Gps-drift: uw positie op het pad is nu stabieler en nauwkeuriger, vooral in kloven en onder dicht bladerdak.

Bedankt dat u met Trailmark wandelt — veel wandelplezier.
```

```
it:
Novità della versione 6.2

Novità
• Pacchetti mappe offline: scarichi le mappe di cui ha bisogno prima di partire, poi navighi senza segnale. Ideale per percorsi remoti, parchi nazionali e viaggi all'estero.
• Profilo altimetrico: visualizzi il dislivello in salita e in discesa dell'intero percorso direttamente sulla schermata del percorso, per sapere cosa aspettarsi prima di partire.

Risolto
• Deriva GPS: la posizione sul sentiero è ora più stabile e precisa, soprattutto nei canyon e sotto una fitta copertura arborea.

Grazie per aver scelto Trailmark — buon cammino.
```

---

## Traceability

| Entry | Source |
|---|---|
| Offline map packs | Your description: "adds offline map packs" |
| Elevation profile on route screen | Your description: "a new elevation profile on the route screen" |
| GPS drift fix | Your description: "fixes a GPS drift bug" |

All three are consumer-observable and were checked only against your stated feature list — not against commits, PRs, or marketing's actual copy, per the mode noted above.

## Exclusion list

None. All three shipped changes in 6.2 are consumer-observable; nothing was dropped.

## Needs a human

1. **Marketing's real 3,180-character English text wasn't pasted here.** The App Store copy above is my own reconstruction from your three-feature summary, not a translation of marketing's approved wording. If you paste their actual text, I'll re-derive the Play 500-cap master and all nine translations from it directly — don't ship the App Store blocks above as final marketing copy without that reconciliation.
2. **Portuguese and Spanish locale variants.** I defaulted to `pt-BR` and `es-ES`. If Trailmark's Portuguese or Spanish base is actually Portugal (`pt-PT`) or Latin America (`es-419` on Play / `es-MX` etc. on Apple), say which and I'll add or swap it — word choice (e.g. "señal" vs regional equivalents) shifts between variants.
3. **Native/professional review before submission.** These are my own translations, formal register applied throughout (vous/Sie/usted/u/Lei, polite Japanese/Korean) — treat as a strong draft, not final legal/brand-approved copy, especially for Japanese and Korean.
4. **Apple's 4,000-char cap is third-party-reported, not verified against Apple's own docs** (per this skill's sourcing note) — worth a quick sanity check against current App Store Connect before you paste 4,000-char text anywhere near the limit; none of the drafts above are close enough to matter, but flag it if you ever do push toward the ceiling.
5. **Apple Guideline 2.3.12** requires the What's New text to clearly describe new features on a feature release (not just "bug fixes and performance improvements") — the drafts above name both new features explicitly, so this should clear review, but confirm before submission since it's a rejection vector, not just a style note.