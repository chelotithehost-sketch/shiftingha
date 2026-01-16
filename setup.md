# Quick Setup Guide - Enhanced Shift Scheduler

## 📦 What You Received

1. **app.py** - Enhanced shift scheduling application
2. **USER_GUIDE.md** - Comprehensive user documentation
3. **SETUP.md** - This file

## 🚀 Quick Deployment to Streamlit

### Step 1: Update Your Repository

Replace your current `app.py` file with the new one:

```bash
# In your repository folder
cp app.py /path/to/your/shiftingha/app.py
```

### Step 2: Update requirements.txt

Make sure your `requirements.txt` has:

```
streamlit
pandas>=2.2.0
openpyxl
```

**Note**: Changed from `pandas==2.1.4` to `pandas>=2.2.0` for Python 3.13 compatibility

### Step 3: Push to GitHub

```bash
git add app.py requirements.txt
git commit -m "Enhanced shift scheduler with SAST times and advanced features"
git push origin main
```

### Step 4: Streamlit Will Auto-Deploy

Streamlit Community Cloud will automatically detect the changes and redeploy your app!

---

## ✨ New Features

### 1. **Enhanced Shift Types with SAST Times**
- **D1**: Day Shift 1 (7 AM - 4 PM SAST)
- **D2**: Day Shift 2 (8 AM - 5 PM SAST)
- **EM**: Early Morning (3 AM - 11 AM SAST)
- **L**: Layover (2 PM - 10 PM SAST)
- **N**: Night Shift (4 PM - 1 AM SAST)
- **WD/WEM/WN**: Weekend shifts
- **HD/HEM/HN**: Holiday shifts
- **X/SL/TR**: Leave, Sick Leave, Training

### 2. **Bulk Assignment**
Schedule multiple consecutive days at once:
- Select member → Choose date range → Pick shift type → Apply
- Perfect for weekly schedules or extended assignments

### 3. **Shift Patterns**
Create and save repeating shift sequences:
- Example: "2 days on, 2 days off"
- Example: "Night rotation: N, N, N, Off, Off"
- Save patterns and reuse them
- Apply to any member starting any day

### 4. **Calendar View**
Visual month calendar with:
- Day-of-week labels
- Weekend highlighting
- Scheduled count per day
- Quick daily editing

### 5. **Comprehensive User Guide**
Built-in guide with:
- Shift type reference
- Step-by-step tutorials
- Common scenarios
- Tips & best practices
- Troubleshooting

---

## 📁 File Structure

After deployment, your app will create:

```
your-app/
├── app.py              # Main application
├── requirements.txt    # Dependencies
└── data/              # Auto-created on first run
    ├── team_members.json
    ├── shift_schedule.json
    ├── shift_patterns.json
    └── settings.json
```

---

## 🎯 First-Time Usage

### 1. Start with the User Guide
- Open your app
- Select "📖 User Guide" in sidebar
- Read "Quick Start Guide" section

### 2. Add Your Team
- Go to "👥 Team Setup"
- Add your teams and members
- Fill in all details (name, location, WHMCS ID)

### 3. Choose Your Scheduling Method

**For Regular Weekly Schedules**:
→ Use "⚡ Bulk Assign"

**For Rotating Shifts**:
→ Use "🔄 Shift Patterns"

**For Quick Visual Scheduling**:
→ Use "📅 Calendar View"

**For Single Quick Edits**:
→ Use "📊 Grid View"

### 4. Export & Share
- Click "📥 Export to Excel" in sidebar
- Download formatted Excel file
- Share with your team

---

## 💡 Key Differences from Previous Version

| Feature | Old Version | New Version |
|---------|-------------|-------------|
| Shift Types | 6 basic types | 14 detailed types with SAST times |
| Scheduling | One-by-one only | Bulk assign + Patterns + Individual |
| Views | 2 views | 6 specialized views + User Guide |
| Shift Times | Generic labels | Specific SAST time ranges |
| Weekend Shifts | Generic | Dedicated WD/WEM/WN codes |
| Holiday Shifts | Not supported | Dedicated HD/HEM/HN codes |
| Leave Tracking | Basic | Leave (X), Sick Leave (SL), Training (TR) |
| Patterns | Not supported | Create, save, and reuse shift patterns |
| Calendar | Not supported | Visual month calendar with highlights |
| Documentation | None | Built-in comprehensive guide |

---

## 🔧 Troubleshooting

### App Won't Start
**Check**: `requirements.txt` has `pandas>=2.2.0` (not 2.1.4)

### Data Not Saving
**Check**: `data/` folder is being created (auto-created on first run)

### Excel Export Not Working
**Check**: `openpyxl` is in requirements.txt

### Shifts Not Showing
**Check**: 
1. Members are added in Team Setup
2. Team filter includes the team (Grid View)
3. Correct month/year selected (sidebar)

---

## 📚 Documentation

**Full User Guide**: See `USER_GUIDE.md` for:
- Complete shift type reference
- Detailed feature explanations  
- Step-by-step tutorials
- Common scenarios
- Tips & best practices
- Troubleshooting guide

**Built-in Help**: The app includes a complete user guide accessible from the "📖 User Guide" view in the sidebar.

---

## 🎉 You're All Set!

Your enhanced shift scheduler is ready to use with:
✅ 14 shift types with SAST times
✅ Bulk assignment capability
✅ Shift pattern creation
✅ Visual calendar view
✅ Comprehensive documentation
✅ Excel export

**Next Steps**:
1. Deploy to Streamlit
2. Open the app
3. Read the built-in User Guide
4. Add your team members
5. Start scheduling!

---

## 📞 Support

If you need help:
1. Check the built-in "📖 User Guide" in the app
2. Review `USER_GUIDE.md` for detailed instructions
3. Common issues are covered in Troubleshooting sections

---

**Happy Scheduling!** 📅✨

*Enhanced Shift Schedule Manager v3.0*
