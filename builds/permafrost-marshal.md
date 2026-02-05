────────────────────────────────────────────────────────────

# Permafrost Marshal — Live Build Grid
Use this as the canonical grid; reproduce it in full at the bottom of every reply

Core class: Warden (Animal Companions)
Subclasses: Necromancer (Grave Lord); Dragonknight (Draconic Power)
CP total: 1804

## Validation (read first)
- **Presentation rule:** Always reproduce this grid verbatim as normal Markdown (no triple-backtick code fences); keep all table pipes `|` intact so the tables render as the default grid view.
- Subclassing is ON (Update 46+): mixed class skill lines in this grid are intentional and valid.
- Subclassing constraint check: you may add up to two class skill lines from other classes, and you can’t take two lines from the same other class.
- Review rule: do not apply pre-Update 46 “single-class-only” assumptions; if anything looks contradictory, ask what the base class + chosen subclass lines are instead of declaring the grid invalid.
- Authority rule: treat this grid as authoritative for the build; when uncertain, ask clarifying questions before making legality/validity claims.
- Change-control rule: Only modify cells explicitly requested in the current message; otherwise keep every cell identical (prevents accidental drift across replies).
- Effects column rule: Named effects (Major/Minor buffs/debuffs, plus other named effects like Gallop) are listed only in the “Effects (Named)” column; do not repeat named effects in Target/Notes/Line columns.
- Named-only rule: “Effects (Named)” is for named effects only; % stat modifiers and other non-named passives stay out of this column.
- Trigger tag rule: Every entry in “Effects (Named)” must start with one of: “Slotted:”, “On cast:”, “On hit:”, or “Passive (always):”.
- Bar-scope rule: If an effect depends on what is slotted on a bar, track it on the Skills row(s) for that bar (not in Lines).
- PvE-only tag rule: If an effect is “vs monsters only” or otherwise PvE-only, include it only if we explicitly want it tracked, and tag it “[PVE]” inside the Effects cell.
- Display scope rule (Lines): Treat the “Lines” section as internal reference data for theorycrafting only. Do NOT display or reprint the “Lines” section by default when reproducing the grid. Only display the “Lines” section if I explicitly request it or if I request a change that affects class/weapon/armor/guild/PvP lines (i.e., anything that would require updating the “Lines” table). Otherwise, keep “Lines” hidden and preserve it unchanged in the canonical file.
- Display scope rule (Validation): Treat the “Validation (read first)” section as internal operating rules, not default display content. Do NOT reprint the “Validation (read first)” section when reproducing the grid unless I explicitly request it or unless you detect a validation/consistency problem that requires referencing it. Keep following those rules silently. Continue to display the full grid each reply, but omit “Validation (read first)” by default (same idea as “Lines”); **exception:** always keep the header metadata block (Core class/Subclasses/CP total, etc.) and “Format Notes” viewable.
- (Lines): and (Validation): must be displayed for each offline backup of the md file.

## Objectives (condensed)
| Pillar | Target | Notes | — | — | S |
|---|---|---|---|---|:--:|
| Resist | 43k+ shown (buffed, in-combat), so you stay 33k+ after debuffs | Pass/fail identity for the build | — | — | 🔒 |
| Health | Max Health-focused | Health-first stat profile | — | — | 🔒 |
| Speed | Extreme speed | Choose fights; disengage on demand | — | — | 🔒 |
| HoTs | Multiple HoTs running | Sustain baseline is HoTs | — | — | 🔒 |
| Shield | 2 running in combat | Baseline survivability layer | — | — | 🔒 |
| Core | Deep Fissure + Unnerving Boneyard + Glacial Colossus | Core use of the build | — | — | 🔒 |

## 12 Skills (Front/Back)

