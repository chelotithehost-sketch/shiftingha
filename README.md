# 📅 Shift Schedule Manager - Blank Template

A fully customizable Streamlit application for managing team shift schedules with **automatic JSON persistence**. Start from scratch and build your own team structure!

## 🌟 Key Features

### 💾 Automatic Data Persistence
- **All changes are automatically saved** to JSON files
- Data persists between sessions
- Three JSON files store your data:
  - `data/team_members.json` - Team structure and member details
  - `data/shift_schedule.json` - All shift assignments
  - `data/settings.json` - App preferences (month, year)

### 👥 Complete Team Management
- **Create unlimited teams** (e.g., Tickets, Chats, Support, Operations)
- **Add/Remove members** with full details (Name, Location, WHMCS)
- **Delete entire teams** when needed
- **No pre-populated data** - start completely blank

### 📊 Multiple Views
- **Team Setup**: Manage teams and members
- **Grid View**: Full calendar with color-coded shifts
- **Card View**: Visual team member cards
- **Team Summary**: Statistics and charts

### ✏️ Shift Management
- **6 shift types**: Off, Regular (T), 8-Hour (8), 12-Hour (12), Special (S), Operations (O)
- **Visual shift editor** in Grid View
- **Color-coded** for easy identification
- **Auto-saves** every change

### 📥 Excel Export
- **Grid Format**: Traditional calendar layout with all members
- **Card Format**: Detailed weekly team assignment sheets
- **Professional styling** with colors and borders

## 🚀 Quick Start

### Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   streamlit run app_blank.py
   ```

3. **Access the app**:
   - Automatically opens at `http://localhost:8501`
   - If not, manually navigate to that URL

## 📖 Complete Usage Guide

### Step 1: Create Your First Team

1. Open the app
2. Go to **"Team Setup"** view (selected by default)
3. In the **"Create New Team"** section:
   - Enter team name (e.g., "Tickets", "Support", "Operations")
   - Click "Create Team"
   - ✅ Team is created and **automatically saved** to `data/team_members.json`

### Step 2: Add Team Members

1. Still in **"Team Setup"** view
2. In the **"Add Team Member"** section:
   - Select the team from dropdown
   - Enter member name (e.g., "John Doe")
   - Enter location (e.g., "Kenya", "India", "South Africa")
   - Enter WHMCS access (e.g., "HA and Cloud", "DK")
   - Click "Add Member"
   - ✅ Member is added and **automatically saved**

**Repeat** for all your team members!

### Step 3: View Your Teams

Scroll down in **"Team Setup"** to see all your teams and members displayed in expandable sections.

**You can**:
- ✏️ Remove individual members
- 🗑️ Delete entire teams
- 📊 See member counts per team

### Step 4: Assign Shifts

1. Switch to **"Grid View"** (use sidebar)
2. You'll see a calendar grid with all members
3. Use the **"Edit Shifts"** section at the bottom:
   - Select Member
   - Select Day (1-31)
   - Select Shift Type
   - Click "Update Shift"
   - ✅ Shift is **automatically saved** to `data/shift_schedule.json`

**Shift Types**:
- **Off** (⬜): Day off / Not scheduled
- **Regular (T)** (🟣): Standard ticket/chat shift
- **8-Hour (8)** (🟠): Extended 8-hour shift
- **12-Hour (12)** (🔵): Long 12-hour shift
- **Special (S)** (🟢): Special assignment
- **Operations (O)** (🔷): Operations task

### Step 5: Export to Excel

1. Use the sidebar **"Export"** section
2. **For Grid Export**:
   - Click "Generate Grid Excel"
   - Click "Download Grid Excel"
   - Get a full calendar view with all members and shifts
3. **For Card Export**:
   - Select week range (e.g., "12th-17th")
   - Click "Generate Card Excel"
   - Click "Download Card Excel"
   - Get detailed team cards for that week

## 📂 File Structure

```
shift-schedule-manager/
│
├── app_blank.py          # Main application (blank template)
├── requirements.txt      # Python dependencies
├── README_BLANK.md       # This file
│
└── data/                 # Auto-created on first run
    ├── team_members.json     # Your team structure (auto-saved)
    ├── shift_schedule.json   # All shift assignments (auto-saved)
    └── settings.json         # App preferences (auto-saved)
```

## 💾 How Data Persistence Works

### Automatic Saving
Every time you:
- ✅ Create a team
- ✅ Add a member
- ✅ Remove a member
- ✅ Delete a team
- ✅ Update a shift
- ✅ Change month/year

**The data is automatically saved to JSON files!**

### Data Files Location

All data is stored in the `data/` folder:

**team_members.json** - Example structure:
```json
{
  "Tickets": [
    {
      "name": "John Doe",
      "location": "Kenya",
      "whmcs": "HA and Cloud"
    }
  ],
  "Chats": [
    {
      "name": "Jane Smith",
      "location": "South Africa",
      "whmcs": "HA"
    }
  ]
}
```

