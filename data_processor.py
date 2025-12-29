"""
data_processor.py
-----------------
Dispatcher module for source-specific processors.
Routes processing to the appropriate source handler.
"""

from sources import get_processor


def process_excel(filepath, source='rhv'):
    """
    Process virtualization export file.
    
    Args:
        filepath: Path to the export file
        source: Source platform ('rhv' or 'vmware')
        
    Returns:
        Dictionary with all data needed by dashboard tabs
    """
    processor = get_processor(source)
    return processor.process(filepath)


# For backward compatibility
def process_rhv(filepath):
    """Process RHV export (backward compatible)."""
    return process_excel(filepath, source='rhv')


def process_vmware(filepath):
    """Process VMware/RVTools export."""
    return process_excel(filepath, source='vmware')


# For testing
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python data_processor.py <source> <excel_file>")
        print("  source: rhv | vmware")
        sys.exit(1)
    
    source = sys.argv[1]
    filepath = sys.argv[2]
    
    data = process_excel(filepath, source=source)
    
    print(f"\n{'='*50}")
    print(f"PROCESSING SUMMARY")
    print(f"{'='*50}")
    print(f"Source: {data['source_display_name']}")
    print(f"Total VMs: {data['stats']['total_vms']}")
    print(f"Total vCPUs: {data['stats']['total_vcpus']}")
    print(f"Total Memory: {data['stats']['total_memory_gb']} GB")
    print(f"Has Date Data: {data['has_date_data']}")
