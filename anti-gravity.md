# Anti-Gravity Diwali Crackers Pricing & Box Verification Engine

## Executive Summary
This document provides the operational specification, business rules, system architecture, and fast-lookup algorithms for the **Diwali Crackers Pricing, Inventory & Box Verification Web Application**.

---

## 1. Business Context & Problem Statement

### The Problem
During Diwali cracker inventory reception:
- **Wholesale Consignment**: A massive shipment of fireworks was procured from **Lakshmi Vasavi Crackers (Chilakaluripet)** and delivered to the sales shed at **Nandigama**.
- **94 Total Product Line Items**:
  - **74 items** documented on the White Bills (numbered sequentially 1 through 74).
  - **20 items** documented on the Pink Bill (Chinna Pasumarru, items P1 through P20).
- **Physical Reality at the Shed**:
  - Every carton/box arriving off the truck has a **sticker with a number**.
  - Workers must unload, inspect, verify quantities, calculate overhead-adjusted costs, set the retail selling price, and physically label each box with the new selling price.
  - Doing this manually by flipping through multi-page handwritten bills takes **2 to 4 minutes per box**, causing massive bottlenecks, errors, and exhaustion.

### The Solution: Smart Verification & Pricing Web App
1. **Instant Sticker Number Lookup**: Type or tap the sticker number (`1` to `74` or `P1` to `P20`) on a mobile-friendly numeric keypad. The app renders the exact product, wholesale rate, cost + 10% overhead, pack details, and selling price in **< 10 milliseconds**.
2. **Automated Cost + 10% Pricing Formula**: Automatically adds 10% overhead buffer to each unit rate and computes both unit cost and total inventory cost.
3. **Retail Selling Price & Margin Management**: Set custom selling prices per item or apply smart markup presets (+30%, +50%, +75%, +100%, 2x, 3x) with auto-rounding to customer-friendly denominations (nearest ₹5 or ₹10).
4. **Box Labeling Progress Tracker**: 1-tap "Mark Verified & Labeled" with live progress bars and audio/haptic feedback.
5. **Full Financial Reconciliation**: Incorporates the ₹74,700 shed and operational expenses with the ₹3,32,518 cracker bills (Grand total ₹4,07,218), tracking break-even and profit targets.

---

## 2. Core Financial Data & Equations

### Cost Calculations
$$\text{Base Wholesale Rate} = R$$
$$\text{Cost with 10\% Overhead} = R \times 1.10$$
$$\text{Wholesale Total} = \text{Units} \times R$$
$$\text{Total Cost with 10\%} = \text{Units} \times (R \times 1.10) = \text{Wholesale Total} \times 1.10$$

### Sales & Profit Calculations
$$\text{Selling Price per Unit} = S$$
$$\text{Total Revenue Potential} = \sum (\text{Units} \times S)$$
$$\text{Gross Profit per Item} = (\text{Units} \times S) - \text{Total Cost with 10\%}$$
$$\text{Overall Net Business Profit} = \text{Total Revenue Potential} - \text{Total Project Investment (\₹4,07,218)}$$