| Bar | Slot | Skill | Duration(s) | Line | Effects (Named) | S |
|---|---:|---|---|---|---|:--:|
| Front | 1 | Deep Fissure | 9s | Animal Companions | On hit: (Major Breach) (Minor Breach) | 🔒 |
| Front | 2 | Unnerving Boneyard | 10s | Grave Lord | On hit: (Major Breach) (Minor Vulnerability) | 🔒 |
| Front | 3 | Hardened Armor | 20s / 6s | Draconic Power | On cast: (Major Resolve) | 🔒 |
| Front | 4 | Green Dragon Blood | 20s / 5s | Draconic Power | On cast: (Minor Vitality) (Major Fortitude) (Major Endurance) | 🔒 |
| Front | 5 | Blinding Flare | 5s | Support | Slotted: (Major Protection) | 🔒 |
| Front | ULT | Reviving Barrier | 30s / 15s | Support | — | 🔒 |
| . | . | . | . | . | . | . |
| Back | 1 | Ulfsild's Contingency | 22s | Mages Guild (Focus: Shield; Signature: Damage reduction; Affix: Minor Expedition) | On cast: (Minor Expedition) | 🔒 |
| Back | 2 | Resolving Vigor | 5s / 20s | Assault | On cast: (Minor Resolve) | 🔒 |
| Back | 3 | Bull Netch / Blue Betty | 25s | Animal Companions | On cast: (Major Brutality) (Major Sorcery) | 🔒 |
| Back | 4 | Wield Soul | 10s | Soul Magic (Focus: Healing; Signature: Sustain; Affix: Vitality) | On cast: (Major Vitality) (Magicka sustain) | 🔒 |
| Back | 5 | Blinding Flare | 5s | Support | Slotted: (Major Protection) | 🔒 |
| Back | ULT | Glacial Colossus | 3s / 12s | Grave Lord | On hit: (Major Vulnerability) | 🔒 |

## 12 Gear (all slots)

| Gear slot | Set | Weight | Trait | Enchant | Effects (Named) | S |
|---|---|---|---|---|---|:--:|
| Head | Nibenay (1pc) | Heavy | Reinforced | Max Magicka | — | 🔒 |
| Shoulder | Adept Rider | Heavy | Impenetrable | Max Magicka | Passive (always): (Major Expedition) (Major Gallop) | 🔒 |
| Chest | Adept Rider | Heavy | Reinforced | Max Magicka | Passive (always): (Major Expedition) (Major Gallop) | 🔒 |
| Hands | Adept Rider | Medium | Impenetrable | Max Magicka | Passive (always): (Major Expedition) (Major Gallop) | 🔒 |
| Waist | Adept Rider | Light | Impenetrable | Max Magicka | Passive (always): (Major Expedition) (Major Gallop) | 🔒 |
| Legs | Adept Rider | Heavy | Reinforced | Max Magicka | Passive (always): (Major Expedition) (Major Gallop) | 🔒 |
| Feet | Mark of the Pariah | Heavy | Impenetrable | Max Magicka | — | 🔒 |
| Neck | Mark of the Pariah | — | Swift | Magicka Recovery | — | 🔒 |
| Ring 1 | Mark of the Pariah | — | Swift | Magicka Recovery | — | 🔒 |
| Ring 2 (Mythic/Alt) | Ring of the Wild Hunt | — | Swift | Magicka Recovery | Passive (always): (+15% Movement Speed IN) (+45% Movement Speed OUT) | 🔒 |
| Front weapon | Mark of the Pariah (Ice staff) | — | Defending | Absorb Magicka | — | 🔒 |
| Back weapon | Mark of the Pariah (Ice staff) | — | Defending | Absorb Magicka | — | 🔒 |

## Attributes

| Stat | Points | Unbuffed Total | Buffed Total | S |
|---|---:|---:|---:|:--:|
| Health | 64 |  |  | 🔒 |
| Magicka | 0 |  |  | 🔒 |
| Stamina | 0 |  |  | 🔒 |

## CP stars (slotted only)

| Tree | Slot 1 | Slot 2 | Slot 3 | Slot 4 | S |
|---|---|---|---|---|:--:|
| Warfare | Ironclad | Duelist's Rebuff | Bulwark | Resilience | 🔒 |
| Fitness | Celerity | Pain's Refuge | Sustained by Suffering | Bastion | 🔒 |
| Craft | Steed's Blessing | War Mount | Gifted Rider | Sustaining Shadows | 🔒 |

## Speed sources

| Source ID | Adept Rider | Wild Hunt | Celerity | Steed’s Blessing | Ulfsild | Swift (all jewelry) | Total | S |
|---|---|---|---|---|---|---|---|:--:|
| In-combat % | +30 | +15 | +10 | 0 | +15 | +19 | +89 | 🔒 |
| Out-of-combat % | +30 | +45 | +10 | +20 | +15 | +19 | +139 | 🔒 |

## Lines...

