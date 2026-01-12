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
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'team_members' not in st.session_state:
    st.session_state.team_members = {
        'Tickets': [
            {'name': 'Russell', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Jasper', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Simphiwe', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Zaheyd', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Joanitha', 'location': 'Kenya', 'whmcs': 'HA and Cloud'},
            {'name': 'Raul', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Daniel', 'location': 'Kenya', 'whmcs': 'HA and Cloud'},
            {'name': 'Khyati', 'location': 'India', 'whmcs': 'HA and Cloud'},
            {'name': 'Tarryn', 'location': 'South Africa', 'whmcs': 'HA and Cloud'}
        ],
        'Chats': [
            {'name': 'Sipho', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Monicah', 'location': 'Kenya', 'whmcs': 'HA'},
            {'name': 'Matthew', 'location': 'Kenya', 'whmcs': 'HA'},
            {'name': 'Noma', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Alex', 'location': 'Kenya', 'whmcs': 'HA and Cloud'},
            {'name': 'Simphiwe', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Jessica', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Mduduzi', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Ntobz', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Andile', 'location': 'South Africa', 'whmcs': 'HA and Cloud'},
            {'name': 'Avha', 'location': 'South Africa', 'whmcs': 'HA and Cloud'}
        ],
        'Abuse': [
            {'name': 'Victor', 'location': 'India', 'whmcs': 'HA'},
            {'name': 'Angelo', 'location': 'Kenya', 'whmcs': 'HA and Cloud'}
        ],
        'Early Shift': [
            {'name': 'Athira', 'location': 'India', 'whmcs': 'HA and Cloud'}
        ],
        'Nightshift': [
            {'name': 'Victor', 'location': 'India', 'whmcs': 'HA'},
            {'name': 'Monicah', 'location': 'Kenya', 'whmcs': 'HA'}
        ],
        'Layover': [
            {'name': 'Josh', 'location': 'Kenya', 'whmcs': 'HA and Cloud'}
        ],
        'Leave': [
            {'name': 'Matthew', 'location': 'Kenya', 'whmcs': 'HA and Cloud'}
        ],
        'DomainKing': [
            {'name': 'Anaximene', 'location': 'India', 'whmcs': 'DK and DK'},
            {'name': 'Kristina', 'location': 'India', 'whmcs': 'DK and DK'},
            {'name': 'Susmishma', 'location': 'India', 'whmcs': 'DK'},
            {'name': 'Vicky', 'location': 'India', 'whmcs': 'DK'},
            {'name': 'Binod', 'location': 'India', 'whmcs': 'DK'}
        ]
    }

if 'shift_schedule' not in st.session_state:
    # Initialize with sample data for January 2025
    st.session_state.shift_schedule = {}
    for team, members in st.session_state.team_members.items():
        for member in members:
            # Initialize 31 days with default values (0 = off, 1 = regular, 2 = 8hr, 3 = 12hr, 4 = special)
            st.session_state.shift_schedule[member['name']] = [0] * 31

if 'current_month' not in st.session_state:
    st.session_state.current_month = datetime.now().month
    st.session_state.current_year = datetime.now().year

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

def create_excel_grid(year, month):
    """Create Excel file with grid view similar to the uploaded image"""
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
    ws['A1'] = f'Jan-{str(year)[-2:]}'
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
    """Create Excel file with card/section view similar to second uploaded image"""
    wb = Workbook()
    ws = wb.active
    ws.title = f"{start_day}th-{end_day}th"
    
    # Title
    ws['A1'] = f"{start_day}th-{end_day}th"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:D1')
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    
    current_row = 3
    
    # HostAfrica/Cloud Section
    ws.cell(row=current_row, column=1, value='HostAfrica/Cloud')
    ws.cell(row=current_row, column=1).fill = PatternFill(start_color='87CEEB', end_color='87CEEB', fill_type='solid')
    ws.cell(row=current_row, column=1).font = Font(bold=True, size=12, color='FFFFFF')
    ws.merge_cells(f'A{current_row}:D{current_row}')
    current_row += 1
    
    # Tickets section
    ws.cell(row=current_row, column=1, value='Tickets')
    ws.cell(row=current_row, column=1).fill = PatternFill(start_color='808080', end_color='808080', fill_type='solid')
    ws.cell(row=current_row, column=1).font = Font(bold=True, color='FFFFFF')
    current_row += 1
    
    for member in st.session_state.team_members['Tickets']:
        ws.cell(row=current_row, column=1, value=f"Name: {member['name']}")
        ws.cell(row=current_row, column=1).fill = PatternFill(start_color='90EE90', end_color='90EE90', fill_type='solid')
        ws.cell(row=current_row, column=1).font = Font(size=9)
        
        ws.cell(row=current_row + 1, column=1, value=f"Title: Support Technician")
        ws.cell(row=current_row + 1, column=1).font = Font(size=8)
        
        ws.cell(row=current_row + 2, column=1, value=f"Location: {member['location']}")
        ws.cell(row=current_row + 2, column=1).font = Font(size=8)
        
        ws.cell(row=current_row + 3, column=1, value=f"WHMCS: {member['whmcs']}")
        ws.cell(row=current_row + 3, column=1).font = Font(size=8)
        
        current_row += 5
    
    # Chats section
    ws.cell(row=current_row, column=2, value='Chats')
    ws.cell(row=current_row, column=2).fill = PatternFill(start_color='808080', end_color='808080', fill_type='solid')
    ws.cell(row=current_row, column=2).font = Font(bold=True, color='FFFFFF')
    current_row += 1
    
    chat_row_start = current_row
    for member in st.session_state.team_members['Chats']:
        ws.cell(row=current_row, column=2, value=f"Name: {member['name']}")
        ws.cell(row=current_row, column=2).fill = PatternFill(start_color='90EE90', end_color='90EE90', fill_type='solid')
        ws.cell(row=current_row, column=2).font = Font(size=9)
        
        ws.cell(row=current_row + 1, column=2, value=f"Title: Support Technician")
        ws.cell(row=current_row + 1, column=2).font = Font(size=8)
        
        ws.cell(row=current_row + 2, column=2, value=f"Location: {member['location']}")
        ws.cell(row=current_row + 2, column=2).font = Font(size=8)
        
        ws.cell(row=current_row + 3, column=2, value=f"WHMCS: {member['whmcs']}")
        ws.cell(row=current_row + 3, column=2).font = Font(size=8)
        
        current_row += 5
    
    # Add other sections (Abuse, Early Shift, Nightshift, etc.)
    special_sections = ['Abuse', 'Early Shift', 'Nightshift', 'Layover', 'Leave']
    col = 3
    for section in special_sections:
        if section in st.session_state.team_members:
            ws.cell(row=3, column=col, value=section)
            ws.cell(row=3, column=col).fill = PatternFill(start_color='808080', end_color='808080', fill_type='solid')
            ws.cell(row=3, column=col).font = Font(bold=True, color='FFFFFF')
            
            row = 4
            for member in st.session_state.team_members[section]:
                ws.cell(row=row, column=col, value=f"Name: {member['name']}")
                ws.cell(row=row, column=col).fill = PatternFill(start_color='D3D3D3', end_color='D3D3D3', fill_type='solid')
                ws.cell(row=row, column=col).font = Font(size=9)
                
                ws.cell(row=row + 1, column=col, value=f"Title: Support Technician")
                ws.cell(row=row + 1, column=col).font = Font(size=8)
                
                ws.cell(row=row + 2, column=col, value=f"Location: {member['location']}")
                ws.cell(row=row + 2, column=col).font = Font(size=8)
                
                ws.cell(row=row + 3, column=col, value=f"WHMCS: {member['whmcs']}")
                ws.cell(row=row + 3, column=col).font = Font(size=8)
                
                row += 5
    
    # DomainKing Section
    current_row = max(current_row, chat_row_start + len(st.session_state.team_members['Chats']) * 5) + 2
    ws.cell(row=current_row, column=4, value='DomainKing')
    ws.cell(row=current_row, column=4).fill = PatternFill(start_color='87CEEB', end_color='87CEEB', fill_type='solid')
    ws.cell(row=current_row, column=4).font = Font(bold=True, size=12, color='FFFFFF')
    current_row += 1
    
    for member in st.session_state.team_members['DomainKing']:
        ws.cell(row=current_row, column=4, value=f"Name: {member['name']}")
        ws.cell(row=current_row, column=4).fill = PatternFill(start_color='FFA500', end_color='FFA500', fill_type='solid')
        ws.cell(row=current_row, column=4).font = Font(size=9, color='FFFFFF', bold=True)
        
        ws.cell(row=current_row + 1, column=4, value=f"Title: Support Technician")
        ws.cell(row=current_row + 1, column=4).fill = PatternFill(start_color='FFA500', end_color='FFA500', fill_type='solid')
        ws.cell(row=current_row + 1, column=4).font = Font(size=8, color='FFFFFF')
        
        ws.cell(row=current_row + 2, column=4, value=f"Location: {member['location']}")
        ws.cell(row=current_row + 2, column=4).fill = PatternFill(start_color='FFA500', end_color='FFA500', fill_type='solid')
        ws.cell(row=current_row + 2, column=4).font = Font(size=8, color='FFFFFF')
        
        ws.cell(row=current_row + 3, column=4, value=f"WHMCS: {member['whmcs']}")
        ws.cell(row=current_row + 3, column=4).fill = PatternFill(start_color='FFA500', end_color='FFA500', fill_type='solid')
        ws.cell(row=current_row + 3, column=4).font = Font(size=8, color='FFFFFF')
        
        current_row += 5
    
    # Adjust column widths
    for col in range(1, 5):
        ws.column_dimensions[get_column_letter(col)].width = 25
    
    return wb

# Main app layout
st.title("📅 Shift Schedule Manager")
st.markdown("### Comprehensive Team Management System")

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
    
    st.divider()
    
    # View options
    st.header("📊 View Options")
    view_type = st.radio("Select View", ["Grid View", "Card View", "Team Summary", "Add Member"])
    
    st.divider()
    
    # Export options
    st.header("📥 Export")
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

# Main content area
if view_type == "Grid View":
    st.header(f"📊 Shift Schedule - {selected_month} {selected_year}")
    
    # Stats
    col1, col2, col3, col4 = st.columns(4)
    total_members = sum(len(members) for members in st.session_state.team_members.values())
    
    with col1:
        st.metric("Total Members", total_members)
    with col2:
        st.metric("Tickets Team", len(st.session_state.team_members['Tickets']))
    with col3:
        st.metric("Chats Team", len(st.session_state.team_members['Chats']))
    with col4:
        days = get_days_in_month(selected_year, st.session_state.current_month)
        st.metric("Days in Month", days)
    
    st.divider()
    
    # Team filter
    team_filter = st.multiselect("Filter by Team", 
                                list(st.session_state.team_members.keys()), 
                                default=["Tickets", "Chats"])
    
    # Create schedule grid
    days = get_days_in_month(selected_year, st.session_state.current_month)
    
    # Build dataframe for display
    schedule_data = []
    for team in team_filter:
        for member in st.session_state.team_members[team]:
            row = {' 'Member': member['name'], 'Team': team, 'Location': member['location']}
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
    else:
        st.info("No team members selected. Please select teams from the filter above.")
    
    # Legend
    st.divider()
    st.subheader("Legend")
    legend_cols = st.columns(5)
    with legend_cols[0]:
        st.markdown("🟣 **T** - Regular Ticket/Chat")
    with legend_cols[1]:
        st.markdown("🟠 **8** - 8-Hour Shift")
    with legend_cols[2]:
        st.markdown("🔵 **12** - 12-Hour Shift")
    with legend_cols[3]:
        st.markdown("🟢 **S** - Special Shift")
    with legend_cols[4]:
        st.markdown("🔷 **O** - Operations")

elif view_type == "Card View":
    st.header(f"📋 Team Overview - {week_range}")
    
    # HostAfrica/Cloud Section
    st.subheader("🌐 HostAfrica/Cloud")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Tickets Team")
        for member in st.session_state.team_members['Tickets']:
            with st.expander(f"👤 {member['name']}"):
                st.write(f"**Title:** Support Technician")
                st.write(f"**Location:** {member['location']}")
                st.write(f"**WHMCS:** {member['whmcs']}")
    
    with col2:
        st.markdown("#### Chats Team")
        for member in st.session_state.team_members['Chats']:
            with st.expander(f"👤 {member['name']}"):
                st.write(f"**Title:** Support Technician")
                st.write(f"**Location:** {member['location']}")
                st.write(f"**WHMCS:** {member['whmcs']}")
    
    st.divider()
    
    # Special Roles
    st.subheader("⚡ Special Roles")
    
    special_cols = st.columns(3)
    special_teams = ['Abuse', 'Early Shift', 'Nightshift', 'Layover', 'Leave']
    
    for idx, team in enumerate(special_teams):
        if team in st.session_state.team_members:
            with special_cols[idx % 3]:
                st.markdown(f"#### {team}")
                for member in st.session_state.team_members[team]:
                    with st.expander(f"👤 {member['name']}"):
                        st.write(f"**Location:** {member['location']}")
                        st.write(f"**WHMCS:** {member['whmcs']}")
    
    st.divider()
    
    # DomainKing Section
    st.subheader("👑 DomainKing Team")
    dk_cols = st.columns(3)
    for idx, member in enumerate(st.session_state.team_members['DomainKing']):
        with dk_cols[idx % 3]:
            st.markdown(f"""
            <div style='background-color: #F59E0B; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4 style='color: white; margin: 0;'>{member['name']}</h4>
                <p style='color: white; margin: 5px 0;'><strong>Title:</strong> Support Technician</p>
                <p style='color: white; margin: 5px 0;'><strong>Location:</strong> {member['location']}</p>
                <p style='color: white; margin: 5px 0;'><strong>WHMCS:</strong> {member['whmcs']}</p>
            </div>
            """, unsafe_allow_html=True)

elif view_type == "Team Summary":
    st.header("📊 Team Statistics")
    
    # Overall stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Teams", len(st.session_state.team_members))
    with col2:
        st.metric("Total Members", sum(len(members) for members in st.session_state.team_members.values()))
    with col3:
        st.metric("Active Month", f"{selected_month} {selected_year}")
    
    st.divider()
    
    # Team breakdown
    for team, members in st.session_state.team_members.items():
        with st.expander(f"**{team}** ({len(members)} members)", expanded=True):
            team_df = pd.DataFrame(members)
            st.dataframe(team_df, use_container_width=True, hide_index=True)

elif view_type == "Add Member":
    st.header("➕ Add New Team Member")
    
    with st.form("add_member_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            new_name = st.text_input("Full Name*")
            new_team = st.selectbox("Select Team*", list(st.session_state.team_members.keys()))
        
        with col2:
            new_location = st.text_input("Location*")
            new_whmcs = st.text_input("WHMCS*")
        
        submitted = st.form_submit_button("Add Member", use_container_width=True)
        
        if submitted:
            if new_name and new_team and new_location and new_whmcs:
                new_member = {
                    'name': new_name,
                    'location': new_location,
                    'whmcs': new_whmcs
                }
                st.session_state.team_members[new_team].append(new_member)
                st.session_state.shift_schedule[new_name] = [0] * 31
                st.success(f"✅ {new_name} added to {new_team} team successfully!")
                st.rerun()
            else:
                st.error("❌ Please fill in all required fields")
    
    st.divider()
    
    # Remove member
    st.subheader("🗑️ Remove Team Member")
    
    all_members = []
    for team, members in st.session_state.team_members.items():
        for member in members:
            all_members.append(f"{member['name']} ({team})")
    
    if all_members:
        member_to_remove = st.selectbox("Select member to remove", all_members)
        
        if st.button("Remove Member", type="secondary", use_container_width=True):
            member_name = member_to_remove.split(' (')[0]
            team_name = member_to_remove.split('(')[1].replace(')', '')
            
            # Remove from team
            st.session_state.team_members[team_name] = [
                m for m in st.session_state.team_members[team_name] 
                if m['name'] != member_name
            ]
            
            # Remove from schedule
            if member_name in st.session_state.shift_schedule:
                del st.session_state.shift_schedule[member_name]
            
            st.success(f"✅ {member_name} removed successfully!")
            st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Shift Schedule Manager v1.0 | Built with Streamlit 🎈</p>
    <p>Export to Excel • Manage Teams • Track Shifts</p>
</div>
""", unsafe_allow_html=True)
