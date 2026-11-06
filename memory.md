# Project Memory: Diwali Crackers Pricing & Inventory Verification System

## Context & Objectives
- **User Intent**: The user runs a seasonal Diwali crackers business at Nandigama with supplies sourced from Lakshmi Vasavi Crackers, Chilakaluripet.
- **Goal**: Rapidly look up and verify cracker boxes based on the sticker numbers, see wholesaler rates, compute rate + 10% overhead, manage retail selling prices, track verification progress, and analyze total project financials and profits.
- **Key Files**:
  - `diwali_expense_record(2).md`: Voice note transcription & expense reconciliation.
  - `WhatsApp Image 2026-11-06 at 8.20.07 AM.jpeg`: Pink slip (20 items, ₹1,33,548).
  - `WhatsApp Image 2026-11-06 at 8.20.07 AM (1).jpeg`: White bill page 1 (items 1–35).
  - `WhatsApp Image 2026-11-06 at 8.20.07 AM (2).jpeg`: White bill page 2 (items 36–70).
  - `WhatsApp Image 2026-11-06 at 8.20.08 AM.jpeg`: White bill page 3 (items 71–74, payment notes).
  - `ChatGPT Image Nov 6, 2026, 08_27_55 AM.png`: Infographic of the expense breakdown.
  - `anti-gravity.md`: Architectural specification and user workflow.
  - `memory.md`: This state and memory document.
  - `index.html`: The complete, interactive web application.

---

## Complete Financial Ledger

### 1. Purchase Invoices (Fireworks Stock)
- **Pink Bill Total**: ₹1,33,548 (20 items, 2,205 units)
- **White Bill Total**: ₹1,98,970 (74 items, 1,720 units)
- **Combined Stock Value**: ₹3,32,518 (94 items, 3,925 total units)
- **Stock Value with +10% Overhead**: ₹3,65,769.80

### 2. Operational & Shed Expenses
- **Auto Transportation**: ₹10,000
- **Unloading Labour (10 workers)**: ₹2,000
- **Car Petrol**: ₹2,200
- **Food for Workers**: ₹1,000
- **Additional Auto (Return Home)**: ₹500
- **Shed Setup Charges**: ₹3,000
- **Wooden Poles Rental Advance**: ₹5,000 (Daily rent ₹400/day pending)
- **Ropes & Misc Setup**: ₹1,000
- **Shed Permissions & Licences**: ₹50,000
- **Total Operational Overhead**: ₹74,700
- **Total Investment Required**: ₹4,07,218 (~ ₹4,07,700 as rounded in voice record)

### 3. Payment Tracking (Lakshmi Vasavi Account)
- **Cash Deposited (జమ)**: ₹60,000
- **GPay 1**: ₹80,000
- **GPay 2**: ₹80,000
- **Total Paid**: ₹2,20,000
- **Pending Payable**: ₹1,12,518

---

## Product Data Reference
- **Total SKUs**: 94 items
- **White Bill Range**: Stickers 1 to 74
- **Pink Bill Range**: Stickers P1 to P20 (also searchable by 101-120 or item name)
- **Default Overhead Multiplier**: 1.10 (+10% on base rate)
- **Default Suggested Selling Price Rule**: Minimum 35% margin or customizable presets (+30%, +50%, +75%, +100%, 2x, 2.5x, 3x) rounded to neat integers.

---

## Operational Features Enabled in Web App
1. **Ultra-Fast Numpad Lookup**: Large tap targets for single-hand mobile use while standing at boxes.
2. **Instant Search Bar**: Search by sticker number or product name.
3. **Box Verification**: Toggle "Verified & Tagged" state saved directly to browser storage.
4. **Editable Selling Price**: Inline editing per item with instant margin calculation.
5. **Bulk Markup & Auto-Rounder**: 1-click batch selling price generator based on target margins.
6. **Printable Price Labels / Tags**: Formatted sticker sheet for physical printing and sticking on boxes.
7. **Expense & ROI Dashboard**: Live breakdown of revenue, expenses, breakeven, and net profit.
8. **Original Bill Viewer**: Instant reference to original handwriting photos.