### Bill Breakdown Summary
| Document | Items Count | Wholesale Total (₹) | Total with +10% (₹) |
|---|---:|---:|---:|
| **Pink Bill** (Chilakaluripet) | 20 items (P1–P20) | ₹1,33,548 | ₹1,46,902.80 |
| **White Bill** (Nandigama Items 1–74) | 74 items (#1–#74) | ₹1,98,970 | ₹2,18,867.00 |
| **Combined Fireworks Consignment** | **94 items** | **₹3,32,518** | **₹3,65,769.80** |

### Additional Operational & Shed Expenses
| S.No. | Description | Amount (₹) |
|---|---|---:|
| 1 | Auto Transportation Charges | ₹10,000 |
| 2 | Labour Charges for Unloading (10 workers) | ₹2,000 |
| 3 | Car Petrol Expenses | ₹2,200 |
| 4 | Worker Food Expenses | ₹1,000 |
| 5 | Additional Auto Charges (home return) | ₹500 |
| 6 | Shed Setup Charges | ₹3,000 |
| 7 | Wooden Poles Rental Advance (₹400/day ongoing) | ₹5,000 |
| 8 | Ropes and Miscellaneous Hardware | ₹1,000 |
| 9 | Shed Permissions & Approvals | ₹50,000 |
| **Total Overhead Expenses** | | **₹74,700** |
| **Grand Total Project Investment** | **₹3,32,518 + ₹74,700** | **₹4,07,218** |

### Payment Records from Wholesaler Bill
- **Cash Deposit (జమ)**: ₹60,000
- **Google Pay (GPay)**: ₹80,000 + ₹80,000 = ₹1,60,000
- **Total Amount Paid So Far**: ₹2,20,000
- **Balance Outstanding to Wholesaler**: ₹3,32,518 - ₹2,20,000 = **₹1,12,518**

---

## 3. Product Catalog Specification

### Complete White Bill (Stickers 1 to 74)
| Sticker # | Product Description | Units | Rate (₹) | Rate + 10% (₹) | Bill Total (₹) |
|---|---|---:|---:|---:|---:|
| 1 | 3 1/2 Lakshmi (15P) | 20 | 150 | 165.00 | 3,000 |
| 2 | 4" Laxmi | 25 | 150 | 165.00 | 3,750 |
| 3 | 4" Dlx Lion | 10 | 260 | 286.00 | 2,600 |
| 4 | Gold Laxmi | 10 | 280 | 308.00 | 2,800 |
| 5 | 5" Hulk | 10 | 280 | 308.00 | 2,800 |
| 6 | 6" Bruslee | 10 | 330 | 363.00 | 3,300 |
| 7 | 2 Sound Crackers | 10 | 280 | 308.00 | 2,800 |
| 8 | 3 Sound Colanatia | 10 | 350 | 385.00 | 3,500 |
| 9 | Smoke Bomb | 10 | 250 | 275.00 | 2,500 |
| 10 | 28 Cholasa | 10 | 550 | 605.00 | 5,500 |
| 11 | 28 Gaint | 10 | 550 | 605.00 | 5,500 |
| 12 | 24 Dlx | 5 | 450 | 495.00 | 2,250 |
| 13 | 50 Dlx | 5 | 450 | 495.00 | 2,250 |
| 14 | 100 mega Dlx | 10 | 350 | 385.00 | 3,500 |
| 15 | 18 cm pencil | 50 | 70 | 77.00 | 3,500 |
| 16 | 12 cm Pencil Gaint | 20 | 50 | 55.00 | 1,000 |
| 17 | 7 cm Pencil | 50 | 22 | 24.20 | 1,100 |
| 18 | 100 wala | 50 | 27 | 29.70 | 1,350 |
| 19 | 200 wala | 25 | 50 | 55.00 | 1,250 |
| 20 | Rocket Bomb | 50 | 60 | 66.00 | 3,000 |
| 21 | Lunik Rocket | 25 | 90 | 99.00 | 2,250 |
| 22 | Music Rocket | 10 | 120 | 132.00 | 1,200 |
| 23 | Flp Small | 100 | 36 | 39.60 | 3,600 |
| 24 | Flp Spl | 125 | 65 | 71.50 | 8,125 |
| 25 | Flp Gaint | 20 | 120 | 132.00 | 2,400 |
| 26 | WiFi | 10 | 120 | 132.00 | 1,200 |
| 27 | 5 Colour mini fountain | 30 | 160 | 176.00 | 4,800 |
| 28 | Clk Dlx Royal | 12 | 330 | 363.00 | 3,960 |
| 29 | Clk Dlx (Leo) | 12 | 350 | 385.00 | 4,200 |
| 30 | Clk Mega Dlx mithra | 10 | 330 | 363.00 | 3,300 |
| 31 | Glc Big (25P) | 24 | 65 | 71.50 | 1,560 |
| 32 | Glc Spl Leo | 75 | 65 | 71.50 | 4,875 |
| 33 | Glc Dlx | 75 | 96 | 105.60 | 7,200 |
| 34 | Wheel Spinner | 30 | 100 | 110.00 | 3,000 |
| 35 | Spinner Spl Royal | 20 | 160 | 176.00 | 3,200 |
| 36 | Wire Chakkar | 10 | 140 | 154.00 | 1,400 |
| 37 | 1 1/2 Twinkling | 100 | 18 | 19.80 | 1,800 |
| 38 | 4" Twinkling | 150 | 60 | 66.00 | 9,000 |
| 39 | Hele copter | 20 | 80 | 88.00 | 1,600 |
| 40 | Dola Dola Leo | 100 | 38 | 41.80 | 3,800 |
| 41 | Mega kit kat | 50 | 50 | 55.00 | 2,500 |
| 42 | Ganga Jamuna | 30 | 75 | 82.50 | 2,250 |
| 43 | Flower Bomb vcl | 20 | 150 | 165.00 | 3,000 |
| 44 | Butterfly Yuva | 30 | 70 | 77.00 | 2,100 |
| 45 | 2 Comment (P) Window | 10 | 70 | 77.00 | 700 |
| 46 | 7 shot (10P) | 5 | 200 | 220.00 | 1,000 |
| 47 | 4" comment (1P) | 2 | 760 | 836.00 | 1,520 |
| 48 | 4" Comment (3P) | 2 | 900 | 990.00 | 1,800 |
| 49 | Small Bullet Bomb | 150 | 13 | 14.30 | 1,950 |
| 50 | Solar Bomb | 50 | 45 | 49.50 | 2,250 |
| 51 | Classic Bomb | 50 | 92 | 101.20 | 4,600 |
| 52 | Military Bomb | 10 | 165 | 181.50 | 1,650 |
| 53 | Marshal Black | 25 | 160 | 176.00 | 4,000 |
| 54 | Digital Bomb | 20 | 190 | 209.00 | 3,800 |
| 55 | Jurassic Marshal | 20 | 180 | 198.00 | 3,600 |
| 56 | 240 Shot (Jyothi) | 3 | 3100 | 3,410.00 | 9,300 |
| 57 | Lamp | 15 | 250 | 275.00 | 3,750 |
| 58 | 50 Ele | 10 | 130 | 143.00 | 1,300 |
| 59 | 50 Colour | 10 | 140 | 154.00 | 1,400 |
| 60 | Robin King Siren | 5 | 65 | 71.50 | 325 |
| 61 | Dil Se (1P) | 5 | 210 | 231.00 | 1,050 |
| 62 | Cukoo | 5 | 130 | 143.00 | 650 |
| 63 | Butterscotch | 5 | 230 | 253.00 | 1,150 |
| 64 | Golden Rabbit | 5 | 260 | 286.00 | 1,300 |
| 65 | Speed Test mithra | 15 | 125 | 137.50 | 1,875 |
| 66 | 900 cc | 10 | 130 | 143.00 | 1,300 |
| 67 | Turbo wheel | 10 | 80 | 88.00 | 800 |
| 68 | Top Gun | 5 | 180 | 198.00 | 900 |
| 69 | Pistol 58 | 5 | 230 | 253.00 | 1,150 |
| 70 | Bada Peacock Standard | 5 | 250 | 275.00 | 1,250 |
| 71 | Chota Bhai Siren | 9 | 170 | 187.00 | 1,530 |
| 72 | Big Elephant | 5 | 200 | 220.00 | 1,000 |
| 73 | Bat & Ball | 2 | 350 | 385.00 | 700 |
| 74 | Wicked Willow Rocket | 6 | 300 | 330.00 | 1,800 |
| **Subtotal (White Bill)** | | **1,720 units** | | | **₹1,98,970** |

---

### Complete Pink Bill (Stickers P1 to P20)
| Sticker # | Product Description | Pack Details | Units | Rate (₹) | Rate + 10% (₹) | Bill Total (₹) |
|---|---|---|---:|---:|---:|---:|
| P1 | 100 Bijili | 1 x 300 | 300 | 25 | 27.50 | 7,500 |
| P2 | CLK Ishwarya | 1 x 60 | 60 | 160 | 176.00 | 9,600 |
| P3 | FLP Ashoka | 1 x 100 | 100 | 85 | 93.50 | 8,500 |
| P4 | 7 CM Electric | 4 | 4 | 1000 | 1,100.00 | 4,000 |
| P5 | 15 CM Colour | 3 x 100 | 300 | 30 | 33.00 | 9,000 |
| P6 | 15 CM Electric | 3 x 100 | 300 | 28 | 30.80 | 8,400 |
| P7 | 30 CM Colour | 3 x 100 | 300 | 30 | 33.00 | 9,000 |
| P8 | 30 CM Electric | 3 x 100 | 300 | 28 | 30.80 | 8,400 |
| P9 | 1K Wala | 1 x 36 | 36 | 130 | 143.00 | 4,680 |
| P10 | 2K Wala | 1 x 20 | 20 | 260 | 286.00 | 5,200 |
| P11 | 5K Wala | 1 x 8 | 8 | 650 | 715.00 | 5,200 |
| P12 | 10K Wala | 1 x 5 | 5 | 1300 | 1,430.00 | 6,500 |
| P13 | 30 Shot | 1 x 18 | 18 | 380 | 418.00 | 6,840 |
| P14 | 60 Shot | 1 x 12 | 12 | 760 | 836.00 | 9,120 |
| P15 | 120 Shot | 1 x 6 | 6 | 1520 | 1,672.00 | 9,120 |
| P16 | 12 Shot Himalaya | 1 x 36 | 36 | 138 | 151.80 | 4,968 |
| P17 | Robin Big Kids | 1 x 60 | 60 | 42 | 46.20 | 2,520 |
| P18 | Robin 5 Star | 1 x 40 | 40 | 125 | 137.50 | 5,000 |
| P19 | Mathabu | 2 x 50 | 100 | 58 | 63.80 | 5,800 |
| P20 | Look Pots | 2 x 100 | 200 | 21 | 23.10 | 4,200 |
| **Subtotal (Pink Bill)** | | | **2,205 units** | | | **₹1,33,548** |

---

## 4. Web App Architecture & Design

### Technology Stack
- **Architecture**: Single Page Application (SPA), zero external build step needed, 100% self-contained in `index.html`.
- **UI / Styling**: Premium Tailwind-grade CSS design system with Dark/Festive Gold & Royal Navy Diwali theme, optimized for mobile handheld use in outdoor sheds as well as desktop.
- **State Management**: Reactive vanilla JavaScript state engine with automated browser `localStorage` persistence (persisting custom selling prices, verified flags, notes, and margin adjustments).
- **Audio & Haptic System**: Web Audio API synthesized tones (chime on verification, click on numpad) and browser vibration feedback for rapid tactile confirmation.
- **Speech Synthesis (TTS)**: Optional Text-to-Speech voice callout announcing product name and price so the user can keep eyes on the boxes.

---

## 5. User Workflow for Maximum Speed
1. **Unloading Cartons**: A box arrives with sticker e.g. "33".
2. **Input**: Tap `3` then `3` on the app numpad.
3. **Instant Display**:
   - Item Name: **GLC Dlx**
   - Units in Box: **75**
   - Cost + 10%: **₹105.60**
   - Recommended Selling Price: **₹150** (or whatever margin selected)
4. **Action**:
   - Write selling price on the box.
   - Tap **"Mark Verified"** (Turns green, updates progress counter).
5. **Move to next box**: Numpad auto-clears, ready for next sticker in < 1 second.
