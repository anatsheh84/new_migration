# Virtualization Migration Dashboard

A comprehensive Python tool for analyzing virtualization environments and generating interactive HTML dashboards to plan migration to OpenShift Virtualization.

**Supports Multiple Source Platforms:**
- Red Hat Virtualization (RHV/oVirt)
- VMware vSphere (RVTools exports)
- Future: Nutanix (planned)

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/anatsheh84/new_migration.git
cd new_migration

# Install dependencies
pip install pandas openpyxl
```

### Basic Usage

```bash
# RHV source
python generate_dashboard.py --source rhv RHV-Export.xlsx

# VMware source (RVTools export)
python generate_dashboard.py --source vmware RVTools-Export.xlsx

# Specify custom output filename
python generate_dashboard.py --source rhv RHV-Export.xlsx migration_analysis.html

# Help
python generate_dashboard.py --help
```

## Features

### 6 Interactive Dashboard Tabs

1. **Overview** - Executive summary with key metrics and OS distribution
2. **Sizing** - VM sizing analysis and categorization (Small/Medium/Large/X-Large)
3. **Migration** - Migration complexity assessment and 4-wave migration planning
4. **Trends** - Historical growth analysis (RHV only - requires creation dates)
5. **Forecast** - Capacity forecasting (RHV only - requires creation dates)
6. **Inventory** - Searchable VM inventory with all attributes

### Analytics & Insights

- **Complexity Scoring:** Automatically categorizes VMs as Low/Medium/High migration complexity
- **Migration Waves:** Proposes phased migration approach
- **Growth Analysis:** Historical trends and monthly creation patterns (where available)
- **Resource Planning:** Total vCPUs, memory, and storage requirements
- **OS Consolidation:** Simplifies OS versions (RHEL 8.6 → RHEL 8, Windows Server 2019 → Windows 2019)


## Supported Sources

### RHV (Red Hat Virtualization)

Full feature support including:
- All 6 dashboard tabs
- Historical growth trends
- Capacity forecasting
- Complete VM inventory

**Required columns:** vm_name, cluster_name, guest_os, vm_host, status, mem_size_GB, num_of_cpus, storage_size_GB, used_size_GB, creation_date

### VMware vSphere (RVTools)

Supported features:
- Overview, Sizing, Migration, and Inventory tabs
- Migration complexity assessment
- VM categorization

**Note:** Trends and Forecast tabs display "Data Not Available" message as RVTools exports do not include VM creation dates.

**Required sheet:** vInfo

**Auto-mapped columns:** VM, Cluster, Host, CPUs, Memory, Powerstate, OS according to the VMware Tools, Provisioned MB, In Use MB

## CLI Interface

```
usage: generate_dashboard.py [-h] -s {rhv,vmware} input_file [output_file]

Generate OpenShift Virtualization Migration Dashboard

positional arguments:
  input_file            Path to the Excel export file
  output_file           Output HTML file path (optional)

options:
  -h, --help            show this help message and exit
  -s {rhv,vmware}, --source {rhv,vmware}
                        Source virtualization platform
```

## Output

The tool generates a **single self-contained HTML file** with:

- Embedded CSS styling
- Chart.js visualization library
- JavaScript interactivity
- No external dependencies (works offline)
- Responsive design (desktop/tablet)
- Search and filtering capabilities

## Project Structure

```
new_migration/
├── generate_dashboard.py      # Main CLI with --source flag
├── data_processor.py          # Dispatcher to source processors
├── requirements.txt
├── README.md
├── sources/                   # Source-specific processors
│   ├── __init__.py
│   ├── base_processor.py      # Abstract base class
│   ├── rhv_processor.py       # RHV logic
│   └── vmware_processor.py    # VMware/RVTools logic
├── components/                # Dashboard UI components
│   ├── __init__.py
│   ├── base.py                # Source-aware HTML structure
│   ├── styles.py              # CSS styles
│   ├── scripts.py             # JavaScript
│   ├── tab_overview.py
│   ├── tab_sizing.py
│   ├── tab_migration.py
│   ├── tab_trends.py          # Handles "no data" case
│   ├── tab_forecast.py        # Handles "no data" case
│   └── tab_inventory.py
├── sample_data/
│   ├── rhv/
│   └── vmware/
└── documentation/
```

## Dependencies

- **pandas** - Data manipulation and aggregation
- **openpyxl** - Excel file reading
- Python 3.6+

## License

This project is open source. Use, modify, and distribute as needed.

---

**Current Version:** 2.0  
**Last Updated:** December 2025