| Category | Line | Tool tip | S |
|---|---|---|:--:|
| Class 1 | Animal Companions | Passive: Bond with Nature — Anytime one of your Animal Companion skills end, you are healed for 1530 Health. | 🔒 |
| Class 1 | Animal Companions | Passive: Savage Beast — Casting an Animal Companions ability while are in combat generates 4 Ultimate. This effect can occur once every 8 seconds. | 🔒 |
| Class 1 | Animal Companions | Passive: Flourish — WITH AN ANIMAL COMPANION ABILITY SLOTTED Increases your Magicka and Stamina recovery by 20%. | 🔒 |
| Class 1 | Animal Companions | Passive: Advanced Species — Increases your Critical Damage by 5% for each Animal Companion ability slotted. | 🔒 |
| Class 2 | Grave Lord | Passive: Reusable Parts — When your Sacrificial Bones, Skeletal Mage, or Spirit Mender dies, the cost of your next Sacrificial Bones, Skeletal Mage, or Spirit Mender is reduced by 66%. | 🔒 |
| Class 2 | Grave Lord | Passive: Death Knell — WITH A GRAVE LORD ABILITY SLOTTED Increases your Critical Strike Chance against enemies under 33% Health by 20%. | 🔒 |
| Class 2 | Grave Lord | Passive: Dismember — While a Grave Lord ability is active, your Spell and Physical Penetration are increased by 3271. | 🔒 |
| Class 2 | Grave Lord | Passive: Rapid Rot — Increases your damage done with damage over time effects by 10%. | 🔒 |
| Class 3 | Draconic Power | Passive: Iron Skin — Increases the amount of damage you block by 10%. | 🔒 |
| Class 3 | Draconic Power | Passive: Burning Heart — While a Draconic Power ability is active, your healing received is increased by 9%. | 🔒 |
| Class 3 | Draconic Power | Passive: Elder Dragon — Increases your Health Recovery by 323 for each Draconic Power ability slotted. | 🔒 |
| Class 3 | Draconic Power | Passive: Scaled Armor — Increases your Physical and Spell Resistance by 2974. | 🔒 |
| Weapon | Destruction Staff (Ice) | Passive: Tri Focus — With Destruction Staff Equipped Fully-charged Ice Staff Heavy Attacks grant you a damage shield that absorbs 5280 damage (scales off Max Health); while an Ice Staff is equipped, blocking costs Magicka instead of Stamina. | 🔒 |
| Weapon | Destruction Staff (Ice) | Passive: Penetrating Magic — With Destruction Staff Equipped Your Destruction Staff abilities ignore 2974 of the enemy's Spell Resistance. | 🔒 |
| Weapon | Destruction Staff (Ice) | Passive: Elemental Force — With Destruction Staff Equipped Increases your chance to apply status effects by 100%. | 🔒 |
| Weapon | Destruction Staff (Ice) | Passive: Ancient Knowledge — With Destruction Staff Equipped Equipping an Ice Staff reduces the cost of blocking by 36% and increases the amount of damage you block by 20%. | 🔒 |
| Weapon | Destruction Staff (Ice) | Passive: Destruction Expert — With Destruction Staff Equipped When you kill an enemy with a Destruction Staff ability, you restore 3600 Magicka; when you absorb damage using a Destruction Staff Damage Shield, you restore 1800 Magicka (once every 10 seconds). | 🔒 |
| Armor | 5H / 1M / 1L | Heavy Armor Passive: Heavy Armor Bonuses — Each piece of Heavy Armor does the following: Reduces damage taken from Martial attacks by 1%; increases the amount of damage blocked by 1%; increases damage done with Bash by 30; reduces your damage taken while immune to crowd control by 1%. | 🔒 |
| Armor | 5H / 1M / 1L | Heavy Armor Passive: Heavy Armor Penalties — Each piece of Heavy Armor does the following: Increases damage taken from Magical attacks by 1%; reduces the Movement Speed bonus of Sprint by 1%; increases the cost of Roll Dodge by 3%; increases the size of your detection area while Sneaking by 10%. | 🔒 |
| Armor | 5H / 1M / 1L | Heavy Armor Passive: Resolve — Increases your Physical and Spell Resistance by 343 for each piece of Heavy Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Heavy Armor Passive: Constitution — Increases your Health Recovery by 4% for each piece of Heavy Armor equipped; you restore 108 Magicka and Stamina when you take damage for each piece of Heavy Armor equipped (once every 4 seconds). | 🔒 |
| Armor | 5H / 1M / 1L | Heavy Armor Passive: Juggernaut — Increases your Max Health by 2% for each piece of Heavy Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Heavy Armor Passive: Revitalize — Increases the Magicka or Stamina your Heavy Attacks restore by 4% for each piece of Heavy Armor worn. | 🔒 |
| Armor | 5H / 1M / 1L | Heavy Armor Passive: Rapid Mending — Increases your healing received by 1% for each piece of Heavy Armor worn. | 🔒 |
| Armor | 5H / 1M / 1L | Medium Armor Passive: Medium Armor Bonuses — Each piece of Medium Armor does the following: Reduces the cost of Sprint by 1%; reduces the cost of Sneak by 5%; reduces the cost of Block by 3%; reduces damage taken from Area of Effect attacks by 2% for 2 seconds after you use Roll Dodge; increases Movement Speed by 2% while immune to crowd control. | 🔒 |
| Armor | 5H / 1M / 1L | Medium Armor Passive: Dexterity — Increases your Critical Damage and Healing done rating by 2% for every piece of Medium Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Medium Armor Passive: Wind Walker — Increases your Stamina Recovery by 4% per piece of Medium Armor equipped; reduces the Stamina cost of your abilities by 2% per piece of Medium Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Medium Armor Passive: Improved Sneak — Reduces the cost of Sneak by 7% for each piece of Medium Armor equipped; reduces the size of your detection area while Sneaking by 5% for each piece of Medium Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Medium Armor Passive: Agility — Increases your Weapon and Spell Damage by 2% for each piece of Medium Armor worn. | 🔒 |
| Armor | 5H / 1M / 1L | Medium Armor Passive: Athletics — Increases the Movement Speed bonus of Sprint by 3% for each piece of Medium Armor equipped; reduces the cost of Roll Dodge by 4% for each piece of Medium Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Light Armor Passive: Light Armor Bonuses — Each piece of Light Armor does the following: Reduces damage taken from Magical attacks by 1%; reduces the cost of Roll Dodge by 3%; reduces the Movement Speed penalty of Sneak by 5%; reduces the cost of Break Free by 5%; reduces the cost of Bash by 3%. | 🔒 |
| Armor | 5H / 1M / 1L | Light Armor Passive: Light Armor Penalties — Each piece of Light Armor does the following: Increases damage taken from Martial attacks by 1%; increases the cost of Block by 3%; decreases damage done with Bash by 1%. | 🔒 |
| Armor | 5H / 1M / 1L | Light Armor Passive: Grace — Reduces the effectiveness of snares applied to you by 4% for each piece of Light Armor worn; reduces the cost of Sprint by 3% for each piece of Light Armor worn. | 🔒 |
| Armor | 5H / 1M / 1L | Light Armor Passive: Evocation — Increases your Magicka Recovery by 4% for each piece of Light Armor equipped; reduces the Magicka cost of your abilities by 2% for each piece of Light Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Light Armor Passive: Spell Warding — Increases your Spell Resistance by 726 for each piece of Light Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Light Armor Passive: Prodigy — Increases your Weapon and Spell Critical rating by 219 for each piece of Light Armor equipped. | 🔒 |
| Armor | 5H / 1M / 1L | Light Armor Passive: Concentration — Increases your Physical and Spell Penetration by 939 for each piece of Light Armor worn. | 🔒 |
| Guild | Mages Guild | Passive: Persuasive Will — Allows you to Persuade NPCs in conversation. | 🔒 |
| Guild | Mages Guild | Passive: Mage Adept — Reduces the Magicka and Health cost of your Mages Guild abilities by 15%. | 🔒 |
| Guild | Mages Guild | Passive: Everlasting Magic — Increases the duration of your Mages Guild abilities by 2 seconds. | 🔒 |
| Guild | Mages Guild | Passive: Magicka Controller — Increases your Max Magicka and Magicka Recovery by 2% for each Mages Guild ability slotted. | 🔒 |
| Guild | Mages Guild | Passive: Might of the Guild — Casting a Mages Guild ability grants you Empower, increasing the damage of your Heavy Attacks against monsters by 70% for 10 seconds. | 🔒 |
| PvP | Alliance War (Assault + Support) | Assault Passive: Continuous Attack — Increases your Weapon and Spell Damage by 10% and Health/Magicka/Stamina Recovery by 20% for 10 minutes after you capture a Lumber Mill, Farm, Mine, or Keep; gain Gallop at all times, increasing Mount Speed by 15%. | 🔒 |
| PvP | Alliance War (Assault + Support) | Assault Passive: Reach — Increases the range of long-range abilities by 5 meters while near a keep or outpost (any ability with range greater than 28 meters). | 🔒 |
| PvP | Alliance War (Assault + Support) | Assault Passive: Combat Frenzy — You generate 20 Ultimate when you kill an enemy player. | 🔒 |
| PvP | Alliance War (Assault + Support) | Support Passive: Magicka Aid — Increases your Magicka Recovery by 10% for each Support ability slotted. | 🔒 |
| PvP | Alliance War (Assault + Support) | Support Passive: Combat Medic — Increases your healing done by 20% when you are near a Keep. | 🔒 |
| PvP | Alliance War (Assault + Support) | Support Passive: Battle Resurrection — Reduces the time it takes you to resurrect another player by 30% while you are in a PvP area. | 🔒 |

---

## Format Notes
- **S column**: 🔒 = Locked, ☐ = Open
