# 📅 Shift Schedule Manager

A comprehensive Streamlit application for managing team shift schedules with Excel export capabilities.

## Features

### 🎯 Core Features
- **Grid View**: Full calendar view showing all team members and their shifts for the entire month
- **Card View**: Detailed team member cards with role information and assignments
- **Team Summary**: Statistical overview of all teams and members
- **Member Management**: Add or remove team members dynamically
- **Excel Export**: Generate professional Excel files in two formats:
  - Grid View: Traditional calendar-style schedule
  - Card View: Detailed weekly team assignment sheets

### 👥 Team Management
- **Tickets Team**: Support technicians handling ticket queue
- **Chats Team**: Support technicians handling live chat
- **Abuse Team**: Dedicated abuse handling specialists
- **Early Shift/Nightshift**: Special shift workers
- **Layover/Leave**: Team members on leave
- **DomainKing**: Domain-specific support team

### 📊 Shift Types
- **Regular (T)**: Standard ticket/chat shifts - Purple
- **8-Hour (8)**: 8-hour extended shifts - Orange
- **12-Hour (12)**: 12-hour long shifts - Blue
- **Special (S)**: Special assignments - Green
- **Operations (O)**: Operations tasks - Cyan

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   streamlit run app.py
   ```

3. **Access the app**:
   Open your browser and navigate to `http://localhost:8501`

## Usage Guide

### Navigation
Use the sidebar to:
- Select month and year
- Choose view type (Grid, Card, Summary, Add Member)
- Export schedules to Excel

### Adding Team Members
1. Select "Add Member" from the view options
2. Fill in the member details:
   - Full Name
   - Team assignment
   - Location
   - WHMCS access level
3. Click "Add Member" to save

### Removing Team Members
1. Go to "Add Member" view
2. Scroll to "Remove Team Member" section
3. Select the member from the dropdown
4. Click "Remove Member" to confirm

### Exporting to Excel

#### Grid Export
1. Select desired month and year
2. Click "Generate Grid Excel"
3. Download the file
4. File contains:
   - All team members in rows
   - Days of month in columns
   - Color-coded shift types
   - Frozen header row and member column

#### Card Export
1. Select week range (e.g., "12th-17th")
2. Click "Generate Card Excel"
3. Download the file
4. File contains:
   - Team sections (HostAfrica/Cloud, DomainKing)
   - Member cards with details
   - Role assignments (Tickets, Chats, Abuse, etc.)
   - Special role sections (Early Shift, Nightshift, Layover, Leave)

## File Structure

```
shift-schedule-manager/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Features Breakdown

### Grid View
- **Responsive Table**: Displays all members and their shifts
- **Team Filtering**: Filter by specific teams
- **Color Coding**: Visual indication of shift types
- **Statistics**: Real-time metrics (total members, team sizes, days in month)

### Card View
- **Team Sections**: Organized by team type
- **Member Details**: Full information for each team member
- **Visual Hierarchy**: Clear separation between different teams
- **Special Roles**: Dedicated sections for Abuse, Nightshift, etc.

### Team Summary
- **Overall Statistics**: Total teams, members, and active period
- **Team Breakdown**: Expandable sections for each team
- **Member Lists**: Tabular view of all members per team

### Excel Export Features

#### Grid Format
- Header row with day numbers
- Member names in first and last columns
- Color-coded cells matching shift types
- Frozen panes for easy navigation
- Professional formatting with borders

#### Card Format
- Title section with date range
- HostAfrica/Cloud section:
  - Tickets subsection (green background)
  - Chats subsection (green background)
- Special roles section (gray background):
  - Abuse
  - Early Shift
  - Nightshift
  - Layover
  - Leave
- DomainKing section (orange background)
- Each member card includes:
  - Name
  - Title
  - Location
  - WHMCS access

## Customization

### Adding New Teams
Edit the `team_members` initialization in `app.py`:

```python
if 'team_members' not in st.session_state:
    st.session_state.team_members = {
        'Your New Team': [
            {'name': 'Member Name', 'location': 'Location', 'whmcs': 'Access Level'}
        ]
    }
```

### Adding New Shift Types
Update these sections in `app.py`:

1. Color mapping in `get_shift_color()`
2. Label mapping in `get_shift_label()`
3. Color codes in Excel generation functions

### Modifying Excel Styles
Adjust the openpyxl styling in:
- `create_excel_grid()` - for grid format
- `create_excel_card_view()` - for card format

## Troubleshooting

### Common Issues

**App won't start**:
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

**Excel files won't download**:
- Check browser download settings
- Ensure you have write permissions
- Try a different browser

**Data not saving**:
- Streamlit uses session state - data resets on page reload
- Export to Excel to save permanently

**Styling issues**:
- Clear browser cache
- Reload the page
- Check browser compatibility (Chrome, Firefox, Safari recommended)

## Support

For issues, questions, or feature requests:
1. Check this README first
2. Review the code comments in `app.py`
3. Test with sample data

## Version History

### v1.0 (Current)
- Initial release
- Grid and Card view support
- Excel export in two formats
- Team member management
- Multi-team support
- Shift type color coding

## License

This project is provided as-is for shift scheduling management.

## Credits

Built with:
- [Streamlit](https://streamlit.io/) - Web framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Excel file generation
- [NumPy](https://numpy.org/) - Numerical operations