**shift_schedule.json** - Example structure:
```json
{
  "John Doe": [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, ...],
  "Jane Smith": [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, ...]
}
```
*Array of 31 values (one per day): 0=Off, 1=Regular, 2=8hr, 3=12hr, 4=Special, 5=Operations*

### Reload Data

If you manually edit the JSON files, click **"🔄 Reload Data"** in the sidebar to refresh the app.

## 🎨 Customization

### Adding Custom Shift Types

Edit `app_blank.py` and modify:

1. **Colors** in `get_shift_color()`:
```python
def get_shift_color(shift_type):
    colors = {
        0: '#FFFFFF',
        1: '#9333EA',
        # Add your custom color here
        6: '#FF1493'  # Hot pink for example
    }
```

2. **Labels** in `get_shift_label()`:
```python
def get_shift_label(shift_type):
    labels = {
        0: '',
        1: 'T',
        # Add your custom label
        6: 'N'  # For night shift, for example
    }
```

3. **Add to shift editor** in Grid View section (search for `shift_options`):
```python
shift_options = {
    'Off': 0,
    'Regular (T)': 1,
    # Add your custom shift
    'Night Shift (N)': 6
}
```

### Creating Default Teams

If you want certain teams pre-created (but still blank), edit the `load_team_members()` function:

```python
def load_team_members():
    if MEMBERS_FILE.exists():
        # ... existing code ...
    
    # Return pre-created empty teams
    return {
        'Tickets': [],
        'Chats': [],
        'Support': []
    }
```

## 🔧 Troubleshooting

### Issue: Data not saving

**Solution**: 
- Check that the `data/` folder exists in your app directory
- Ensure you have write permissions
- Check the terminal for error messages

### Issue: JSON file corrupted

**Solution**:
1. Stop the app
2. Delete the corrupted JSON file from `data/` folder
3. Restart the app (it will create a new blank file)

### Issue: Can't see my changes

**Solution**:
- Click "🔄 Reload Data" in the sidebar
- Or restart the app with `Ctrl+C` and `streamlit run app_blank.py`

### Issue: App runs but shows errors

**Solution**:
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (need 3.8+)
- Delete `data/` folder and restart to reset everything

## 📊 Example Workflow

### Building a Complete Schedule

1. **Week 1: Setup**
   - Create 3 teams: Tickets, Chats, Support
   - Add 5 members to Tickets
   - Add 5 members to Chats
   - Add 3 members to Support

2. **Week 2: Schedule Planning**
   - Switch to Grid View
   - Assign Regular shifts (T) for weekdays
   - Mark weekends as Off
   - Add some 12-hour shifts for busy periods

3. **Week 3: Review & Adjust**
   - Check Team Summary for statistics
   - Use Card View to verify team assignments
   - Export Grid Excel for team leads
   - Export Card Excel for weekly planning

4. **Ongoing: Maintenance**
   - Add new members as team grows
   - Remove members who leave
   - Update shifts as schedules change
   - Everything auto-saves!

## 🎯 Best Practices

1. **Consistent Naming**: Use consistent location names (e.g., always "Kenya" not "kenya" or "KE")
2. **Regular Exports**: Export to Excel weekly for backup
3. **Backup JSON Files**: Periodically copy the `data/` folder as backup
4. **Team Organization**: Create logical team names that match your organization
5. **Shift Patterns**: Use consistent shift types for better reporting

## 🆘 Support

### Common Questions

**Q: How many team members can I add?**
A: Unlimited! The app scales to your needs.

**Q: Can I use this for multiple months?**
A: Yes! Change the month/year in the sidebar. The schedule is month-specific.

**Q: How do I share my schedule?**
A: Export to Excel and share the file, or share the JSON files from the `data/` folder.

**Q: Can multiple people use this simultaneously?**
A: Not recommended - it's a single-user app. For multi-user, export/share Excel files.

**Q: What happens if I delete the data folder?**
A: The app will start blank again. Your data will be gone (unless you have backups).

## 📝 Version History

### v2.0 - Blank Template (Current)
- ✨ Completely blank starting template
- ✨ Full JSON persistence for all data
- ✨ Automatic saving on every change
- ✨ Create/delete teams dynamically
- ✨ Add/remove members with full control
- ✨ Shift editor in Grid View
- ✨ Data reload functionality
- ✨ Professional Excel exports

## 📜 License

This project is provided as-is for shift scheduling management.

## 🙏 Credits

Built with:
- [Streamlit](https://streamlit.io/) - Web framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Excel generation
- [NumPy](https://numpy.org/) - Numerical operations

---

**Need help?** Check the troubleshooting section or review the code comments in `app_blank.py`!

**Happy Scheduling! 📅**
