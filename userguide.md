# Advanced Shift Schedule Manager - User Guide

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Shift Types & Times](#shift-types--times)
4. [Features Overview](#features-overview)
5. [Step-by-Step Tutorials](#step-by-step-tutorials)
6. [Common Scenarios](#common-scenarios)
7. [Tips & Best Practices](#tips--best-practices)
8. [Troubleshooting](#troubleshooting)

---

## 🎯 Introduction

The Advanced Shift Schedule Manager is a comprehensive tool for managing team schedules with support for:
- **Multiple shift types** including day, night, layover, weekend, and holiday shifts
- **SAST (South African Standard Time)** specific scheduling
- **Bulk assignment** for efficient scheduling
- **Shift patterns** for repeating rotations
- **Visual calendar and grid views**
- **Excel export** functionality

---

## 🚀 Getting Started

### Initial Setup (3 Simple Steps)

#### Step 1: Add Your Teams and Members
1. Click **"👥 Team Setup"** in the sidebar
2. Go to the **"Add Members"** tab
3. Fill in:
   - **Team Name** (e.g., "Support Team A", "Night Crew")
   - **Member Name** (e.g., "John Doe")
   - **Location** (e.g., "Cape Town", "Johannesburg")
   - **WHMCS ID** (e.g., "EMP001")
4. Click **"Add Member"**
5. Repeat for all team members

💡 **Tip**: Create separate teams for different departments or locations

#### Step 2: Schedule Shifts
Choose your preferred method:
- **Calendar View**: Visual month-by-month scheduling
- **Grid View**: Spreadsheet-style for quick edits
- **Bulk Assign**: Schedule multiple days at once
- **Shift Patterns**: Apply repeating schedules

#### Step 3: Export & Share
1. Click **"📥 Export to Excel"** in the sidebar
2. Download the formatted Excel file
3. Share with your team or print for display

---

## 🕐 Shift Types & Times

### Weekday Shifts (SAST)

| Code | Shift Name | Time Range | Color | Usage |
|------|------------|------------|-------|-------|
| **D1** | Day Shift 1 | 7:00 AM - 4:00 PM | 🔵 Blue | Standard morning shift |
| **D2** | Day Shift 2 | 8:00 AM - 5:00 PM | 🔵 Blue | Alternative day shift |
| **EM** | Early Morning | 3:00 AM - 11:00 AM | 🟣 Purple | Early morning coverage |
| **L** | Layover | 2:00 PM - 10:00 PM | 🟠 Orange | Afternoon/evening coverage |
| **N** | Night Shift | 4:00 PM - 1:00 AM | ⚫ Dark Grey | Night operations |

### Weekend Shifts (SAST)

| Code | Shift Name | Time Range | Color | Usage |
|------|------------|------------|-------|-------|
| **WD** | Weekend Day | 7:00 AM - 4:00 PM | 🟢 Green | Weekend day coverage |
| **WEM** | Weekend Early | 3:00 AM - 11:00 AM | 🟢 Green | Weekend early shift |
| **WN** | Weekend Night | 4:00 PM - 1:00 AM | 🟢 Green | Weekend night shift |

### Holiday Shifts (SAST)

| Code | Shift Name | Time Range | Color | Usage |
|------|------------|------------|-------|-------|
| **HD** | Holiday Day | 7:00 AM - 4:00 PM | 🔴 Red | Public holiday day shift |
| **HEM** | Holiday Early | 3:00 AM - 11:00 AM | 🔴 Red | Public holiday early |
| **HN** | Holiday Night | 4:00 PM - 1:00 AM | 🔴 Red | Public holiday night |

### Leave & Special

| Code | Shift Name | Description | Color | Usage |
|------|------------|-------------|-------|-------|
| **X** | Leave | Approved time off | 🩷 Pink | Vacation, personal leave |
| **SL** | Sick Leave | Medical leave | 🔴 Red | Sick days |
| **TR** | Training | Training/Development | 🔵 Cyan | Training sessions |
| **(blank)** | Off | Day off | ⬜ White | Rest days |

---

## ✨ Features Overview

### 1. 📖 User Guide
**Access**: Select "📖 User Guide" in sidebar

**Features**:
- Quick start instructions
- Complete shift type reference
- Feature explanations
- Common scenario tutorials
- Best practices
- Troubleshooting help

**When to use**: First time using the app or need reference

---

### 2. 👥 Team Setup
**Access**: Select "👥 Team Setup" in sidebar

**Features**:
- Add new team members
- Organize by teams
- Store member details (name, location, WHMCS ID)
- Remove members when needed
- View all teams and members

**How to use**:
1. Enter team name
2. Fill in member details
3. Click "Add Member"
4. Member appears in team list immediately

**Tips**:
- Create teams by department, shift type, or location
- Keep WHMCS IDs consistent for tracking
- Review teams regularly to keep updated

---

### 3. 📅 Calendar View
**Access**: Select "📅 Calendar View" in sidebar

**Features**:
- Visual month calendar layout
- Day-of-week labels
- Weekend highlighting (light red background)
- Scheduled count per day
- Quick day editing
- View who's working specific days

**How to use**:
1. Browse the calendar to see monthly overview
2. Weekends are highlighted in light red
3. Each day shows how many people are scheduled
4. Use the "Edit Specific Day" section below to assign shifts
5. Check "Who's Working on Day X?" to see daily schedule

**Best for**:
- Getting monthly overview
- Identifying gaps in coverage
- Planning around weekends
- Checking specific day assignments

---

### 4. 📊 Grid View
**Access**: Select "📊 Grid View" in sidebar

**Features**:
- Spreadsheet-style schedule display
- Color-coded shift cells
- Filter by team
- Quick statistics (total members, shifts, etc.)
- Single-shift quick editor
- Complete month view in one screen

**How to use**:
1. Use team filter to focus on specific teams
2. Scroll horizontally to see all days
3. Colors indicate shift types (see legend at bottom)
4. Use "Quick Edit" section to change individual shifts
5. Check stats at the top for overview

**Best for**:
- Reviewing entire schedule at once
- Making quick single-shift edits
- Comparing team member schedules
- Preparing for meetings

---

### 5. ⚡ Bulk Assign
**Access**: Select "⚡ Bulk Assign" in sidebar

**Features**:
- Assign multiple consecutive days at once
- Date range selection (start to end day)
- Preview before applying
- Shows day-of-week for each day
- Immediate application

**How to use**:
1. Select team member from dropdown
2. Choose start day (e.g., Day 1)
3. Choose end day (e.g., Day 5)
4. Select shift type
5. Review preview table
6. Click "Apply Bulk Assignment"

**Example scenarios**:
- Monday-Friday week: Days 1-5 → D1 (Day Shift 1)
- Weekend coverage: Days 6-7 → WD (Weekend Day)
- Week-long assignment: Days 10-16 → any shift type
- Leave period: Days 20-24 → X (Leave)

**Best for**:
- Scheduling weekly shifts
- Assigning extended periods
- Planning vacations
- Quick batch updates

---

### 6. 🔄 Shift Patterns
**Access**: Select "🔄 Shift Patterns" in sidebar

**Features**:
- Create repeating shift sequences
- Save patterns for reuse
- Apply patterns starting any day
- Preview pattern before applying
- Manage saved patterns

**How to use**:

#### Creating a Pattern:
1. Go to "Create Pattern" tab
2. Enter pattern name (e.g., "2-2 Night Rotation")
3. Select shifts in order and click "Add" for each
4. Review the pattern sequence
5. Click "Save Pattern"

#### Common Pattern Examples:

**2 Days On, 2 Days Off**:
- Add: D1 (Day Shift 1)
- Add: D1 (Day Shift 1)
- Add: Off
- Add: Off
- Result: Works 2 days, rests 2 days, repeats

**Night Rotation with Rest**:
- Add: N (Night Shift)
- Add: N (Night Shift)
- Add: N (Night Shift)
- Add: Off
- Add: Off
- Result: Works 3 nights, rests 2 days, repeats

**Layover + Weekend**:
- Add: L (Layover)
- Add: L (Layover)
- Add: Off
- Add: WD (Weekend Day)
- Add: WD (Weekend Day)
- Add: Off
- Add: Off

#### Applying a Pattern:
1. Go to "Apply Pattern" tab
2. Select team member
3. Choose saved pattern
4. Pick start day
5. Preview shows how pattern will apply
6. Click "Apply Pattern"

**Best for**:
- Rotating schedules
- Fair distribution of shifts
- Regular night shift rotations
- Weekend rotation planning

---

### 7. 📋 Card View
**Access**: Select "📋 Card View" in sidebar

**Features**:
- Visual member cards
- Shows member details
- Displays scheduled days count
- Organized by team
- Clean, easy-to-read layout

**Best for**:
- Team overview
- Quick reference
- Presentations
- Checking who's in each team

---

### 8. 📈 Team Summary
**Access**: Select "📈 Team Summary" in sidebar

**Features**:
- Overall statistics
- Shift type distribution chart
- Per-team analytics
- Member workload comparison
- Bar charts for visualization

**Best for**:
- Management reporting
- Identifying workload imbalances
- Planning future schedules
- Team meetings

---

## 📝 Step-by-Step Tutorials

### Tutorial 1: Schedule a Regular Work Week

**Scenario**: Schedule John Doe for regular day shifts Monday-Friday

**Steps**:
1. Go to **"⚡ Bulk Assign"**
2. Select **"John Doe"** from dropdown
3. Set **Start Day**: 1 (assuming 1st is Monday)
4. Set **End Day**: 5
5. Select **"Day Shift 1"** (7 AM - 4 PM)
6. Review preview - should show Days 1-5 with D1
7. Click **"✅ Apply Bulk Assignment"**
8. Success! John is scheduled for the week

---

### Tutorial 2: Set Up Night Shift Rotation

**Scenario**: Create a rotating night shift schedule for Sarah (2 nights on, 2 nights off)

**Steps**:
1. Go to **"🔄 Shift Patterns"**
2. Click **"Create Pattern"** tab
3. Enter name: **"2-2 Night Rotation"**
4. Build pattern:
   - Select "Night Shift", click "➕ Add"
   - Select "Night Shift", click "➕ Add"
   - Select "Off", click "➕ Add"
   - Select "Off", click "➕ Add"
5. Click **"💾 Save Pattern"**
6. Go to **"Apply Pattern"** tab
7. Select **"Sarah"**
8. Choose **"2-2 Night Rotation"**
9. Set **Start from Day**: 1
10. Review preview
11. Click **"✅ Apply Pattern"**
12. Pattern applies to entire month!

---

### Tutorial 3: Schedule Weekend Coverage

**Scenario**: Mark needs to work both weekend days this month

**Steps**:

**Option A - Using Bulk Assign**:
1. Go to **"⚡ Bulk Assign"**
2. Select **"Mark"**
3. For first weekend:
   - Start Day: 6 (Saturday)
   - End Day: 7 (Sunday)
   - Shift: "Weekend Day"
   - Apply
4. Repeat for remaining weekends (days 13-14, 20-21, 27-28)

**Option B - Using Calendar View**:
1. Go to **"📅 Calendar View"**
2. For each weekend day:
   - Select the day number (6, 7, 13, 14, etc.)
   - Select "Mark"
   - Choose "Weekend Day"
   - Click "Update Shift"

---

### Tutorial 4: Mark Someone on Leave

**Scenario**: Lisa is on vacation Days 15-20

**Steps**:
1. Go to **"⚡ Bulk Assign"**
2. Select **"Lisa"**
3. Start Day: **15**
4. End Day: **20**
5. Shift Type: **"Leave"** (X)
6. Review - shows 6 days of leave
7. Click **"✅ Apply Bulk Assignment"**
8. Lisa now shows as on leave for those days

---

### Tutorial 5: Handle Sick Day

**Scenario**: Tom calls in sick on Day 8

**Steps**:
1. Go to **"📊 Grid View"** or **"📅 Calendar View"**
2. In Quick Edit section:
   - Select Member: **"Tom"**
   - Day: **8**
   - Shift Type: **"Sick Leave"** (SL)
3. Click **"Update Shift"**
4. Schedule updates immediately
5. Optional: Assign replacement:
   - Select another member
   - Day: 8
   - Assign their shift type
   - Update

---

### Tutorial 6: Schedule Holiday Shifts

**Scenario**: December 25th (Day 25) is a public holiday, need coverage

**Steps**:
1. Go to **"📅 Calendar View"**
2. Select Day: **25**
3. For each person working:
   - Select member name
   - Choose appropriate holiday shift:
     - **HD** (Holiday Day) for 7 AM - 4 PM
     - **HEM** (Holiday Early) for 3 AM - 11 AM
     - **HN** (Holiday Night) for 4 PM - 1 AM
4. Click **"Update Shift"** for each
5. Check "Who's Working on Day 25?" to verify coverage

---

## 🎯 Common Scenarios

### Scenario 1: Creating a Monthly Schedule from Scratch

**Goal**: Schedule entire team for the month

**Recommended Approach**:

1. **Plan Your Needs**:
   - How many people needed per shift?
   - What shift types are required?
   - Weekend/holiday coverage needs?

2. **Use Bulk Assignment for Regular Workers**:
   - Assign weekday shifts (D1/D2) to Monday-Friday workers
   - Days 1-5, 8-12, 15-19, 22-26, 29-31 (adjust for actual days)

3. **Use Shift Patterns for Rotations**:
   - Create patterns for rotating staff
   - Apply to team members who rotate shifts

4. **Assign Weekends Separately**:
   - Use Calendar or Bulk Assign
   - Assign WD, WEM, or WN shifts

5. **Mark Known Leave**:
   - Use Bulk Assign for vacation periods
   - Mark as "X" (Leave)

6. **Review in Grid View**:
   - Check for gaps
   - Ensure adequate coverage
   - Balance workload

---

### Scenario 2: Balancing Night Shifts Fairly

**Goal**: Distribute night shifts evenly across team

**Steps**:

1. **Count Total Night Shifts Needed**:
   - Example: 10 nights per month

2. **Divide Among Team**:
   - 5 team members = 2 nights each
   - Create staggered pattern

3. **Create Patterns for Each Person**:
   - Person A: Nights on Days 1-2
   - Person B: Nights on Days 8-9
   - Person C: Nights on Days 15-16
   - Person D: Nights on Days 22-23
   - Person E: Nights on Days 29-30

4. **Apply Using Calendar or Bulk Assign**

5. **Review in Team Summary**:
   - Check distribution is fair
   - Adjust if needed

---

### Scenario 3: Covering Unexpected Absence

**Goal**: Someone called in sick, need immediate replacement

**Steps**:

1. **Mark Original Person as Sick**:
   - Grid View → Quick Edit
   - Select person, day, set to "SL"
   - Update

2. **Find Replacement**:
   - Check Grid View or Calendar
   - See who's off that day
   - Contact available person

3. **Assign Replacement**:
   - Select replacement person
   - Same day
   - Assign appropriate shift
   - Update

4. **Document**:
   - Export to Excel
   - Keep record of change

---

### Scenario 4: Planning Layover Shift Coverage

**Goal**: Ensure afternoon/evening coverage with layover shifts

**Approach**:

1. **Identify Layover Days Needed**:
   - Example: Monday-Friday every week

2. **Assign Layover Shifts**:
   - Use Bulk Assign or Pattern
   - Shift Type: "L - Layover" (2 PM - 10 PM)

3. **Create Rotation if Multiple People**:
   - Week 1: Person A
   - Week 2: Person B
   - Week 3: Person C
   - Week 4: Person D

4. **Apply in Blocks**:
   - Person A: Days 1-5 → Layover
   - Person B: Days 8-12 → Layover
   - Person C: Days 15-19 → Layover
   - Person D: Days 22-26 → Layover

---

## 💡 Tips & Best Practices

### Scheduling Best Practices

✅ **Plan Ahead**:
- Schedule at least 2-3 weeks in advance
- Communicate schedule to team early
- Allow time for swap requests

✅ **Balance Workload**:
- Track total shifts per person
- Use Team Summary to check distribution
- Rotate undesirable shifts (nights, weekends) fairly

✅ **Consider Rest Periods**:
- Don't schedule consecutive night shifts without breaks
- Ensure adequate days off
- Follow labor laws for minimum rest periods

✅ **Document Everything**:
- Export schedule to Excel regularly
- Keep backup copies
- Save monthly schedules for reference

✅ **Communication**:
- Share schedule with team
- Use consistent format
- Update immediately when changes occur

---

### Efficiency Tips

🚀 **Use the Right Tool for the Job**:
- **Grid View**: Quick single edits
- **Bulk Assign**: Consecutive days
- **Shift Patterns**: Repeating cycles
- **Calendar View**: Visual overview

🚀 **Create Reusable Patterns**:
- Save common rotations
- Build library of patterns
- Name patterns clearly (e.g., "2-2 Night", "Weekend Rotation")

🚀 **Use Filters**:
- Filter by team in Grid View
- Focus on one team at a time
- Reduces clutter and errors

🚀 **Keyboard Shortcuts** (when entering data):
- Tab to move between fields
- Enter to submit forms
- Makes data entry faster

🚀 **Regular Backups**:
- Export to Excel weekly
- Save in organized folder structure
- Keep at least 3 months of history

---

### Data Management

💾 **Understanding Data Storage**:
- All data saved automatically
- Stored in `data/` folder as JSON files
- Three files:
  - `team_members.json` - Team and member data
  - `shift_schedule.json` - All shift assignments
  - `shift_patterns.json` - Saved patterns
  - `settings.json` - App settings

💾 **Backing Up**:
- Copy entire `data/` folder
- Store in safe location
- Do this weekly or before major changes

💾 **Restoring Data**:
- Replace `data/` folder with backup
- Restart application
- All data restored

💾 **Starting Fresh**:
- Delete all files in `data/` folder
- Refresh application
- Clean slate, no data loss risk

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### Issue: "Changes aren't saving"

**Possible Causes**:
- No write permission to `data/` folder
- Disk space full
- File corruption

**Solutions**:
1. Check folder permissions
2. Ensure adequate disk space (at least 10MB free)
3. Try exporting to Excel (if this works, data is fine)
4. Restart the application
5. If persistent, delete `data/` folder and recreate

---

#### Issue: "Member not showing in schedule views"

**Possible Causes**:
- Not added to team yet
- Team filter excluding them
- Wrong month selected

**Solutions**:
1. Go to Team Setup → verify member exists
2. In Grid View → check team filter includes their team
3. Check month/year selector in sidebar
4. Try searching in Card View (shows all members)

---

#### Issue: "Excel export is blank or missing shifts"

**Possible Causes**:
- No shifts assigned yet
- Export failed mid-process
- Browser blocked download

**Solutions**:
1. Verify shifts exist in Grid View
2. Check browser download permissions
3. Try different browser
4. Click export button again
5. Check Downloads folder

---

#### Issue: "Applied shift pattern but it looks wrong"

**Possible Causes**:
- Pattern applied from wrong start day
- Pattern sequence incorrect
- Month has fewer days than expected

**Solutions**:
1. Review pattern in Shift Patterns → Apply Pattern tab
2. Check start day selection
3. Preview shows exactly how it will apply
4. Can reapply from different day
5. Can use Bulk Assign to override specific days

---

#### Issue: "Can't see current month"

**Possible Causes**:
- Month/year selector set to different period
- Settings file corrupted

**Solutions**:
1. Check sidebar month/year selector
2. Change to desired month
3. Settings save automatically
4. If broken, delete `settings.json` in `data/` folder

---

#### Issue: "Accidentally deleted team member"

**Possible Causes**:
- Clicked remove button
- No undo feature (yet)

**Solutions**:
1. If just deleted: Re-add member with same details
2. Their old schedule is gone - need to reschedule
3. Prevention: Export to Excel before removing anyone
4. Keep Excel backups for recovery

---

#### Issue: "Application is slow"

**Possible Causes**:
- Too many team members (>100)
- Browser memory issues
- Old browser version

**Solutions**:
1. Close other browser tabs
2. Clear browser cache
3. Update browser to latest version
4. Try different browser (Chrome/Firefox recommended)
5. Reduce teams/members if using excessively

---

### Getting Help

If you encounter issues not covered here:

1. **Check User Guide**: Full reference in app
2. **Review This Document**: Search for keywords
3. **Export Data**: Save current state before experimenting
4. **Test in Sandbox**: Create test team to try solutions
5. **Contact Support**: Provide:
   - What you were trying to do
   - What happened instead
   - Screenshot if possible
   - Browser and version

---

## 📋 Quick Reference Card

### Shift Codes Quick Reference

| Code | Name | Time (SAST) |
|------|------|-------------|
| D1 | Day Shift 1 | 7 AM - 4 PM |
| D2 | Day Shift 2 | 8 AM - 5 PM |
| EM | Early Morning | 3 AM - 11 AM |
| L | Layover | 2 PM - 10 PM |
| N | Night | 4 PM - 1 AM |
| WD | Weekend Day | 7 AM - 4 PM |
| WEM | Weekend Early | 3 AM - 11 AM |
| WN | Weekend Night | 4 PM - 1 AM |
| HD | Holiday Day | 7 AM - 4 PM |
| HEM | Holiday Early | 3 AM - 11 AM |
| HN | Holiday Night | 4 PM - 1 AM |
| X | Leave | Approved Leave |
| SL | Sick Leave | Sick Day |
| TR | Training | Training |

---

### View Selection Guide

| Need to... | Use This View |
|------------|---------------|
| Add/remove team members | 👥 Team Setup |
| See month at a glance | 📅 Calendar View |
| Make single quick edit | 📊 Grid View |
| Schedule multiple days | ⚡ Bulk Assign |
| Create rotation | 🔄 Shift Patterns |
| View team info | 📋 Card View |
| Check statistics | 📈 Team Summary |
| Learn features | 📖 User Guide |

---

## 🎓 Advanced Usage

### Creating Complex Patterns

**Example: 4-Week Rotation with Multiple Shift Types**

Week 1: Day shifts
Week 2: Layover shifts
Week 3: Night shifts
Week 4: Off

**Pattern**:
D1, D1, D1, D1, D1, Off, Off (Week 1 - 7 days)
L, L, L, L, L, Off, Off (Week 2 - 7 days)
N, N, N, N, N, Off, Off (Week 3 - 7 days)
Off, Off, Off, Off, Off, Off, Off (Week 4 - 7 days)

Total: 28-day pattern

**To Create**:
1. Go to Shift Patterns → Create
2. Add all 28 shifts in order
3. Name: "4-Week Rotation"
4. Save and apply starting Day 1

---

### Managing Multiple Locations

**Scenario**: Team members in different cities

**Best Practice**:
1. Create separate teams by location
   - "Cape Town Team"
   - "Johannesburg Team"
   - "Durban Team"

2. Use location field for additional detail

3. Filter by team in Grid View to focus on one location

4. Export creates separate sections for each team

---

### Handling Shift Swaps

**When two members want to swap shifts**:

1. Go to Grid View
2. Note Person A's shift on Day X
3. Note Person B's shift on Day X
4. Update Person A → Day X → Person B's shift
5. Update Person B → Day X → Person A's shift
6. Export updated schedule
7. Communicate change to both

---

## 🎉 Conclusion

You now have comprehensive knowledge of the Advanced Shift Schedule Manager!

**Remember**:
- Start with Team Setup
- Use the right tool for each task
- Bulk Assign and Patterns save time
- Export regularly for backups
- Refer to this guide anytime

**Happy Scheduling!** 📅✨

---

*Advanced Shift Schedule Manager v3.0*  
*With SAST Time Zone Support*  
*© 2024 - All Rights Reserved*
