import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import calendar
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import io
import json
import os
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Shift Schedule Manager",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    .shift-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    div[data-testid="stMetricValue"] {
        font-size: 2em;
        font-weight: bold;
    }
    .success-message {
        padding: 10px;
        background-color: #10B981;
        color: white;
        border-radius: 5px;
        margin: 10px 0;
    }
    .error-message {
        padding: 10px;
        background-color: #EF4444;
        color: white;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# File paths for persistent storage
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MEMBERS_FILE = DATA_DIR / "team_members.json"
SCHEDULE_FILE = DATA_DIR / "shift_schedule.json"
SETTINGS_FILE = DATA_DIR / "settings.json"

# Data management functions
def load_team_members():
    """Load team members from JSON file"""
    if MEMBERS_FILE.exists():
        try:
            with open(MEMBERS_FILE, 'r') as f:
                data = json.load(f)
                # Ensure data is valid
                if isinstance(data, dict):
                    return data
        except Exception as e:
            st.error(f"Error loading team members: {e}")
    
    # Return empty structure if file doesn't exist or is invalid
    return {}

def save_team_members(team_members):
    """Save team members to JSON file"""
    try:
        with open(MEMBERS_FILE, 'w') as f:
            json.dump(team_members, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving team members: {e}")
        return False

def load_shift_schedule():
    """Load shift schedule from JSON file"""
    if SCHEDULE_FILE.exists():
        try:
            with open(SCHEDULE_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading shift schedule: {e}")
    return {}

def save_shift_schedule(shift_schedule):
    """Save shift schedule to JSON file"""
    try:
        with open(SCHEDULE_FILE, 'w') as f:
            json.dump(shift_schedule, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving shift schedule: {e}")
        return False

def load_settings():
    """Load app settings from JSON file"""
    if SETTINGS_FILE.exists():
        try:
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading settings: {e}")
    return {
        'current_month': datetime.now().month,
        'current_year': datetime.now().year
    }

def save_settings(settings):
    """Save app settings to JSON file"""
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(settings, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving settings: {e}")
        return False

# Initialize session state with persistent data
if 'team_members' not in st.session_state:
    st.session_state.team_members = load_team_members()

if 'shift_schedule' not in st.session_state:
    st.session_state.shift_schedule = load_shift_schedule()

if 'settings' not in st.session_state:
    st.session_state.settings = load_settings()

if 'current_month' not in st.session_state:
    st.session_state.current_month = st.session_state.settings.get('current_month', datetime.now().month)

if 'current_year' not in st.session_state:
    st.session_state.current_year = st.session_state.settings.get('current_year', datetime.now().year)

# Helper functions
def get_days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

def get_shift_color(shift_type):
    colors = {
        0: '#FFFFFF',  # Off
        1: '#9333EA',  # Regular (Purple)
        2: '#F59E0B',  # 8-hour (Orange)
        3: '#3B82F6',  # 12-hour (Blue)
        4: '#10B981',  # Special (Green)
        5: '#06B6D4'   # Operations (Cyan)
    }
    return colors.get(shift_type, '#FFFFFF')

def get_shift_label(shift_type):
    labels = {
        0: '',
        1: 'T',
        2: '8',
        3: '12',
        4: 'S',
        5: 'O'
    }
    return labels.get(shift_type, '')

def update_shift(member_name, day, shift_type):
    """Update a shift and save to file"""
    if member_name not in st.session_state.shift_schedule:
        st.session_state.shift_schedule[member_name] = [0] * 31
    
    if day < len(st.session_state.shift_schedule[member_name]):
        st.session_state.shift_schedule[member_name][day] = shift_type
        save_shift_schedule(st.session_state.shift_schedule)

def add_team_member(team_name, member_data):
    """Add a new team member and save"""
    if team_name not in st.session_state.team_members:
        st.session_state.team_members[team_name] = []
    
    # Check if member already exists
    existing_names = [m['name'] for m in st.session_state.team_members[team_name]]
    if member_data['name'] in existing_names:
        return False, "Member already exists in this team"
    
    st.session_state.team_members[team_name].append(member_data)
    
    # Initialize schedule for new member
    st.session_state.shift_schedule[member_data['name']] = [0] * 31
    
    # Save both files
    save_team_members(st.session_state.team_members)
    save_shift_schedule(st.session_state.shift_schedule)
    
    return True, "Member added successfully"

def remove_team_member(team_name, member_name):
    """Remove a team member and save"""
    if team_name in st.session_state.team_members:
        st.session_state.team_members[team_name] = [
            m for m in st.session_state.team_members[team_name] 
            if m['name'] != member_name
        ]
        
        # Remove empty teams
        if len(st.session_state.team_members[team_name]) == 0:
            del st.session_state.team_members[team_name]
        
        # Remove from schedule
        if member_name in st.session_state.shift_schedule:
            del st.session_state.shift_schedule[member_name]
        
        # Save both files
        save_team_members(st.session_state.team_members)
        save_shift_schedule(st.session_state.shift_schedule)
        
        return True, "Member removed successfully"
    
    return False, "Team not found"

def add_new_team(team_name):
    """Add a new team category"""
    if team_name and team_name not in st.session_state.team_members:
        st.session_state.team_members[team_name] = []
        save_team_members(st.session_state.team_members)
        return True, f"Team '{team_name}' created successfully"
    elif team_name in st.session_state.team_members:
        return False, f"Team '{team_name}' already exists"
    return False, "Team name cannot be empty"

def delete_team(team_name):
    """Delete an entire team"""
    if team_name in st.session_state.team_members:
        # Remove all members from schedule
        for member in st.session_state.team_members[team_name]:
            if member['name'] in st.session_state.shift_schedule:
                del st.session_state.shift_schedule[member['name']]
        
        # Remove team
        del st.session_state.team_members[team_name]
        
        # Save both files
        save_team_members(st.session_state.team_members)
        save_shift_schedule(st.session_state.shift_schedule)
        
        return True, f"Team '{team_name}' deleted successfully"
    return False, "Team not found"

def create_excel_grid(year, month):
    """Create Excel file with grid view"""
    wb = Workbook()
    ws = wb.active
    ws.title = f"{calendar.month_name[month]} {year}"
    
    days_in_month = get_days_in_month(year, month)
    
    # Styling
    header_fill = PatternFill(start_color='D4AF37', end_color='D4AF37', fill_type='solid')
    header_font = Font(bold=True, size=11, color='000000')
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # Headers - Days row
    ws['A1'] = f'{calendar.month_abbr[month]}-{str(year)[-2:]}'
    ws['A1'].fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    ws['A1'].font = Font(bold=True, size=10)
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    
    # Day numbers
    for day in range(1, days_in_month + 1):
        col = day + 1
        ws.cell(row=1, column=col, value=day)
        ws.cell(row=1, column=col).fill = header_fill
        ws.cell(row=1, column=col).font = header_font
        ws.cell(row=1, column=col).alignment = Alignment(horizontal='center', vertical='center')
        ws.cell(row=1, column=col).border = border
        ws.column_dimensions[get_column_letter(col)].width = 4
    
    # Add member column at the end
    ws.cell(row=1, column=days_in_month + 2, value=ws['A1'].value)
    ws.cell(row=1, column=days_in_month + 2).fill = ws['A1'].fill
    ws.cell(row=1, column=days_in_month + 2).font = ws['A1'].font
    ws.cell(row=1, column=days_in_month + 2).alignment = ws['A1'].alignment
    
    # Set first column width
    ws.column_dimensions['A'].width = 15
    ws.column_dimensions[get_column_letter(days_in_month + 2)].width = 15
    
    # Shift type colors
    shift_colors = {
        0: 'FFFFFF',  # Off - White
        1: '9333EA',  # Regular - Purple
        2: 'F59E0B',  # 8-hour - Orange
        3: '3B82F6',  # 12-hour - Blue
        4: '10B981',  # Special - Green
        5: '06B6D4'   # Operations - Cyan
    }
    
    # Add all team members
    current_row = 2
    for team, members in st.session_state.team_members.items():
        for member in members:
            # Member name in first column
            ws.cell(row=current_row, column=1, value=member['name'])
            ws.cell(row=current_row, column=1).fill = PatternFill(start_color='90EE90', end_color='90EE90', fill_type='solid')
            ws.cell(row=current_row, column=1).font = Font(bold=True, size=10)
            ws.cell(row=current_row, column=1).border = border
            
            # Shift data
            schedule = st.session_state.shift_schedule.get(member['name'], [0] * days_in_month)
            for day in range(days_in_month):
                col = day + 2
                shift_type = schedule[day] if day < len(schedule) else 0
                shift_label = get_shift_label(shift_type)
                
                cell = ws.cell(row=current_row, column=col, value=shift_label)
                cell.fill = PatternFill(start_color=shift_colors[shift_type], 
                                       end_color=shift_colors[shift_type], 
                                       fill_type='solid')
                cell.alignment = Alignment(horizontal='center', vertical='center')
                cell.border = border
                if shift_type > 0:
                    cell.font = Font(bold=True, color='FFFFFF', size=9)
            
            # Member name in last column
            ws.cell(row=current_row, column=days_in_month + 2, value=member['name'])
            ws.cell(row=current_row, column=days_in_month + 2).fill = ws.cell(row=current_row, column=1).fill
            ws.cell(row=current_row, column=days_in_month + 2).font = ws.cell(row=current_row, column=1).font
            ws.cell(row=current_row, column=days_in_month + 2).border = border
            
            current_row += 1
    
    # Freeze panes
    ws.freeze_panes = 'B2'
    
    return wb

def create_excel_card_view(year, month, start_day, end_day):
    """Create Excel file with card/section view"""
    wb = Workbook()
    ws = wb.active
    ws.title = f"{start_day}th-{end_day}th"
    
    # Title
    ws['A1'] = f"{start_day}th-{end_day}th"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:D1')
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    
    current_row = 3
    col_index = 1
    
    # Process each team
    for team, members in st.session_state.team_members.items():
        # Team header
        ws.cell(row=current_row, column=col_index, value=team)
        ws.cell(row=current_row, column=col_index).fill = PatternFill(start_color='808080', end_color='808080', fill_type='solid')
        ws.cell(row=current_row, column=col_index).font = Font(bold=True, color='FFFFFF', size=11)
        current_row += 1
        
        # Team members
        for member in members:
            ws.cell(row=current_row, column=col_index, value=f"Name: {member['name']}")
            ws.cell(row=current_row, column=col_index).fill = PatternFill(start_color='90EE90', end_color='90EE90', fill_type='solid')
            ws.cell(row=current_row, column=col_index).font = Font(size=9, bold=True)
            
            ws.cell(row=current_row + 1, column=col_index, value=f"Location: {member['location']}")
            ws.cell(row=current_row + 1, column=col_index).font = Font(size=8)
            
            ws.cell(row=current_row + 2, column=col_index, value=f"WHMCS: {member['whmcs']}")
            ws.cell(row=current_row + 2, column=col_index).font = Font(size=8)
            
            current_row += 4
        
        current_row += 2  # Space between teams
        
        # Move to next column after certain number of rows
        if current_row > 50:
            current_row = 4
            col_index += 1
    
    # Adjust column widths
    for col in range(1, col_index + 1):
        ws.column_dimensions[get_column_letter(col)].width = 25
    
    return wb

# Main app layout
st.title("📅 Shift Schedule Manager")
st.markdown("### Blank Template - Build Your Own Team")

# Check if data exists
total_members = sum(len(members) for members in st.session_state.team_members.values())

if total_members == 0:
    st.info("👋 Welcome! Start by creating your first team and adding members below.")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Month/Year selector
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    selected_month = st.selectbox("Select Month", months, index=st.session_state.current_month - 1)
    selected_year = st.number_input("Select Year", min_value=2020, max_value=2030, 
                                    value=st.session_state.current_year)
    
    st.session_state.current_month = months.index(selected_month) + 1
    st.session_state.current_year = selected_year
    
    # Save settings
    st.session_state.settings['current_month'] = st.session_state.current_month
    st.session_state.settings['current_year'] = st.session_state.current_year
    save_settings(st.session_state.settings)
    
    st.divider()
    
    # View options
    st.header("📊 View Options")
    view_type = st.radio("Select View", ["Team Setup", "Grid View", "Card View", "Team Summary"])
    
    st.divider()
    
    # Export options
    st.header("📥 Export")
    
    if total_members > 0:
        if st.button("Generate Grid Excel", use_container_width=True):
            wb = create_excel_grid(st.session_state.current_year, st.session_state.current_month)
            buffer = io.BytesIO()
            wb.save(buffer)
            buffer.seek(0)
            
            st.download_button(
                label="Download Grid Excel",
                data=buffer,
                file_name=f"shift_schedule_grid_{selected_month}_{selected_year}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        # Week selector for card view
        week_range = st.selectbox("Select Week for Card View", 
                                 ["1st-5th", "8th-12th", "15th-19th", "22nd-26th", "29th-31st"])
        
        if st.button("Generate Card Excel", use_container_width=True):
            start_day = int(week_range.split('-')[0].replace('st', '').replace('th', '').replace('nd', '').replace('rd', ''))
            end_day = int(week_range.split('-')[1].replace('st', '').replace('th', '').replace('nd', '').replace('rd', ''))
            
            wb = create_excel_card_view(st.session_state.current_year, st.session_state.current_month, 
                                        start_day, end_day)
            buffer = io.BytesIO()
            wb.save(buffer)
            buffer.seek(0)
            
            st.download_button(
                label="Download Card Excel",
                data=buffer,
                file_name=f"shift_schedule_card_{week_range}_{selected_month}_{selected_year}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("Add team members first to export")
    
    st.divider()
    
    # Data management
    st.header("💾 Data Management")
    
    if st.button("🔄 Reload Data", use_container_width=True):
        st.session_state.team_members = load_team_members()
        st.session_state.shift_schedule = load_shift_schedule()
        st.rerun()
    
    st.caption("💡 All changes are automatically saved to JSON files in the 'data' folder")

# Main content area
if view_type == "Team Setup":
    st.header("👥 Team & Member Management")
    
    # Stats at top
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Teams", len(st.session_state.team_members))
    with col2:
        st.metric("Total Members", total_members)
    with col3:
        st.metric("Data Status", "✅ Saved" if MEMBERS_FILE.exists() else "❌ Not Saved")
    
    st.divider()
    
    # Two columns: Create Team | Add Member
    setup_col1, setup_col2 = st.columns(2)
    
    with setup_col1:
        st.subheader("➕ Create New Team")
        with st.form("create_team_form"):
            new_team_name = st.text_input("Team Name*", placeholder="e.g., Tickets, Chats, Support")
            team_submit = st.form_submit_button("Create Team", use_container_width=True)
            
            if team_submit:
                success, message = add_new_team(new_team_name)
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
    
    with setup_col2:
        st.subheader("➕ Add Team Member")
        
        if len(st.session_state.team_members) == 0:
            st.warning("Create a team first before adding members")
        else:
            with st.form("add_member_form"):
                member_team = st.selectbox("Select Team*", list(st.session_state.team_members.keys()))
                member_name = st.text_input("Full Name*", placeholder="e.g., John Doe")
                member_location = st.text_input("Location*", placeholder="e.g., Kenya, India, South Africa")
                member_whmcs = st.text_input("WHMCS Access*", placeholder="e.g., HA and Cloud, DK")
                
                member_submit = st.form_submit_button("Add Member", use_container_width=True)
                
                if member_submit:
                    if member_name and member_location and member_whmcs:
                        member_data = {
                            'name': member_name,
                            'location': member_location,
                            'whmcs': member_whmcs
                        }
                        success, message = add_team_member(member_team, member_data)
                        if success:
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
                    else:
                        st.error("Please fill in all required fields")
    
    st.divider()
    
    # Display current teams and members
    st.subheader("📋 Current Teams & Members")
    
    if len(st.session_state.team_members) == 0:
        st.info("No teams created yet. Create your first team above!")
    else:
        for team_name, members in st.session_state.team_members.items():
            with st.expander(f"**{team_name}** ({len(members)} members)", expanded=True):
                # Team actions
                team_action_col1, team_action_col2, team_action_col3 = st.columns([3, 1, 1])
                
                with team_action_col3:
                    if st.button(f"🗑️ Delete Team", key=f"delete_team_{team_name}", type="secondary"):
                        success, message = delete_team(team_name)
                        if success:
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
                
                if len(members) == 0:
                    st.info("No members in this team yet.")
                else:
                    # Create dataframe of members
                    df_members = pd.DataFrame(members)
                    st.dataframe(df_members, use_container_width=True, hide_index=True)
                    
                    # Remove member section
                    st.markdown("**Remove Member:**")
                    remove_cols = st.columns([3, 1])
                    with remove_cols[0]:
                        member_to_remove = st.selectbox(
                            "Select member to remove",
                            [m['name'] for m in members],
                            key=f"remove_select_{team_name}"
                        )
                    with remove_cols[1]:
                        if st.button("Remove", key=f"remove_btn_{team_name}", type="secondary"):
                            success, message = remove_team_member(team_name, member_to_remove)
                            if success:
                                st.success(message)
                                st.rerun()
                            else:
                                st.error(message)

elif view_type == "Grid View":
    st.header(f"📊 Shift Schedule - {selected_month} {selected_year}")
    
    if total_members == 0:
        st.warning("No team members added yet. Go to 'Team Setup' to add members.")
    else:
        # Stats
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Members", total_members)
        with col2:
            st.metric("Total Teams", len(st.session_state.team_members))
        with col3:
            days = get_days_in_month(selected_year, st.session_state.current_month)
            st.metric("Days in Month", days)
        with col4:
            # Count scheduled days
            scheduled_count = sum(
                sum(1 for shift in schedule if shift > 0)
                for schedule in st.session_state.shift_schedule.values()
            )
            st.metric("Scheduled Shifts", scheduled_count)
        
        st.divider()
        
        # Team filter
        team_filter = st.multiselect("Filter by Team", 
                                    list(st.session_state.team_members.keys()), 
                                    default=list(st.session_state.team_members.keys()))
        
        # Create schedule grid
        days = get_days_in_month(selected_year, st.session_state.current_month)
        
        # Build dataframe for display
        schedule_data = []
        for team in team_filter:
            if team in st.session_state.team_members:
                for member in st.session_state.team_members[team]:
                    row = {'Member': member['name'], 'Team': team, 'Location': member['location']}
                    schedule = st.session_state.shift_schedule.get(member['name'], [0] * days)
                    for day in range(1, days + 1):
                        shift_type = schedule[day - 1] if day - 1 < len(schedule) else 0
                        row[f'Day {day}'] = get_shift_label(shift_type)
                    schedule_data.append(row)
        
        if schedule_data:
            df = pd.DataFrame(schedule_data)
            
            # Style the dataframe
            def color_cells(val):
                if val == 'T':
                    return 'background-color: #9333EA; color: white; font-weight: bold'
                elif val == '8':
                    return 'background-color: #F59E0B; color: white; font-weight: bold'
                elif val == '12':
                    return 'background-color: #3B82F6; color: white; font-weight: bold'
                elif val == 'S':
                    return 'background-color: #10B981; color: white; font-weight: bold'
                elif val == 'O':
                    return 'background-color: #06B6D4; color: white; font-weight: bold'
                return ''
            
            styled_df = df.style.applymap(color_cells, subset=[col for col in df.columns if col.startswith('Day')])
            st.dataframe(styled_df, use_container_width=True, height=600)
            
            # Shift editor
            st.divider()
            st.subheader("✏️ Edit Shifts")
            
            edit_col1, edit_col2, edit_col3, edit_col4 = st.columns(4)
            
            with edit_col1:
                all_members = []
                for team in team_filter:
                    if team in st.session_state.team_members:
                        all_members.extend([m['name'] for m in st.session_state.team_members[team]])
                
                selected_member = st.selectbox("Select Member", all_members)
            
            with edit_col2:
                selected_day = st.number_input("Day", min_value=1, max_value=days, value=1)
            
            with edit_col3:
                shift_options = {
                    'Off': 0,
                    'Regular (T)': 1,
                    '8-Hour (8)': 2,
                    '12-Hour (12)': 3,
                    'Special (S)': 4,
                    'Operations (O)': 5
                }
                selected_shift = st.selectbox("Shift Type", list(shift_options.keys()))
            
            with edit_col4:
                st.write("")  # Spacing
                st.write("")  # Spacing
                if st.button("Update Shift", use_container_width=True):
                    update_shift(selected_member, selected_day - 1, shift_options[selected_shift])
                    st.success(f"✅ Updated {selected_member}'s shift for day {selected_day}")
                    st.rerun()
        else:
            st.info("No team members selected. Please select teams from the filter above.")
        
        # Legend
        st.divider()
        st.subheader("Legend")
        legend_cols = st.columns(6)
        with legend_cols[0]:
            st.markdown("⬜ **Off** - Day Off")
        with legend_cols[1]:
            st.markdown("🟣 **T** - Regular Shift")
        with legend_cols[2]:
            st.markdown("🟠 **8** - 8-Hour Shift")
        with legend_cols[3]:
            st.markdown("🔵 **12** - 12-Hour Shift")
        with legend_cols[4]:
            st.markdown("🟢 **S** - Special Shift")
        with legend_cols[5]:
            st.markdown("🔷 **O** - Operations")

elif view_type == "Card View":
    st.header(f"📋 Team Overview - {selected_month} {selected_year}")
    
    if total_members == 0:
        st.warning("No team members added yet. Go to 'Team Setup' to add members.")
    else:
        # Display all teams in card format
        for team_name, members in st.session_state.team_members.items():
            st.subheader(f"👥 {team_name}")
            
            # Create columns for members (3 per row)
            member_cols = st.columns(3)
            
            for idx, member in enumerate(members):
                with member_cols[idx % 3]:
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                        <h4 style='color: white; margin: 0;'>👤 {member['name']}</h4>
                        <p style='color: white; margin: 5px 0; font-size: 14px;'>
                            <strong>Location:</strong> {member['location']}</p>
                        <p style='color: white; margin: 5px 0; font-size: 14px;'>
                            <strong>WHMCS:</strong> {member['whmcs']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.divider()

elif view_type == "Team Summary":
    st.header("📊 Team Statistics")
    
    if total_members == 0:
        st.warning("No team members added yet. Go to 'Team Setup' to add members.")
    else:
        # Overall stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Teams", len(st.session_state.team_members))
        with col2:
            st.metric("Total Members", total_members)
        with col3:
            st.metric("Active Month", f"{selected_month} {selected_year}")
        with col4:
            scheduled_count = sum(
                sum(1 for shift in schedule if shift > 0)
                for schedule in st.session_state.shift_schedule.values()
            )
            st.metric("Total Scheduled Shifts", scheduled_count)
        
        st.divider()
        
        # Team breakdown with charts
        for team, members in st.session_state.team_members.items():
            with st.expander(f"**{team}** ({len(members)} members)", expanded=True):
                if len(members) > 0:
                    team_df = pd.DataFrame(members)
                    
                    # Display member table
                    st.dataframe(team_df, use_container_width=True, hide_index=True)
                    
                    # Show shift statistics for this team
                    st.markdown("**Shift Statistics:**")
                    team_shifts = {}
                    for member in members:
                        schedule = st.session_state.shift_schedule.get(member['name'], [])
                        total_shifts = sum(1 for shift in schedule if shift > 0)
                        team_shifts[member['name']] = total_shifts
                    
                    if team_shifts:
                        shift_df = pd.DataFrame(list(team_shifts.items()), columns=['Member', 'Scheduled Days'])
                        st.bar_chart(shift_df.set_index('Member'))
                else:
                    st.info("No members in this team")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #fff; padding: 20px;'>
    <p><strong>Shift Schedule Manager v2.0</strong> | Blank Template with JSON Persistence</p>
    <p>💾 All data automatically saved to: <code>data/team_members.json</code> & <code>data/shift_schedule.json</code></p>
    <p>🔄 Changes persist between sessions | 📥 Export to Excel anytime</p>
</div>
""", unsafe_allow_html=True)
